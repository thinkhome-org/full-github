import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / ".codex-plugin/plugin.json").read_text())
assert manifest["name"] == "full-github"
assert (root / manifest["skills"] / "full-github/SKILL.md").is_file()
marketplace = json.loads((root / ".agents/plugins/marketplace.json").read_text())
assert marketplace["plugins"][0]["name"] == manifest["name"]
for reference in ("features.md", "workflows.md", "operations.md", "collaboration.md", "delivery-security.md", "administration.md"):
    assert (root / "skills/full-github/references" / reference).is_file()
assert (root / "skills/full-github/SKILL.md").read_text().startswith("---\n")
data = root / "skills/full-github/data"
capabilities = json.loads((data / "capabilities.json").read_text())["capabilities"]
assert len({entry["id"] for entry in capabilities}) == len(capabilities)
for entry in capabilities:
    for field in ("id", "category", "capability", "operations", "surfaces", "source", "verification", "limitations"):
        assert entry.get(field), (entry["id"], field)
rest = json.loads((data / "rest-operations.json").read_text())["operations"]
retired = json.loads((data / "retired-operations.json").read_text())
assert retired.keys() <= rest.keys()
for name, reason in retired.items():
    assert rest[name].get("unavailable") == reason
graphql = json.loads((data / "graphql-operations.json").read_text())
assert set(graphql["mutations"]) == {entry["name"] for entry in graphql["types"]["Mutation"]["fields"]}
assert set(graphql["queries"]) == {entry["name"] for entry in graphql["types"]["Query"]["fields"]}
print(f"Validated {len(capabilities)} capabilities, {len(rest)} REST operations and {len(graphql['types'])} GraphQL types")
print("Plugin manifest, marketplace and skill references are valid")
