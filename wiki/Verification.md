# Verification

## Release 0.1.0

- Four automated tests cover invalid repository input, API pagination, permission failure, timeouts and malformed JSON. Failures preserve successful evidence.
- Plugin and marketplace paths validated locally and in GitHub Actions.
- Public Git marketplace registered and plugin installed using the documented commands.
- A fresh Codex CLI session located the installed skill and read both references.
- Issue #1 linked to Project 5 and PR #3. CI passed, PR merged and issue closed. Built-in Project workflow changed status to Done.
- Public Project has table, board and roadmap views, Priority and date fields. Built-in Item closed workflow is enabled with Done. Insights exposes the default Burn up chart.
- Wiki pages published through the separate Wiki Git remote.
- Main branch requires check, including administrators. Private vulnerability reporting, Dependabot alerts, secret scanning and push protection enabled.

## Limits

The full profile is an agent workflow. The audit script collects seven API categories. Automatic invocation depends on Codex skill selection and repository instructions.

Exhaustive setup of every GitHub feature and repeat-setup preservation on unrelated repositories have not been end-to-end tested. In particular, organization policies, paid capabilities, custom Project charts and access changes require context-specific verification. License selection remains pending with the owner. Distribution is through this Git marketplace.
