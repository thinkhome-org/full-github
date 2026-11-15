import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest import mock

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
import package_release
import publish_release


class PackagingTests(unittest.TestCase):
    def test_committed_marketplace_source_portability_is_verified(self):
        for failure in ("source_symlink", "manifest_symlink", "missing_manifest", "portable"):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary) / "repo"
                root.mkdir()
                files = {
                    ".codex-plugin/plugin.json": json.dumps({"name": "full-github", "version": "0.3.0"}),
                    ".agents/plugins/marketplace.json": json.dumps({"plugins": [{"name": "full-github", "source": {"source": "local", "path": "./nested"}}]}),
                    "skills/full-github/SKILL.md": "skill",
                    "NOTICE.md": "third-party notice",
                }
                for name, content in files.items():
                    path = root / name
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(content)
                if failure == "source_symlink":
                    (root / "nested").symlink_to(".", target_is_directory=True)
                elif failure == "manifest_symlink":
                    path = root / "nested/.codex-plugin/plugin.json"
                    path.parent.mkdir(parents=True)
                    external = Path(temporary) / "external.json"
                    external.write_text(files[".codex-plugin/plugin.json"])
                    path.symlink_to(external)
                elif failure == "portable":
                    path = root / "nested/.codex-plugin/plugin.json"
                    path.parent.mkdir(parents=True)
                    path.write_text(files[".codex-plugin/plugin.json"])
                for arguments in (["init", "-b", "main", "--quiet"], ["config", "user.name", "Fixture"],
                                  ["config", "user.email", "fixture@example.invalid"], ["add", "."],
                                  ["commit", "--quiet", "-m", "fixture"], ["tag", "v0.3.0"]):
                    subprocess.run(["git", *arguments], cwd=root, check=True)
                if failure == "portable":
                    destination = package_release.package(root, Path(temporary) / "output", "v0.3.0")
                    with zipfile.ZipFile(destination) as zipped:
                        self.assertEqual(json.loads(zipped.read("full-github/nested/.codex-plugin/plugin.json"))["name"], "full-github")
                else:
                    with self.assertRaisesRegex(ValueError, "[Ss]ymlink|[Mm]issing"):
                        package_release.package(root, Path(temporary) / "output", "v0.3.0")
                    self.assertFalse((Path(temporary) / "output/full-github-0.3.0.zip").exists())

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
                              ["commit", "--quiet", "-m", "fixture"],
                              ["tag", "-a", "v0.3.0", "-m", "annotated release"], ["tag", "v0.3.1"]):
                subprocess.run(["git", *arguments], cwd=root, check=True)
            destination = package_release.package(root, Path(temporary) / "output", "v0.3.0")
            with zipfile.ZipFile(destination) as zipped:
                self.assertIn("full-github/.codex-plugin/plugin.json", zipped.namelist())
                self.assertIn("full-github/.agents/plugins/marketplace.json", zipped.namelist())
            self.assertEqual(hashlib.sha256(destination.read_bytes()).hexdigest(), Path(str(destination) + ".sha256").read_text().split()[0])
            with self.assertRaisesRegex(ValueError, "committed plugin version"):
                package_release.package(root, Path(temporary) / "output", "v0.3.1")
            self.assertFalse((Path(temporary) / "output/full-github-0.3.1.zip").exists())
            original = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            archive_before = destination.read_bytes()
            (root / "payload.txt").write_text("changed source, same version")
            for arguments in (["add", "."], ["commit", "--quiet", "-m", "different source"], ["tag", "-f", "v0.3.0"], ["checkout", "--quiet", original]):
                subprocess.run(["git", *arguments], cwd=root, check=True, capture_output=True)
            with self.assertRaisesRegex(ValueError, "checked-out source commit"):
                package_release.package(root, Path(temporary) / "output", "v0.3.0")
            self.assertEqual(destination.read_bytes(), archive_before)
            moved_head = subprocess.check_output(["git", "rev-parse", "v0.3.0^{commit}"], cwd=root, text=True).strip()
            subprocess.run(["git", "tag", "-f", "v0.3.0", original], cwd=root, check=True, capture_output=True)
            original_run = subprocess.run
            def switch_head_during_archive(argv, **kwargs):
                if argv[:2] == ["git", "archive"]:
                    original_run(["git", "checkout", "--quiet", moved_head], cwd=root, check=True)
                return original_run(argv, **kwargs)
            with mock.patch.object(package_release.subprocess, "run", side_effect=switch_head_during_archive):
                stable = package_release.package(root, Path(temporary) / "output", "v0.3.0")
            with zipfile.ZipFile(stable) as archived:
                self.assertEqual(archived.comment.decode(), original)
                self.assertNotIn("full-github/payload.txt", archived.namelist())


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.assets = [Path(self.directory.name) / "plugin.zip", Path(self.directory.name) / "plugin.zip.sha256"]
        self.commit = "a" * 40
        self.remote_commit = self.commit
        self.annotated = False
        self.tag_reads = 0
        self.move_tag_after_first_read = False
        self.notes = Path(self.directory.name) / "notes.md"
        self.notes.write_text("Installation, validation evidence and known limitations.")
        with zipfile.ZipFile(self.assets[0], "w") as archive:
            archive.writestr("payload.txt", "source")
            archive.comment = self.commit.encode("ascii")
        self.assets[1].write_bytes(b"checksum")
        self.exists = False
        self.draft = True
        self.prerelease = False
        self.remote = {"human-notes.txt": b"preserve"}
        self.uploads = []
        self.fail_second_upload = False
        self.body = "human-written draft notes"
        self.created_notes = None

    def run_gh(self, argv, **kwargs):
        if argv[1] == "api":
            if "/git/ref/" in argv[2]:
                self.tag_reads += 1
                commit = "b" * 40 if self.move_tag_after_first_read and self.tag_reads > 1 else self.remote_commit
                target = dict(type="tag", sha="c" * 40) if self.annotated else dict(type="commit", sha=commit)
            else:
                target = dict(type="commit", sha=self.remote_commit)
            return subprocess.CompletedProcess(argv, 0, json.dumps(dict(object=target)), "")
        action = argv[2]
        if action == "view":
            if not self.exists:
                return subprocess.CompletedProcess(argv, 1, "", "release not found")
            value = dict(isDraft=self.draft, isPrerelease=self.prerelease, assets=[dict(name=name) for name in self.remote], url="https://github.com/o/r/releases/tag/v0.3.0")
            return subprocess.CompletedProcess(argv, 0, json.dumps(value), "")
        if action == "create":
            self.exists = True
            self.prerelease = "--prerelease" in argv
            self.created_notes = Path(argv[argv.index("--notes-file") + 1]).read_text()
            self.body = self.created_notes + "\ngenerated change history"
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
            publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertTrue(self.draft)
        self.fail_second_upload = False
        publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertFalse(self.draft)
        self.assertEqual(self.uploads, ["plugin.zip", "plugin.zip.sha256"])
        self.assertEqual(self.remote["human-notes.txt"], b"preserve")
        publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertEqual(len(self.uploads), 2)

    def test_different_existing_asset_is_preserved_and_blocks_publication(self):
        self.exists = True
        self.remote["plugin.zip"] = b"different"
        with self.assertRaisesRegex(RuntimeError, "no asset was overwritten"):
            publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertTrue(self.draft)
        self.assertEqual(self.remote["plugin.zip"], b"different")

    def test_published_release_is_never_repaired_by_silent_mutation(self):
        self.exists = True
        self.draft = False
        with self.assertRaisesRegex(RuntimeError, "Published release is missing"):
            publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertFalse(self.uploads)

    def test_rc_release_is_published_as_prerelease(self):
        publish_release.publish("o/r", "v0.3.0-rc.1", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertTrue(self.prerelease)
        self.assertFalse(self.draft)

    def test_invalid_targets_and_duplicate_names_fail_before_draft_creation(self):
        with self.assertRaises(ValueError):
            publish_release.publish("../..", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        with self.assertRaisesRegex(ValueError, "unique"):
            publish_release.publish("o/r", "v0.3.0", [self.assets[0], self.assets[0]], self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertFalse(self.exists)

    def test_annotated_remote_tag_is_peeled_to_expected_commit(self):
        self.annotated = True
        publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertFalse(self.draft)
        self.assertGreaterEqual(self.tag_reads, 3)

    def test_moved_tag_blocks_new_and_resumed_publication(self):
        self.remote_commit = "b" * 40
        for exists in (False, True):
            self.exists = exists
            with self.assertRaisesRegex(RuntimeError, "Remote release tag"):
                publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
            self.assertTrue(self.draft)
        self.assertFalse(self.uploads)

    def test_tag_moved_during_upload_blocks_final_publication(self):
        self.move_tag_after_first_read = True
        with self.assertRaisesRegex(RuntimeError, "Remote release tag"):
            publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertTrue(self.draft)

    def test_artifact_commit_mismatch_fails_before_any_remote_mutation(self):
        with zipfile.ZipFile(self.assets[0], "a") as archive:
            archive.comment = b"b" * 40
        with self.assertRaisesRegex(ValueError, "Artifact source commit"):
            publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertFalse(self.exists)
        self.assertEqual(self.tag_reads, 0)

    def test_reviewed_notes_are_used_and_existing_human_notes_preserved(self):
        publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertEqual(self.created_notes, self.notes.read_text())
        self.assertIn("generated change history", self.body)
        self.body = "human edited notes after publication"
        publish_release.publish("o/r", "v0.3.0", self.assets, self.run_gh, expected_commit=self.commit, notes_file=self.notes)
        self.assertEqual(self.body, "human edited notes after publication")


if __name__ == "__main__":
    unittest.main()
