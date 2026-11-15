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
for plugin in marketplace["plugins"]:
    source = plugin["source"]
    assert source["source"] == "local", "This repository publishes local plugin sources"
    assert isinstance(source["path"], str) and source["path"].startswith("./"), "Plugin source must use a ./ path"
    assert "\\" not in source["path"], "Plugin source must use portable path separators"
    component = root
    for part in (*Path(source["path"]).parts, ".codex-plugin", "plugin.json"):
        component = component / part
        assert not component.is_symlink(), f"Symlink in plugin source: {component}"
        assert component.resolve().is_relative_to(root), "Plugin source escapes the repository"
    plugin_root = (root / source["path"]).resolve()
    assert plugin_root.is_relative_to(root), "Plugin source escapes the repository"
    plugin_manifest = plugin_root / ".codex-plugin/plugin.json"
    assert plugin_manifest.is_file(), f"Plugin source manifest missing: {plugin_manifest}"
    assert json.loads(plugin_manifest.read_text())["name"] == plugin["name"], "Plugin source identity does not match marketplace"
    policy = plugin.get("policy", {})
    assert policy.get("installation", "AVAILABLE") in ("AVAILABLE", "NOT_AVAILABLE", "INSTALLED_BY_DEFAULT"), "Unsupported installation policy"
    assert policy.get("authentication", "ON_INSTALL") in ("ON_INSTALL", "ON_USE"), "Unsupported authentication policy"
    products = policy.get("products")
    assert products is None or (isinstance(products, list) and all(
        product in ("chatgpt", "codex", "atlas", "CHATGPT", "CODEX", "ATLAS") for product in products)), "Unsupported product restrictions"
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
