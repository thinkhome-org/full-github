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

    def test_paginated_response_is_preserved(self):
        def run(argv, **kwargs):
            self.assertIn("--paginate", argv)
            return subprocess.CompletedProcess(argv, 0, '[[{"id":1}],[{"id":2}]]', "")
        self.assertEqual(len(module.audit("owner/repo", run)["labels"]["pages"]), 2)


if __name__ == "__main__":
    unittest.main()
