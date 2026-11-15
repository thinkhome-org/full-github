# Collaboration and work management capabilities

Official-documentation inventory checked 2026-11-15. This is a capability map, not a claim that every feature is enabled, licensed, permitted or live-tested in the target repository. Use the catalog IDs when recording applicability and evidence. GitHub.com and GitHub Enterprise Server versions can differ.

## Operating rules

- Resolve owner/repository and token identity first. Public reads do not prove private access. A masked 404, 403, failed query or unknown GraphQL field is an access/support question, not proof an object is absent.
- Read the current object before each write; reuse IDs and preserve unrelated settings. Re-read after writing. For ambiguous timeouts, reconcile before retrying. Capture URL/ID, expected and resulting SHA, relevant fields and timestamp.
- CLI is a convenience surface, not broader permission. Use `gh help`, `gh api` and the current REST/GraphQL schema when a dedicated command does not exist. Scope credentials to repository Contents, Issues, Pull requests, Administration, Discussions or owner Projects/Issue Types/Issue Fields as required by the exact endpoint. Repository role and token permission both matter.
- Project access, repository access and organization ownership are separate. Do not flatten restricted issue fields or private items into a public Project, report or Wiki. Check visibility with an appropriately scoped reader when sharing matters.
- Prefer immutable refs and expected-head guards for content and merges. Use Git for complete source/history and multi-file commits. Do not trust GitHub search, a diff preview, a successful enqueue response or a Markdown checklist as proof a change is complete.
- Operation surfaces below are specific: an API that lists an object may not edit it. In particular, current Projects v2 REST has view creation and saved-view item retrieval, while GraphQL documents view CRUD and status-update CRUD at `/en/graphql/reference/projects`. Workflow configuration and chart APIs still need operation-level checks. UI-only remaining steps need rendered evidence.

## Repository-specific audit sequence

1. Read repository flags/default branch/community files, effective rules and CODEOWNERS errors. Discover owner defaults and links to Projects/Discussions/Wiki.
2. List issue types/fields and existing labels/milestones. Inspect representative issue hierarchies, dependencies and recent timeline events before making a triage convention.
3. Inspect open PR heads, linked issues, requested reviews, check results, queue/auto-merge settings and draft state. Do not infer required reviews from CODEOWNERS alone.
4. Enumerate Projects including archived items and all field/view pages. Record field/option IDs, layouts/filters, workflows, charts, templates, status updates and permissions separately. A Project number alone proves none of those settings.
5. Pull the separate Wiki remote and compare source/publication revisions. Read notification state only when relevant to the user; changing subscriptions is a separate authorized action.

## Capability details

### Repositories

#### `repository-lifecycle` — Repository lifecycle and metadata

- Operations: List/get/create/update repositories; Rename/transfer/archive/unarchive/delete with explicit scope; Set description/homepage/topics/visibility/default branch/features.
- Access path: REST, GraphQL, gh repo, UI.
- Permissions and limits: Metadata read for discovery; Administration write and owner/organization policy govern settings. Transfers, visibility changes and deletion require specific authorization; archive is not deletion.
- Verification: Read repository again, inspect owner/name/visibility/default branch and feature flags.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/repos/repos).

#### `repository-templates` — Template repositories and generated repositories

- Operations: Inspect is_template; Generate a repository from a template; Choose owner/visibility and include branches where supported.
- Access path: REST, gh repo create --template, UI.
- Permissions and limits: Creation rights in destination owner required; template generation is distinct from a fork and does not establish shared Git history.
- Verification: Read generated repository and compare expected files and default branch.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/repos/repos#create-a-repository-using-a-template).

#### `repository-forks` — Fork networks and upstream synchronization

- Operations: List/create forks; Inspect parent/source; Sync fork upstream; Fetch upstream and submit cross-repository PRs.
- Access path: REST, gh repo fork, gh repo sync, git, UI.
- Permissions and limits: Contents write for synchronization; private/internal fork policy and organization access apply; never force-sync divergent work without authorization.
- Verification: Read parent/source and compare upstream/fork commit SHAs.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/repos/forks).

#### `repository-content` — Contents, README, archives and immutable source reads

- Operations: Read files/directories at a ref; Create/update/delete file with expected blob SHA; Read README; Download zip/tar archives.
- Access path: REST, GraphQL, gh api, git.
- Permissions and limits: Contents read/write; workflow-file edits additionally need Workflows permission. Contents API size/directory limits apply; use Git/trees for large listings and batches; download URLs expire.
- Verification: Read changed file at returned commit SHA; inspect archive contents and source ref.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/repos/contents).

#### `repository-git-objects` — Git blobs, trees, commits, refs and annotated tags

- Operations: Read/create blobs/trees/commits/tags; List/create/update/delete refs; Batch multiple file changes into one commit.
- Access path: REST, GraphQL, git.
- Permissions and limits: Contents permissions and branch rules apply. Use non-force ref update; preserve unrelated tree entries. Empty repositories need initialization; PR merge refs are not a durable mergeability source.
- Verification: Read final ref and commit/tree; compare expected parent SHA and changed paths.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-your-git-database).

#### `repository-history` — History, compare, blame and commit verification

- Operations: List/get commits and associated PRs; Compare branches/tags/SHAs; Inspect diff and signature verification; Read file history/blame.
- Access path: REST, GraphQL, git log, git blame, gh api.
- Permissions and limits: Contents read; paginated compare/file limits require local Git for complete large diffs. A signature validity result is not a trust decision by itself.
- Verification: Record base/head SHAs and verify diff against Git checkout.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/commits/commits).

#### `repository-branches` — Branch management and synchronization

- Operations: List/get/rename branches; Read protection and applicable rules; Merge branches and sync fork; Create/delete branches with Git refs.
- Access path: REST, gh api, git, UI.
- Permissions and limits: Contents write for branch changes; rename/default branch administration can require admin and ruleset bypass. Never infer a branch can be deleted merely because a PR merged.
- Verification: Read renamed/updated branch SHA, default branch and affected open PR bases.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/branches/branches).

#### `repository-community` — Community standards and shared contribution files

- Operations: Inspect community profile; Maintain README/CONTRIBUTING/CODE_OF_CONDUCT/SUPPORT/SECURITY; Discover owner .github defaults; Maintain funding links.
- Access path: REST, git, UI.
- Permissions and limits: Community health is a checklist rather than proof of policy quality; shared default files may supply files absent locally. License and funding choices remain owner decisions.
- Verification: Read community profile health/files plus rendered links at the default branch.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/metrics/community).

#### `repository-autolinks` — External tracker autolinks

- Operations: List/get/create/delete issue-reference autolinks; Configure key prefix and URL pattern.
- Access path: REST, UI.
- Permissions and limits: Administration read/write; avoid collisions with current tracker prefixes; autolinks do not synchronize external issue state.
- Verification: Read configured prefix/template and inspect rendered sample reference.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/repos/autolinks).

