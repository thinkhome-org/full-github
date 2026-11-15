# Full GitHub

[![Checks](https://github.com/thinkhome-org/full-github/actions/workflows/check.yml/badge.svg)](https://github.com/thinkhome-org/full-github/actions/workflows/check.yml)
[![CodeQL](https://github.com/thinkhome-org/full-github/actions/workflows/security.yml/badge.svg)](https://github.com/thinkhome-org/full-github/actions/workflows/security.yml)
[![Release](https://img.shields.io/github/v/release/thinkhome-org/full-github)](https://github.com/thinkhome-org/full-github/releases)

A native Codex plugin for discovering, configuring and using GitHub throughout a project's life. Published by ThinkHome.

## Coverage

The 2026-11-15 inventory contains **261 capability families**, **1,281 published REST operations**, **32 GraphQL queries**, **285 GraphQL mutations** and **1,881 GraphQL types**. Deprecated and retired operations are identified separately. Eighteen confirmed retired operations are blocked by the REST executor.

- Repository content, Git, Issues, owner issue fields, sub-issues/dependencies, PR stacks, Agent Merge, reviews, rulesets and merge queues.
- Projects fields/options, table/board/roadmap views, view CRUD, workflows, status updates, templates and Insights.
- Discussions, Wiki, search, notifications and collaboration.
- Actions policies, runs, jobs, logs, artifacts, caches, concurrency, runners, environments, approvals, secrets/variables and OIDC.
- Code scanning/quality, Dependabot/dependency graph, secret scanning, security advisories, campaigns and organizational security.
- Releases, assets, attestations, Packages, Pages and deployments.
- Organization/enterprise roles, membership, teams, apps, webhooks, audit, billing, properties, migrations, Codespaces/LFS, Copilot/Spaces, agents/tasks/automations and credentials.

Browse the [capability directory](docs/CAPABILITIES.md) and [complete operation directory](docs/OPERATIONS.md). Each capability has operations, interfaces, official sources, permission gates and verification criteria in the bundled catalog. See [verification](docs/VERIFICATION.md) for executed checks.

## Install

Requires Codex with plugin support, Python 3.10 or newer, Git and authenticated GitHub CLI.

```sh
codex plugin marketplace add thinkhome-org/full-github
codex plugin add full-github@thinkhome
```

For an existing installation, run codex plugin marketplace upgrade thinkhome, then codex plugin add full-github@thinkhome. Open a new Codex chat in your repository and select Full GitHub.

## Use from Codex

- “Audit this repository with Full GitHub and cover every capability.”
- “Set up this repository using the full profile, preserving existing content.”
- “Deliver this issue and maintain its Project, reviews, Wiki and release.”
- “Inspect organization capabilities and report which permissions are missing.”

The agent discovers individual capabilities and uses existing gh, Git, connectors and UI tools. Full setup evaluates the entire catalog and records explicit configuration, applicability and permission evidence. Repository-specific instructions are maintained in GITHUB.md linked from AGENTS.md. Skill selection and automatic invocation depend on the Codex host.

## Discover and execute exact operations

```sh
python3 scripts/operations.py capabilities projects
python3 scripts/operations.py search issue-field
python3 scripts/operations.py describe repos/get
python3 scripts/operations.py call repos/get --params '{"owner":"thinkhome-org","repo":"full-github"}'
python3 scripts/operations.py search ProjectV2 --graphql
python3 scripts/operations.py type UpdateProjectV2ViewInput
python3 scripts/audit.py thinkhome-org/full-github --organization --project 5
```

REST call executes the selected operation using the current gh identity, including writes. Use describe to inspect the method, parameters and official documentation. Supply request bodies through --body-file and preview with --dry-run. GraphQL operations use native gh api graphql with structured variables.

The expanded audit performs repository/organization probes and paginated Project reads. Failed reads remain unknown. It inspects classic branch protection separately from rulesets. Feature-specific object inspection and UI verification complete the coverage ledger.

## Documentation and development

Use the [Wiki](https://github.com/thinkhome-org/full-github/wiki), [execution guide](skills/full-github/references/operations.md), [contribution guide](CONTRIBUTING.md) and [repository workflow](GITHUB.md).

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/render_catalog.py --check
```

The source-backed inventory and executable API routes cover a wider surface than the live mutation tests. Plan, credentials, organization policies and host versions determine which operations can execute. The registries identify deprecated and known retired routes. See the verification record for tested operations and unresolved access gates.

## License

The project owner has not selected a license for original plugin content. Third-party OpenAPI data is covered by the MIT notice in [NOTICE.md](NOTICE.md). Contact ThinkHome before redistribution beyond rights granted by GitHub's terms.
