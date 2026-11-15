"""Render the published capability and operation directories from their registries."""
import argparse
from collections import defaultdict
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = root / "skills/full-github/data"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--check", action="store_true")
args = parser.parse_args()


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


features = json.loads((data / "capabilities.json").read_text())
rest = json.loads((data / "rest-operations.json").read_text())
graphql = json.loads((data / "graphql-operations.json").read_text())
lines = ["# GitHub capability directory", "", f"Reviewed {features['retrieved']}. {len(features['capabilities'])} feature families.", "",
         "Search using python3 scripts/operations.py capabilities TERM. Inspect a family using capability ID.", "",
         "Each linked official source defines current permissions, product limits and operation details. The catalog records available interfaces and evidence requirements. Live verification is recorded separately in docs/VERIFICATION.md.", ""]
groups = defaultdict(list)
for entry in features["capabilities"]:
    groups[entry["category"]].append(entry)
for category, entries in sorted(groups.items()):
    lines.extend([f"## {category}", "", "| ID | Capability | Interfaces | Official source |", "| --- | --- | --- | --- |"])
    for entry in entries:
        sources = entry["source"]
        if isinstance(sources, str):
            sources = [sources]
        links = " ".join(f"[Docs {number}]({url})" for number, url in enumerate(sources, 1))
        lines.append(f"| {cell(entry['id'])} | {cell(entry['capability'])} | {cell(', '.join(entry['surfaces']))} | {links} |")
    lines.append("")
outputs = {root / "docs/CAPABILITIES.md": "\n".join(lines) + "\n"}
lines = ["# GitHub operation directory", "", f"Snapshot {rest['retrieved']}. {len(rest['operations'])} published REST operations, {len(graphql['queries'])} GraphQL queries and {len(graphql['mutations'])} mutations.", "",
         "The directory includes deprecated and retired operations. Availability and permissions vary by host, plan, credential and rollout. Retired entries are blocked by the executor.", "",
         "Use python3 scripts/operations.py search TERM and describe OPERATION for current bundled parameters. For GraphQL add --graphql, then inspect argument types with the type command.", ""]
groups = defaultdict(list)
for name, operation in rest["operations"].items():
    groups[operation["category"]].append((name, operation))
for category, entries in sorted(groups.items()):
    lines.extend([f"## REST {category}", "", "| Operation | Method | Route | Availability |", "| --- | --- | --- | --- |"])
    for name, operation in entries:
        status = "retired" if operation.get("unavailable") else "deprecated" if operation.get("deprecated") else "indexed"
        lines.append(f"| [{name}]({operation['documentation']}) | {operation['method']} | {cell(operation['path'])} | {status} |")
    lines.append("")
for kind in ("queries", "mutations"):
    lines.extend([f"## GraphQL {kind}", "", "| Operation | Availability |", "| --- | --- |"])
    for name, operation in sorted(graphql[kind].items()):
        status = "deprecated" if operation.get("isDeprecated") else "indexed"
        lines.append(f"| {name} | {status} |")
    lines.append("")
outputs[root / "docs/OPERATIONS.md"] = "\n".join(lines) + "\n"
for path, content in outputs.items():
    if args.check:
        if not path.exists() or path.read_text() != content:
            raise SystemExit(f"Outdated generated catalog: {path.name}")
    else:
        path.write_text(content)
print("Capability and operation directories are current")
