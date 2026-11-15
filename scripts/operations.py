"""Discover GitHub operations and execute documented REST operations through gh."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote, urlencode

DATA = Path(__file__).resolve().parents[1] / "skills/full-github/data"


def load_catalog(graphql=False):
    filename = "graphql-operations.json" if graphql else "rest-operations.json"
    return json.loads((DATA / filename).read_text())


def build_request(operation, parameters, body=None, extra_headers=()):
    """Build argv without shell evaluation, keeping path and query inputs distinct."""
    if not isinstance(parameters, dict):
        raise ValueError("Parameters must be a JSON object")
    known = {p["name"] for p in operation["parameters"]}
    unknown = parameters.keys() - known
    if unknown:
        raise ValueError(f"Unknown parameters: {', '.join(sorted(unknown))}")
    endpoint = operation["path"]
    query = []
    headers = []
    accept = None
    for header in extra_headers:
        name, separator, value = header.partition(":")
        if not separator or not re.fullmatch(r"[A-Za-z0-9!#$%&'*+.^_`|~-]+", name) or "\n" in value or "\r" in value:
            raise ValueError("Invalid request header")
        headers.extend(["-H", header])
        if name.lower() == "accept":
            accept = value.strip().lower()
    for parameter in operation["parameters"]:
        name = parameter["name"]
        if name not in parameters:
            if parameter["required"]:
                raise ValueError(f"Missing parameter: {name}")
            continue
        value = parameters[name]
        location = parameter["location"]
        if location == "path":
            if value is None or isinstance(value, (dict, list, bool)) or str(value) in ("", ".", ".."):
                raise ValueError(f"Invalid path parameter: {name}")
            endpoint = endpoint.replace("{" + name + "}", quote(str(value), safe=""))
        elif location == "query":
            values = value if isinstance(value, list) else [value]
            encoded_values = []
            for item in values:
                if isinstance(item, (dict, list)) or item is None:
                    raise ValueError(f"Invalid query parameter: {name}")
                encoded_values.append(json.dumps(item) if isinstance(item, bool) else str(item))
            wire_name = parameter.get("wire_name", name)
            if isinstance(value, list) and not parameter.get("explode", True):
                separator = {"form": ",", "spaceDelimited": " ", "pipeDelimited": "|"}.get(parameter.get("style", "form"))
                if separator is None:
                    raise ValueError(f"Unsupported query style: {name}")
                query.append((wire_name, separator.join(encoded_values)))
            else:
                query.extend((wire_name, item) for item in encoded_values)
        elif location == "header":
            if not isinstance(value, (str, int)) or "\n" in str(value) or "\r" in str(value):
                raise ValueError(f"Invalid header parameter: {name}")
            headers.extend(["-H", f"{name}: {value}"])
        else:
            raise ValueError(f"Unsupported parameter location: {location}")
    if re.search(r"\{[^}]+\}", endpoint):
        raise ValueError("Unresolved path parameter")
    if query:
        endpoint += "?" + urlencode(query)
    endpoint = operation.get("server", "") + endpoint
    method = operation["method"]
    if operation["body_required"] and body is None:
        raise ValueError("This operation requires a request body")
    if body is not None and method in ("GET", "HEAD"):
        raise ValueError("Use query parameters for GET/HEAD requests")
    command = ["gh", "api", "--method", method, endpoint, *headers]
    if method == "GET" and "application/json" in operation.get("response_media_types", []) and accept in (None, "application/json", "application/vnd.github+json"):
        command.extend(["--paginate", "--slurp"])
    if body is not None:
        content_types = operation.get("body_content_types", [])
        has_content_type = any(header.lower().startswith("content-type:") for header in headers[1::2])
        if content_types and "application/json" not in content_types and not has_content_type:
            command.extend(["-H", f"Content-Type: {content_types[0]}"])
        command.extend(["--input", "-"])
    return command


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    search = commands.add_parser("search", help="Search all REST or GraphQL operations")
    search.add_argument("term", nargs="?", default="")
    search.add_argument("--graphql", action="store_true")
    describe = commands.add_parser("describe", help="Show parameters and official documentation")
    describe.add_argument("operation")
    describe.add_argument("--graphql", action="store_true")
    features = commands.add_parser("capabilities", help="Search source-backed feature families")
    features.add_argument("term", nargs="?", default="")
    feature = commands.add_parser("capability", help="Show a feature's operations, limitations and verification")
    feature.add_argument("name")
    schema = commands.add_parser("type", help="Inspect a GraphQL input, enum or result type")
    schema.add_argument("name")
    call = commands.add_parser("call", help="Execute one REST operation using current gh authentication")
    call.add_argument("operation")
    call.add_argument("--params", default="{}", help="JSON path, query and header parameters")
    call.add_argument("--body-file", type=Path, help="Request body file, sent unchanged, including binary bodies")
    call.add_argument("--dry-run", action="store_true", help="Print argv and body presence without executing")
    call.add_argument("--header", action="append", default=[], help="Additional request header, such as Accept or If-Match")
    args = parser.parse_args()
    if args.command in ("capabilities", "capability"):
        entries = json.loads((DATA / "capabilities.json").read_text())["capabilities"]
        if args.command == "capabilities":
            for entry in entries:
                if args.term.lower() in json.dumps(entry).lower():
                    print(f"{entry['id']}\t{entry['category']}\t{entry['capability']}")
            return 0
        for entry in entries:
            if entry["id"] == args.name:
                print(json.dumps(entry, indent=2))
                return 0
        parser.error("Unknown capability. Use capabilities to discover IDs.")
    if args.command == "type":
        types = load_catalog(True).get("types", {})
        if args.name not in types:
            parser.error("Unknown GraphQL type")
        print(json.dumps(types[args.name], indent=2))
        return 0
    catalog = load_catalog(getattr(args, "graphql", False))
    operations = catalog.get("operations")
    if operations is None:
        operations = {**catalog["queries"], **catalog["mutations"]}
    if args.command == "search":
        for name, operation in operations.items():
            if args.term.lower() in (name + " " + json.dumps(operation)).lower():
                kind = operation.get("method", "mutation" if name in catalog.get("mutations", {}) else "query")
                status = "retired" if operation.get("unavailable") else "deprecated" if operation.get("deprecated") or operation.get("isDeprecated") else "indexed"
                print(f"{name}\t{kind}\t{status}\t{operation.get('summary', '')}")
        return 0
    if args.operation not in operations:
        parser.error("Unknown operation. Use search to discover operation IDs.")
    operation = operations[args.operation]
    if args.command == "describe":
        print(json.dumps(operation, indent=2))
        return 0
    try:
        if operation.get("unavailable"):
            raise ValueError("Unavailable operation: " + operation["unavailable"]["reason"])
        parameters = json.loads(args.params)
        body = args.body_file.read_bytes() if args.body_file else None
        command = build_request(operation, parameters, body, args.header)
        if args.dry_run:
            print(json.dumps({"argv": command, "body_bytes": len(body) if body is not None else None}, indent=2))
            return 0
        return subprocess.run(command, input=body).returncode
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
