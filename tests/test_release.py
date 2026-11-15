import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
import package_release
import publish_release


class PackagingTests(unittest.TestCase):
    def test_hidden_manifests_and_committed_version_are_verified(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            root.mkdir()
            files = {
                ".codex-plugin/plugin.json": json.dumps({"version": "0.3.0"}),
                ".agents/plugins/marketplace.json": "{}",
                "skills/full-github/SKILL.md": "skill",
                "NOTICE.md": "third-party notice",
            }
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            for arguments in (["init", "-b", "main", "--quiet"], ["config", "user.name", "Fixture"],
                              ["config", "user.email", "fixture@example.invalid"], ["add", "."],
                              ["commit", "--quiet", "-m", "fixture"]):
                subprocess.run(["git", *arguments], cwd=root, check=True)
            destination = package_release.package(root, Path(temporary) / "output", "v0.3.0")
            with zipfile.ZipFile(destination) as zipped:
                self.assertIn("full-github/.codex-plugin/plugin.json", zipped.namelist())
                self.assertIn("full-github/.agents/plugins/marketplace.json", zipped.namelist())
            self.assertEqual(hashlib.sha256(destination.read_bytes()).hexdigest(), Path(str(destination) + ".sha256").read_text().split()[0])
            with self.assertRaisesRegex(ValueError, "committed plugin version"):
                package_release.package(root, Path(temporary) / "output", "v0.3.1")
            self.assertFalse((Path(temporary) / "output/full-github-0.3.1.zip").exists())


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.assets = [Path(self.directory.name) / "plugin.zip", Path(self.directory.name) / "plugin.zip.sha256"]
        self.assets[0].write_bytes(b"archive")
        self.assets[1].write_bytes(b"checksum")
        self.exists = False
        self.draft = True
        self.prerelease = False
        self.remote = {"human-notes.txt": b"preserve"}
        self.uploads = []
        self.fail_second_upload = False

    def run_gh(self, argv, **kwargs):
        action = argv[2]
        if action == "view":
            if not self.exists:
                return subprocess.CompletedProcess(argv, 1, "", "release not found")
            value = dict(isDraft=self.draft, isPrerelease=self.prerelease, assets=[dict(name=name) for name in self.remote], url="https://github.com/o/r/releases/tag/v0.3.0")
            return subprocess.CompletedProcess(argv, 0, json.dumps(value), "")
        if action == "create":
            self.exists = True
            self.prerelease = "--prerelease" in argv
        elif action == "upload":
            path = Path(argv[4])
            if self.fail_second_upload and path == self.assets[1].resolve():
                raise subprocess.CalledProcessError(1, argv)
            self.assertNotIn(path.name, self.remote)
            self.remote[path.name] = path.read_bytes()
            self.uploads.append(path.name)
        elif action == "download":
            name = argv[argv.index("--pattern") + 1]
            directory = Path(argv[argv.index("--dir") + 1])
            (directory / name).write_bytes(self.remote[name])
        elif action == "edit":
            if "--draft=false" in argv:
                self.assertTrue(all(path.name in self.remote for path in self.assets))
                self.draft = False
            if "--prerelease=true" in argv:
                self.prerelease = True
            if "--prerelease=false" in argv:
                self.prerelease = False
        else:
            self.fail(f"Unexpected command {argv}")
        return subprocess.CompletedProcess(argv, 0, "", "")

    def test_retry_resumes_partial_draft_and_keeps_human_assets(self):
        self.fail_second_upload = True
        with self.assertRaises(subprocess.CalledProcessError):
            publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh)
        self.assertTrue(self.draft)
        self.fail_second_upload = False
        publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh)
        self.assertFalse(self.draft)
        self.assertEqual(self.uploads, ["plugin.zip", "plugin.zip.sha256"])
        self.assertEqual(self.remote["human-notes.txt"], b"preserve")
        publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh)
        self.assertEqual(len(self.uploads), 2)

    def test_different_existing_asset_is_preserved_and_blocks_publication(self):
        self.exists = True
        self.remote["plugin.zip"] = b"different"
        with self.assertRaisesRegex(RuntimeError, "no asset was overwritten"):
            publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh)
        self.assertTrue(self.draft)
        self.assertEqual(self.remote["plugin.zip"], b"different")

    def test_published_release_is_never_repaired_by_silent_mutation(self):
        self.exists = True
        self.draft = False
        with self.assertRaisesRegex(RuntimeError, "Published release is missing"):
            publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh)
        self.assertFalse(self.uploads)

    def test_rc_release_is_published_as_prerelease(self):
        publish_release.publish("o/r", "v0.3.0-rc.1", self.assets, self.run_gh)
        self.assertTrue(self.prerelease)
        self.assertFalse(self.draft)

    def test_invalid_targets_and_duplicate_names_fail_before_draft_creation(self):
        with self.assertRaises(ValueError):
            publish_release.publish("../..", "v0.3.0", self.assets, self.run_gh)
        with self.assertRaisesRegex(ValueError, "unique"):
            publish_release.publish("o/r", "v0.3.0", [self.assets[0], self.assets[0]], self.run_gh)
        self.assertFalse(self.exists)


if __name__ == "__main__":
    unittest.main()
