"""Regenerate operation indexes from official OpenAPI and live GraphQL JSON files."""
import argparse
import json
import hashlib
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("openapi", type=Path)
parser.add_argument("graphql", type=Path, help="Full GraphQL type introspection JSON")
parser.add_argument("--date", required=True, help="UTC retrieval date YYYY-MM-DD")
args = parser.parse_args()
spec = json.loads(args.openapi.read_text())


def resolve(value):
    while "$ref" in value:
        current = spec
        for part in value["$ref"].removeprefix("#/").split("/"):
            current = current[part.replace("~1", "/").replace("~0", "~")]
        value = current
    return value


operations = {}
data = Path(__file__).resolve().parents[1] / "skills/full-github/data"
retired = json.loads((data / "retired-operations.json").read_text())
for path, item in spec["paths"].items():
    for method, operation in item.items():
        if method not in {"get", "post", "put", "patch", "delete", "head", "options"}:
            continue
        parameters = [resolve(p) for p in item.get("parameters", []) + operation.get("parameters", [])]
        body = resolve(operation.get("requestBody", {}))
        schema = resolve(body.get("content", {}).get("application/json", {}).get("schema", {}))
        entry = {
            "method": method.upper(), "path": path, "category": operation["tags"][0],
            "summary": operation["summary"],
            "documentation": operation.get("externalDocs", {}).get("url", "https://docs.github.com/en/rest"),
            "parameters": [{"name": p["name"], "location": p["in"], "required": p.get("required", False),
                            "schema": p.get("schema", {}), "style": p.get("style", "form" if p["in"] == "query" else "simple"),
                            "explode": p.get("explode", p["in"] == "query"),
                            "wire_name": p["name"] + "[]" if p["name"] + "[]=" in str(p.get("schema", {}).get("example", "")) else p["name"]}
                           for p in parameters],
            "body_required": body.get("required", False),
            "body_content_types": sorted(body.get("content", {})),
            "body_fields": sorted(schema.get("properties", {})),
            "body_required_fields": schema.get("required", []),
            "deprecated": operation.get("deprecated", False),
        }
        media_types = set()
        for status, response in operation["responses"].items():
            if status.startswith(("2", "3")):
                media_types.update(resolve(response).get("content", {}))
        entry["response_media_types"] = sorted(media_types)
        if operation.get("servers"):
            entry["server"] = operation["servers"][0]["url"]
        if operation["operationId"] in retired:
            entry["unavailable"] = retired[operation["operationId"]]
        operations[operation["operationId"]] = entry
rest = {"source": "https://github.com/github/rest-api-description", "retrieved": args.date,
        "source_sha256": hashlib.sha256(args.openapi.read_bytes()).hexdigest(),
        "spec_version": spec["info"]["version"], "operations": operations}
(data / "rest-operations.json").write_text(json.dumps(rest, indent=2) + "\n")
graph = {"source": "https://docs.github.com/en/graphql/reference", "retrieved": args.date}
schema = json.loads(args.graphql.read_text())["data"]["__schema"]
types = schema["types"]
graph["types"] = {entry["name"]: entry for entry in types}
graph["query_type"] = schema["queryType"]["name"]
graph["mutation_type"] = schema["mutationType"]["name"]
graph["directives"] = schema["directives"]
graph["queries"] = {entry["name"]: entry for entry in graph["types"][graph["query_type"]]["fields"]}
graph["mutations"] = {entry["name"]: entry for entry in graph["types"][graph["mutation_type"]]["fields"]}
(data / "graphql-operations.json").write_text(json.dumps(graph, indent=2) + "\n")
print(f"Indexed {len(operations)} REST operations, {len(graph['queries'])} queries, {len(graph['mutations'])} mutations")
