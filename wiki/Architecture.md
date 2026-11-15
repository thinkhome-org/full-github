# Architecture

The native Codex plugin packages one orchestration skill, domain runbooks, a capability catalog and operation registries.

## Discovery

The capability catalog records 258 feature families, actual interfaces, official sources, permission/plan gates and verification. The REST registry is generated from GitHub's official OpenAPI description. GraphQL operations and input/result types come from live introspection.

operations.py searches and describes exact operations without loading full registries into the model context. The REST executor builds gh argv using encoded path/query parameters and passes payloads through stdin. GraphQL uses native gh with structured variables.

## Workflow

The agent establishes context, assigns a coverage row to every applicable family, discovers operations, inspects live state and reconciles authorized changes. Domain discovery can run across independent agents. Read-back evidence and repeat reconciliation close each change.

audit.py probes repository/organization settings and paginated Project fields/items/views. Unknown failures remain visible. GITHUB.md and AGENTS.md preserve repository-specific rules across sessions.

## Distribution and maintenance

The Git marketplace installs the versioned plugin into Codex. CI validates tests, manifests, catalog schema and generated documentation. CodeQL scans Python. The Wiki mirrors source-controlled pages. See [[API]] for registry refresh.
