"""Read-only GitHub snapshot. Failed endpoints remain unknown."""
import argparse
import json
import re
import subprocess
from urllib.parse import quote


REPOSITORY_READS = {
    "branches": "branches", "tags": "tags", "topics": "topics",
    "issue_types": "issue-types", "custom_properties": "properties/values",
    "autolinks": "autolinks", "codeowners_errors": "codeowners/errors",
    "collaborators": "collaborators", "teams": "teams",
    "actions_permissions": "actions/permissions",
    "workflow_permissions": "actions/permissions/workflow",
    "actions_policies": "actions/policies",
    "actions_retention": "actions/permissions/artifact-and-log-retention",
    "runners": "actions/runners", "actions_secret_names": "actions/secrets",
    "environments": "environments", "deployments": "deployments",
    "dependency_alerts": "dependabot/alerts",
    "dependabot_runner_settings": "dependabot/runner-settings",
    "code_scanning_setup": "code-scanning/default-setup",
    "code_scanning_analyses": "code-scanning/analyses",
    "code_quality_setup": "code-quality/setup",
    "security_configuration": "code-security-configuration",
    "private_reporting": "private-vulnerability-reporting",
    "immutable_releases": "immutable-releases", "pages": "pages",
    "interaction_limits": "interaction-limits", "webhooks": "hooks",
    "deploy_keys": "keys", "license": "license", "languages": "languages",
    "copilot_agent_configuration": "copilot/cloud-agent/configuration",
    "copilot_review_settings": "copilot/code-review/settings",
}

ORGANIZATION_READS = {
    "organization": "", "organization_teams": "/teams",
    "organization_roles": "/organization-roles", "organization_rulesets": "/rulesets",
    "organization_custom_properties": "/properties/schema",
    "organization_issue_types": "/issue-types", "organization_issue_fields": "/issue-fields",
    "organization_actions_permissions": "/actions/permissions",
    "organization_runner_groups": "/actions/runner-groups",
    "organization_security_configurations": "/code-security/configurations",
    "organization_installations": "/installations",
}


def read_probe(command, run):
    try:
        response = run(command, capture_output=True, text=True, timeout=60)
        if response.returncode:
            return {"status": "unknown", "error": response.stderr.strip()}
        if not response.stdout.strip():
            return {"status": "observed", "pages": [], "empty_response": True}
        pages = json.loads(response.stdout)
        if isinstance(pages, list) and any(isinstance(page, dict) and page.get("errors") for page in pages):
            return {"status": "unknown", "error": "GraphQL returned errors", "pages": pages}
        return {"status": "observed", "pages": pages}
    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError) as error:
        return {"status": "unknown", "error": str(error)}


def audit(repo, run=subprocess.run, organization=False, project=None):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo) or any(part in (".", "..") for part in repo.split("/")):
        raise ValueError("Expected OWNER/REPO")
    if project is not None and (not isinstance(project, int) or project < 1):
        raise ValueError("Project number must be positive")
    endpoints = {
        "repository": f"repos/{repo}",
        "labels": f"repos/{repo}/labels",
        "milestones": f"repos/{repo}/milestones?state=all",
        "rulesets": f"repos/{repo}/rulesets",
        "workflows": f"repos/{repo}/actions/workflows",
        "releases": f"repos/{repo}/releases",
        "community": f"repos/{repo}/community/profile",
    }
    endpoints.update({name: f"repos/{repo}/{path}" for name, path in REPOSITORY_READS.items()})
    owner = repo.split("/")[0]
    if organization:
        endpoints.update({key: f"orgs/{owner}{path}" for key, path in ORGANIZATION_READS.items()})
    result = {}
    for name, endpoint in endpoints.items():
        result[name] = read_probe(["gh", "api", "--paginate", "--slurp", endpoint], run)
    repository_pages = result["repository"].get("pages", [])
    if isinstance(repository_pages, list) and repository_pages and isinstance(repository_pages[0], dict):
        branch = repository_pages[0].get("default_branch")
        if branch:
            endpoint = f"repos/{repo}/branches/{quote(branch, safe='')}/protection"
            result["default_branch_protection"] = read_probe(["gh", "api", "--paginate", "--slurp", endpoint], run)
    if project is not None:
        owner_kind = "organization" if organization else "user"
        for key, connection, fields in (
            ("project_fields", "fields", "... on ProjectV2FieldCommon {id name dataType isIssueField} ... on ProjectV2SingleSelectField {options {id name color description}} ... on ProjectV2MultiSelectField {multiSelectOptions {id name color description}} ... on ProjectV2IterationField {configuration {duration startDay iterations {id title startDate duration} completedIterations {id title startDate duration}}}"),
            ("project_items", "items", "id type isArchived"),
            ("project_views", "views", "id name layout filter"),
        ):
            query = ("query($owner:String!,$number:Int!,$endCursor:String){" + owner_kind +
                     "(login:$owner){projectV2(number:$number){id title url " + connection +
                     "(first:100,after:$endCursor){nodes{" + fields + "}pageInfo{hasNextPage endCursor}}}}}")
            command = ["gh", "api", "graphql", "--paginate", "--slurp", "-f", "query=" + query,
                       "-F", "owner=" + owner, "-F", "number=" + str(project)]
            result[key] = read_probe(command, run)
            if result[key]["status"] == "observed":
                for page in result[key]["pages"]:
                    project_owner = page.get("data", {}).get(owner_kind)
                    if not project_owner or project_owner.get("projectV2") is None:
                        result[key]["status"] = "unknown"
                        result[key]["error"] = "Project is absent or inaccessible"
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository")
    parser.add_argument("--organization", action="store_true", help="Also inspect repository owner's organization configuration")
    parser.add_argument("--project", type=int, help="Inspect an owner Project's fields, items and views")
    args = parser.parse_args()
    try:
        snapshot = audit(args.repository, organization=args.organization, project=args.project)
    except (ValueError, subprocess.TimeoutExpired, OSError) as error:
        parser.exit(2, f"{error}\n")
    print(json.dumps(snapshot, indent=2))
