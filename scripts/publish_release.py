"""Resume a draft release and publish only after asset bytes match local artifacts."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile


def publish(repo, tag, assets, run=subprocess.run):
    if (
        not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo)
        or any(part in (".", "..") for part in repo.split("/"))
        or not re.fullmatch(r"v\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?", tag)
    ):
        raise ValueError("Invalid repository or release tag")
    if not assets or any(not path.is_file() for path in assets):
        raise ValueError("Every release asset must exist before publication")
    if len({path.name for path in assets}) != len(assets):
        raise ValueError("Release asset names must be unique")
    prerelease = "-" in tag

    def gh(*arguments, check=True):
        return run(["gh", *arguments, "--repo", repo], capture_output=True, text=True, check=check)

    response = gh("release", "view", tag, "--json", "isDraft,isPrerelease,assets,url", check=False)
    if response.returncode:
        if "release not found" not in response.stderr.lower():
            raise RuntimeError(response.stderr)
        flags = ["--draft", "--verify-tag", "--generate-notes", "--title", "Full GitHub " + tag[1:]]
        if prerelease:
            flags.append("--prerelease")
        gh("release", "create", tag, *flags)
        response = gh("release", "view", tag, "--json", "isDraft,isPrerelease,assets,url")
    release = json.loads(response.stdout)
    if release["isPrerelease"] != prerelease:
        if not release["isDraft"]:
            raise RuntimeError("Published release classification conflicts with its tag; preserve history and investigate")
        gh("release", "edit", tag, "--prerelease=" + str(prerelease).lower())
    existing = {asset["name"] for asset in release["assets"]}
    for path in assets:
        if path.name not in existing:
            if not release["isDraft"]:
                raise RuntimeError("Published release is missing an expected asset; preserve publication history and investigate")
            gh("release", "upload", tag, str(path.resolve()))
        with tempfile.TemporaryDirectory() as temporary:
            gh("release", "download", tag, "--pattern", path.name, "--dir", temporary)
            downloaded = Path(temporary) / path.name
            if hashlib.sha256(downloaded.read_bytes()).digest() != hashlib.sha256(path.read_bytes()).digest():
                raise RuntimeError(f"Existing asset differs from the build: {path.name}; no asset was overwritten")
    if release["isDraft"]:
        gh("release", "edit", tag, "--draft=false")
    final = json.loads(gh("release", "view", tag, "--json", "isDraft,isPrerelease,url").stdout)
    if final["isDraft"] or final["isPrerelease"] != prerelease:
        raise RuntimeError("Release publication state does not match its tag")
    return final["url"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("assets", type=Path, nargs="+")
    args = parser.parse_args()
    print(publish(args.repo, args.tag, args.assets))