#### `repository-codeowners` — Ownership and review routing

- Operations: Read matching CODEOWNERS; Validate CODEOWNERS errors; Route user/team reviews; Require owner review through branch rules.
- Access path: REST, git, UI.
- Permissions and limits: Owners must have write access; team visibility/access and matching order matter. CODEOWNERS alone does not require an approving review; configure enforcement separately.
- Verification: Query CODEOWNERS errors and inspect reviewer request on a matching PR.
- Official source: [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

#### `repository-lfs-submodules` — Large files, submodules and checkout fidelity

- Operations: Inspect .gitattributes and LFS pointers; Fetch required LFS objects; Initialize pinned submodules; Read symlink/executable metadata.
- Access path: git, git lfs, REST.
- Permissions and limits: Git LFS requires installed client and storage/bandwidth entitlement; a pointer or submodule link is not its file content. Do not execute untrusted submodule hooks or code.
- Verification: Verify object contents, submodule SHA and file modes in the actual checkout.
- Official source: [GitHub Docs](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage).

### Issues

#### `issue-lifecycle` — Issue lifecycle and completion reasons

- Operations: List/get/create/edit/close/reopen issues; Set completed/not_planned reason; Lock/unlock discussion.
- Access path: REST, GraphQL, gh issue, UI.
- Permissions and limits: Issues read/write and actor role apply; REST issue lists also contain PRs, so filter pull_request entries. Closing an issue is separate from merging or deploying a fix.
- Verification: Read issue state/state_reason/title/body and timeline.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/issues).

#### `issue-metadata` — Labels, assignees and milestones

- Operations: List/create/edit/delete repository labels; Add/remove issue labels and assignees; Check assignability; Create/edit/close milestones and due dates.
- Access path: REST, gh label, gh issue, UI.
- Permissions and limits: Issues write generally required for management; respect existing names/colors. Set/replace operations remove omitted labels; prefer add/remove for narrow changes.
- Verification: Re-read issue metadata and milestone counters/dates; compare IDs rather than display names alone.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/labels).

#### `issue-assignees` — Assignable users and assignment validation

- Operations: List eligible assignees; Check user assignability; Add/remove issue or PR assignees.
- Access path: REST, gh issue edit, gh pr edit, UI.
- Permissions and limits: Issues or Pull requests permissions per endpoint; account/repository eligibility applies. Assignment notifies people and is not proof they accepted work.
- Verification: Read final assignees and confirm intended user, not just successful HTTP status.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/assignees).

#### `issue-milestones` — Milestone planning and progress

- Operations: List/get/create/update/delete milestones; Set due date and open/closed state; Assign issues and PRs to milestones.
- Access path: REST, gh api, UI.
- Permissions and limits: Issues write for mutation; milestone is repository-scoped. Deleting or closing a milestone does not finish its open work.
- Verification: Read due_on/state and included open/closed issues and PRs.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/milestones).

#### `issue-types` — Owner issue types and per-issue type assignment

- Operations: List inherited enabled repository types; List/create/update/delete owner types; Assign/change/remove issue type.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Repository type discovery needs Metadata read; owner type management has separate Issue Types permissions. Types can belong to organizations or personal accounts; do not hard-code Bug/Task/Feature or confuse type with label.
- Verification: Read repository available types and issue type ID/name after assignment.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/repos/issue-types).

#### `issue-types-owner` — Organization and personal issue type administration

- Operations: Manage organization issue types at /orgs/ORG/issue-types; Manage own types at /user/issue-types; Enable/disable and set name/description/color.
- Access path: REST, UI.
- Permissions and limits: Issue Types organization read/write; personal counterpart uses Issue Types user permission and user-scoped token. Changes affect multiple repositories; preserve existing definitions.
- Verification: List owner definitions and repository inherited enabled types.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/orgs/issue-types).

#### `issue-fields` — Owner-wide structured issue fields

- Operations: List/create/update/delete field definitions; Manage single-select options and supported types; Configure pinning/type applicability/visibility in owner settings.
- Access path: REST, UI.
- Permissions and limits: Issue Fields owner permissions and organization/account ownership required. Issue fields are distinct from Project custom fields; UI and REST supported types can differ by API version, so inspect schema before choosing multi_select.
- Verification: Read field definitions and inspect visibility and pinned placement on a representative issue.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/orgs/issue-fields).

#### `issue-field-values` — Per-issue structured field values

- Operations: List/add/set/delete issue field values; Reuse owner field and option IDs.
- Access path: REST, UI.
- Permissions and limits: Issues read/write; field visibility may restrict public values. Add vs set are different operations; user-owned field definitions use /user/issue-fields.
- Verification: Read final values from issue endpoint and rendered issue; confirm no unrelated values were replaced.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/issue-field-values).

#### `issue-forms-templates` — Issue forms, templates and contact routing

- Operations: Maintain YAML forms with validations/dropdowns; Maintain Markdown templates and chooser config; Configure contact_links and blank_issues_enabled.
- Access path: git, REST contents, UI.
- Permissions and limits: Contents write and default-branch placement; form YAML schema is constrained and not arbitrary workflow code. Check owner .github defaults before duplicating templates.
- Verification: Open new-issue chooser and render/test each form without submitting unwanted issues.
- Official source: [GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms).

#### `issue-subissues` — Parent/sub-issue hierarchy and ordering

- Operations: Get parent; List/add/remove sub-issues; Reprioritize children; Track nested work and progress.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Issues read/write; hierarchy/access/size/depth restrictions apply. Use issue database IDs where endpoint expects them, not issue numbers; removing child relation does not delete the issue.
- Verification: Read both parent and child relationships and final ordering.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/sub-issues).

#### `issue-dependencies` — Blocking and blocked-by relationships

- Operations: List blockers; Add/remove blocked-by dependency; List issues blocked by this issue.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Issues read/write and access to linked issues required; dependencies are separate from parent/child and from a Markdown mention. Preserve existing unrelated dependencies.
- Verification: Read blocked_by and blocking sides; verify intended direction and no duplicate edge.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/issue-dependencies).

#### `issue-related` — Related issues and suggested relationships

- Operations: List/add/remove related issues; List suggested issue relationships; Approve/dismiss suggestions.
- Access path: REST, UI.
- Permissions and limits: Issues permissions and endpoint eligibility apply. Suggestions are proposals, not established dependencies; approve only evidence-backed relationships.
- Verification: Read accepted relationships or suggestion disposition and linked issue IDs.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/issues#list-issues-related-to-an-issue).

#### `issue-comments` — Conversation comments, pinned comments and reactions

