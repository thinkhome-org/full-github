import importlib.util
from pathlib import Path
import unittest
from unittest import mock
import io
import contextlib
import os
import shutil
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import threading
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

spec = importlib.util.spec_from_file_location("operations", Path(__file__).parents[1] / "scripts/operations.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class OperationTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        patch = mock.patch.object(module.execution_history, "DATABASE", Path(directory.name) / "history.sqlite3")
        patch.start()
        self.addCleanup(patch.stop)
    @classmethod
    def setUpClass(cls):
        cls.catalog = module.load_catalog()["operations"]

    def test_required_parameters_are_checked(self):
        with self.assertRaisesRegex(ValueError, "Missing parameter"):
            module.build_request(self.catalog["repos/get"], {"owner": "owner"})

    def test_path_is_encoded_and_query_does_not_change_method(self):
        argv = module.build_request(self.catalog["issues/list-for-repo"],
                                    {"owner": "owner", "repo": "repo", "labels": "a&state=closed"})
        self.assertEqual(argv[3], "GET")
        self.assertIn("labels=a%26state%3Dclosed", argv[4])
        self.assertIn("--paginate", argv)

    def test_shell_input_stays_one_encoded_argument(self):
        argv = module.build_request(self.catalog["repos/get"], {"owner": "owner", "repo": "$(echo bad)/x"})
        self.assertEqual(argv[4], "/repos/owner/%24%28echo%20bad%29%2Fx")

    def test_body_uses_stdin_and_explicit_write_method(self):
        argv = module.build_request(self.catalog["issues/create"], {"owner": "owner", "repo": "repo"}, b'{"title":"x"}')
        self.assertEqual(argv[3], "POST")
        self.assertEqual(argv[-2:], ["--input", "-"])
        self.assertNotIn("--paginate", argv)

    def test_unknown_parameter_and_unsafe_path_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown parameters"):
            module.build_request(self.catalog["repos/get"], {"owner": "o", "repo": "r", "bogus": 1})
        for name in ("", ".", ".."):
            with self.assertRaises(ValueError):
                module.build_request(self.catalog["repos/get"], {"owner": "o", "repo": name})

    def test_body_is_required_when_documented(self):
        with self.assertRaisesRegex(ValueError, "requires a request body"):
            module.build_request(self.catalog["issues/create"], {"owner": "o", "repo": "r"})

    def test_every_path_parameter_has_a_declaration(self):
        import re
        for name, operation in self.catalog.items():
            names = {p["name"] for p in operation["parameters"] if p["location"] == "path"}
            self.assertEqual(set(re.findall(r"\{([^}]+)\}", operation["path"])), names, name)

    def test_binary_upload_uses_upload_host_and_content_type(self):
        argv = module.build_request(self.catalog["repos/upload-release-asset"],
                                    {"owner": "o", "repo": "r", "release_id": 1, "name": "a.zip"}, b"zip")
        self.assertTrue(argv[4].startswith("https://uploads.github.com/"))
        self.assertIn("Content-Type: application/octet-stream", argv)

    def test_explicit_upload_content_type_is_preserved(self):
        argv = module.build_request(self.catalog["repos/upload-release-asset"],
                                    {"owner": "o", "repo": "r", "release_id": 1, "name": "a.zip"}, b"zip",
                                    extra_headers=["Content-Type: application/zip"])
        self.assertIn("Content-Type: application/zip", argv)
        self.assertNotIn("Content-Type: application/octet-stream", argv)

    def test_retired_operation_never_reaches_network(self):
        with mock.patch("sys.argv", ["operations.py", "call", "dependency-graph/export-sbom"]), mock.patch.object(module.subprocess, "run") as run:
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(module.main(), 2)
            run.assert_not_called()

    def test_graphql_index_includes_deprecated_mutations_and_input_types(self):
        graph = module.load_catalog(True)
        self.assertTrue(any(op["isDeprecated"] for op in graph["mutations"].values()))
        self.assertIn("UpdateProjectV2ViewInput", graph["types"])
        self.assertIn("updateProjectV2View", graph["mutations"])
        members = graph["types"]["ProjectV2FieldConfiguration"]["possibleTypes"]
        self.assertIn("ProjectV2MultiSelectField", {entry["name"] for entry in members})

    def test_cli_preserves_remote_error_exit_status(self):
        with mock.patch("sys.argv", ["operations.py", "call", "repos/get", "--params", '{"owner":"o","repo":"r"}']), mock.patch.object(module.subprocess, "run") as run:
            run.return_value.returncode = 7
            self.assertEqual(module.main(), 7)

    def test_dry_run_never_reaches_network(self):
        with mock.patch("sys.argv", ["operations.py", "call", "repos/get", "--params", '{"owner":"o","repo":"r"}', "--dry-run"]), mock.patch.object(module.subprocess, "run") as run:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(module.main(), 0)
            run.assert_not_called()

    def test_dry_run_redacts_authentication_headers(self):
        arguments = ["operations.py", "call", "repos/get", "--params", '{"owner":"o","repo":"r"}', "--dry-run", "--header", "Authorization: Bearer secret-value"]
        output = io.StringIO()
        with mock.patch("sys.argv", arguments), contextlib.redirect_stdout(output):
            self.assertEqual(module.main(), 0)
        self.assertNotIn("secret-value", output.getvalue())
        self.assertIn("redacted", output.getvalue())

    def test_array_filter_names_match_documented_wire_format(self):
        for name in ("orgs/list-pat-grant-requests", "orgs/list-pat-grants"):
            argv = module.build_request(self.catalog[name], {"org": "o", "owner": ["a", "b"], "token_id": [1, 2]})
            self.assertIn("owner%5B%5D=a&owner%5B%5D=b", argv[4])
            self.assertIn("token_id%5B%5D=1&token_id%5B%5D=2", argv[4])

    def test_negotiated_binary_response_disables_json_wrapping(self):
        argv = module.build_request(self.catalog["repos/get-release-asset"],
                                    {"owner": "o", "repo": "r", "asset_id": 1},
                                    extra_headers=["Accept: application/octet-stream"])
        self.assertNotIn("--slurp", argv)
        self.assertIn("Accept: application/octet-stream", argv)
        with self.assertRaisesRegex(ValueError, "Invalid request header"):
            module.build_request(self.catalog["repos/get"], {"owner": "o", "repo": "r"},
                                 extra_headers=["Accept: json\r\nInjected: x"])

    @unittest.skipUnless(shutil.which("gh"), "Requires GitHub CLI for byte-preservation regression")
    def test_binary_download_bytes_are_preserved_through_real_gh(self):
        payload = bytes([80, 75, 3, 4, 0, 255, 10])
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *args):
                pass
        with HTTPServer(("127.0.0.1", 0), Handler) as server:
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                operation = dict(self.catalog["repos/download-zipball-archive"], server=f"http://127.0.0.1:{server.server_port}")
                argv = module.build_request(operation, {"owner": "o", "repo": "r", "ref": "main"})
                self.assertNotIn("--slurp", argv)
                response = subprocess.run(argv, capture_output=True, check=True, env=dict(os.environ, GH_TOKEN="local-test-token"))
                self.assertEqual(response.stdout, payload)
            finally:
                server.shutdown()
                thread.join()


if __name__ == "__main__":
    unittest.main()
