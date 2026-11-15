# Workflows and recovery

Use gh help and official REST/GraphQL documentation before uncertain commands. Pass text bodies through files or structured tool arguments. Never interpolate untrusted issue text into shell commands.

## Discovery

- gh repo view OWNER/REPO --json nameWithOwner,url,description,defaultBranchRef
- gh api repos/OWNER/REPO
- gh issue list --repo OWNER/REPO
- gh pr list --repo OWNER/REPO
- gh api repos/OWNER/REPO/rulesets
- gh project list --owner OWNER --format json
- gh project field-list NUMBER --owner OWNER --format json
- gh project view NUMBER --owner OWNER --format json
- gh run list --repo OWNER/REPO

Paginate list APIs. A 403 or 404 may indicate insufficient permission. Preserve the failure and verify access before interpreting absence.

## Reconciliation

Inspect existing object IDs before creating. Use gh label create --force only after confirming the desired edit to that matching label. Use gh project item-add with the actual issue URL, then edit fields using returned IDs and the project's field options. Re-read existing items after an interrupted write. Never create a second Project because its first creation timed out.

For Projects views, charts and built-in workflows, check current GraphQL support. Use the GitHub UI for operations absent from the API when computer control is available. Otherwise record the exact remaining UI step as blocked. Never claim a view or automation was created merely because the project exists.

## Delivery

Use the repo's branch convention, or codex/<short-task> when none exists. Create PRs with linked issues and validation evidence. Use gh pr checks and gh run view to diagnose failure. Fix recoverable failures and rerun. Do not weaken checks to make a PR merge. After merging, verify the resulting commit and issue/Project state.

## Wiki

Enable Wiki only within authorized setup. GitHub may require creating the first page through the UI before its .wiki.git remote exists. Clone https://github.com/OWNER/REPO.wiki.git into a separate temporary directory. Pull before editing. Preserve unrelated pages, commit only intended pages, push, and read the remote back. Keep Home.md and _Sidebar.md navigation valid. Do not claim source files under wiki/ are already published.

## Security and releases

Select CI based on the detected stack. Pin third-party Actions to verified commit SHAs and keep updates configured. Run trusted release jobs only on authorized tags. Never execute untrusted PR code with repository secrets or write tokens.

Validate package manifest, referenced paths, skills and marketplace discovery before a release. Match tag and manifest version. Verify release assets by downloading and inspecting them. Distribution through a Git marketplace and acceptance into OpenAI's public directory are separate publication steps.