- Operations: List/create/edit/delete comments; Pin/unpin issue comment; Add/remove supported reactions.
- Access path: REST, GraphQL, gh issue comment, UI.
- Permissions and limits: Issues or Pull requests permissions per endpoint; edit/delete rights differ for own vs others comments. Comments on PR conversation use issue comments, not review-comment endpoints.
- Verification: Read comment by ID, rendered body and pinned state; compare author before editing.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/comments).

#### `issue-artifacts` — Issue-attached artifacts

- Operations: List/get/create/update/delete generic/link/plan/embedded_html artifacts; Filter artifacts by type.
- Access path: REST.
- Permissions and limits: Issues or Pull requests permissions; list response has no Link/total pagination metadata. Issue artifacts differ from Actions artifacts and ordinary Markdown attachments; inspect rendered HTML behavior before sharing.
- Verification: Read artifact by ID/number and fetch all pages until an empty page.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/artifacts).

#### `issue-timeline` — Timeline, audit context and cross references

- Operations: Read chronological events; Trace state/assignment/label/milestone changes; Inspect cross references and linked closing PRs.
- Access path: REST, GraphQL, gh api.
- Permissions and limits: Issues read; pagination and actor visibility apply. A mention or cross-reference does not necessarily establish an auto-closing link.
- Verification: Record event IDs/timestamps and associated commit/PR URLs.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/issues/timeline).

#### `issue-transfer-pin-duplicate` — Transfer, pinning and duplicate triage

- Operations: Transfer issues between eligible repositories; Pin/unpin important issues; Mark/unmark duplicates; Delete only when authorized.
- Access path: GraphQL, gh issue transfer, gh issue pin, UI.
- Permissions and limits: Role/owner/visibility eligibility and feature limits apply. Transfer can alter labels/milestones and links; deletion is destructive. Duplicate marking does not prove the underlying issue is resolved.
- Verification: Read new canonical URL and metadata after transfer; inspect duplicate/pinned timeline and repository pin list.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository).

#### `issue-saved-views` — Issue dashboard and advanced triage views

- Operations: Build boolean AND/OR/NOT and parenthesized filters; Save reusable issue views; Filter issue types, metadata, dates, blockers and hierarchy where supported.
- Access path: UI, REST search, GraphQL search, gh search issues.
- Permissions and limits: UI dashboard and global/API search grammars are not identical. Check current qualifiers and API advanced_search support before reusing nested queries verbatim.
- Verification: Run filter and inspect sampled matching and non-matching issues; verify saved view survives reload.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests).

### Pull Requests

#### `pr-lifecycle` — Pull request lifecycle, drafts and base/head management

- Operations: Create/read/edit/close/reopen PR; Convert draft/ready; Change base; Enable maintainer edits; Read commits/files/diff/checks.
- Access path: REST, GraphQL, gh pr, git.
- Permissions and limits: Pull requests read/write; Contents and source branch access may also be needed. Diff/file pagination limits matter; mergeable can be temporarily unknown and needs re-query.
- Verification: Read PR head/base SHA, draft/state and complete diff; confirm expected source repository.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/pulls/pulls).

#### `pr-linking` — Linked issues and automatic closure

- Operations: Use closing keywords with correct issue reference; Read closingIssuesReferences; Manually link eligible issues; Verify default-branch merge closure.
- Access path: GraphQL, gh pr, UI.
- Permissions and limits: Closing keywords act when merged into default branch; references to other repositories need correct owner/repo. Mentioning an issue alone is not an auto-closing relationship.
- Verification: Read linked issues before merge and actual issue state/timeline after merge.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).

#### `pr-templates` — PR templates and contribution checklist

- Operations: Maintain default/multiple PR templates; Use body-file with validation evidence and closing reference; Preserve repository template conventions.
- Access path: git, REST contents, gh pr create, UI.
- Permissions and limits: Contents write to default branch; multiple templates require correct template query. A checked checkbox is not test evidence.
- Verification: Preview new PR body and read published PR body.
- Official source: [GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository).

#### `pr-review-requests` — Reviewer requests and rerequests

- Operations: List/request/remove reviewers; Request teams; Rerequest after changes; Inspect reviewDecision and latest reviews.
- Access path: REST, GraphQL, gh pr edit, UI.
- Permissions and limits: Pull requests write and reviewer eligibility required; authors cannot approve their own PR. Team review request and individual approval are different facts.
- Verification: Read requested reviewers and review history; verify stale reviews are handled by current rules.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/pulls/review-requests).

#### `pr-reviews` — Review submission and dismissal

- Operations: List/create pending review; Submit COMMENT/APPROVE/REQUEST_CHANGES; Update review body; Delete pending review; Dismiss with reason.
- Access path: REST, GraphQL, gh pr review, UI.
- Permissions and limits: Pull requests write; dismissal may require elevated role or rules permissions. Review the actual head and connected code; do not approve on behalf of another actor.
- Verification: Read submitted review state, author, commit SHA and dismissal reason.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/pulls/reviews).

#### `pr-review-comments` — Inline review comments, suggestions and threads

- Operations: Create line/range comments and replies; Edit/delete own comments; Batch review comments; Read thread outdated/resolved state; Resolve/unresolve threads via GraphQL.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Pull requests read/write; LEFT/RIGHT and start_line must match diff. Resolution is not review dismissal; code suggestions alter code only when applied and committed.
- Verification: Read comment path/line/side/commit and thread state against current PR diff.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/pulls/comments).

#### `pr-merge` — Guarded merge and asynchronous merge results

- Operations: Check mergeability and protections; Merge/squash/rebase using expected head SHA; Start asynchronous merge when supported; Read merge result and merge commit.
- Access path: REST, GraphQL, gh pr merge, UI.
- Permissions and limits: Contents write and all branch/rules checks required. Pass expected SHA to avoid merging a newly changed head; queued/asynchronous acceptance is not completion.
- Verification: Read merged=true and merge_commit_sha; inspect base branch commit and issue state.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request).

#### `pr-auto-merge` — Auto-merge scheduling

- Operations: Inspect repository auto-merge setting; Enable/disable per-PR auto-merge; Choose allowed method; Observe execution after required checks/reviews.
- Access path: GraphQL, gh pr merge --auto, UI.
- Permissions and limits: Repository maintainer enables capability; PR actor needs write. Public Free or private paid-plan availability applies. Head/base changes or untrusted pushes can disable auto-merge.
- Verification: Read autoMergeRequest then final merged state and commit.
- Official source: [GitHub Docs](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/automatically-merging-a-pull-request).

#### `pr-merge-queue` — Merge queue configuration and enrollment

