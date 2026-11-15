"""Package committed plugin files, including hidden manifests, for a matching tag."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import tempfile
import zipfile


def read_archive_file(zipped, relative):
    """Read committed bytes without following nonportable symlink components."""
    if PurePosixPath(relative).is_absolute() or "\\" in relative:
        raise ValueError("Archive path must be portable and relative")
    components = ["full-github"]
    for part in PurePosixPath(relative).parts:
        if part == "..":
            if len(components) == 1:
                raise ValueError("Archive path escapes the repository")
            components.pop()
            continue
        components.append(part)
        path = "/".join(components)
        try:
            info = zipped.getinfo(path)
        except KeyError:
            try:
                info = zipped.getinfo(path + "/")
            except KeyError as error:
                raise ValueError(f"Missing committed archive path: {relative}") from error
        if stat.S_ISLNK(info.external_attr >> 16):
            raise ValueError(f"Symlink in committed archive path: {path}")
    return zipped.read("/".join(components))


def package(root, output, tag):
    if not re.fullmatch(r"v\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?", tag):
        raise ValueError("Expected a v-prefixed release version")
    source_commit = subprocess.check_output(["git", "rev-parse", "HEAD^{commit}"], cwd=root, text=True).strip()
    tag_commit = subprocess.check_output(["git", "rev-parse", "--verify", f"refs/tags/{tag}^{{commit}}"], cwd=root, text=True).strip()
    if source_commit != tag_commit:
        raise ValueError("Release tag does not point to the checked-out source commit")
    output.mkdir(parents=True, exist_ok=True)
    filename = f"full-github-{tag[1:]}.zip"
    with tempfile.TemporaryDirectory(dir=output) as temporary:
        archive = Path(temporary) / filename
        subprocess.run(["git", "archive", "--format=zip", "--prefix=full-github/", "-o", str(archive.resolve()), source_commit], cwd=root, check=True)
        with zipfile.ZipFile(archive) as zipped:
            if zipped.testzip() is not None:
                raise ValueError("Invalid ZIP payload")
            manifest = json.loads(read_archive_file(zipped, ".codex-plugin/plugin.json"))
            if manifest["version"] != tag[1:]:
                raise ValueError("Tag does not match the committed plugin version")
            for required in (".agents/plugins/marketplace.json", "skills/full-github/SKILL.md", "NOTICE.md"):
                read_archive_file(zipped, required)
            marketplace = json.loads(read_archive_file(zipped, ".agents/plugins/marketplace.json"))
            for plugin in marketplace.get("plugins", []):
                source = plugin["source"]
                if source["source"] != "local" or not isinstance(source["path"], str) or not source["path"].startswith("./"):
                    raise ValueError("Marketplace source must be a local ./ path")
                plugin_manifest = json.loads(read_archive_file(zipped, source["path"] + "/.codex-plugin/plugin.json"))
                if plugin_manifest.get("name") != plugin["name"]:
                    raise ValueError("Committed plugin source identity does not match marketplace")
        destination = output / filename
        archive.replace(destination)
    checksum = hashlib.sha256(destination.read_bytes()).hexdigest()
    (output / (filename + ".sha256")).write_text(checksum + "  " + filename + "\n")
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(package(Path(__file__).resolve().parents[1], args.output.resolve(), args.tag))
