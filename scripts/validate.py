import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / ".codex-plugin/plugin.json").read_text())
assert manifest["name"] == "full-github"
assert (root / manifest["skills"] / "full-github/SKILL.md").is_file()
marketplace = json.loads((root / ".agents/plugins/marketplace.json").read_text())
assert marketplace["plugins"][0]["name"] == manifest["name"]
for reference in ("features.md", "workflows.md"):
    assert (root / "skills/full-github/references" / reference).is_file()
assert (root / "skills/full-github/SKILL.md").read_text().startswith("---\n")
print("Plugin manifest, marketplace and skill references are valid")
