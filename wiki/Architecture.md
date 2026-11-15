# Architecture

The native Codex plugin packages one orchestration skill, domain runbooks, a capability catalog and operation registries.

## Discovery

The capability catalog records 261 feature families, actual interfaces, official sources, permission/plan gates and verification. The REST registry is generated from GitHub's official OpenAPI description. GraphQL operations and input/result types come from live introspection.

operations.py searches and describes exact operations without loading full registries into the model context. The REST executor builds gh argv using encoded path/query parameters and passes payloads through stdin. GraphQL uses native gh with structured variables.

## Workflow

The agent establishes context, assigns a coverage row to every applicable family, discovers operations, inspects live state and reconciles authorized changes. Domain discovery can run across independent agents. Read-back evidence and repeat reconciliation close each change.

audit.py probes repository/organization settings and paginated Project fields/items/views. Unknown failures remain visible. GITHUB.md and AGENTS.md preserve repository-specific rules across sessions.

## Distribution and maintenance

The Git marketplace installs the versioned plugin into Codex. CI validates tests, manifests, catalog schema and generated documentation. CodeQL scans Python. The Wiki mirrors source-controlled pages. See [[API]] for registry refresh.

## Configuration and execution records

The complete official REST source is stored compressed with a digest. The option layer maps every capability to concrete values and project decision/verification rules, including dated official and community evidence. Source-backed errata remain distinct from the original schema.

The executor journals attempts/results in private local SQLite state and records later verification references separately. Native GitHub records preserve actors, reviews, discussion/Wiki history and publication. Release jobs produce checksums and provenance and resume partial drafts without overwriting asset bytes.