- Operations: Require queue on protected branch/ruleset; Configure method/concurrency/timeouts/group limits; Enqueue/dequeue PR; Read queue position and failure/removal reason.
- Access path: REST rules, GraphQL, gh pr merge, UI.
- Permissions and limits: Public organization repositories or private organization repositories on Enterprise Cloud; admin config and write enqueue rights. CI must handle merge_group; PR-only passing checks cannot establish queued batch safety.
- Verification: Inspect queue entry and merge_group check run; verify final base commit after dequeue/merge.
- Official source: [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue).

#### `pr-update-revert-cleanup` — Update branch, revert and branch cleanup

- Operations: Update PR branch using expected head SHA; Resolve conflicts locally; Revert merged change with PR; Delete or restore merged branch.
- Access path: REST, git, gh pr update-branch, gh pr revert, UI.
- Permissions and limits: Contents/PR write and protection rules apply; update is asynchronous. GitHub UI revert may fail on conflicts; revert is a new change requiring validation, not history erasure.
- Verification: Read updated head and checks; verify revert tree and retained branches before cleanup.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/pulls/pulls#update-a-pull-request-branch).

#### `pr-stacks` — Native stacked pull requests

- Operations: List/create/get stacks; Add/remove PRs from stack; Inspect ordering/base relationships.
- Access path: REST, UI.
- Permissions and limits: Pull requests read/write and stack eligibility apply; native stacks differ from unrelated branches described as stacked. API exposure does not prove feature enabled on every host/account.
- Verification: Read stack with all PR IDs and compare bases/heads after mutation.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/pulls/stacks).

#### `pr-agent-merge` — Agent Merge enrollment and allowed automation actions

- Operations: Get enrollment; Enable/update fix_ci and resolve_merge_conflicts actions; Disable enrollment.
- Access path: REST, UI.
- Permissions and limits: Paid Copilot excluding Free, repository write, Allow automations, no fork or stack for enrollment. Only latest enrolling user changes allowed actions; Agent tasks write remains needed for cleanup. Never enroll as an implicit substitute for ordinary merge.
- Verification: Read /agents/repos/OWNER/REPO/pulls/N/agent-merge and inspect actual subsequent PR/check history.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/pulls/agent-merge).

### Branches Rules

#### `branch-protection` — Classic branch protection

- Operations: Read/update required checks/reviews/signatures/restrictions; Require conversations resolved and linear history; Block deletion/force-push; Inspect admin enforcement.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Administration permissions; public Free and private paid-plan availability apply. Classic protection matching differs from cumulative rulesets; inspect both before deciding effective policy.
- Verification: Read effective protection and test behavior on an authorized disposable branch/PR.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/branches/branch-protection).

#### `repository-rulesets` — Branch/tag/push rulesets and effective rules

- Operations: List/get/create/update/delete rulesets; Inspect inherited rules and bypass actors; Target branch/tag patterns; Require reviews/checks/signatures/deployments and constrain pushes.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Read available to repository readers; admin/custom edit-rules role for writes. Public Free/private paid plans; push rulesets have additional plan/scope restrictions. Bypass and evaluate mode are not enforced compliance.
- Verification: Read effective branch rules plus source ruleset and enforcement state; inspect rule suites for real outcomes.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/repos/rules).

#### `ruleset-insights` — Rule evaluation and enforcement evidence

- Operations: List/get rule suites; Diagnose failed pushes and merge requirements; Identify inherited rule source and bypass use.
- Access path: REST, UI.
- Permissions and limits: Repository access and applicable rules permissions required; rule history retention and plan vary. Do not weaken policy to make a delivery pass.
- Verification: Record rule-suite conclusion, actor/ref, evaluated rules and enforcement mode.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/repos/rule-suites).

#### `repository-merge-policy` — Repository merge methods and branch cleanup policy

- Operations: Configure merge/squash/rebase availability; Configure default merge titles/messages; Toggle auto-delete branches and update-branch suggestions.
- Access path: REST, gh repo edit, UI.
- Permissions and limits: Administration write; merge method must also satisfy branch rules. Default branch or protected branches may not be auto-deleted.
- Verification: Read repository merge flags and inspect resulting merge commit/message on an actual PR.
- Official source: [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges).

### Projects

#### `projects-lifecycle` — Projects v2 discovery, lifecycle and repository links

- Operations: List/get owner projects via REST; Create/copy/edit/close/reopen/delete using GraphQL/gh; Link/unlink repositories; Set README/description/visibility/template status.
- Access path: REST, GraphQL, gh project, UI.
- Permissions and limits: Project role is separate from repository role. Classic project endpoints are not Projects v2; classic PAT project/read:project scopes or correct fine-grained Projects permissions are needed, plus private repository access for content.
- Verification: Read Project number/node ID/owner/public/closed/readme and linked repositories.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects).

#### `projects-items` — Project issue/PR items and drafts

- Operations: List/add/get/update/delete Project items; Create draft items; Convert drafts to issues; Archive/unarchive and reorder items.
- Access path: REST, GraphQL, gh project item-*, UI.
- Permissions and limits: Projects read/write and repository content access; not every operation exists in REST. Removing an item is not deleting its issue; a draft is not a repository issue until conversion.
- Verification: Read item ID/content ID/field values/archive state and issue URL after conversion.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/projects/items).

#### `projects-fields` — Project custom fields and built-in metadata

- Operations: List/get/add fields through REST; Create/update/delete supported fields using GraphQL/gh; Read labels/assignees/milestone/reviewers/linked PR metadata.
- Access path: REST, GraphQL, gh project field-*, UI.
- Permissions and limits: Projects read/write; built-in issue fields are backed by the issue and not arbitrary custom-field values. Options use IDs; do not match a Status field solely by position.
- Verification: Read field IDs/data types/options and sample item values.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/projects/fields).

#### `projects-field-values` — Typed Project field values and clearing

- Operations: Set/clear text/number/date/single-select/iteration values; Preserve field option IDs and typed GraphQL inputs.
- Access path: REST, GraphQL, gh project item-edit, UI.
- Permissions and limits: Project write; mutation types differ by field and API. An issue may appear in multiple Projects with different statuses; editing one does not update all.
- Verification: Read the specific item field value including option/iteration ID after write.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects).

#### `projects-iterations` — Iteration planning, schedules and breaks

- Operations: Create iteration field; Inspect current/completed/future iterations; Configure duration/start dates/breaks; Assign items and use relative iteration filters.
- Access path: GraphQL, gh project item-edit, UI.
- Permissions and limits: Project write for schedule changes; gh/API support is operation-specific. Changing iteration definitions can affect many items; preserve completed history.
- Verification: Read iteration configuration and item iteration ID; inspect current and next iteration views.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-iteration-fields).

#### `projects-views` — Saved table, board and roadmap views

