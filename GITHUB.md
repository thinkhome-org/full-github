# Repository workflow

Repository https://github.com/thinkhome-org/full-github

Use the full profile in skills/full-github/references/features.md. Keep the public Wiki and Issues current.

## Development

Create an issue for substantial work, assign its existing type/labels and add it to the Full GitHub Project. Use codex/<task> branches and PRs with closing references. Validate with python3 -m unittest discover -s tests -v and python3 scripts/validate.py and python3 scripts/render_catalog.py --check. Keep status Todo, In Progress or Done aligned with actual progress.

## Reviews and CI

Checks must pass before merging. CODEOWNERS routes review to @SamuelPalubaCZ. Required peer approval is zero for this initial single-maintainer project. Use squash merge and remove merged branches.

## Releases

Match .codex-plugin/plugin.json version with the v-prefixed release tag. Include installation instructions, validation evidence and limitations. Inspect the release archive before publishing. Public marketplace distribution is maintained in this repository.

## Documentation and Wiki

Keep README installation commands and Wiki pages aligned with shipped behavior. Wiki source is under wiki/. Publish through the separate GitHub Wiki Git repository after verifying remote changes. Never claim publication solely from these source files.

## Security and applicability

Use read-only CI tokens. Dependabot updates GitHub Actions. No new runtime dependencies. Packages and Pages currently have no separate artifact/site requirement. Local hooks are optional because the same checks run in CI. NOTICE.md preserves the official OpenAPI dataset license. Runtime requirements are documented in README. License selection remains with the owner.

Project https://github.com/orgs/thinkhome-org/projects/5 uses Status options Todo, In Progress and Done.

## Capability inventory

Keep all 261 capability families and complete API directories current. Each release records source dates, retired endpoints, operation counts and live validation separately. Use scripts/operations.py for exact REST routes and GraphQL input discovery. Registry generation and catalog rendering must remain reproducible.
