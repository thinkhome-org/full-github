"""Discover GitHub operations and execute documented REST operations through gh."""
import argparse
import json
import gzip
from pathlib import Path
import re
import subprocess
import sys
import sqlite3
from urllib.parse import quote, urlencode
import execution_history

DATA = Path(__file__).resolve().parents[1] / "skills/full-github/data"


def load_catalog(graphql=False):
    filename = "graphql-operations.json" if graphql else "rest-operations.json"
    return json.loads((DATA / filename).read_text())


def json_pointer(document, pointer):
    if pointer in ("", "#"):
        return document
    pointer = pointer.removeprefix("#")
    if not pointer.startswith("/"):
        raise ValueError("Use a JSON pointer beginning with / or #/")
    current = document
    for token in pointer[1:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current


def inspect_schema(operation, section="operation", pointer=""):
    with gzip.open(DATA / "rest-schema.json.gz", "rt") as source:
        spec = json.load(source)
    value = spec["paths"][operation["path"]][operation["method"].lower()]
    if section == "document":
        value = spec
    elif section != "operation":
        value = value[section]
    def dereference(current):
        seen = set()
        while isinstance(current, dict) and "$ref" in current:
            reference = current["$ref"]
            if reference in seen:
                raise ValueError("Cyclic schema reference")
            seen.add(reference)
            current = json_pointer(spec, reference)
        return current
    pointer = pointer.removeprefix("#")
    if pointer and not pointer.startswith("/"):
        raise ValueError("Use a JSON pointer beginning with / or #/")
    for token in pointer[1:].split("/") if pointer else []:
        token = token.replace("~1", "/").replace("~0", "~")
        value = dereference(value)
        value = value[int(token)] if isinstance(value, list) else value[token]
    return dereference(value)


def collection_items(page, pointer=""):
    if pointer:
        items = json_pointer(page, pointer)
    elif isinstance(page, list):
        items = page
    elif isinstance(page, dict):
        arrays = [value for value in page.values() if isinstance(value, list)]
        if len(arrays) != 1:
            raise ValueError("Select the collection using --items-pointer")
        items = arrays[0]
    else:
        raise ValueError("Response does not contain a collection")
    if not isinstance(items, list):
        raise ValueError("Collection pointer must identify an array")
    return items


def collect_pages(operation, parameters, pointer="", headers=(), run=subprocess.run):
    if operation["method"] != "GET" or "application/json" not in operation.get("response_media_types", []):
        raise ValueError("collect requires a JSON GET operation")
    definitions = {p["name"]: p for p in operation["parameters"]}
    if not {"page", "per_page"} <= definitions.keys():
        raise ValueError("This operation uses a different pagination protocol; inspect its schema and use native pagination")
    if parameters.get("page", 1) != 1:
        raise ValueError("A complete collection starts at page 1; use call for an individual page")
    page_size = parameters.get("per_page", definitions["per_page"]["schema"].get("default", 30))
    if not isinstance(page_size, int) or isinstance(page_size, bool) or page_size < 1:
        raise ValueError("per_page must be a positive integer")
    report = {"complete": False, "pages": [], "item_count": 0, "per_page": page_size}
    seen_pages = set()
    page_number = 1
    expected_total = None
    while True:
        params = dict(parameters, page=page_number, per_page=page_size)
        command = build_request(operation, params, extra_headers=headers)
        command = [part for part in command if part not in ("--paginate", "--slurp")]
        try:
            response = run(command, capture_output=True, text=True, timeout=60)
            if response.returncode:
                report["error"] = response.stderr.strip() or f"GitHub CLI exited {response.returncode}"
                return report
            page = json.loads(response.stdout)
            report["pages"].append(page)
            items = collection_items(page, pointer)
        except (ValueError, KeyError, IndexError, OSError, subprocess.TimeoutExpired) as error:
            report["error"] = str(error)
            return report
        fingerprint = json.dumps(items, sort_keys=True)
        if items and fingerprint in seen_pages:
            report["error"] = "Pagination made no progress; the server repeated a page"
            return report
        seen_pages.add(fingerprint)
        report["item_count"] += len(items)
        if isinstance(page, dict) and page.get("incomplete_results") is True:
            report["error"] = "GitHub reported incomplete search results; narrow the query and reconcile each scope"
            return report
        if isinstance(page, dict) and isinstance(page.get("total_count"), int):
            if expected_total is not None and expected_total != page["total_count"]:
                report["error"] = "Collection total changed during pagination; reconcile against a stable scope"
                return report
            expected_total = page["total_count"]
            report["expected_total"] = expected_total
        has_next = page.get("has_next_page") if isinstance(page, dict) else None
        finished = has_next is False or (has_next is None and (not items or expected_total == report["item_count"]))
        if finished:
            if expected_total is not None and report["item_count"] != expected_total:
                report["error"] = "Collected item count does not match total_count"
            else:
                report["complete"] = True
            return report
        if not items:
            report["error"] = "Server claims a next page but returned no items"
            return report
        page_number += 1


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
    option_groups = commands.add_parser("options", help="Find nested configuration choices and decision rules")
    option_groups.add_argument("term", nargs="?", default="")
    option_group = commands.add_parser("option", help="Inspect one configuration group or a named option")
    option_group.add_argument("group")
    option_group.add_argument("--name", help="Filter options by name")
    schema = commands.add_parser("type", help="Inspect a GraphQL input, enum or result type")
    schema.add_argument("name")
    rest_schema = commands.add_parser("schema", help="Inspect the full official REST schema, including nested options and constraints")
    rest_schema.add_argument("operation")
    rest_schema.add_argument("--section", choices=["operation", "parameters", "requestBody", "responses", "document"], default="operation")
    rest_schema.add_argument("--pointer", default="", help="JSON pointer within the selected section; references are resolved")
    call = commands.add_parser("call", help="Execute one REST operation using current gh authentication")
    call.add_argument("operation")
    call.add_argument("--params", default="{}", help="JSON path, query and header parameters")
    call.add_argument("--body-file", type=Path, help="Request body file, sent unchanged, including binary bodies")
    call.add_argument("--dry-run", action="store_true", help="Print argv and body presence without executing")
    call.add_argument("--header", action="append", default=[], help="Additional request header, such as Accept or If-Match")
    call.add_argument("--context", default="", help="GitHub issue/PR/discussion URL explaining the operation")
    call.add_argument("--no-history", action="store_true", help="Execute without local history, for explicitly ephemeral inspection")
    collect = commands.add_parser("collect", help="Collect page-based JSON data even when Link headers are missing")
    collect.add_argument("operation")
    collect.add_argument("--params", default="{}")
    collect.add_argument("--items-pointer", default="", help="JSON pointer to the array when the response contains multiple arrays")
    collect.add_argument("--header", action="append", default=[])
    collect.add_argument("--context", default="")
    collect.add_argument("--no-history", action="store_true")
    history = commands.add_parser("history", help="Read the local append-only execution history")
    history.add_argument("--limit", type=int, default=100, help="Recent event count; 0 returns all events")
    verify = commands.add_parser("verify-event", help="Append a read-back verification reference to a recorded execution")
    verify.add_argument("run_id")
    verify.add_argument("--outcome", choices=["matched", "mismatch", "unknown"], required=True)
    verify.add_argument("--evidence", required=True)
    args = parser.parse_args()
    if args.command in ("history", "verify-event"):
        try:
            if args.command == "history":
                print(json.dumps(execution_history.read_events(args.limit), indent=2))
            else:
                execution_history.verify(args.run_id, args.outcome, args.evidence)
            return 0
        except (ValueError, OSError, sqlite3.Error) as error:
            parser.error(str(error))
    if args.command in ("options", "option"):
        groups = json.loads((DATA / "configuration-options.json").read_text())["groups"]
        if args.command == "options":
            for group in groups:
                if args.term.lower() in json.dumps(group).lower():
                    print(f"{group['id']}\t{group.get('title', '')}\t{len(group['options'])} decisions")
            return 0
        for group in groups:
            if group["id"] == args.group:
                if args.name:
                    group = dict(group, options=[option for option in group["options"] if args.name.lower() in option["name"].lower()])
                    if not group["options"]:
                        parser.error("No matching option name")
                print(json.dumps(group, indent=2))
                return 0
        parser.error("Unknown option group")
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
    if args.command == "schema":
        try:
            print(json.dumps(inspect_schema(operation, args.section, args.pointer), indent=2))
            return 0
        except (KeyError, ValueError, IndexError) as error:
            parser.error(f"Schema location unavailable: {error}")
    if args.command == "describe":
        notes = json.loads((DATA / "api-errata.json").read_text()).get(args.operation)
        if notes:
            operation = dict(operation, operational_notes=notes)
        print(json.dumps(operation, indent=2))
        return 0
    try:
        if operation.get("unavailable"):
            raise ValueError("Unavailable operation: " + operation["unavailable"]["reason"])
        parameters = json.loads(args.params)
        if not isinstance(parameters, dict):
            raise ValueError("Parameters must be a JSON object")
        if args.command == "collect":
            def perform():
                report = collect_pages(operation, parameters, args.items_pointer, args.header)
                print(json.dumps(report, indent=2))
                return 0 if report["complete"] else 1
            return execute_recorded(args, operation, parameters, perform)
        body = args.body_file.read_bytes() if args.body_file else None
        command = build_request(operation, parameters, body, args.header)
        if args.dry_run:
            preview = list(command)
            for index, argument in enumerate(preview):
                if index and preview[index - 1] == "-H":
                    name = argument.partition(":")[0].lower()
                    if name in ("authorization", "proxy-authorization", "cookie") or any(part in name for part in ("secret", "token", "api-key")):
                        preview[index] = argument.partition(":")[0] + ": [redacted]"
            print(json.dumps({"argv": preview, "body_bytes": len(body) if body is not None else None}, indent=2))
            return 0
        return execute_recorded(args, operation, parameters, lambda: subprocess.run(command, input=body).returncode)
    except (ValueError, OSError, sqlite3.Error) as error:
        print(str(error), file=sys.stderr)
        return 2


def execute_recorded(args, operation, parameters, perform):
    if args.no_history:
        return perform()
    run_id = execution_history.start(args.operation, operation, parameters, args.context)
    print(f"Execution history {run_id}", file=sys.stderr)
    try:
        returncode = perform()
    except BaseException:
        execution_history.finish(run_id, None)
        raise
    execution_history.finish(run_id, returncode)
    return returncode


if __name__ == "__main__":
    sys.exit(main())