- Operations: Read/create/update/delete views through GraphQL; Create views via REST with layout/filter/visible_fields/sort_by/group_by/vertical_group_by; Duplicate/reorder through UI when API unsupported.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Projects write; REST documents create while GraphQL exposes createProjectV2View/updateProjectV2View/deleteProjectV2View. visible_fields excludes roadmap and grouping requires eligible fields. GraphQL configuration currently exposes visibleFieldIds; REST creation additionally accepts grouping/sort. Use UI for unsupported controls.
- Verification: Read view identity/layout/filter with GraphQL and open rendered view; verify persistence on reload.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/projects).

#### `projects-layout` — Grouping, slicing, sorting and field visibility

- Operations: Set table grouping/sort/visible columns; Set board columns/swimlanes/limits; Configure roadmap dates/iterations/zoom/markers; Slice/filter and save changes.
- Access path: UI, REST view creation, GraphQL read.
- Permissions and limits: Write role to save shared views; available controls differ by layout and field. API support for creation parameters does not imply support for every subsequent layout edit.
- Verification: Inspect rendered table/board/roadmap with representative items and reload saved settings.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/changing-the-layout-of-a-view).

#### `projects-filters` — Project filters and saved-view item retrieval

- Operations: Filter by fields/state/labels/assignees/repository/type and relative iterations; List REST view items with saved filter applied; Use fields selection for desired values.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Projects read and private item access; REST page cursors use Link headers. Title alone can be the default response; explicitly request needed field IDs. Issue search grammar is not Project filter grammar.
- Verification: Compare API view item IDs with rendered filtered view and unfiltered project totals.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/projects/items#list-items-for-an-organization-project-view).

#### `projects-insights` — Current and historical insights charts

- Operations: View/create/customize charts; Configure filters/chart type/grouping; Inspect historical trends and burn-up style progress.
- Access path: UI.
- Permissions and limits: Project write to configure, read to view; plan-dependent chart/history limits. Archived/deleted items are excluded. No chart mutation API verified here; keep explicit UI evidence instead of assuming chart exists from Project fields.
- Verification: Open saved chart, inspect filters/time range and reconcile plotted totals with source items.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects).

#### `projects-workflows` — Built-in Project status workflows

- Operations: List/get workflow name/enabled state via GraphQL; Delete workflow via deleteProjectV2Workflow; Enable/disable/configure event transitions and issue-close behavior in UI.
- Access path: GraphQL read/delete, UI configuration.
- Permissions and limits: Project write; not every workflow is enabled by default. Status option names are project-specific; automation can close issues, so treat its effects as writes to repository work.
- Verification: Read saved workflow configuration; exercise authorized sample event and read resulting field/state.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations).

#### `projects-auto-add` — Automatic item intake

- Operations: Configure repository/filter auto-add workflows; Inspect scope and matching future issues/PRs; Reconcile existing items separately.
- Access path: UI, Actions with GraphQL.
- Permissions and limits: Project write and repository visibility; workflow count/plan limits and supported filter qualifiers apply. Built-in auto-add is not a guaranteed historical backfill and templates do not copy auto-add workflows.
- Verification: Read saved filter/repository and verify a newly matching item appears with its content ID.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically).

#### `projects-auto-archive` — Automatic archival and retention

- Operations: Configure auto-archive filter; Inspect archived items; Restore archived work where authorized.
- Access path: UI, GraphQL, gh project item-archive.
- Permissions and limits: Project write; archiving is not completion or deletion. Charts exclude archived items, so archive policy changes reporting and must be documented.
- Verification: Read saved workflow and final archived state; check restored item remains visible.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically).

#### `projects-actions` — Project automation through Actions and webhooks

- Operations: React to issue/PR/project events; Add items and set fields through API; Use installation token with Project access; Reconcile after retry.
- Access path: Actions, GraphQL, REST, webhooks.
- Permissions and limits: Repository GITHUB_TOKEN does not automatically have owner Project access; suitable App/PAT scope required. Do not expose credentials to untrusted PR code or duplicate items after ambiguous failure.
- Verification: Inspect successful workflow run and read target item state plus idempotent rerun behavior.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions).

#### `projects-templates` — Organization Project templates and copying

- Operations: Mark/unmark template; Set recommended templates; Create/copy from template; Preserve fields/views/drafts/workflows/insights where supported.
- Access path: GraphQL, gh project copy, UI.
- Permissions and limits: Organization owner/template permissions and project roles apply. Templates omit auto-add workflows; copied item/permission options vary. Project existence alone is not evidence the full template was reproduced.
- Verification: Open resulting Project and compare fields/views/drafts/workflows/charts; explicitly inspect missing auto-add rules.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-project-templates-in-your-organization).

#### `projects-updates` — Project status updates and subscriptions

- Operations: Read update history; Publish/edit/delete high-level Markdown update via createProjectV2StatusUpdate/updateProjectV2StatusUpdate/deleteProjectV2StatusUpdate; Set project status/start/target dates; Subscribe/unsubscribe.
- Access path: GraphQL, UI.
- Permissions and limits: Project write to publish, read to view/subscribe; templates cannot have updates. Project-wide health is distinct from an item Status field; inspect current GraphQL schema before using mutation names.
- Verification: Read latest update and full history with dates/status; inspect header and subscriber behavior.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/sharing-project-updates).

#### `projects-access` — Project visibility, access and linking

- Operations: Inspect/set public/private; Manage individual/team/base access; Link Project to repositories and teams; Inspect restricted/private item visibility.
- Access path: GraphQL, UI.
- Permissions and limits: Project admin/owner controls; a public Project never grants access to private repository issues. Access changes need explicit owner authorization; do not infer exposure from one privileged token.
- Verification: Read permission/visibility settings and verify with an appropriately scoped reader.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects).

#### `projects-issue-fields` — Reuse owner issue fields in Projects

- Operations: Attach an owner issue field using createProjectV2IssueField; Read shared values rather than maintain duplicate custom fields.
- Access path: GraphQL, UI.
- Permissions and limits: Project write plus issue-field visibility/access; owner issue fields and Project-only fields have different lifetimes. Do not create a duplicate Priority field before checking the existing owner field.
- Verification: Compare issue field ID/value and Project issue-field binding on the same issue.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/projects).

#### `projects-multiselect` — Multiple-choice Project fields

- Operations: Discover ProjectV2MultiSelectField and options; Read item multi-select values; Write only when current field-value input supports the operation.
- Access path: GraphQL, UI.
- Permissions and limits: Project permissions; schema/API-version support differs. Preserve existing selection IDs; do not coerce a multi-select into single-select or assume all gh project commands expose it.
- Verification: Read field data type, option IDs and resulting item selections.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/projects).

### Discussions

#### `discussions-lifecycle` — Repository and organization Discussions

- Operations: Enable repository Discussions; List/create/read/edit/delete/close/reopen discussions; Set categories/title/body; Search and read threaded comments.
- Access path: GraphQL, REST repository feature toggle, UI.
- Permissions and limits: Discussions repository permission and role apply; organization discussions use a chosen source repository. GraphQL is primary content API; gh api graphql works without inventing native gh discussion commands.
- Verification: Read discussion/category/comment node IDs and rendered state.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-discussions).

