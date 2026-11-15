import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name) / "repository"
        for name in ("scripts", "skills", "docs", "wiki", ".codex-plugin", ".agents"):
            shutil.copytree(ROOT / name, self.root / name)
        self.marketplace_path = self.root / ".agents/plugins/marketplace.json"
        self.marketplace = json.loads(self.marketplace_path.read_text())

    def run_script(self, name, *arguments):
        return subprocess.run([sys.executable, str(self.root / "scripts" / name), *arguments],
                              capture_output=True, text=True)

    def validate_entry(self, **changes):
        entry = self.marketplace["plugins"][0]
        entry.update(changes)
        self.marketplace_path.write_text(json.dumps(self.marketplace))
        return self.run_script("validate.py")

    def test_missing_local_plugin_source_fails_validation(self):
        result = self.validate_entry(source={"source": "local", "path": "./does-not-exist"})
        self.assertNotEqual(result.returncode, 0)

    def test_nonlocal_and_nonrelative_sources_fail_validation(self):
        for source in ({"source": "git", "path": "./"}, {"source": "local", "path": str(self.root)}):
            with self.subTest(source=source):
                self.assertNotEqual(self.validate_entry(source=source).returncode, 0)

    def test_sources_cannot_escape_through_parent_paths_or_symlinks(self):
        outside = self.root.parent / "outside"
        shutil.copytree(self.root / ".codex-plugin", outside / ".codex-plugin")
        (self.root / "linked").symlink_to(outside, target_is_directory=True)
        for path in ("./../outside", "./linked"):
            with self.subTest(path=path):
                self.assertNotEqual(self.validate_entry(source={"source": "local", "path": path}).returncode, 0)

    def test_source_manifest_identity_must_match_marketplace_entry(self):
        nested = self.root / "nested/.codex-plugin"
        nested.mkdir(parents=True)
        (nested / "plugin.json").write_text('{"name":"different-plugin"}')
        self.assertNotEqual(self.validate_entry(source={"source": "local", "path": "./nested"}).returncode, 0)

    def test_symlinked_source_and_manifest_components_fail_validation(self):
        (self.root / "alias").symlink_to(".", target_is_directory=True)
        self.assertNotEqual(self.validate_entry(source={"source": "local", "path": "./alias"}).returncode, 0)
        nested = self.root / "nested/.codex-plugin"
        nested.mkdir(parents=True)
        outside = self.root.parent / "external.json"
        outside.write_text((self.root / ".codex-plugin/plugin.json").read_text())
        (nested / "plugin.json").symlink_to(outside)
        self.assertNotEqual(self.validate_entry(source={"source": "local", "path": "./nested"}).returncode, 0)

    def test_invalid_product_restrictions_fail_validation(self):
        for products in ("CODEX", ["NOT_A_PRODUCT"], [1], {}):
            with self.subTest(products=products):
                self.assertNotEqual(self.validate_entry(policy={"products": products}).returncode, 0)

    def test_supported_product_restrictions_pass_validation(self):
        for products in (None, [], ["codex", "chatgpt", "atlas"], ["CODEX", "CHATGPT", "ATLAS"]):
            with self.subTest(products=products):
                result = self.validate_entry(policy={"products": products})
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_unknown_marketplace_policies_fail_validation(self):
        for policy in ({"installation": "SOMETIMES", "authentication": "ON_INSTALL"},
                       {"installation": "AVAILABLE", "authentication": "ON_FIRST_USE"}):
            with self.subTest(policy=policy):
                self.assertNotEqual(self.validate_entry(policy=policy).returncode, 0)

    def test_supported_marketplace_policies_pass_validation(self):
        for installation in ("AVAILABLE", "NOT_AVAILABLE", "INSTALLED_BY_DEFAULT"):
            for authentication in ("ON_INSTALL", "ON_USE"):
                with self.subTest(installation=installation, authentication=authentication):
                    result = self.validate_entry(policy={"installation": installation, "authentication": authentication})
                    self.assertEqual(result.returncode, 0, result.stderr)

    def test_check_rejects_stale_wiki_and_render_repairs_it(self):
        self.assertEqual(self.run_script("render_catalog.py").returncode, 0)
        for name in ("Capabilities.md", "Configuration.md"):
            with self.subTest(name=name):
                path = self.root / "wiki" / name
                path.write_text("stale wiki source\n")
                self.assertNotEqual(self.run_script("render_catalog.py", "--check").returncode, 0)
                result = self.run_script("render_catalog.py")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotEqual(path.read_text(), "stale wiki source\n")
                self.assertEqual(self.run_script("render_catalog.py", "--check").returncode, 0)
        capabilities = (self.root / "wiki/Capabilities.md").read_text()
        self.assertIn("https://github.com/thinkhome-org/full-github/blob/main/docs/VERIFICATION.md", capabilities)


if __name__ == "__main__":
    unittest.main()
