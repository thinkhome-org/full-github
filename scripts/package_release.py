"""Package committed plugin files, including hidden manifests, for a matching tag."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile


def package(root, output, tag):
    if not re.fullmatch(r"v\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?", tag):
        raise ValueError("Expected a v-prefixed release version")
    output.mkdir(parents=True, exist_ok=True)
    filename = f"full-github-{tag[1:]}.zip"
    with tempfile.TemporaryDirectory(dir=output) as temporary:
        archive = Path(temporary) / filename
        subprocess.run(["git", "archive", "--format=zip", "--prefix=full-github/", "-o", str(archive.resolve()), "HEAD"], cwd=root, check=True)
        with zipfile.ZipFile(archive) as zipped:
            if zipped.testzip() is not None:
                raise ValueError("Invalid ZIP payload")
            manifest = json.loads(zipped.read("full-github/.codex-plugin/plugin.json"))
            if manifest["version"] != tag[1:]:
                raise ValueError("Tag does not match the committed plugin version")
            for required in (".agents/plugins/marketplace.json", "skills/full-github/SKILL.md", "NOTICE.md"):
                zipped.getinfo("full-github/" + required)
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
