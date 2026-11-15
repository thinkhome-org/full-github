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


## Configuration decisions and history

Before changing a feature, read its option group and complete nested schema. Preserve provider defaults separately from this project's chosen policy. Keep the rationale, source dates, affected people and read-back evidence linked from the issue or PR. Record superseding decisions in docs/DECISIONS.md without rewriting earlier reasoning.

Use --context for executor calls and record verify-event after actual read-back. Unknown/interrupted calls require reconciliation before retry. GitHub timelines, review threads, Wiki Git history, immutable published asset bytes and CHANGELOG retain the native history. The local SQLite journal covers this executor's attempts and verification references.

## Human participation

Q&A Discussions handle questions; Ideas handles proposals; issue forms handle reproducible defects; PR review threads handle code/configuration review. Discussion 10 is the pinned entry point. Preserve authors, comments and source links during transfers/conversions. Required human approvals must come from eligible actual reviewers. A local event or automated self-review cannot replace one.

## Tagged publication

Push the matching v-prefixed tag only after checks pass and the reviewed source is on main. The Release workflow builds the ZIP, verifies hidden manifests, passes it as a workflow artifact, creates a provenance attestation and publishes through a resumable draft.

Existing asset bytes and human-added assets are preserved. A mismatch blocks publication and requires investigation. RC tags remain prereleases. Download the final ZIP/checksum and run gh attestation verify against this repository before declaring a release verified.

The release environment permits matching v* tags. Build verifies the tagged commit belongs to main history. The publish job checks transferred checksums before attestation and publication; it does not require a fabricated human reviewer in this single-maintainer setup.

This repository enables native release immutability. Future published tags/assets are frozen, and corrections are issued as a new release.

Release tags matching v* have an active no-bypass ruleset blocking updates and deletion before publication. Packaging checks the peeled local tag against HEAD, and publication compares the artifact comment and peeled remote tag with the build job commit. Reviewed release notes are supplied explicitly. Review pre-existing drafts created outside this workflow for required delivery information before using them; the publisher preserves their existing prose.


## Active full-profile delivery

Read skills/full-github/references/issue-lifecycle.md. Append new issue comments for kickoff, material findings/decisions, review and final delivery. A body edit or local journal entry cannot replace that native conversation. Independent workers must not edit a shared first comment. Read back comment IDs and reconcile uncertain posts before retrying.

Native child issues 15/16 decompose work tracked in 14. Use sub-issues for independently accepted work and dependencies for actual ordering. Read native type, labels, assignee, shared values, Project status/priority, milestone and development links. Preserve organization-only issue field visibility and existing Project views. The public Project-local Priority remains visible without exposing restricted owner fields. Start dates are observations; target dates are explicitly best-effort estimates.

Use scripts/audit.py OWNER/REPO --issue NUMBER for issue-level evidence. For full setup/audit use scripts/check_completion.py LEDGER.json with every catalog capability; resolve unfinished rows before claiming full completion. The check validates evidence claims, so linked live state must still be inspected. Ordinary fixes assess all relevant controls without manufacturing irrelevant objects.
