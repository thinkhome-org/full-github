import contextlib
import gzip
import hashlib
import io
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
import operations
import execution_history


class ConfigurationDepthTests(unittest.TestCase):
    def test_every_capability_has_concrete_option_decisions(self):
        capabilities = json.loads((operations.DATA / "capabilities.json").read_text())["capabilities"]
        groups = json.loads((operations.DATA / "configuration-options.json").read_text())["groups"]
        covered = {capability for group in groups for capability in group["capability_ids"]}
        self.assertEqual({capability["id"] for capability in capabilities}, covered)
        self.assertEqual(len(groups), len({group["id"] for group in groups}))
        for group in groups:
            self.assertTrue(group["sources"], group["id"])
            self.assertTrue(group["options"], group["id"])
            for option in group["options"]:
                for key in ("name", "values", "decision_rule", "verification"):
                    self.assertTrue(option[key], (group["id"], key))

    def test_full_schema_matches_official_source_digest_and_all_indexed_routes(self):
        with gzip.open(operations.DATA / "rest-schema.json.gz", "rb") as source:
            raw = source.read()
        index = operations.load_catalog()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), index["source_sha256"])
        schema = json.loads(raw)
        for name, operation in index["operations"].items():
            self.assertEqual(schema["paths"][operation["path"]][operation["method"].lower()]["operationId"], name)

    def test_nested_reference_preserves_defaults_and_enum_constraints(self):
        catalog = operations.load_catalog()["operations"]
        value = operations.inspect_schema(catalog["repos/update"], "requestBody", "/content/application~1json/schema/properties/allow_squash_merge")
        self.assertIs(value["default"], True)
        value = operations.inspect_schema(catalog["projects/create-view-for-org"], "requestBody", "/content/application~1json/schema/properties/layout")
        self.assertEqual(value["enum"], ["table", "board", "roadmap"])
        value = operations.inspect_schema(catalog["billing/get-all-budgets-org"], "responses", "/200/content/application~1json/schema/properties/budgets/items/properties")
        self.assertIn("id", value)
        root = operations.inspect_schema(catalog["repos/get"], pointer="#")
        self.assertEqual(root["operationId"], "repos/get")


class CollectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.operation = operations.load_catalog()["operations"]["issues/list-labels-for-repo"]

    def collect(self, pages, operation=None, pointer="", params=None):
        responses = iter(pages)
        def run(argv, **kwargs):
            self.assertNotIn("--slurp", argv)
            self.assertNotIn("--paginate", argv)
            value = next(responses)
            if isinstance(value, Exception):
                raise value
            return subprocess.CompletedProcess(argv, 0, json.dumps(value), "")
        return operations.collect_pages(operation or self.operation,
                                        params or {"owner": "o", "repo": "r", "per_page": 2}, pointer, run=run)

    def test_missing_link_header_cannot_truncate_full_pages(self):
        report = self.collect([[{"id": 1}, {"id": 2}], [{"id": 3}], []])
        self.assertTrue(report["complete"])
        self.assertEqual(report["item_count"], 3)
        self.assertEqual(len(report["pages"]), 3)

    def test_explicit_next_page_takes_precedence_over_short_page(self):
        report = self.collect([{"budgets": [{"id": 1}], "has_next_page": True, "total_count": 2},
                               {"budgets": [{"id": 2}], "has_next_page": False, "total_count": 2}])
        self.assertTrue(report["complete"])
        self.assertEqual(report["item_count"], 2)

    def test_repeated_page_stops_without_claiming_completeness(self):
        report = self.collect([[1, 2], [1, 2]])
        self.assertFalse(report["complete"])
        self.assertIn("no progress", report["error"])

    def test_changed_totals_and_partial_failures_preserve_evidence(self):
        report = self.collect([{"items": [1, 2], "total_count": 3}, {"items": [3], "total_count": 4}])
        self.assertFalse(report["complete"])
        self.assertEqual(len(report["pages"]), 2)
        report = self.collect([[1, 2], subprocess.TimeoutExpired("gh", 60)])
        self.assertFalse(report["complete"])
        self.assertEqual(report["pages"], [[1, 2]])

    def test_ambiguous_arrays_need_an_explicit_pointer(self):
        report = self.collect([{"items": [1], "errors": []}])
        self.assertFalse(report["complete"])
        self.assertEqual(report["pages"], [{"items": [1], "errors": []}])
        report = self.collect([{"items": [1], "errors": []}, {"items": [], "errors": []}], pointer="/items")
        self.assertTrue(report["complete"])

    def test_backend_page_size_cap_does_not_truncate_collection(self):
        report = self.collect([list(range(100)), [100], []], params={"owner": "o", "repo": "r", "per_page": 101})
        self.assertTrue(report["complete"])
        self.assertEqual(report["item_count"], 101)

    def test_incomplete_search_flag_is_never_a_complete_collection(self):
        report = self.collect([{"items": [{"id": 1}], "total_count": 1, "incomplete_results": True}])
        self.assertFalse(report["complete"])
        self.assertEqual(report["item_count"], 1)
        self.assertEqual(len(report["pages"]), 1)

    def test_total_mismatch_never_claims_completeness(self):
        report = self.collect([{"items": [1], "total_count": 2}, {"items": [], "total_count": 2}])
        self.assertFalse(report["complete"])
        self.assertIn("does not match", report["error"])


class HistoryTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        patch = mock.patch.object(execution_history, "DATABASE", Path(directory.name) / "private/history.sqlite3")
        patch.start()
        self.addCleanup(patch.stop)

    def test_attempt_result_and_verification_are_separate_append_only_events(self):
        run_id = execution_history.start("issues/update", {"method": "PATCH"}, {"owner": "o", "repo": "r", "issue_number": 1})
        execution_history.finish(run_id, 0)
        execution_history.verify(run_id, "matched", "https://github.com/o/r/issues/1")
        events = execution_history.read_events(0)
        self.assertEqual([event["kind"] for event in reversed(events)], ["started", "command_succeeded", "verification_recorded"])
        self.assertEqual(len({event["sequence"] for event in events}), 3)
        self.assertEqual(execution_history.DATABASE.stat().st_mode & 0o777, 0o600)

    def test_failure_and_interruption_remain_unknown(self):
        run_id = execution_history.start("issues/update", {"method": "PATCH"}, {})
        execution_history.finish(run_id, 7)
        self.assertEqual(execution_history.read_events()[0]["kind"], "outcome_unknown")
        interrupted = execution_history.start("issues/update", {"method": "PATCH"}, {})
        self.assertEqual(execution_history.read_events()[0]["run_id"], interrupted)
        self.assertEqual(execution_history.read_events()[0]["kind"], "started")

    def test_sensitive_parameters_are_excluded_and_credential_links_rejected(self):
        execution_history.start("apps/test", {"method": "POST"}, {"owner": "o", "token": "secret-value", "body": "private-body"})
        text = json.dumps(execution_history.read_events())
        self.assertNotIn("secret-value", text)
        self.assertNotIn("private-body", text)
        with self.assertRaises(ValueError):
            execution_history.start("apps/test", {"method": "POST"}, {}, "https://github.com/o/r?token=secret")

    def test_concurrent_writers_preserve_every_event(self):
        def record(number):
            run_id = execution_history.start("issues/get", {"method": "GET"}, {"issue_number": number})
            execution_history.finish(run_id, 0)
        with ThreadPoolExecutor(max_workers=4) as pool:
            list(pool.map(record, range(8)))
        events = execution_history.read_events(0)
        self.assertEqual(len(events), 16)
        self.assertEqual(len({event["run_id"] for event in events}), 8)

    def test_reading_missing_history_creates_no_database(self):
        self.assertEqual(execution_history.read_events(), [])
        self.assertFalse(execution_history.DATABASE.exists())
        with self.assertRaises(ValueError):
            execution_history.verify("unknown", "matched", "https://github.com/o/r")


if __name__ == "__main__":
    unittest.main()
