import json
import gzip
import hashlib
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / ".codex-plugin/plugin.json").read_text())
assert manifest["name"] == "full-github"
assert (root / manifest["skills"] / "full-github/SKILL.md").is_file()
marketplace = json.loads((root / ".agents/plugins/marketplace.json").read_text())
assert marketplace["plugins"][0]["name"] == manifest["name"]
for reference in ("features.md", "workflows.md", "operations.md", "collaboration.md", "delivery-security.md", "administration.md", "collaboration-options.md", "delivery-options.md", "administration-options.md", "history-interaction.md"):
    assert (root / "skills/full-github/references" / reference).is_file()
assert (root / "skills/full-github/SKILL.md").read_text().startswith("---\n")
data = root / "skills/full-github/data"
capabilities = json.loads((data / "capabilities.json").read_text())["capabilities"]
assert len({entry["id"] for entry in capabilities}) == len(capabilities)
for entry in capabilities:
    for field in ("id", "category", "capability", "operations", "surfaces", "source", "verification", "limitations"):
        assert entry.get(field), (entry["id"], field)
rest_index = json.loads((data / "rest-operations.json").read_text())
rest = rest_index["operations"]
with gzip.open(data / "rest-schema.json.gz", "rb") as source:
    assert hashlib.sha256(source.read()).hexdigest() == rest_index["source_sha256"]
groups = json.loads((data / "configuration-options.json").read_text())["groups"]
assert len(groups) == len({group["id"] for group in groups})
assert {entry["id"] for entry in capabilities} == {name for group in groups for name in group["capability_ids"]}
for group in groups:
    assert group["sources"] and group["options"], group["id"]
    for option in group["options"]:
        assert all(option.get(field) for field in ("name", "values", "decision_rule", "verification")), group["id"]
errata = json.loads((data / "api-errata.json").read_text())
assert errata.keys() <= rest.keys()
retired = json.loads((data / "retired-operations.json").read_text())
assert retired.keys() <= rest.keys()
for name, reason in retired.items():
    assert rest[name].get("unavailable") == reason
graphql = json.loads((data / "graphql-operations.json").read_text())
assert set(graphql["mutations"]) == {entry["name"] for entry in graphql["types"]["Mutation"]["fields"]}
assert set(graphql["queries"]) == {entry["name"] for entry in graphql["types"]["Query"]["fields"]}
print(f"Validated {len(capabilities)} capabilities, {len(rest)} REST operations and {len(graphql['types'])} GraphQL types")
print("Plugin manifest, marketplace and skill references are valid")