#### `discussions-answers` — Answers, reactions and community feedback

- Operations: Read/add/edit/delete discussion comments and replies; Mark/unmark answer in answerable categories; Add reactions and inspect upvotes.
- Access path: GraphQL, UI.
- Permissions and limits: Discussion author/maintainer rights differ; category must allow answers. Upvotes/reactions indicate feedback and are not review approvals or implementation acceptance.
- Verification: Read answerChosenAt/answer node and thread structure; verify selected answer belongs to correct discussion.
- Official source: [GitHub Docs](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/participating-in-a-discussion).

#### `discussions-organization` — Categories, forms, polls and moderation

- Operations: Configure open/Q&A/announcement/poll categories; Maintain category forms; Pin/lock/transfer discussions and moderate disruptive content; Convert suitable issues/discussions.
- Access path: UI, GraphQL where mutation documented, git forms.
- Permissions and limits: Maintainer/admin or moderation permissions; format-specific APIs may be read-only or absent. Poll/category management and transfer need operation-level schema check; do not substitute issue labels for Discussion categories.
- Verification: Inspect category format/forms, pinned state, locks and transferred canonical URL.
- Official source: [GitHub Docs](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions).

### Wiki

#### `wiki-pages` — Wiki publishing and independent Git history

- Operations: Enable Wiki; Create first page via UI if necessary; Clone/pull/edit/commit/push OWNER/REPO.wiki.git; Read page revision history and revert with new commit.
- Access path: git, UI, REST repository feature toggle.
- Permissions and limits: Public Free/private paid plans; Wiki edit policy and repository write apply. Wiki is separate Git repository, not wiki/ source directory; no supported general-purpose Wiki content REST API established.
- Verification: Read remote Wiki commit with ls-remote and open published page; compare rendered content and links.
- Official source: [GitHub Docs](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis).

#### `wiki-navigation` — Wiki sidebar, footer, assets and navigation

- Operations: Maintain Home.md/_Sidebar.md/_Footer.md; Add relative page links/images; Rename/delete pages carefully; Preserve existing assets and history.
- Access path: git, UI.
- Permissions and limits: Pull before edits; Wiki markup/page naming can change link resolution. Wiki does not inherit the main repository PR/branch-protection workflow automatically; publishing source is a separate write.
- Verification: Open Home and each changed navigation target; inspect image URLs and remote commit.
- Official source: [GitHub Docs](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content).

### Search Notifications

#### `search-cross-github` — Cross-GitHub discovery and search coverage

- Operations: Search repositories/issues/PRs/commits/code/users/topics/labels; Scope by repo/org/owner and dates; Paginate and partition searches.
- Access path: REST, GraphQL, gh search, UI.
- Permissions and limits: Search has separate rate limits and up-to-1000-result windows; indexing and incomplete results make empty search insufficient proof of absence. Code search authentication/indexing restrictions differ from ordinary repository read.
- Verification: Record query, time, result count, incomplete_results and retrieved IDs; partition above result cap.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/search/search).

#### `search-code` — Code search versus local source inspection

- Operations: Use path/repo/language/symbol/content and regular-expression UI qualifiers; Use REST code search supported syntax; Inspect Git at an exact ref for complete verification.
- Access path: UI, REST, gh search code, rg, git.
- Permissions and limits: New web code search and REST code search are distinct engines; regex/symbol qualifiers are not automatically available through REST. Ignored/unindexed/generated/large files may require Git inspection.
- Verification: Open matching file at immutable SHA and reproduce critical search locally.
- Official source: [GitHub Docs](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax).

#### `search-issues-prs` — Issue and PR search qualifiers

- Operations: Search authors/assignees/labels/types/dates/missing metadata; Find requested reviews/drafts/merge states/linked work; Build stale/blocked/unassigned triage queries.
- Access path: REST, GraphQL, gh search issues, gh search prs, UI.
- Permissions and limits: Global search, repository advanced filters and Project filters differ; requested-reviewer results change after review. Quote multiword values; do not mistake missing results for no permission-restricted work.
- Verification: Sample results and verify qualifiers against source objects and current identity.
- Official source: [GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests).

#### `notifications-inbox` — Notification inbox and thread state

- Operations: List global/repository notifications; Read thread/reason; Mark read/done; Subscribe/unsubscribe/ignore thread; Inspect unread/participating filters.
- Access path: REST, UI.
- Permissions and limits: User-specific notifications are not a repository audit feed. Classic/OAuth notification scopes apply; fine-grained/App token support differs by endpoint. Marking done/read or ignoring is an external user-state write, not passive discovery.
- Verification: Read thread subscription and notification state using same user; preserve before/after timestamps.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/activity/notifications).

#### `notifications-watch` — Repository watches, stars and subscriptions

- Operations: Read/set repository subscription; Configure custom watch events in UI; Star/unstar; Inspect watchers/stargazers.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Authenticated user controls personal state; App/fine-grained compatibility varies. Watching can create substantial notifications; do not subscribe or star silently as setup.
- Verification: Read subscription/subscribed/ignored state and selected event preferences.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/activity/watching).

#### `activity-events` — Repository and user activity feeds

- Operations: Read repository/user/organization event streams; Inspect pushes/issues/PR activity; Use feeds for recent-change discovery.
- Access path: REST, UI.
- Permissions and limits: Feeds have retention, latency and pagination limits and are not complete audit logs. Use enterprise/org audit log where authorized for security evidence.
- Verification: Record event IDs/timestamps and confirm consequential facts on owning issue/PR/commit API.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/activity/events).

## Practical probes and mutation guards

These examples are read-only. Substitute known identifiers without interpolating issue or PR prose into shell code. Paginate full collections; GraphQL connections need cursor iteration independently at every nested level.

```sh
gh api repos/OWNER/REPO
gh api --paginate repos/OWNER/REPO/issues --jq '.[] | select(.pull_request == null)'
gh api repos/OWNER/REPO/issue-types
gh api repos/OWNER/REPO/issues/NUMBER/sub_issues
gh api repos/OWNER/REPO/issues/NUMBER/dependencies/blocked_by
gh api repos/OWNER/REPO/issues/NUMBER/issue-field-values
gh api repos/OWNER/REPO/issues/NUMBER/artifacts
gh api repos/OWNER/REPO/pulls/NUMBER
gh api repos/OWNER/REPO/stacks
gh api repos/OWNER/REPO/rules/branches/BRANCH
gh api repos/OWNER/REPO/codeowners/errors
gh project list --owner OWNER --format json
gh project field-list NUMBER --owner OWNER --format json
gh project item-list NUMBER --owner OWNER --format json
gh api orgs/ORG/projectsV2/NUMBER
gh api orgs/ORG/projectsV2/NUMBER/fields
gh api orgs/ORG/projectsV2/NUMBER/views/VIEW_NUMBER/items
git ls-remote https://github.com/OWNER/REPO.wiki.git
```

