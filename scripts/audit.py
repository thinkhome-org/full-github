"""Read-only GitHub snapshot. Failed endpoints remain unknown."""
import argparse
import json
import re
import subprocess


def audit(repo, run=subprocess.run):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError("Expected OWNER/REPO")
    endpoints = {
        "repository": f"repos/{repo}",
        "labels": f"repos/{repo}/labels",
        "milestones": f"repos/{repo}/milestones?state=all",
        "rulesets": f"repos/{repo}/rulesets",
        "workflows": f"repos/{repo}/actions/workflows",
        "releases": f"repos/{repo}/releases",
        "community": f"repos/{repo}/community/profile",
    }
    result = {}
    for name, endpoint in endpoints.items():
        try:
            response = run(["gh", "api", "--paginate", "--slurp", endpoint],
                           capture_output=True, text=True, timeout=60)
            if response.returncode:
                result[name] = {"status": "unknown", "error": response.stderr.strip()}
            else:
                result[name] = {"status": "observed", "pages": json.loads(response.stdout)}
        except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError) as error:
            result[name] = {"status": "unknown", "error": str(error)}
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository")
    args = parser.parse_args()
    try:
        snapshot = audit(args.repository)
    except (ValueError, subprocess.TimeoutExpired, OSError) as error:
        parser.exit(2, f"{error}\n")
    print(json.dumps(snapshot, indent=2))
