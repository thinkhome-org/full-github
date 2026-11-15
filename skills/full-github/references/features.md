# Full capability profile

The catalog covers 258 source-backed feature families across collaboration, delivery/security and administration. The operation registry indexes 1,281 published REST operations and the live GraphQL schema, including deprecated and retired entries identified separately. Snapshot date is 2026-11-15.

Use the machine-readable catalog through operations.py capabilities or capability ID. Each entry contains operations, access surfaces, official sources, verification and limitations. Read the relevant sections of these references.

| Reference | Coverage |
| --- | --- |
| [Collaboration](collaboration.md) | Repository identity/content/Git, Issues and shared fields, sub-issues/dependencies, PR stacks and Agent Merge, protection/rulesets, Projects fields/views/workflows/status updates/insights, Discussions, Wiki, search and notifications |
| [Delivery and security](delivery-security.md) | Actions and policies, runs/jobs/logs/artifacts/caches/concurrency, runners, secrets/variables/OIDC, environments/deployments, code scanning/quality, Dependabot/dependency graph, secret scanning, advisories, campaigns, releases/attestations, Packages and Pages |
| [Administration](administration.md) | User/org/enterprise identity and policies, roles/teams/membership, custom properties, apps/OAuth/tokens/webhooks/audit, billing/usage, migrations, Codespaces/LFS, Copilot and Spaces, agent tasks/automations/credentials, private registries and historical closed APIs |
| [Operation execution](operations.md) | Complete REST operation search/describe/call, GraphQL input types, token constraints, compatibility, registry refresh and retirement handling |

## Coverage and applicability

A full setup produces one decision per feature family. For each, record its ID, desired state, observed state, action, permission/plan gate, verification and final state. Expensive or enterprise-only features still receive an explicit entry. Enable applicable features within existing authorization and rights.

The catalog also covers personal, organization and enterprise operations beyond a repository. Determine ownership and authorization before acting. A public repository does not imply organization administration permission.

The REST index comes from GitHub's official OpenAPI description. The GraphQL index comes from live authenticated schema introspection. These schemas can contain deprecated endpoints that are closed or scheduled for closure. Closed endpoints carry unavailable metadata and the executor refuses them. Capabilities may remain behind a plan, preview, GitHub App permission or UI.

Use current official documentation and live schema to settle drift. GitHub Enterprise Server has a versioned surface; compare its schema and docs with the indexed GitHub.com snapshot. No catalog snapshot guarantees future availability.