Before constructing a GraphQL mutation, inspect the current schema and obtain node IDs from a read. REST numeric IDs, issue numbers, Project numbers and GraphQL node IDs are not interchangeable. A Project item ID differs from its content issue ID. Use `gh api graphql -F` typed variables rather than concatenating untrusted strings into a query.

For PR delivery, bind reviews and merge intent to the observed head SHA; after any head change, reconsider checks/review freshness. Inspect async merge completion and queued merge completion on the PR, then the default branch. Preserve queue requirements and never bypass them to match a local plan.

When updating single-select options, preserve existing option IDs: recreating options can clear assigned item values. Read the current option list before editing and verify representative items afterward.

For Projects, keep item Status separate from issue open/closed state and project-wide health. Verify any default automation before manually setting status: reopening, merging or archiving can trigger another transition. When copying a template, inspect the resulting views, custom fields, draft items, workflows and charts individually; configure omitted auto-add workflows separately when authorized.

## Evidence gaps that must stay explicit

This inventory verifies official documentation paths and documented support, not end-to-end mutations or entitlement on the target account. Chart mutations, unsupported advanced view controls, poll/category management, saved dashboard views and Project built-in workflow configuration need current schema inspection or UI verification. GraphQL documents view CRUD, status-update CRUD and workflow deletion; do not mislabel those operations as UI-only. Preview/rolling-release features such as native PR stacks, issue artifacts, issue suggestions and Agent Merge may be absent on a given host/version. Record exact HTTP/schema/UI failure and continue independently supported work; never silently replace native relationships with text and call the feature configured.

## Second completeness pass: additional operation families

Checked against all bundled GraphQL mutation names and current product documentation on 2026-11-15. These additions complement the existing families rather than treating REST support alone as the product boundary. Independent Checks and commit-status families live in the delivery/security reference.

### Repositories additions

#### `repository-commit-comments` — Commit discussion comments

- Operations: List repository/commit comments; Get/create/edit/delete a commit comment; Read path/line/position and reactions.
- Access path: REST, GraphQL read, UI.
- Permissions and limits: Contents read for discovery; endpoint-specific Contents write for creation and ownership/role for edits. Commit comments are distinct from PR conversation and review comments; validate line anchors on the referenced commit.
- Verification: Read comment ID/body/commit SHA and any line anchor.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/commits/comments).

### Issues additions

#### `issue-linked-branches` — Issue-linked development branches

- Operations: Read linkedBranches; Create branch linked to issue using createLinkedBranch; Remove issue/branch association with deleteLinkedBranch.
- Access path: GraphQL, gh issue develop, git, UI.
- Permissions and limits: Repository content/issue access and actor eligibility apply. A linked branch is distinct from a closing PR reference; unlinking does not establish issue completion or safe branch deletion.
- Verification: Read issue linkedBranches and actual ref SHA; confirm association removal leaves intended branch/content intact.
- Official source: [GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue).

#### `issue-planning-status` — Native issue planning statuses (preview)

- Operations: Read repository planningStatuses and issue.status; Check viewerCanSetStatus; Set issue status with setIssueStatus including duplicate issue where applicable.
- Access path: GraphQL, UI where enrolled.
- Permissions and limits: Preview enrollment required; unavailable can return null. Distinct from Project item Status and open/closed state, but status transitions can close/reopen the issue. Discover valid IDs instead of hard-coding status names.
- Verification: Read status ID plus issue state/stateReason and duplicate relation after transition.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/issues#setissuestatus).

### Pull Requests additions

#### `pr-file-view-state` — Per-viewer reviewed-file state

- Operations: Read file viewerViewedState; Mark/unmark a file as viewed using markFileAsViewed/unmarkFileAsViewed.
- Access path: GraphQL, UI.
- Permissions and limits: Authenticated viewer state; marking viewed is not a submitted review or proof the file is correct. File changes can invalidate prior viewed state; do not mark unrelated files as reviewed.
- Verification: Read exact file path and viewed state as the same viewer on current PR head.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/pulls#markfileasviewed).

#### `pr-archival` — Native pull request archiving

- Operations: Archive PR with archivePullRequest; Unarchive with unarchivePullRequest; Read archive and closure state.
- Access path: GraphQL, UI.
- Permissions and limits: Triage role or higher; host/version eligibility applies. Archiving closes a PR and differs from deleting branches, repository archival, or Project item archival; unarchiving is not necessarily reopening.
- Verification: Read resulting PR archived/state fields and timeline; inspect any lock changes on current host.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/pulls#archivepullrequest).

### Community additions

#### `community-comment-minimization` — Hide and restore off-topic or disruptive comments

- Operations: Read viewerCanMinimize/isMinimized/minimizedReason; Minimize with classification; Restore with unminimizeComment.
- Access path: GraphQL, UI.
- Permissions and limits: Role and comment-type restrictions apply across issue/commit/PR/gist comments. Minimization preserves content and differs from deletion or locking; do not hide technical disagreement solely because it blocks delivery.
- Verification: Read minimized state/reason and rendered comment visibility.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/issues#minimizecomment).

#### `community-interaction-limits` — Temporary interaction restrictions

