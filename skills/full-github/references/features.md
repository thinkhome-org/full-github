# Full profile coverage

Inspect all rows. Use the current official GitHub documentation for fields or APIs whose support is uncertain. Do not assume UI features have write APIs.

| Area | Inspect and reconcile | Evidence |
| --- | --- | --- |
| Identity | Description, homepage, topics, visibility, default branch, features | Repository API and About |
| Issues | Templates/forms, labels, organization issue types, assignees, milestones, sub-issues, dependencies, duplicate handling | Issue API, concrete issue |
| Projects | Existing linked organization/user Projects v2, fields, status, priority, iteration, dates, issue types, table/board/roadmap views, filters/grouping, insights, workflows, templates, updates | GraphQL/gh project plus UI for unsupported mutations |
| Collaboration | Discussions, pinned issues, contributing guidance, support route, ownership | Settings, files and rendered pages |
| Branches and PRs | Naming, linked issues, templates, review routing, CODEOWNERS, rulesets, required checks, merge strategies, stale branch cleanup | Rulesets API and tested PR |
| Actions | Stack-appropriate build/test/lint, least privilege permissions, pinned actions, concurrency, untrusted PR safety, release workflows | Successful workflow runs |
| Security | SECURITY.md, vulnerability reporting, dependency graph, Dependabot alerts/updates, code scanning, secret scanning and push protection where available | Security APIs/settings and workflow runs |
| Documentation | README, badges tied to actual checks/releases, CONTRIBUTING.md, GITHUB.md linked from AGENTS.md, support, license choice and notices | Rendered documents and working links |
| Wiki | Home, sidebar, installation, usage, architecture, permissions, troubleshooting, maintenance | Published Wiki pages and checked links |
| Releases | Version source, changelog/release notes, tags, artifacts, prerelease policy, provenance where relevant | Release API, downloaded artifact validation |
| Packages | Actual distributable package, registry permissions and supported ecosystem | Published package when applicable |
| Pages | Documentation site when requested or useful, source and deployment policy | Successful deployment and public URL |
| Git hooks | Existing local validation needs, explicit installation and platform support | Executed hook when applicable |
| Organization | Teams, issue types, Project templates, shared workflows, policies within authorized scope | Organization APIs/settings |

Use conventional uppercase GitHub community filenames. NOTICE is needed for applicable attribution obligations. Ask about an unresolved license before selecting one. AGENTS.md is the Codex instruction entry point. engines.md has no established universal GitHub behavior; clarify intended content or document actual runtime requirements in the ecosystem's native manifest.

Mark unavailable paid features as unavailable with evidence. Keep a documented coverage gap for UI-only capabilities until inspected. Do not imply that writing GITHUB.md changes GitHub settings.
