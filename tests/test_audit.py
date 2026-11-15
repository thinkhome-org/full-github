import importlib.util
import subprocess
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("audit", Path(__file__).parents[1] / "scripts/audit.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AuditTests(unittest.TestCase):
    def test_invalid_repository_never_executes(self):
        with self.assertRaises(ValueError):
            module.audit("owner/repo;echo bad", lambda *a, **k: self.fail("executed"))

    def test_permission_failure_is_unknown(self):
        result = module.audit("owner/repo", lambda *a, **k: subprocess.CompletedProcess(a, 1, "", "HTTP 403"))
        self.assertEqual(result["labels"]["status"], "unknown")
        self.assertIn("403", result["labels"]["error"])

    def test_endpoint_failures_preserve_other_evidence(self):
        for failure in ("timeout", "json"):
            calls = []
            def run(argv, **kwargs):
                calls.append(argv)
                if len(calls) == 2:
                    if failure == "timeout":
                        raise subprocess.TimeoutExpired(argv, 60)
                    return subprocess.CompletedProcess(argv, 0, "{invalid", "")
                return subprocess.CompletedProcess(argv, 0, "[{}]", "")
            result = module.audit("owner/repo", run)
            self.assertEqual(result["labels"]["status"], "unknown")
            self.assertEqual(result["community"]["status"], "observed")
            self.assertEqual(len(calls), 7 + len(module.REPOSITORY_READS))

    def test_empty_success_is_observed(self):
        result = module.read_probe(["gh", "api", "x"], lambda *a, **k: subprocess.CompletedProcess(a, 0, "", ""))
        self.assertEqual(result["status"], "observed")
        self.assertTrue(result["empty_response"])

    def test_invalid_project_never_executes(self):
        with self.assertRaises(ValueError):
            module.audit("owner/repo", lambda *a, **k: self.fail("executed"), project=-1)

    def test_protected_default_branch_is_inspected_separately_from_rulesets(self):
        calls = []
        def run(argv, **kwargs):
            calls.append(argv)
            return subprocess.CompletedProcess(argv, 0, '[{"default_branch":"release/main"}]', "")
        result = module.audit("owner/repo", run)
        self.assertEqual(result["default_branch_protection"]["status"], "observed")
        self.assertIn("repos/owner/repo/branches/release%2Fmain/protection", calls[-1])

    def test_project_queries_are_paginated_and_errors_remain_unknown(self):
        calls = []
        def run(argv, **kwargs):
            calls.append(argv)
            return subprocess.CompletedProcess(argv, 0, '[{"errors":[{"message":"forbidden"}]}]', "")
        result = module.audit("owner/repo", run, organization=True, project=5)
        self.assertEqual(result["project_views"]["status"], "unknown")
        for argv in calls[-3:]:
            self.assertIn("--paginate", argv)
            self.assertIn("--slurp", argv)
            self.assertIn("$endCursor", argv[6])
        fields_query = calls[-3][6]
        self.assertIn("ProjectV2MultiSelectField", fields_query)
        self.assertIn("completedIterations", fields_query)

    def test_project_null_is_unknown_even_with_http_success(self):
        def run(argv, **kwargs):
            return subprocess.CompletedProcess(argv, 0, '[{"data":{"organization":{"projectV2":null}}}]', "")
        result = module.audit("owner/repo", run, organization=True, project=5)
        self.assertEqual(result["project_views"]["status"], "unknown")
        self.assertIn("inaccessible", result["project_views"]["error"])

    def test_paginated_response_is_preserved(self):
        def run(argv, **kwargs):
            self.assertIn("--paginate", argv)
            return subprocess.CompletedProcess(argv, 0, '[[{"id":1}],[{"id":2}]]', "")
        self.assertEqual(len(module.audit("owner/repo", run)["labels"]["pages"]), 2)


if __name__ == "__main__":
    unittest.main()