- Operations: Read/set/remove repository/organization/user interaction limits; Choose eligible contributor class and duration; Inspect inheritance.
- Access path: REST, GraphQL, UI.
- Permissions and limits: Organization owner/repository admin or personal-account ownership as applicable. Restricts real contributors and can affect multiple repositories; choose narrow authorized scope. Owner-wide restrictions and blocked-user lists are separate controls.
- Verification: Read limit class, expiry and owner scope; verify effective repository restriction without disruptive test posts.
- Official source: [GitHub Docs](https://docs.github.com/en/rest/interactions).

#### `community-saved-replies` — Personal saved replies and reusable response insertion

- Operations: Create/edit/delete saved replies; Preview Markdown; Insert/customize reply in issue/PR/Discussion composer.
- Access path: UI.
- Permissions and limits: Personal-account feature, up to 100 replies. No stable public CRUD API verified; saved replies do not authorize sending messages. Preserve existing replies and avoid adding sensitive project details to reusable text.
- Verification: Reload saved reply settings and preview inserted draft; posting requires separate authorized comment write.
- Official source: [GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies).

### Profiles Social additions

#### `profile-status` — Personal availability status

- Operations: Read User.status; Set emoji/message/organization scope/availability/expiry using changeUserStatus; Clear status.
- Access path: GraphQL, UI.
- Permissions and limits: Current-user authorization and organization membership apply; personal user state is separate from account bio and issue/project status. Respect chosen visibility and avoid announcing availability changes without authorization.
- Verification: Read status and expiresAt as the user; inspect public or organization-scoped rendering.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/users#changeuserstatus).

#### `profile-star-lists` — Named lists of starred repositories

- Operations: Read user lists and repository membership; Create/update/delete lists; Assign/remove repository from lists with updateUserListsForItem.
- Access path: GraphQL, UI.
- Permissions and limits: Authenticated personal-account feature; starring and list membership are different operations. Use IDs, preserve other memberships, and inspect current visibility limits before storing private planning notes in list descriptions.
- Verification: Read list IDs/name/description and intended repository membership.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/users#createuserlist).

#### `profile-content-pins` — Personal profile README, pins and contribution display

- Operations: Maintain USER/USER README; Pin/unpin/reorder repositories and gists; Configure contribution/private-profile display and achievements where supported.
- Access path: git, REST contents, GraphQL read, UI.
- Permissions and limits: Account owner and Contents write for profile repository. Public README/pins expose chosen content; REST profile update does not configure these surfaces. Pins/display settings need UI unless current API explicitly supports them.
- Verification: Open profile as intended audience and verify README, pins and contribution visibility.
- Official source: [GitHub Docs](https://docs.github.com/en/account-and-profile/how-tos/profile-customization).

#### `profile-follow-organizations` — Follow organization activity

- Operations: Read followed organizations; Follow/unfollow organization using followOrganization/unfollowOrganization; Inspect dashboard activity.
- Access path: GraphQL, UI.
- Permissions and limits: Personal social state; host/preview availability varies. Following organization differs from joining it or watching all its repositories and does not grant access or membership.
- Verification: Read viewerIsFollowing or matching followed-organization relation as same user.
- Official source: [GitHub Docs](https://docs.github.com/en/get-started/exploring-projects-on-github/following-organizations).

### Sponsors additions

#### `sponsors-listing` — Sponsors eligibility and listing setup

- Operations: Discover sponsorables/listings; Create listing via createSponsorsListing; Configure profile and fiscal-host details through supported setup.
- Access path: GraphQL, UI.
- Permissions and limits: Eligible personal/organization account and Sponsors enrollment required; country/fiscal-host verification applies. Listing creation does not complete financial onboarding or publish approved payment details.
- Verification: Read listing and setup/published eligibility state.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/sponsors#createsponsorslisting).

#### `sponsors-tiers` — Sponsorship tiers and benefits

- Operations: Create/publish/retire tier through GraphQL; Configure one-time/monthly amounts, description and repository-access benefit in UI.
- Access path: GraphQL, UI.
- Permissions and limits: Sponsors maintainer/organization authority required. Paid tiers and repository benefits affect billing/access; retired tiers can retain existing sponsors. Preserve current subscribers; do not interpret retirement as cancellation.
- Verification: Read tier amount/recurrence/publication/retired state and benefit access rules.
- Official source: [GitHub Docs](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers).

#### `sponsors-transactions` — Individual and bulk sponsorship commitments

- Operations: Create one or bulk sponsorships via createSponsorship/createSponsorships; Cancel with cancelSponsorship; Read active and historical commitments.
- Access path: GraphQL, UI.
- Permissions and limits: Financial commitment requires explicit scope/amount/payer authorization, valid payment method and account eligibility. A partial bulk result is not all-or-nothing; cancellation and failed writes need read-back before retry.
- Verification: Read sponsor/sponsorable/tier/amount/recurrence and each bulk result separately.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/sponsors#createsponsorship).

#### `sponsors-preferences` — Sponsorship privacy and connected platform preferences

- Operations: Update sponsorship privacy/email preferences; Inspect sponsor visibility; Manage Patreon sponsorability linkage using documented mutation.
- Access path: GraphQL, UI.
- Permissions and limits: Sponsor/maintainer authority and linked-platform eligibility apply. Privacy changes can publish sponsor identity; platform connection is not equivalent to a completed sponsorship or payment authorization.
- Verification: Read updated preference and relevant public/private relationship.
- Official source: [GitHub Docs](https://docs.github.com/en/graphql/reference/sponsors#updatesponsorshippreferences).

#### `sponsors-analytics` — Sponsor activity, lifetime value and exports

- Operations: Read sponsorships/sponsors/activity and permitted lifetime value; View transaction analytics; Export CSV/JSON within supported time windows.
- Access path: GraphQL, UI.
- Permissions and limits: Sponsors owner/admin and visibility scopes required. Export can trigger email delivery and contains financial/personal data; initiating delivery needs explicit authorization. Export is not proof all payments settled.
- Verification: Reconcile date window/currency/account and exported rows against dashboard totals.
- Official source: [GitHub Docs](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/viewing-your-sponsors-and-sponsorships).

#### `sponsors-newsletters` — Sponsor newsletters and tier-targeted updates

- Operations: Read permitted newsletter history; Draft/preview sponsor update; Select tiers and publish to opted-in recipients when explicitly requested.
- Access path: GraphQL read, UI.
- Permissions and limits: Sponsors owner/admin; opt-in recipient policy applies. Publishing sends email and requires explicit instruction to message recipients; listing management or repository setup alone does not authorize newsletters.
- Verification: Read sent update/target tiers and published history; distinguish draft from sent update.
- Official source: [GitHub Docs](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/contacting-your-sponsors).

#### `sponsors-payouts` — Payout status and receipts

- Operations: Inspect payout history and payment holds; View/export receipts; Follow official payout-account management flow.
- Access path: UI, GraphQL permitted metadata.
- Permissions and limits: Financial identity/account-owner access and supported payout-provider/country rules apply. Banking/tax updates require owner handling; never infer payout completion from sponsorship creation or an API listing.
- Verification: Match account/currency/date and receipt to payout history; report pending versus paid accurately.
- Official source: [GitHub Docs](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-payouts-from-github-sponsors).

#### `sponsors-goals` — Sponsorship goals and progress

- Operations: Configure sponsorship goal and description; Read goal kind/target/progress; Update or remove goal through supported UI.
- Access path: UI, GraphQL read.
- Permissions and limits: Sponsors maintainer authority; public presentation and financial target are owner decisions. Goal progress is not recognized revenue and should not replace transaction/payout evidence.
- Verification: Read displayed goal and progress on intended Sponsors profile.
- Official source: [GitHub Docs](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-goal).

Poll voting has a documented GraphQL path: `addDiscussionPollVote`; poll options/counts and current viewer voting state can be read. This complements the category/poll configuration family above; do not classify every poll operation as UI-only. Topic suggestions have `acceptTopicSuggestion`/`declineTopicSuggestion`, complementing existing repository topic management. Public schema presence still does not prove target-host feature eligibility.
