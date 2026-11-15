# Configuration decisions

Reviewed 2026-11-15. 82 decision groups contain 459 concrete configuration choices covering every catalog capability.

Choose settings from the project's actual requirements, observed state, access policy and host version. Record the selected value, rationale, owner, historical evidence and read-back verification. Preserve existing custom settings and identities.

Official documentation establishes current supported behavior. Community links provide incident history and practical pitfalls. Check their date and current applicability before applying a workaround. Full REST schemas and GraphQL input types provide the nested API constraints alongside these decisions.

## Repository identity, defaults and collaboration surfaces

Group ID repository-collaboration-settings.

Capabilities repository-lifecycle, repository-branches, repository-autolinks, repository-community.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| visibility / private | public, private, internal where eligible | Preserve observed visibility; assess access and discoverability before a requested change, never make a private project public as routine setup. | Re-read visibility and intended reader access; inspect fork implications before changing. |
| default_branch | existing branch name | Retain the current branch unless migration is required; discover branch names before configuring CI, templates or closing links. | Read repository default_branch, ref SHA and PR bases after any authorized rename. |
| has_issues / has_projects / has_wiki / has_discussions | independent booleans | Enable the surfaces the project will actively use; enabling a repository Projects tab does not create or configure an owner Project. | Read each flag and follow the actual tab and linked owner Project. |
| description / homepage / topics | text, HTTPS URL, topic list | Use concise purpose and a working primary documentation URL; preserve unrelated topics and owner-defined metadata. | Read metadata and open rendered links; check topic replacement semantics before writing. |
| autolinks.key_prefix / url_template / is_alphanumeric | tracker prefix, URL with <num>, boolean | Add only for a real external tracker; choose a non-colliding prefix and correct numeric versus alphanumeric matching. | Read rule IDs and test a harmless rendered example without sending a comment. |
| archived / disabled | repository lifecycle flags | Archive only when work truly ends; do not archive to represent a finished milestone or Project. | Re-read flags, open work and expected read-only behavior; record unarchive recovery path. |
| has_pull_requests / pull_request_creation_policy | has_pull_requests boolean; documented default true, pull_request_creation_policy: all or collaborators_only | Preserve contribution access unless a restriction is intended. Organization collaborators for this setting have write, maintain or admin access; personal collaborators are invited users. Disabling hides existing PRs rather than deleting them. | Read both settings and intended contributor eligibility; inspect PR visibility. Re-enable to restore existing PR availability; restore prior policy if legitimate contributions are blocked. |
| web_commit_signoff_required | boolean; documented default false, effective organization policy also applies | Choose only an owner-approved signoff agreement. This adds author signoff to web commits, differs from cryptographic signing, and does not enforce CLI signoffs; CLI authors use --signoff. | Read repository and organization policies; inspect the Sign off and commit changes form and resulting Signed-off-by trailer on an authorized commit. Restore prior setting if misconfigured; retain existing commit history. |

### Pitfalls

- Repository flag defaults vary with creation path and owner settings; never infer actual configuration from product availability.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/repos/repos)
- [Official sources 2](https://docs.github.com/en/rest/repos/autolinks)
- [Official sources 3](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/disabling-pull-requests)
- [Official sources 4](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-commit-signoff-policy-for-your-repository)

## Source changes, history and repository derivation

Group ID source-and-history-policy.

Capabilities repository-content, repository-git-objects, repository-history, repository-lfs-submodules, repository-templates, repository-forks, repository-commit-comments.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| content.ref / expected sha | immutable commit SHA, branch, tag; update blob SHA | Read immutable refs for evidence; use Git for multi-file work and expected old SHAs for API writes. | Inspect resulting commit tree and parents plus changed-file list; reconcile timeout before retry. |
| ref.force / git push strategy | non-force, force-with-lease when explicitly justified | Preserve human commits; default to non-force updates, compare remote head and use a lease only for authorized history rewrite. | Fetch and compare old/new ref OIDs; stop if remote changed unexpectedly. |
| merge history | merge commit, squash, rebase | Follow repository policy; merge preserves branch commits, squash gives one logical commit, rebase rewrites commit identities. | Match resulting base-branch commit and PR merge metadata; keep issue/PR links as decision history. |
| template.include_all_branches / fork.default_branch_only | boolean choices | Template copies start a separate history; forks preserve an upstream relationship. Choose based on contribution versus new-project intent. | Inspect parent/source or is_template relationship and compare expected branches/files. |
| LFS / submodule checkout | pointer versus object, pinned SHA, recursive checkout | Fetch only required objects and pinned submodules; never treat an LFS pointer or gitlink as tested source content. | Verify actual object bytes, submodule OIDs and executable/symlink modes. |
| comment anchor | commit SHA, file path, valid line | Commit comments discuss a specific historical revision; use a PR review thread for an actionable PR finding. | Read returned comment ID, commit_id and line metadata; retain URL when following up. |

### Pitfalls

- A Git clone does not contain issues, review conversations, Project configuration or Wiki history. Separate evidence stores are needed for those records.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/repos/contents)
- [Official sources 2](https://docs.github.com/en/rest/git/refs)
- [Official sources 3](https://docs.github.com/en/pull-requests/reference/pull-request-merges)

## Who receives review and when

Group ID codeowner-routing.

Capabilities repository-codeowners, pr-review-requests.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| CODEOWNERS location / matching order | .github/CODEOWNERS, root CODEOWNERS, docs/CODEOWNERS; last matching pattern | Use one authoritative file on the PR base branch, broad ownership first and narrow overrides later; list multiple owners together. | Read actual base-branch file, query CODEOWNERS errors and map representative changed paths. |
| owner eligibility | user with write, visible team with explicit write | Reuse real maintainers; do not invent a reviewer or broaden team visibility/access to make routing work. | Verify team visibility and repository role; inspect requests on a matching ready PR. |
| requested_reviewers / requested_teams | user logins, organization team slugs | Request the smallest relevant set; requests notify people, so repository setup alone is not authority to send them. | Read outstanding review requests and submitted reviews separately; a removed request may mean review completed. |
| draft to ready | draft, ready for review | Keep incomplete work draft; move ready when description, diff and checks support review. CODEOWNERS automatic requests happen on readiness. | Re-read isDraft and automatic requests; explain review scope in the authorized PR description. |
| require_code_owner_reviews | false, true through branch policy | Routing alone never enforces approval; enable enforcement where actual independent owners exist and repository rules call for it. | Read effective protection/ruleset plus PR reviewDecision; avoid self-approval deadlock. |

### Pitfalls

- The author cannot approve their own PR. A single-maintainer repository may deliberately require zero peer approvals while retaining routing and required checks.

### Official sources

- [Official sources 1](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [Official sources 2](https://docs.github.com/en/rest/pulls/review-requests)

## Issue chooser and PR template routing

Group ID issue-intake-routing.

Capabilities issue-forms-templates, pr-templates.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| chooser.blank_issues_enabled / contact_links | true, false; name/url/about entries | Keep an accessible path for unusual reports; route support and private vulnerabilities to actual staffed destinations. | Render chooser as intended contributor; open every contact URL without submitting. |
| form.name / description / title | unique chooser name, purpose text, optional title prefix | Separate reproducible defects from proposals only when triage differs; avoid prefixes duplicating structured type. | Open every template on default branch and check readable chooser order and defaults. |
| form.labels / assignees / type | existing labels, assignable users, existing owner issue type | Reuse taxonomy; default assignees only when maintainers accept that responsibility; labels must already exist. | Check available labels/types/assignees and inspect a permitted representative result. |
| form.projects | OWNER/NUMBER list | For external reporters prefer Project auto-add because template project insertion needs the submitter's write access to that Project. | Verify with relevant contributor permission context; do not use maintainer success as outsider proof. |
| PR template selection | .github/pull_request_template.md, PULL_REQUEST_TEMPLATE/name.md and template query | Use concise purpose/validation/risk prompts; multiple templates need an actual selection link/process, not an assumed automatic chooser. | Open new-PR draft composer and test the intended template URL without posting. |
| inheritance / placement | repository templates, owner .github defaults | Inventory inherited files before adding duplicates; default-branch placement controls normal chooser availability. | Compare effective chooser and local/owner file sources, including casing and extension. |

### Pitfalls

- Issue forms become editable Markdown; required form controls are intake aids, not permanent structured-field enforcement. Issue forms are not PR forms.

### Official sources

- [Official sources 1](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
- [Official sources 2](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)

## Nested form controls and validation

Group ID form-controls.

Capabilities issue-forms-templates.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| body[].type / id | markdown, input, textarea, dropdown, checkboxes, upload; unique alphanumeric/-/_ IDs | Pick the control matching the answer; use stable unique IDs for supported prefills and future maintenance. | Validate schema and render each control on the target host; require a non-markdown control. |
| input.attributes | label, description, placeholder, value; validations.required | Require actionable minimum information, not optional diagnostics; placeholders are examples, values are submitted defaults. | Clear required inputs in preview and inspect validation behavior without posting. |
| textarea.attributes | label, description, placeholder, value, render; validations.required | Use render for literal logs/code only; omit it when Markdown editing or attachment affordances are needed. | Check code-fence output and attachment/Markdown behavior in composer. |
| dropdown.attributes | options[], multiple true/false, default index; validations.required | Default only when the common choice is safe; use no default when choosing version/platform must be deliberate. | Check unique options, index bounds, single versus multiple selection and empty validation. |
| checkboxes.attributes.options[] | label, required true/false | Require only a meaningful acknowledgement; individual required flags differ from an optional checklist. | Test unchecked required item and check rendered links and separate labels. |
| markdown / upload | markdown.value, upload label/description/required where supported | Markdown guidance is not submitted content; keep critical reporting requirements in actual controls. Upload only needed files with privacy guidance. | Preview target schema support; inspect attachment expectations and avoid requesting secrets. |

### Pitfalls

- Do not invent regex validators, conditional controls or arbitrary client logic; unsupported YAML keys can prevent the form appearing.

### Official sources

- [Official sources 1](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema)
- [Official sources 2](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/common-validation-errors-when-creating-issue-forms)

## Types, labels, owners and milestone planning

Group ID issue-taxonomy.

Capabilities issue-metadata, issue-assignees, issue-milestones, issue-types, issue-types-owner.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| issue.type / owner definition | enabled type ID, null; name/description/color/is_enabled | Prefer the owner's existing Bug/Task/Feature equivalents; types describe work kind rather than transient status. Owner edits affect other repositories. | List owner and repository types, then read the issue's assigned type ID. |
| labels[] / label color-description | names and IDs, six-digit color, explanatory description | Labels serve useful cross-cutting queries; preserve customized names/colors and add/remove narrowly instead of replacing all. | Compare before/after label ID sets and rendered descriptions; check saved filters still match renamed labels. |
| assignees[] | eligible user logins, empty list | Assign a responsible person only when the task or project convention authorizes it; assignment does not mean acceptance. | Check assignability then re-read the exact assignee set; do not confuse PR reviewer and assignee. |
| milestone.title / description / due_on / state | repository milestone, ISO8601 date, open/closed | Use milestones for real releases/deadlines, not arbitrary duplicates of Project iterations; dates are targets. | Read milestone counters and all included open/closed issues and PRs; closing milestone does not close work. |
| metadata mutation mode | add, remove, replace | Use delta mutations for focused edits; reserve replace for an explicitly reconciled full desired set. | Re-read concurrent metadata before write and confirm unrelated labels/assignees remain. |

### Pitfalls

- Do not create a new taxonomy each run or use a label named Feature as proof native issue type is configured.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/issues/labels)
- [Official sources 2](https://docs.github.com/en/rest/issues/assignees)
- [Official sources 3](https://docs.github.com/en/rest/issues/milestones)
- [Official sources 4](https://docs.github.com/en/rest/orgs/issue-types)

## Shared issue definitions and Project-local fields

Group ID shared-issue-fields.

Capabilities issue-fields, issue-field-values, projects-issue-fields, projects-multiselect.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| field scope / applicability | owner issue field, Project field; same-owner issues only | Put reusable facts on the issue; Project issue-field cells are empty for PRs, draft items and issues from other owners. | Read owner definition, issue sidebar and Project column as intended audience; missing applicability is not missing data. |
| visibility / API enum | Restricted/Public in UI, restricted/all in REST, deprecated organization_members_only | Retain restricted default for nonpublic planning facts; public/internal Projects expose only Public issue fields. Changing to Restricted removes the field from those Projects. | Read exact API visibility and inspect viewer/sidebar/timeline/Project behavior; do not change visibility merely to display a column. |
| pin to types / field limits | selected issue type IDs, Issues without a type, no pins; current 25 owner fields/100 select options/10 pins per type/50 total Project fields | Pin relevant fields so creation/view surfaces show them automatically; unpinned fields remain available through Add field and Projects. Limits differ from Project single-select options. | Read pin mapping for typed and untyped issues and count all system/issue/local Project fields; verify target-host limits before creating. |
| data_type / typed value | text, number, date, single_select, multi_select where supported | Select type from actual schema; use date for dates and number for arithmetic, not formatted strings. | Inspect supported owner and Project types separately; round-trip one permitted value of the selected type. |
| select options | stable ID, name, description, color; default where supported | Reuse IDs; rename in place when supported, never recreate populated options just to reorder or recolor. | Export affected values before change and compare option IDs and representative assignments afterward. |
| issue field values operation | add, set, delete; typed scalar or option IDs | Preserve unrelated values and distinguish adding multi-select members from replacing the selected set. | Read all current issue-field-values and compare exact changed field and option IDs. |
| intake population | sidebar, API, Actions, supported Project column | Do not promise template or URL prefill of native issue fields; those are currently unsupported in the consulted product guide. | Verify creation path then read the issue fields, not Markdown text that happens to have the same heading. |

### Pitfalls

- A community preview announcement is not proof of API type support or entitlement. Inspect the exact host schema and actual rendered field.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-and-managing-issue-fields)
- [Official sources 2](https://docs.github.com/en/rest/issues/issue-field-values)
- [Official sources 3](https://docs.github.com/en/rest/orgs/issue-fields)
- [Official sources 4](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-issue-fields)
- [Official sources 5](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-fields)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/202760)

## Completion, hierarchy, blockers and identity

Group ID issue-state-and-relations.

Capabilities issue-lifecycle, issue-subissues, issue-dependencies, issue-related, issue-transfer-pin-duplicate, issue-linked-branches, issue-planning-status.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| state / state_reason | open, closed; completed, not_planned, reopened where accepted | Close completed only with acceptance evidence; not-planned needs a decision reason; reopen the original issue for the same unfinished work. | Read state/state_reason and timeline; closing is not deployment verification. |
| parent / child order | issue database IDs, parent relationship, ordered sub-issues | Use one parent for decomposition, preserve child identity and ordering; avoid manufacturing hierarchy for unrelated work. | Read parent and child sides, all pages and final sibling order; current product limits are 100 children and eight levels. |
| blocked_by / blocking | directed native issue dependencies | Record A blocked by B when B must finish first; parenthood and a mention do not establish dependency. | Query both directions and verify no self/cyclic/duplicate relationship accepted by the host. |
| related / duplicate | related edge, duplicate_of, mark/unmark duplicate | Link peers as related; point duplicates to the canonical issue and retain the reporter's reproduction details there by reference. | Read canonical URLs and relationship timeline; do not delete duplicate history. |
| transfer / pin | destination repository, pinned/unpinned | Transfer only after access/ownership consequences are understood; use pins for durable current entry points, not every issue. | Follow old URL, read new repository/number/ID, metadata and relationship preservation. |
| linkedBranch.repositoryId / name / oid | chosen repository, branch name, base commit | Start from observed default/base SHA unless task needs a release branch; link existing work before creating duplicate branches. | Read actual ref OID and issue linkedBranches; link does not substitute for a closing PR. |
| planning status | discovered status ID, duplicate reference where supported | Preview planning statuses may transition issue state; use only after discovering viewerCanSetStatus and available statuses. | Read status plus open/closed state and duplicate target; do not equate it to Project Status. |

### Pitfalls

- Removal of a hierarchy/dependency edge is not deletion of either issue. Native relationships need actual API/UI evidence, not a checklist in the body.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/issues/issues)
- [Official sources 2](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)
- [Official sources 3](https://docs.github.com/en/rest/issues/issue-dependencies)
- [Official sources 4](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue)

## Human conversation and durable evidence

Group ID timeline-and-conversation-preservation.

Capabilities issue-comments, issue-timeline, issue-artifacts, repository-history.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| read model | issue body, paginated comments, timeline events, reviews and threads | Read all relevant streams before replying; issue body and last few visible comments omit decisions, force pushes, transfers and prior review outcomes. | Independently paginate nested connections; reconcile IDs/timestamps and retrieve referenced objects. |
| edit versus append | correct current body, new progress/decision comment, retain superseded links | Edit the canonical description to reflect current scope; append material decisions and corrections when authorized so reasoning remains chronological. | Compare prior content and edit history where available; retain earlier evidence URLs and authorship. |
| comment/reply location | issue conversation, PR summary, review thread reply, Discussion answer | Reply in the thread containing the question; distinguish implemented fix, justified disagreement, unresolved question and deferred follow-up. | Read thread root/reply IDs and resulting thread state; never claim a pending review was delivered. |
| notifications / mentions | direct mention, team mention, no mention; user subscription | Mention only relevant people when an authorized message needs their attention; do not silently change watch/subscription settings. | Inspect recipient and final posted location; API success is not proof the user read the message. |
| attachments / artifacts | canonical ID, immutable URL/ref, access-restricted resource | Preserve attachment identity and permissions; reference existing logs/files instead of re-uploading private content publicly. | Verify readable content with permitted audience and identify expiry; attachment presence is not content validation. |
| recovery after ambiguous write | reconcile by ID/body/context, retry missing write only | Avoid duplicate posts after timeouts; inspect recent author/timestamp/body and relationship events before retry. | Capture canonical ID/URL and distinguish already-applied from unapplied writes. |

### Pitfalls

- Git history is not conversation history; activity feeds are not complete audit logs. Loading an old thread in UI may collapse large portions.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/issues/timeline)
- [Official sources 2](https://docs.github.com/en/rest/issues/comments)
- [Official sources 3](https://docs.github.com/en/graphql/reference/users#usercontentedit)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/5119)
- [Community reports 2](https://github.com/orgs/community/discussions/33551)

## PR intent, comparison base and connected work

Group ID pr-creation-and-linking.

Capabilities pr-lifecycle, pr-linking, pr-templates, pr-stacks, pr-archival.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| head / base / draft | owner:branch, repository base branch, boolean | Discover existing PR before creating; choose correct target release/default branch and draft state from readiness. | Read head repo/ref/SHA, base ref/SHA and isDraft; inspect full diff against merge base. |
| title / body / maintainer_can_modify | current problem and result, validation and limits, boolean | Describe final scope and evidence; allow fork-maintainer edits only when contributor intent and repository trust permit. | Re-read rendered description and fork edit permission; retain rationale and linked decisions. |
| closing keyword / manual development link | closes/fixes/resolves #N, OWNER/REPO#N, manual same-repo link | Use closing intent only for fully satisfied issues targeting default branch; use plain references for partial work or release-target PRs. | Check development links before merge, issue state and timeline after merge; commit-only closing may omit PR sidebar linkage. |
| base retarget / branch rewrite | new base, merge update, rebase update | Recheck scope before retargeting; changing base can remove visible commits and make inline comments outdated. Preserve decision URLs and communicate material scope changes in authorized flow. | Compare old/new base/head SHAs, diff, review freshness and unresolved/outdated threads. |
| native stack / archival | detected stack relationship, archive/unarchive | Use native stack support only where available; archive is distinct from close, branch deletion and Project archive. | Read actual stack/base relationships or archived/state fields and timeline; do not simulate support with text and label it configured. |

### Pitfalls

- A PR references the live head branch; pushing after review changes the material under review. Closing without merge does not mean delivered.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/pulls/pulls)
- [Official sources 2](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
- [Official sources 3](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/changing-the-base-branch-of-a-pull-request)

## Review decisions, anchors, pending state and resolution

Group ID review-submission-and-threads.

Capabilities pr-reviews, pr-review-comments, pr-file-view-state.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| review.commit_id / event | observed head SHA; omitted event=PENDING, COMMENT, APPROVE, REQUEST_CHANGES | Bind evidence to the reviewed head. Draft/pending reviews are private; submit only the intended decision and explain actionable findings. | Read review ID, commit_id, state, submitted_at and comments; author cannot approve own PR. |
| inline anchor | commit_id, path, line/side, start_line/start_side, subject_type line/file | Anchor to an actual diff on the observed SHA; prefer current line/side coordinates, not deprecated positional guessing. | Re-read comment diff_hunk, original/current line and commit IDs; wrong anchor requires correction, not silent relocation. |
| reply and suggestion | in_reply_to root ID, suggestion block, batched application | Preserve original conversation; inspect suggestions as code, batch related accepted edits and verify new commits. | Read replies and resulting branch SHA; rerun affected checks after applying suggestions. |
| viewed files / diff settings | mark/unmark viewed, unified/split, ignore whitespace | Viewed is personal progress, not approval; inspect whitespace when meaningful and unmark changed files requiring another pass. | Read viewerViewedState as same viewer and current path/head; record what was actually reviewed. |
| thread.resolve / reopen | resolved, unresolved, outdated | Resolve after code/evidence addresses the finding or recorded agreement; outdated merely means anchor drift, not fixed. | Read isResolved/isOutdated and implementing commit or linked follow-up; preserve unresolved material objections. |
| dismissal.message / restrictions | required rationale, eligible actor | Dismiss only invalidated/unavailable-reviewer feedback with an explicit reason and policy authority; do not erase dissent to unblock merge. | Read dismissed review state and timeline rationale plus remaining effective review requirements. |

### Pitfalls

- Review comments, issue-style PR comments and commit comments are different stores. Never respond to only the summary while missing inline threads.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/pulls/reviews)
- [Official sources 2](https://docs.github.com/en/rest/pulls/comments)
- [Official sources 3](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request)
- [Official sources 4](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/dismissing-a-pull-request-review)

## Merge settings and asynchronous delivery

Group ID merge-options-and-delivery.

Capabilities pr-merge, pr-auto-merge, pr-merge-queue, pr-update-revert-cleanup, pr-agent-merge.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| allow_merge_commit / allow_squash_merge / allow_rebase_merge | independent booleans | Follow existing history policy and effective branch rules; retain squash-only delivery where the repository policy requires it. Avoid introducing several methods without a reason. | Read repository flags and allowed methods in effective rules; inspect actual resulting commit topology. |
| squash_merge_commit_title / message | PR_TITLE or COMMIT_OR_PR_TITLE; PR_BODY or COMMIT_MESSAGES or BLANK | Prefer stable PR title plus reviewed useful body for a one-change PR; inspect generated message for accidental skip directives or sensitive diagnostics. | Preview final message and read resulting commit; verify expected CI ran on the merged SHA. |
| merge_commit_title / message | PR_TITLE or MERGE_MESSAGE; PR_BODY or PR_TITLE or BLANK | If merge commits are enabled, choose a useful durable description without dumping transient logs. | Read supported enum payload and final commit message; no configuration claim from preview alone. |
| merge.sha / merge_method | exact reviewed head SHA, merge/squash/rebase | Guard the merge against concurrent head changes; do not override required checks, outstanding review or queue to satisfy a local plan. | Re-read current head and gate state, then resulting merged flag, merge_commit_sha and base ref. |
| auto-merge / queue entry | enabled/disabled, selected allowed merge method, queued state | Enable only for reviewed intent and qualifying rules; enqueue/enable is pending work, not completion. | Poll meaningful state changes until merge/failure or handoff; inspect queue removal reason and merged commit checks. |
| update_branch.expected_head_sha / delete_branch_on_merge / revert | expected head guard, boolean, revert PR | Update only after inspecting divergence; delete truly merged disposable branches, retain long-lived branches. Revert through a tracked PR rather than history rewrite. | Confirm head after update, branch absent only when intended, and revert result against merged commit. |

### Pitfalls

- Squash of a reused long-lived branch can replay prior commits in later PRs; start a fresh branch. Agent-merge eligibility must be checked separately.

### Official sources

- [Official sources 1](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests)
- [Official sources 2](https://docs.github.com/en/pull-requests/reference/pull-request-merges)
- [Official sources 3](https://docs.github.com/en/rest/pulls/pulls)
- [Official sources 4](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/179965)

## Project scope, access and item identity

Group ID project-identity-access.

Capabilities projects-lifecycle, projects-access, projects-items.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| owner / number / node ID | organization Project, user Project, stable project ID | Reuse an existing matching Project; store owner/number/URL and node ID, never treat repository Projects flag as owner Project setup. | Read Project owner/ID/title/closed/public and linked repository list. |
| visibility / base permission / explicit collaborators | public/private, none/read/write/admin where available, users/teams | Choose least privilege for the real audience; repository access and Project access are separate. Draft titles and custom data can expose information. | Read base/explicit grants and inspect as intended reader; do not broaden repo access to make a Project readable. |
| item content type / IDs | Issue, PullRequest, DraftIssue; item ID distinct from content ID | Keep tracked work as native issues/PRs; draft ideas are appropriate before a repository is selected. Reuse existing item for content ID. | Paginate items and match content node ID/URL, including archived entries. |
| draft conversion | destination repository, issue metadata | Convert when the work has a responsible repository; preserve draft body, relevant fields and links, and check access before conversion. | Read returned issue URL and item content type/field values; do not create a second item for the same work. |
| item reorder / archive / delete | relative item order, archived flag, remove from Project | Use archive for recoverable history; deletion removes membership/field data, not the underlying issue. | Compare item IDs and saved values; restore archive when needed and verify representative fields. |

### Pitfalls

- Successful item-add is not proof that every view will show it: filters, archives, pagination, permissions or a service incident can hide the item.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects)
- [Official sources 2](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-visibility-of-your-projects)
- [Official sources 3](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/193194)

## Project field configuration and value integrity

Group ID project-field-schema.

Capabilities projects-fields, projects-field-values, projects-issue-fields, projects-multiselect.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| field data type / semantic scope | text, number, date, single select, iteration, supported multi-select, built-in issue fields | Reuse built-in title/assignee/type/milestone and shared issue facts; create local fields only for Project-specific planning. | Inventory field IDs/types and example values; distinguish issue fields from similar-name local fields. |
| Status options / order / default | discovered IDs; e.g. Todo/In Progress/Done; optional default | Retain established names/IDs and explicitly define completion. Default to intake/Todo only if all newly added work is truly queued. | Read options/default and a newly added versus existing item; default changes must not silently rewrite old work. |
| select label / description / color | option ID, label, meaning, available color enum | Give ambiguous statuses a usable entry/exit definition; preserve IDs across cosmetic changes. Colors supplement text, never replace meaning. | Compare option IDs before/after, sampled assignments and UI descriptions; inspect schema before option-list replacement. |
| field mutation payload | typed text/number/date/singleSelectOptionId/iterationId, supported multi-select values | Send exactly the relevant value member using discovered IDs; clearing a field is a separate intentional action. | Read the changed field value and verify unrelated values remain; preserve zero versus unset. |
| field deletion / option removal | keep, migrate, delete with affected-value inventory | Migrate populated values before any authorized deletion; export mapping because recreating the same name may not recover identity. | Compare all affected item values and saved-view/filter/workflow references; never prove safety using only one empty item. |

### Pitfalls

- Current single-select guide documents at most 50 options and an optional default for newly added items; target API/UI default support still requires discovery.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields)
- [Official sources 2](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-text-and-number-fields)
- [Official sources 3](https://docs.github.com/en/graphql/reference/projects)

## Iteration schedules and rollover

Group ID project-iterations.

Capabilities projects-iterations.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| iteration configuration | start date, duration number, days/weeks | Match the actual team's planning cadence and timezone assumptions; do not auto-create indefinite schedules. | Read configuration plus automatically created iterations and exact IDs/dates. |
| iteration instance | title, startDate, duration, completed/active iteration ID | Preserve completed iteration identity and assignments; amend future dates deliberately rather than shifting historical interpretation. | Compare old/new date ranges and representative assigned work. |
| breaks | insertion point, break date range | Reflect actual holidays/pauses; inspect generated dates after insertion rather than assuming later schedule is unchanged. | Re-read all affected intervals and check no unintended overlap or shifted promised dates. |
| rollover | selected unfinished items, target iteration ID, preserve completed assignments | Move only unfinished selected work when agreed; keep prior commitment context in authorized update/history instead of silently rewriting all scope. | Compare item IDs/status and previous/target iteration assignments, including nonselected completed work. |

### Pitfalls

- An iteration field initially creates three iterations; a break initially follows the prior duration. Product defaults are starting data, not a planning decision.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-iteration-fields)

## View identity, shared configuration and safe filters

Group ID project-saved-views.

Capabilities projects-views, projects-layout, projects-filters.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| view name / layout / position | table, board, roadmap; saved view ID/order | Name views by the decision they support, e.g. Intake, Active work, Release roadmap; set default/first useful view for readers. | Read every saved view and reload shared URL, including ordering and unsaved-change indicators. |
| filter scope | repo/is/reason/assignee/label/type and custom field qualifiers supported in view | Store exact query, not a prose claim; include explicit repo/type/state where needed and quote multiword names. | Check representative included/excluded items and zero-value/unassigned cases; a filter is not an access boundary. |
| number/date/iteration comparison | > >= < <=, ranges, @current/@next where supported | Use date/iteration semantics of this surface, not issue-search syntax; check boundary and timezone behavior with known values. | Inspect edge dates and missing values; compare returned content IDs to expected fixtures/current known items. |
| view save / duplicate / reset / delete | saved shared changes, duplicate, discard unsaved, remove view | Save intended shared configuration explicitly; use a duplicate for experimentation and do not delete a view with active shared links casually. | Reopen as reader/new session and check persistent configuration and old navigation links. |
| API versus UI | current REST view endpoints, GraphQL view mutations, UI advanced controls | Discover actual supported request fields; REST creation and GraphQL view CRUD exist, so avoid blanket UI-only claims. | Read saved configuration through supported surface; use rendered verification for unsupported controls. |

### Pitfalls

- Auto-add and auto-archive have narrower filter grammars than views. A valid view query cannot be copied blindly into automation.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/managing-your-views)
- [Official sources 2](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects)
- [Official sources 3](https://docs.github.com/en/rest/projects/views)

## Table and board nested controls

Group ID project-layout-controls.

Capabilities projects-layout, projects-views.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| visible fields / column order / card fields | selected field IDs, ordering, shown/hidden fields | Show owner, status and the facts needed for this view; hide unused noise while preserving stored data. | Reload saved view and inspect expected header/card fields and order. |
| board column field / visible columns / limits | single-select or iteration field, displayed values, column limit where offered | Use Status for execution, iteration for planning; hide columns only with an alternate way to find excluded work. Column limits are planning signals, not enforcement. | Verify field ID and value-to-column mapping; inspect hidden/no-value work and displayed limits. |
| group by / vertical_group_by | supported field, no grouping | Group by responsible person, parent or priority for a real triage question; dragging across groups can edit underlying fields. | Read fields after an authorized drag and verify parent/assignee effects rather than assuming presentation-only movement. |
| slice by | supported field, no slicing | Use for fast per-team/repository focus; title/reviewers/linked PRs are not supported slice fields in current guide. | Check slice plus saved filter intersection and clear selection to recover full view. |
| sort primary/secondary / direction | field IDs, ascending/descending, no sorting | Use priority/date order when that drives work, manual order for explicit ranking; sorted boards disallow manual ordering within columns. | Read saved sorting and known equal-value tie examples; distinguish drag-to-column mutation from reorder. |
| field sums | count, selected numeric fields | Sum only compatible measures; points are estimates and mixed currencies/units must not be combined. | Recompute a representative group from actual item values and compare displayed aggregate. |

### Pitfalls

- Grouping a multi-assignee issue can show it in several groups; avoid interpreting row/card counts as unique work without checking IDs.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-table-layout)
- [Official sources 2](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-board-layout)

## Roadmap dates, markers and time windows

Group ID project-roadmap-controls.

Capabilities projects-layout, projects-views.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Date fields.Start date / Target date | chosen date or iteration field IDs | Bind to explicit planning fields, not guessed names; distinguish planned dates from actual completion evidence. | Read both mappings and compare bar boundaries to item values; inspect undated work separately. |
| Markers | iterations, milestone dates, item dates | Display only useful commitment/reference markers to avoid implying every date is a release deadline. | Inspect labels and actual source milestone/date values. |
| Zoom | Month, Quarter, Year | Choose the smallest window supporting the planning decision; preserve a useful shared overview. | Reload view and inspect expected time window and clipped/offscreen work. |
| roadmap drag / resize | changes start/target dates or selected iteration | Treat dragging as a real scheduling mutation; avoid accidental date changes during inspection. | Read changed field values and affected automation afterward; restore exact original values on accidental edit. |
| group / slice / sort / sums | supported fields and order, none | Apply the same data-integrity rules as other layouts; maintain access to ungrouped/undated items through a table view. | Compare item IDs across roadmap and table to explain omissions without inventing missing work. |

### Pitfalls

- A visually complete roadmap can exclude undated items; never equate visible bars with all project scope.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout)

## Event-driven Status transitions and issue closure

Group ID project-event-workflows.

Capabilities projects-workflows, projects-field-values.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| workflow enabled / target field-option | per-workflow enabled flag, discovered Status option ID | Inventory every built-in event workflow before manual reconciliation; retain behavior only when transition matches the project's definition. | Read workflow trigger/enabled/target and verify a permitted representative transition. |
| item added → Status | disabled, intake/Todo option | Default new work to intake if untriaged; do not overwrite imported/customized existing work as a setup side effect. | Observe new item value, existing populated item and applicable field default together. |
| issue/PR closed → Done | enabled default, disabled, alternative supported option | Closed-not-planned is not successful delivery; decide whether one Done column intentionally includes cancellation or needs separate reporting. | Check reason and resulting Status for completed and not-planned examples; correct mismatches without reopening rejected work. |
| PR merged → Done | enabled default, disabled, supported option | Merge may be completion for library work, but deployed systems may still require QA/release. Define that boundary explicitly. | Read merged commit, item Status and downstream release/deployment evidence separately. |
| Status change → issue state | disabled, close issue on configured transition where supported | Enable only when board transitions truly authorize closing the issue; avoid circular/competing automation. | Read issue state/reason and both directions of workflow behavior; identify unexpected loops or last-writer wins. |
| reopen / ready / review-related events | discovered host workflows | Inventory actual available triggers and decide each applicability rather than assume all event workflows exist everywhere. | Read current workflow list/schema/UI and verify exact resulting option IDs after relevant event. |

### Pitfalls

- Initialization enables closed→Done and merged→Done. A successful Status write can be immediately changed by another workflow; verify after automation settles.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)

## Auto-add filters, backfill and execution identity

Group ID project-auto-add.

Capabilities projects-auto-add, projects-actions.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| auto-add.repository / filter | per-repository selector, is/label/reason/assignee/no subset | Scope to intended repository and item kind; exclude automation noise deliberately. Validate native grammar independently of view query. | Read enabled workflow and exact filter; inspect a matching and a nonmatching permitted item. |
| filter values / negation | is:open/closed/merged/draft/issue/pr, label names, reason, assignee, no:label/assignee/reason | Use supported values and negation (no does not support negation); quote labels. Do not invent arbitrary custom-field auto-add filters. | Preview/save and confirm actual matching content IDs; compare available grammar with current official guide. |
| workflow count / duplicate | plan-dependent 1/5/20 limits currently documented, unique filters | Reuse existing workflows; Free has one, Pro/Team five, Enterprise twenty in current guide. Record plan gate rather than adding a token workaround silently. | Read actual count and entitlement; verify each repository selector and duplicate filter. |
| existing backlog | explicit paginated backfill, future matching creates/updates | Enabling auto-add does not backfill existing matches; reconcile backlog as a separate authorized operation preserving item values. | List source issues/PRs, compare content IDs to active/archive membership and add only missing items. |
| custom Action identity | installation token or authorized user credential, least Project/repository permissions | Repository GITHUB_TOKEN generally cannot stand in for owner Project write access; prefer a scoped App only when native workflow is insufficient. | Inspect workflow/token permissions without exposing secrets; verify membership and typed field values after execution. |

### Pitfalls

- Creating a dummy issue to test automation sends real notifications and is not a read-only check; use existing evidence or an explicitly authorized representative fixture.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically)
- [Official sources 2](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions)

## Retention filters, existing matches and restoration

Group ID project-auto-archive.

Capabilities projects-auto-archive, projects-items.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| auto-archive.enabled / filter | disabled, enabled; is/reason/updated only | Prefer disabled until retention criteria are agreed; custom Status is not supported in this automation grammar. | Read exact saved filter and enabled state; enumerate matching existing items before enable. |
| retention clock | updated relative-date expression supported by current surface | Do not call last-updated age closed-age; comments/labels/assignees/milestones/field changes can reset update time. | Test known boundary examples in this automation surface; record literal filter rather than translating comparator from memory. |
| existing matches | immediately eligible after enable, potentially delayed processing | Inventory affected IDs/values first; unlike auto-add, auto-archive also processes old matching items. | Compare before/after active and archive IDs and counts until processing settles. |
| archive versus capacity | recoverable archive, Project membership deletion | Archive keeps custom data and supports restore but still counts toward current 50,000 combined item limit. Deletion needs a separate retention decision. | Read archive entries and restored values; verify underlying issue remains unchanged. |
| recovery | disable workflow, restore selected archived item IDs | Stop faulty automation first, restore exact affected items and values, then correct filter before re-enabling. | Re-read saved filter and representative restored fields; inspect re-archival to detect remaining bad criteria. |

### Pitfalls

- Historical Community reports describe invalid filters partly executing; do not present that old bug as current. Validate native grammar and preserve a restoration inventory.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically)
- [Official sources 2](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/archiving-items-from-your-project)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/36466)
- [Community reports 2](https://github.com/orgs/community/discussions/17085)

## Charts, historical interpretation and project health

Group ID project-insights-and-updates.

Capabilities projects-insights, projects-updates.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| chart filter / layout / X-axis / group | supported chart types, selected category field, Time for historical chart, group or None | Name the actual decision and denominator; chart filters are their own saved configuration, not inherited proof from an open view. | Open saved chart and compare included content IDs/known sample; verify reader access. |
| Y-axis / numeric field | count, sum, average, minimum, maximum; selected numeric field | Count unique work or aggregate compatible numeric units; never equate estimate sums with actual labor or outcome value. | Recompute sample groups including missing/zero values and inspect saved aggregate and field mapping. |
| historical chart state / retention | Time axis; Open/Completed/Closed pull requests/Not planned | Historical charts track native issue/PR states, not arbitrary local Status history. Insights does not track archived or deleted items, so retention affects reporting. | Compare known state transitions and active/archive membership; do not report archive-filtered history as all-time delivery. |
| status update.status | ON_TRACK, AT_RISK, OFF_TRACK, INACTIVE, COMPLETE | Set overall project health from evidence, separately from issue open/closed and item Status; meaningful bad news must remain visible. | Read saved update ID/status and chronological update history. |
| status update.startDate / targetDate / body | dates, Markdown message, prior values as form defaults | Include reason, evidence and next decision; inspect inherited previous dates rather than republish stale commitments. Append meaningful updates, edit only corrections. | Read resulting dates/body and prior entries; templates cannot receive updates and subscriptions can notify readers. |

### Pitfalls

- Chart controls may require UI even when field/view APIs exist. Do not claim chart configuration from project item listing or API capability indexing.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/configuring-charts)
- [Official sources 2](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)
- [Official sources 3](https://docs.github.com/en/issues/planning-and-tracking-with-projects/sharing-project-updates)
- [Official sources 4](https://docs.github.com/en/graphql/reference/projects)

## Template/copy fidelity and initial conditions

Group ID project-copy-template.

Capabilities projects-templates, projects-lifecycle, projects-access, projects-workflows.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| copy owner / title / draft selection | organization/user owner, new title, copy draft issues checkbox | Choose destination deliberately and copy example drafts only when useful; inspect template contents for confidential planning text. | Read new owner/title/ID and copied draft bodies/values. |
| copied configuration | views, custom fields, draft field values, workflows except auto-add, insights | Treat copied settings as a starting point, not desired final state; inherited automation can immediately affect new work. | Compare each copied component and field-option mappings independently with source snapshot. |
| not copied | original issue/PR items, collaborators, team/repository links, auto-add workflows | Recreate only applicable omitted relationships and intake workflow under authorized access scope; backfill existing work separately. | Read membership, grants, links and enabled auto-add on destination; source configuration proves nothing about destination completion. |
| organization template / recommendations | mark/unmark template, recommended template list | Curate only usable templates with documented fields and workflow expectations; avoid promoting an unverified personal experiment. | Read template status and organization recommendation visibility as intended member. |

### Pitfalls

- Copied field/option IDs are destination identities; never apply source item/field IDs to the new Project by name alone.

### Official sources

- [Official sources 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/copying-an-existing-project)
- [Official sources 2](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-project-templates-in-your-organization)

## Discussion purposes, category formats and intake

Group ID discussion-categories-and-forms.

Capabilities discussions-lifecycle, discussions-organization.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| repository versus organization source | repository Discussions, designated organization source repository | Keep repo-specific support near code; organization-wide discussions need explicit source-repository governance and access review. | Read enabled surface, source repository and moderator roles; inspect audience before publishing. |
| category.name / emoji / description / format | open-ended, Q&A, announcement, Polls where offered | Use Q&A for answerable support, open-ended for design, announcement for maintainer-origin updates. Inspect current Polls control rather than treating docs prose inconsistencies as universal support. | Read category IDs and actual format/answerability; announcement posting has stricter permissions than replies. |
| section membership / category rename/delete | one section per category, rename in place, Delete & Move target | Reuse category IDs; preserve navigation and discussion history. Deleting a category moves discussions to a chosen existing category. | Compare IDs/format and counts, destination and old shared links; inspect forms after slug changes. |
| category form path / top-level schema | .github/DISCUSSION_TEMPLATE/<category-slug>.yml; body/labels/title | Match category slug exactly; use supported controls, not issue-form assignee/projects/type top-level keys. | Open actual category composer on default branch and validate required/non-Markdown fields without posting. |
| labels / pins | existing repository labels, global/category pins; four per scope | Pin actionable entry points with a moderator/response owner; avoid a duplicate label taxonomy. | Read pin location, appearance and rendered routing links; global pins and category pins are distinct. |
| category movement / poll intake | recategorize eligible discussion, Polls category cannot move to/from | Select a valid format before intake; do not promise migration of a normal topic into a poll by changing category. | Read current category/format and eligible destinations; preserve original topic links. |

### Pitfalls

- Enabling Discussions creates a surface, not a staffed support process. Define who monitors unanswered questions and how decisions become tracked work.

### Official sources

- [Official sources 1](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions)
- [Official sources 2](https://docs.github.com/en/discussions/managing-discussions-for-your-community/syntax-for-discussion-category-forms)
- [Official sources 3](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions)
- [Official sources 4](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions)

## Answers, polls, conversions and moderation history

Group ID discussion-response-and-moderation.

Capabilities discussions-lifecycle, discussions-answers.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| answer selection | mark answer, unmark, Q&A eligible comment | Mark a correct reusable solution with supporting explanation; an accepted answer is not proof a linked implementation shipped. | Read answer ID/body/author and category answerability; retain unresolved follow-up. |
| reply hierarchy / poll vote | replyToId, pollOptionId; viewerCanVote/viewerHasVoted | Respond to the right question; inspect existing viewer vote and options. Voting is personal participation, not setup. | Read reply parent and viewer vote state/counts; never cast a vote merely to test a feature. |
| poll content | discussion title/body, question, at least two options in Polls composer | Choose clear distinct options and explain how feedback informs a decision; do not invent supported close dates, anonymity or binding voting rules. | Preview composer and read poll question/options/order after an authorized creation; creation API support needs its own discovery. |
| lock / close / reason / allow reactions | lock/unlock, close/reopen, reason supported by host, reaction toggle | Prefer explanation and narrow moderation; lock restricts interaction while preserving content. Do not silence technical disagreement. | Read locked/closed/reason and rendered notice; confirm permitted moderators and reactions separately. |
| issue → discussion conversion | category ID, original issue and resulting discussion IDs | Use only when conversation rather than committed work is appropriate; explain routing when messaging is authorized and snapshot original history first. | Read both objects, canonical links, authors, all comment/reaction pages and issue closure/lock behavior; reconcile timeout before retry. |
| create issue from discussion | linked new issue in responsible repository | Track accepted actionable work while retaining the discussion decision trail; do not assume participants/subscriptions or every metadata field move. | Read both cross-links and preserve original authors and decision context. |
| transfer discussion | eligible same-owner destination repository or organization source repo | Destination creation permission is required; private-to-public and announcement transfers are unsupported. Review audience before any allowed transfer. | Read destination repository/category/access and retained comments/links; reconcile original and returned discussion IDs. |
| minimize / delete | classification and restore, irreversible deletion | Use least destructive appropriate moderation with reason; deletion is not a substitute for marking superseded information. | Read minimized state or exact deleted ID and preserve required moderation rationale without redistributing sensitive content. |

### Pitfalls

- Community conversion threads contain conflicting claims and historical incidents. Current official conversion flow exists; do not repeat a claim that conversion is universally unavailable.

### Official sources

- [Official sources 1](https://docs.github.com/en/discussions/managing-discussions-for-your-community/moderating-discussions)
- [Official sources 2](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/participating-in-a-discussion)
- [Official sources 3](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions)
- [Official sources 4](https://docs.github.com/en/graphql/reference/discussions)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/152627)
- [Community reports 2](https://github.com/orgs/community/discussions/3197)
- [Community reports 3](https://github.com/orgs/community/discussions/2952)

## Wiki content, publication, permissions and discoverability

Group ID wiki-publication-history.

Capabilities wiki-pages, wiki-navigation.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| enabled / editing audience | has_wiki, collaborators-only, public editing on eligible public repos | Default to repository writers for project policy/docs; public editing is a governance choice, not a completeness requirement. | Read repository flag and actual Wiki access control; public/private visibility follows repository audience. |
| source repository / publication ref | OWNER/REPO.wiki.git, actual wiki branch and SHA | Clone/fetch Wiki separately; preserve other contributors' commits and compare source wiki/ files before publishing. | Compare remote before/after commit SHA and rendered pages; source files alone are not proof of publication. |
| page title / filename / markup | supported file extension, stable page slug, relative links | Keep page naming stable and explicit; avoid filesystem case collisions and check renamed-page backlinks. | Render pages and follow links on GitHub, inspect separate Wiki Git log and page history. |
| navigation | Home, _Sidebar.<ext>, _Footer.<ext> | Provide install/use/config/troubleshooting navigation based on actual project scope; footer can carry source/version context. | Open every navigation destination, heading anchor and asset as intended reader. |
| change message / correction / recovery | meaningful commit, revert commit, merge remote changes | Record what changed and why; recover with a new corrective commit rather than force-overwrite others' Wiki work. | Read remote ancestry and page revision, compare preserved unrelated pages and restored content. |
| indexing / size constraints | search-engine eligibility, current soft file limit | Do not promise search-engine discovery for a small Wiki; current guide requires 500 stars and restricted public editing, with soft 5,000-file limit. | Inspect actual audience/search behavior; consider Pages only if indexing or size is an actual requirement. |

### Pitfalls

- A main-repository pull request does not review/enforce separate Wiki pushes automatically; document the publication check and do not conflate branches.

### Official sources

- [Official sources 1](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)
- [Official sources 2](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages)
- [Official sources 3](https://docs.github.com/en/communities/documenting-your-project-with-wikis/creating-a-footer-or-sidebar-for-your-wiki)
- [Official sources 4](https://docs.github.com/en/communities/documenting-your-project-with-wikis/viewing-a-wikis-history-of-changes)

## Search surfaces, query semantics and completeness

Group ID search-and-discovery.

Capabilities search-cross-github, search-code, search-issues-prs, issue-saved-views.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| code search surface | browser Code Search, REST legacy code search, local rg/git grep | Choose syntax for the actual engine; browser Boolean/regex/symbol features do not imply equivalent REST support. Use local Git for exact nondefault-revision inspection. | Record engine, repository and revision; retrieve matched file at immutable SHA before acting. |
| modern code query | repo/org/user, path/language/symbol/content, quoted strings, /regex/, AND/OR/NOT | Scope narrowly and escape literals correctly; a bare term can match path or content. Inspect actual engine limits before assuming exhaustive indexing. | Reproduce match locally at known revision and inspect excluded files/ref; empty search is not absence proof. |
| issue/PR query | is:issue/is:pr, state/reason, author/assignee, review/review-requested, linked, dates | Use explicit type and repository scope, native review qualifiers for review queues and dates for bounded investigations. | Retrieve every consequential issue/PR by ID and paginate authoritative collection for completeness. |
| Discussion query | repo/org, in:title/body/comments, category, is:answered/unanswered where supported, dates | Search existing answers/decisions before creating a new topic; category and issue-search grammars differ. | Open original discussion, current answer and full relevant replies; check date of claim and superseding staff response. |
| REST search result limits | per_page/page, incomplete_results, capped result windows | Treat results as indexed discovery; split disjoint date/repository ranges and reconcile total counts when cap or incompleteness appears. | Inspect incomplete_results and available pages, deduplicate IDs; use owning lists/GraphQL/Git if a full inventory is required. |
| saved queries / issue views | name/query, personal versus shared saved surface | Save useful triage/review queries with explicit audience; a personal saved search is not a shared Project view. | Reload as same viewer, inspect exact query and validate known expected item membership. |

### Pitfalls

- Masked private objects, indexing lag, engine-specific limits and search caps mean zero results cannot establish absence or permission. Never use obsolete legacy limits as modern Code Search limits.

### Official sources

- [Official sources 1](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax)
- [Official sources 2](https://docs.github.com/en/search-github/searching-on-github/searching-code)
- [Official sources 3](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests)
- [Official sources 4](https://docs.github.com/en/search-github/searching-on-github/searching-discussions)
- [Official sources 5](https://docs.github.com/en/rest/search/search)

## Ruleset scope, bypass and evaluation evidence

Group ID ruleset-targets-and-insights.

Capabilities repository-rulesets, ruleset-insights.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| target / conditions | branch, tag, push; ref_name include/exclude; repository targeting at owner scope | Inspect inherited rules and select exact intended ref patterns, including default-branch symbolic selectors when supported; exclusion can silently remove protection. | Read ruleset IDs/source/enforcement plus effective rules for a representative matching and excluded ref. |
| enforcement | disabled, active, evaluate on eligible Enterprise plans | Disabled protects nothing; evaluate observes without blocking and needs a plan check. Preview broad new policy in evaluate where available before enforcement. | Read saved mode and rule-suite results; do not report evaluate as protected. |
| bypass_actors.actor_type / actor_id / bypass_mode | eligible role/team/App IDs; always, pull_request, exempt where supported | Preserve existing authorized exceptions and choose the narrowest useful mode; exempt does not run rules or create a bypass audit entry. | Read actor identity/mode and confirm no accidental broad role exception or App removal. |
| rule suite filters | ref, actor_name, rule_suite_result, time_period; pass/fail/bypass | Inspect operational failures and bypass use, not merely policy JSON. Check current endpoint filter enums and retention before querying. | Read suite ID, actor, ref, evaluation time and per-rule result; distinguish evaluate failures from blocked writes. |
| ruleset history / import-export | ruleset ID/version, export JSON, reviewed imported settings | Preserve baseline/version and review imported selectors/actor IDs; source owner IDs do not automatically mean destination identities. | Compare saved ruleset history, exact imported payload and effective target rules; revert with a corrective version. |

### Pitfalls

- Multiple rulesets can apply together with classic protection. A clear ruleset read does not prove the actor had no bypass or that another inherited rule did not apply.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/repos/rules)
- [Official sources 2](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository)

## Effective review/check requirements and compatible merge behavior

Group ID branch-and-merge-gates.

Capabilities branch-protection, repository-merge-policy.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| required_pull_request_reviews | required_approving_review_count, dismiss_stale_reviews, require_code_owner_reviews, require_last_push_approval | Choose actual independent reviewer availability; stale/last-push rules must match team workflow. Zero peer approval may be intentional with required checks. | Read effective rules and representative current-head review states; inspect reviewer eligibility and outstanding changes requests. |
| review dismissal / bypass restrictions | dismissal_restrictions, bypass_pull_request_allowances, users/teams/apps | Retain narrowly justified emergency routes; never add the running agent as bypass to complete setup. | Compare actor IDs and enabled restrictions, and inspect subsequent dismissal/bypass evidence. |
| required_status_checks | strict, checks context/app_id, legacy contexts | Bind stable check names to expected Apps where supported; strict requires up-to-date branch, queue needs merge_group CI support. GitHub accepts success, skipped and neutral conclusions; a skipped required job does not prove its validation ran. | Compare rules to check-run names/App IDs and results on the relevant PR/test-merge or merge-group SHA. Whole-workflow filter skips leave checks pending; conditional/dependent job skips can allow merging. Require a terminal aggregate gate that evaluates prerequisite results and fails for missing or failed required validation; verify failure and skip cases before relying on it. |
| enforce_admins / restrictions | admin enforcement boolean, allowed users/teams/apps, block_creations where supported | Decide administrator policy deliberately; push allowlists are not equivalent to review bypass. Preserve existing emergency ownership. | Read protection and ruleset bypass together; verify effective actor rights without making a disruptive test push. |
| history / signatures / deletion | require_linear_history, required_signatures, allow_force_pushes, allow_deletions, lock_branch | Match legitimate release workflow and retain no-force/no-delete for protected history unless specifically justified. Locked branches and fork-sync settings need separate intent. | Read all flags and branch status; verify merge methods remain compatible with linear history. |
| conversation/deployment/security gates | required_conversation_resolution, required deployments, required code/secret/quality rules where supported | Require gates only when their producer/workflow exists and can complete; determine exact environment/tool thresholds from the schema and project policy. | Read named environments/tool thresholds and current-head gate results; do not disable failing gates as recovery. |
| repository merge flags | allow_merge_commit/squash/rebase, allow_auto_merge, allow_update_branch, delete_branch_on_merge | Keep methods compatible with effective rules; auto-update visibility is not auto-merge or branch freshness. Clean only disposable merged heads. | Read repository flags and PR merge box/effective rule methods; inspect final merge topology and branch cleanup. |
| merge queue parameters | check timeout, minimum/maximum group size, grouping strategy, merge method where offered | Use only when contention justifies it; inspect current host schema for exact names/enums and ensure queue check triggers exist. | Read queue rule payload and representative merge_group results, queue removal reasons and merged SHA. |

### Pitfalls

- Classic protection update endpoints can replace nested objects and clear omitted policy. Snapshot and merge intended changes; one protected-branch endpoint cannot establish full ruleset enforcement.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/branches/branch-protection)
- [Official sources 2](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [Official sources 3](https://docs.github.com/en/rest/repos/repos)
- [Official sources 4](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)

## Personal watch choices, inbox triage and feed limitations

Group ID notification-and-activity-state.

Capabilities notifications-watch, notifications-inbox, activity-events.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| repository subscription | subscribed, ignored, custom event selection through supported UI | Preserve user preference; watch only requested event categories and distinguish ignored from simply not subscribed. Stars bookmark rather than subscribe. | Read subscription as same user plus UI custom categories; subscribers_count differs from legacy watchers_count/stargazers_count. |
| watcher list restrictions | admin/collaborator-only listing, deprecated user watched-repo endpoint | Current docs describe July 2026 restrictions and deprecated endpoint empty responses; do not infer nobody watches from an empty legacy list. | Check endpoint status/auth identity and direct repository subscription state. |
| inbox query | all, participating, since, before, repository, reason; UI custom filters | Choose smallest needed read window and paginate; inspect reason such as mention/review_request/assign rather than treating all notifications equally. | Read thread ID/subject/reason/unread/last_read_at and canonical owning object. |
| triage operation | read/unread, done, saved, unsubscribe | Read acknowledges visibility; done hides completed notifications, save retains attention, unsubscribe changes future delivery. Apply only explicitly intended selected threads. | Re-read selected thread and UI saved/done state; compare unaffected threads, and reconcile ambiguous writes before retry. |
| retention / subscription recovery | done retained five months, saved indefinitely, resubscribe | Inbox is not permanent project history; unsaving old notifications can make them disappear. Unsubscribe can be superseded by later mention or review request. | Preserve canonical issue/PR URLs for durable context and verify subscription after authorized recovery. |
| authentication / polling | classic PAT notifications/repo scopes per current notification docs, Last-Modified/ETag, X-Poll-Interval | Do not assume fine-grained/App tokens support notification endpoints. Respect server polling interval and conditional requests. | Inspect authentication compatibility and 304 semantics without exposing credentials; permission failure remains unknown state. |
| activity feed window | up to 300 events, past 30 days, latency 30 seconds to six hours | Use feeds for discovery, not real-time completion or complete audit history. Prefer owning issue/PR/commit state for consequential facts. | Record event ID/time and owning object evidence; honor ETag and X-Poll-Interval. |

### Pitfalls

- Personal inbox Done is unrelated to issue closure or Project Done; never complete work by clearing its notification.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/activity/watching)
- [Official sources 2](https://docs.github.com/en/rest/activity/notifications)
- [Official sources 3](https://docs.github.com/en/rest/activity/events)
- [Official sources 4](https://docs.github.com/en/subscriptions-and-notifications/how-tos/viewing-and-triaging-notifications/managing-notifications-from-your-inbox)

## Reusable drafts, reversible hiding and temporary interaction limits

Group ID community-personal-replies-and-moderation.

Capabilities community-saved-replies, community-comment-minimization, community-interaction-limits.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| saved reply title / body / selection | personal title, Markdown body, create/edit/delete, insert and customize | Store generic accurate routing text and customize to the actual report; inserting a draft does not authorize sending. Current documented cap is 100 replies. | Reload personal reply settings and preview inserted draft; do not post a test reply. |
| minimizeComment.subjectId / classifier | ABUSE, OFF_TOPIC, OUTDATED, RESOLVED, DUPLICATE, SPAM | Pick a justified classification and preserve the discussion; disagreement or inconvenient findings are not abuse. Check actor/type eligibility first. | Read viewerCanMinimize/isMinimized/minimizedReason plus original comment link and rendered visibility. |
| unminimize / deletion distinction | restore hidden comment, delete separately authorized content | Use restoration when hiding was mistaken; minimized content still exists and cannot be treated as erased sensitive data. | Read restored state and inspect full thread; handle actual secret exposure through the applicable security process. |
| interaction scope / inheritance | repository, organization public repositories, user-owned public repositories | Choose the narrowest incident scope and inspect inherited limits before overriding; broad owner controls affect uninvolved contributors. | Read effective repo and owner restrictions and record actor, scope and expiry. |
| interaction limit / expiry | existing_users, contributors_only, collaborators_only; one_day/three_days/one_week/one_month/six_months | Prefer the shortest effective restriction consistent with authorized moderation; do not silently block ordinary reporters for routine setup. | Read limit and expires_at from owning endpoint and inspect class semantics; never validate by posting disruption. |
| remove / expire / blocked users | remove temporary limit, automatic expiry, separate account blocking | Restore normal participation after incident and keep rationale; removing a repository limit does not remove an inherited owner restriction. | Re-read repo/owner limit state and separate block lists where authorized; distinguish expired from inaccessible. |

### Pitfalls

- No stable saved-reply CRUD API is established here; inspect current UI. Comment minimization, conversation lock, interaction limit and account blocking are separate controls.

### Official sources

- [Official sources 1](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)
- [Official sources 2](https://docs.github.com/en/graphql/reference/issues)
- [Official sources 3](https://docs.github.com/en/rest/interactions/repos)
- [Official sources 4](https://docs.github.com/en/rest/interactions/orgs)
- [Official sources 5](https://docs.github.com/en/rest/interactions/user)

## Personal availability, bookmarks, featured work and following

Group ID profile-personal-presence.

Capabilities profile-status, profile-star-lists, profile-content-pins, profile-follow-organizations.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| status content / scope | emoji, message, organizationId or public null | Preserve user wording and audience; avoid publishing private project details as status. Organization-scoped status is not an organization announcement. | Read emoji/message/organization and inspect rendering as intended audience. |
| status availability / expiration | limitedAvailability boolean, expiresAt timestamp, clear status | Set busy only for requested availability; use intended timezone converted to exact expiry rather than leave a temporary absence indefinitely. | Read indicatesLimitedAvailability/expiresAt and verify removal/expiry; personal status is unrelated to work-item Status. |
| star list name / description / membership | create/update/delete list, repository membership IDs, starring independently | Keep bookmark organization separate from follow/watch; preserve unrelated list memberships in updateUserListsForItem replacement operations. | Read list ID/content and repository star state separately; list deletion is not repository deletion. |
| profile README / pins | USER/USER README, up to six repositories/gists combined, pin order | Publish only user-approved profile content and intended public featured work; use valid account-named repository for README. | Read immutable README commit and public rendered profile/pin order; preserve existing selections. |
| contribution/profile visibility | public/private profile, private contribution display, achievements/activity options where offered | Treat as personal privacy choice; anonymized private activity is not permission to reveal private repository names. | Inspect profile as owner and public viewer; verify current UI rather than assume profile REST edits cover these settings. |
| organization following | follow/unfollow org, viewerIsFollowing | Follow only requested organizations; preview feature supplies public activity, not membership or repository access. | Read following relation as same viewer and inspect dashboard; no requirement to generate activity for a test. |

### Pitfalls

- Personal starring, following, availability and profile changes can reveal preferences and should not be silently bundled with a repository audit.

### Official sources

- [Official sources 1](https://docs.github.com/en/graphql/reference/users)
- [Official sources 2](https://docs.github.com/en/account-and-profile/concepts/personal-profile)
- [Official sources 3](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile)
- [Official sources 4](https://docs.github.com/en/get-started/exploring-projects-on-github/following-organizations)

## Sponsors identity, eligibility and public listing

Group ID sponsors-listing-onboarding.

Capabilities sponsors-listing.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| listing identity | authenticated personal account, sponsorableLogin organization | Select the actual beneficiary, authority and supported region/fiscal-host route; do not create an organization listing for a similarly named repository owner by assumption. | Read listing/account IDs, owner/admin role and enrollment/approval state. |
| profile fields / featured opt-in | bio, introduction, featured work, matching/featured preferences where eligible | Prepare accurate public purpose and benefits; owner decides marketing consent and funding language. | Read rendered listing and saved preferences; unpublished/draft differs from publicly approved listing. |
| onboarding personal/legal fields | residence, billing/tax/provider verification, fiscal-host details | Let account owner handle required legal/banking attestations and credentials; never infer those from GitHub profile geography or commit email. | Report exact outstanding setup gate without exposing tax/bank data; listing mutation alone is not completed onboarding. |
| publication / funding link | approved listing, draft setup, FUNDING.yml sponsor button | Add funding links only to real intended supported beneficiaries; distinguish external funding URLs from an active GitHub Sponsors listing. | Open public listing and repository sponsor target as intended reader; retain owner decision about platform selection. |

### Pitfalls

- Enrollment/profile setup does not authorize a payment, bank change, tier publication or newsletter.

### Official sources

- [Official sources 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/setting-up-github-sponsors-for-your-personal-account)
- [Official sources 2](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/setting-up-github-sponsors-for-your-organization)
- [Official sources 3](https://docs.github.com/en/graphql/reference/sponsors)

## Amounts, recurrence, publication and benefit access

Group ID sponsors-tier-configuration.

Capabilities sponsors-tiers.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| amount / recurrence | amount in US dollars, isRecurring boolean, documented API range 1–12000 | Choose explicitly approved price and monthly versus one-time meaning; never confuse dollars with cents or interpret isRecurring as an arbitrary billing scheduler. | Read amount/currency/recurrence from returned tier and actual checkout; current API schema defines valid range. |
| description / welcome message | public perks, post-payment instructions | Promise only deliverable benefits, avoid private credentials in broad welcome text, and document entitlement expectations. | Preview public and purchaser-facing text and check instructions/links. |
| publish / retire | draft by default in createSponsorsTier, publish true/false, retire tier | Review concrete tier before publication. Published prices cannot be edited; retire and create a new tier for a new price. | Read published/retired state and remaining active sponsorships; retirement does not cancel existing sponsors. |
| repository benefit | organization-owned private repository ID/name, no repository benefit | Adding a benefit grants read-only access to sponsors and requires explicit access authorization; do not attach source or customer data accidentally. | Verify exact repository owner/visibility and tier benefit, plus current entitlement policy without creating a paid test sponsorship. |
| tier limits | up to ten published one-time, up to ten published monthly | Reuse meaningful existing offers rather than create redundant tiers; keep retired options visible in historical reporting. | Count active published tiers by recurrence and inspect retired-tier subscribers separately. |

### Pitfalls

- Existing sponsors can remain on a retired tier. Do not delete/replace historical tier identity to make the public price list look tidy.

### Official sources

- [Official sources 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers)
- [Official sources 2](https://docs.github.com/en/graphql/reference/sponsors)

## Payer intent, bulk partial outcomes and sponsorship privacy

Group ID sponsors-commitments-and-preferences.

Capabilities sponsors-transactions, sponsors-preferences.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| sponsorship payer / beneficiary / tier | sponsorId/login, sponsorableId/login, tierId or allowed custom amount | Resolve exact accounts and a current valid offer; do not charge a personal account when organization funding was intended. | Read account/tier IDs and current sponsorship before mutation; checkout fees/tax/payment details require current verification. |
| one-time / recurring commitment | approved amount, recurrence, payment/renewal state | Repository setup and recommendation do not authorize spending. Match the explicitly requested commitment and inspect immediate/prorated effects before submission. | Read resulting amount, recurrence, payer, beneficiary and active/pending status; financial mutation timeout requires reconcile-before-retry. |
| bulk sponsorship results | per-beneficiary input, individual success/error results | Treat batch as potentially partial, never all-or-nothing; preserve successful commitments and retry only missing authorized ones. | Read every beneficiary relationship and error individually, compare total approved versus committed amounts. |
| change / cancel | upgrade, downgrade, cancelSponsorship, retired tier retained | Apply requested effective change with current billing semantics; cancellation does not prove refund or immediate entitlement end. | Read resulting tier/state and billing effective date; preserve history of previous commitments. |
| privacy / email preferences | PUBLIC, PRIVATE where current schema supports, receive email updates boolean | Make public identity and update consent deliberate personal choices; private sponsorship does not mean beneficiary sees no information. | Read actual sponsorship preference fields and public appearance; never publish identity merely to test visibility. |
| connected platform | Patreon linkage or documented connected sponsorability preference | Connect only an explicitly selected owned account and inspect permission scope; linkage does not create a paid sponsorship. | Read linkage/preference state and retain external-provider limitations; do not claim payment from a connected badge. |

### Pitfalls

- Current billing/provider terms are changeable. Read the actual checkout/account flow before any authorized commitment and keep sensitive financial data out of public issues.

### Official sources

- [Official sources 1](https://docs.github.com/en/graphql/reference/sponsors)
- [Official sources 2](https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/about-sponsorships-fees-and-taxes)
- [Official sources 3](https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/managing-your-sponsorship)

## Sponsor history, exports and referral metadata

Group ID sponsors-reporting-and-campaigns.

Capabilities sponsors-analytics.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| sponsor filters / activity window | active or retired tiers, date range, new/change/cancellation activity | Separate active sponsors, past sponsors, payments and payouts; distinguish cumulative commitment from settled receipts. | Read account/timezone/date/currency and reconcile paginated source rows to displayed totals. |
| export format / date / delivery | CSV, JSON, supported date window and delivery destination | Export only requested scope to intended private destination; initiating emailed export is an external delivery action requiring authorization. | Verify requested export fields/window, actual received file and row totals; record pending versus completed export. |
| referral metadata syntax | metadata_KEY=value; alphanumeric/dash/underscore; at most ten pairs | Use non-sensitive short campaign codes, never email addresses or secret identifiers in public URLs. Whitespace/invalid characters can produce 404. | Check resulting URL and export metadata key after permitted transaction; keys truncate at 25 chars and values at 100 per current guide. |
| lifetime / revenue interpretation | authorized lifetime value, currency, transaction/payment status | Use financial definitions explicitly; sponsorship totals and estimated next payout are not recognized revenue or a tax report. | Reconcile refunds/fees/date window with account dashboard and payout receipts when applicable. |

### Pitfalls

- Export access does not authorize publishing sponsor identities or payment details in a public Wiki/Project.

### Official sources

- [Official sources 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/viewing-your-sponsors-and-sponsorships)
- [Official sources 2](https://docs.github.com/en/graphql/reference/sponsors)

## Recipient scope, sender identity and publish boundary

Group ID sponsors-newsletters-and-delivery.

Capabilities sponsors-newsletters.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| recipients | opted-in sponsors, all eligible tiers, selected tier IDs | Match requested audience and current opt-in; do not bypass consent with copied sponsor email lists. | Read selected tier recipients and current eligibility before publish; distinguish tier names from stable IDs. |
| subject / body / sender | draft subject/message, personal primary email or noreply based on privacy, organization noreply | Prepare concrete reviewed content and working links; note personal sender exposure when email privacy is off. | Preview sender/subject/body/links and target account in dashboard without sending test mail. |
| draft versus Publish | unsent draft, published email update | Publish sends mail and needs an explicit messaging instruction; repository release/setup authority alone is insufficient. | Read publication/sent history and exact target scope; absence of send evidence must remain draft/unknown. |
| ambiguous delivery recovery | inspect newsletter history first, avoid duplicate Publish | A timeout can occur after sending; do not retry the broadcast before reconciling history and timestamps. | Capture update ID, publication time and recipient tier scope; report uncertainty rather than claim all recipients received/read mail. |

### Pitfalls

- Published/sent means provider acceptance/history, not proof every recipient received or read the message.

### Official sources

- [Official sources 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/contacting-your-sponsors)

## Banking boundaries, estimated payouts and fundraising targets

Group ID sponsors-payouts-and-goals.

Capabilities sponsors-payouts, sponsors-goals.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| payout account / status | past payout, estimated next payout, holds/provider state | Read correct beneficiary/provider and distinguish estimated, pending and paid; never equate incoming sponsorship with completed payout. | Match amount/date/currency and account history to actual receipt where available. |
| bank/fiscal-host management | supported Stripe Connect flow, fiscal-host support route | Owner handles bank/legal verification; fiscal-host accounts cannot directly edit payout information through the same control. Never paste bank/tax data into repository logs. | Inspect provider/account gate and resulting secure status only; record support handoff as unresolved. |
| receipt export | PDF payout receipts for supported Stripe Connect accounts | Export only required receipt to the authorized private destination; respect provider-specific availability. | Open actual receipt and match account/payout amount/date; dashboard display alone is not exported file evidence. |
| goal type / target / description | Number of monthly sponsors, Sponsorships a month, one active goal | Select an owner-approved measurable target and explain funded work accurately; avoid implying contribution guarantees. | Read live goal type/target/text and public progress; only one simultaneous goal is supported in current guide. |
| goal edit / remove / share | update target/text, remove goal, copy/embed link | Preserve rationale for target changes and publish/share externally only when requested; progress is not recognized revenue. | Re-read public goal after update/removal and inspect embed destination; do not send promotion as setup. |

### Pitfalls

- Payout management is provider/account work, not repository administration. Do not claim settled revenue, tax treatment or completed banking verification from GraphQL metadata.

### Official sources

- [Official sources 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-payouts-from-github-sponsors)
- [Official sources 2](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-goal)

## Workflow triggers and typed inputs

Group ID workflow-events.

Capabilities actions-workflows.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| on / types | push, pull_request, pull_request_target, merge_group, schedule, workflow_dispatch, repository_dispatch, workflow_run, workflow_call, release; event-specific activity types | Choose the event whose code/ref and trust model match the job. Add merge_group when required checks serve a merge queue. | Exercise intended event; record event, actor, head_sha and workflow revision. |
| branches / tags / paths | positive/negative glob lists; branches-ignore/tags-ignore/paths-ignore alternatives | Protect required checks against path-filter skips; order negative patterns deliberately; branch and path filters combine. | Test included/excluded branch and file combinations; inspect check state. |
| schedule | POSIX cron; optional on.schedule[].timezone IANA name; UTC default; default-branch workflow; minimum 5-minute interval | Set timezone explicitly when local clock time matters. In DST spring-forward missing hours, execution advances to the next valid time. Use for tolerable delays with manual recovery; scheduling is not a precise timer. | Read cron/timezone from default-branch workflow; compare intended local time, DST transition behavior, scheduled event and actual start. Correct timezone/cron before rerunning missed work with duplicate protection. |
| workflow_dispatch.inputs | boolean, choice, environment, number, string; required/default/options | Validate enum and deployment target; environment input selects a value but does not gate a job without environment. | Run default and explicit input values; reject invalid target in job. |
| workflow_run | requested, in_progress, completed; workflows and branches | Treat upstream code/artifacts as untrusted; privileged follow-up must verify origin and SHA. | Read originating run ID, repository, event, conclusion, SHA and artifact provenance. |
| GITHUB_TOKEN event recursion | Most token-generated events do not launch another workflow; dispatch exceptions exist | Use explicit dispatch for intended chaining, with bounded recursion; do not broaden credentials just to trigger CI. | Match downstream run to dispatch; confirm no duplicate loop. |

### Project applicability

Existing validation CI needs PR and default-branch coverage. Event expansion needs a concrete repository operation.

### History and human interaction

Keep trigger edits in reviewed commits; retain event payload metadata without secrets and explain maintainer-triggered runs.

### Recovery

Inspect event/ref/filters first; dispatch or rerun the exact intended revision only after correcting cause.

### Pitfalls

- A required workflow skipped by filters can leave a required check pending.
- pull_request_target operates in privileged base context; never checkout and execute untrusted PR code there.
- Schedule delays and dropped scheduling events require observability.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [Official sources 2](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Official sources 3](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)
- [Official sources 4](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onschedule)

## Jobs, matrices, conditions and run history

Group ID workflow-execution.

Capabilities actions-workflows, actions-runs, actions-job-logs.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| needs / if | DAG dependencies; success(), failure(), cancelled(), always(); expressions | Use explicit terminal handling. Reserve always() for bounded cleanup; avoid making cancellation ineffective. | Inspect skipped and failed upstream cases plus cancellation. |
| strategy | matrix axes/include/exclude, fail-fast, max-parallel | Test supported platforms; fail-fast false retains all diagnostics at higher cost. | Inspect complete matrix job set and all conclusions. |
| step execution | run/uses, id, with, env, shell, working-directory, outputs, defaults | Pass untrusted strings through environment or typed inputs rather than shell interpolation. | Read exact workflow SHA, command results and produced outputs. |
| timeouts / tolerated failures | job and step timeout-minutes; continue-on-error; retry in command/action | Bound resource use; do not mark safety or release validation optional. | Force representative failure; ensure required job fails and cleanup completes. |
| services / containers | image, credentials, env, volumes, ports, options; supported runner OS | Use when integration tests require services; pin trusted images and isolate credentials. | Health-check service and inspect exact image digest. |
| attempt operations | rerun all, failed jobs, one job, debug logging, cancel/force-cancel; delete logs/run | Rerun after diagnosis. Capture current attempt; debug logs increase disclosure risk. | Record run ID, attempt, job IDs, SHA, conclusion and redacted log URL. |

### Project applicability

Keep the existing small validation workflow unless real platform differences justify a matrix.

### History and human interaction

Preserve previous attempts and reviewer explanation; canceled or deleted logs are not proof of an earlier success.

### Recovery

Read the current attempt before retrying; cancel normally first; force-cancel only after identifying stuck run and external side effects.

### Pitfalls

- A maintainer investigation of discussion #206259 attributed apparent queue blocking to other group jobs and always() preventing cancellation; initial bug claims were incomplete.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Official sources 2](https://docs.github.com/en/rest/actions/workflow-runs)
- [Official sources 3](https://docs.github.com/en/rest/actions/workflow-jobs)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/206259)

## Actions availability, allowed code and token defaults

Group ID actions-policy.

Capabilities actions-permissions, actions-policies, actions-fork-retention.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Actions enabled scope | disabled, all eligible repositories, selected repositories; inherited org/enterprise constraints | Read inheritance before changing repository settings. | Read all controlling scopes and repository eligibility. |
| allowed actions/reusable workflows | all, local-only, selected; GitHub-owned, verified Marketplace, explicit patterns; SHA-pinning policy where supported | Pin reviewed actions; allow only required external automation. | Read selected-action patterns and inspect each uses reference. |
| default_workflow_permissions | read or write; per-workflow/per-job permission map | Keep repository default read; grant needed write permissions only in responsible job. | Inspect setup log effective GITHUB_TOKEN permissions. |
| token permission map | actions, artifact-metadata, attestations, checks, contents, deployments, discussions, id-token, issues, models, packages, pages, pull-requests, security-events, statuses; supported read/write/none values | Once any permission is specified, unspecified permissions become none; metadata/scopes and availability differ. | Compare permissions to each operation schema and actual run grants. |
| PR creation / approval by Actions | allow or deny workflow PR creation/approval | Creation may help automation; automated approval is not independent review and must not satisfy a human governance intent. | Read can_approve_pull_request_reviews and inspect actor of resulting review. |
| fork policy | first-time/first-time-with-new-account/all external contributor approval; private-fork run/read-token/write-token/secrets options | Run contributions without secrets/write token; approval authorizes code execution and consumes resources. | Read fork policy plus run approval actor and effective token. |
| policy objects and retention | schema-defined action policy rules; artifact/log days bounded by parent policy | Inspect current rule schema and inherited maximums; retain enough release evidence without storing sensitive logs. | Read policy IDs/rules and expiry dates on actual run/artifact. |

### Project applicability

Repository rules require read-only CI. Do not enable write or fork secrets merely for fuller coverage.

### History and human interaction

Record who approved contributed code, which SHA was inspected and whether a later update needs review again.

### Recovery

Revert an allowlist through reviewed policy change; preserve run evidence before lowering retention or deleting logs.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/actions/permissions)
- [Official sources 2](https://docs.github.com/en/rest/actions/policies)
- [Official sources 3](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)

## Reusable workflows, actions and templates

Group ID reusable-contract.

Capabilities actions-reusable.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| sharing and reference | same-repo path; owner/repo workflow@SHA/tag/branch; private/internal sharing | Prefer exact reviewed SHA; access/allowed-actions policies must permit every nested workflow. | Read referenced_workflows SHAs and effective access policy. |
| workflow_call contract | boolean/number/string inputs, required/default; explicit secrets; outputs mapped job to workflow | Treat inputs/outputs as an API; avoid stringly typed booleans. | Run caller with omitted/default/explicit values and check outputs. |
| secret forwarding | named secrets or inherit for supported org/enterprise relationship; forwarding at every nested hop | Forward only required names; inheritance is wider. Current docs require passing environment secrets as well. | Fail safely when required secret is empty without printing it. |
| environment scope | environment on called job; same-name environment secret wins | Caller cannot put environment on a reusable-workflow call job. Pass environment identifier as input and bind it inside called workflow. | Observe called job gate and selected environment; verify secret presence only. |
| env and outputs | caller env is not general callee env; job/workflow outputs; reusable matrix output semantics | Pass configuration explicitly; use artifacts for files. | Assert outputs on representative matrix and nested caller. |
| nesting / permissions / concurrency | supported host nesting limit; accessible chain; permissions can only remain or decrease; caller/callee group IDs | Avoid same concurrency key accidentally canceling caller; inspect current host limits rather than hard-code historical limits. | Execute complete chain and inspect grants/group. |
| action forms and templates | composite steps, JavaScript runtime, Docker action; organization workflow-templates metadata | Use a template for copied starting files; reusable workflow for centrally maintained behavior. | Check action.yml inputs/runtime and actual consumer run. |

### Project applicability

Use only if repeated workflows merit a shared contract; small single-repo CI does not need a new abstraction.

### History and human interaction

Version contract changes, review all callers and record actual called SHA rather than mutable tag only.

### Recovery

Pin consumer to prior known SHA; restore compatible input/output contract and test caller before broader rollout.

### Pitfalls

- Issue #4453 reports empty environment secrets without forwarding; current official documentation explicitly requires passing or inherit. required:true checks passing, not non-empty value.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
- [Official sources 2](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations)
- [Official sources 3](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax)

### Community reports

- [Community reports 1](https://github.com/actions/runner/issues/4453)

## Variables, credentials and precedence

Group ID configuration-secrets.

Capabilities actions-variables, actions-secrets, security-dependabot-secrets.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| scope / selected repositories | organization all/private/selected; repository; environment; Actions versus Dependabot secret stores | Place credentials in narrowest necessary scope; variables are public-to-readers configuration. | Read names/metadata and selected repository IDs. |
| same-name precedence | environment over repository over organization; runtime availability/context restrictions | Avoid collisions; check when the job evaluates variables versus when environment values are available. | Inspect effective non-sensitive variable and secret-presence check in bound job. |
| write protocol | scope public key plus encrypted_value; gh secret via stdin/secure file | Never put secret in arguments, source or issue; encrypted API field is not a retrieval path. | Read updated_at/name; exercise minimal authorized operation. |
| fork / Dependabot / reusable contexts | secrets withheld for untrusted fork runs; Dependabot uses its dedicated store; explicit reusable forwarding | Do not duplicate broad credentials to fix a context error. | Read event actor and correct credential store; negative test unauthorized use. |
| rotation / expiry / redaction | provider revoke/reissue, key owner/expiry metadata outside secret value; add-mask for derived values | Rotate at provider; log masking is best effort, not access control. | Confirm old credential rejection and new credential operation without outputting either. |

### Project applicability

Validation should need no repository secret. Dependabot private registries need separate credentials only if present.

### History and human interaction

Record credential purpose, owner, consumer and rotation date; never plaintext values in historical evidence.

### Recovery

Revoke exposed credential first; replace narrow secret and rerun safely; remove/redact logs separately.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
- [Official sources 2](https://docs.github.com/en/actions/reference/workflows-and-actions/variables)
- [Official sources 3](https://docs.github.com/en/rest/actions/secrets)
- [Official sources 4](https://docs.github.com/en/rest/dependabot/secrets)

## Concurrency and queue policy

Group ID concurrency-queues.

Capabilities actions-concurrency.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| group | workflow/job scope; expression; repository-wide case-insensitive group name | Include workflow/ref for isolated CI; use environment-specific shared key for deployment serialization. | Read evaluated group and all related pending/running jobs. |
| queue | single default; max permits up to 100 pending | Use single for latest-state jobs; max when every item matters and host supports it. | Queue a bounded test and inspect pending replacements/overflow. |
| cancel-in-progress | false/default; true; allowed expression | Cancel stale CI; avoid interrupting releases or migrations. queue:max plus true is invalid. | Read old run conclusion and ensure side effects stopped. |
| ordering | FIFO by entering concurrency wait, not original dispatch time; no universal dispatch ordering guarantee | Do not use queue as a transactional ledger; record intended sequence separately if needed. | Compare queue-entry and execution history with expected deployment revisions. |

### Project applicability

CI can cancel outdated branch checks; release and Wiki publication must preserve sequence and existing content.

### History and human interaction

Attach cancellation reason to run history and preserve prior attempt IDs; an operator retry does not establish queue order.

### Recovery

Inspect every workflow sharing the key and always() conditions before calling a queue bug; check runner availability and status incident history.

### Pitfalls

- 2021–2025 complaints about a single pending slot do not describe current queue:max behavior; maintainer announced shipping April 17, 2026.
- The control-concurrency page contains broad examples implying unconditional cancellation; use its explicit queue/cancel policy definitions.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)
- [Official sources 2](https://docs.github.com/en/rest/actions/concurrency-groups)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/5435)
- [Community reports 2](https://github.com/orgs/community/discussions/12835)
- [Community reports 3](https://github.com/orgs/community/discussions/206259)

## Workflow artifact contents and lifecycle

Group ID artifacts.

Capabilities actions-artifacts.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| upload contract | name, path/globs/exclusions, if-no-files-found warn/error/ignore, retention-days | Require expected files; choose unique artifact name per matrix job. | Download exact artifact ID and inspect archive manifest. |
| hidden and file metadata | include-hidden-files false by default; ZIP changes permission fidelity; tar when metadata matters | Include required dotfiles explicitly after excluding credentials; tar executable-sensitive bundles. | Check .codex-plugin files and executable bits in extracted release bundle. |
| compression / overwrite | compression-level supported range; overwrite false default; upload version semantics | Favor low compression for precompressed assets; overwrite deletes old artifact identity. | Record artifact ID, digest, size and expiration after upload. |
| download selection | ID/name/pattern, merge-multiple, path; repository/run/token for cross-run access | Bind release input to trusted run and SHA, never latest name alone. | Verify source run, digest and expected file allowlist. |
| host and action compatibility | supported major/runtime/backend; GHES support differs from GitHub.com | Read current action README and installed runner minimum; do not blindly copy a dot-com major. | Run on target host and inspect resulting artifact/download. |

### Project applicability

Inspect installable plugin archive before release; preservation of hidden plugin metadata is essential.

### History and human interaction

Keep archive manifest, digest and trusted producing SHA with release evidence; retention expiry must not erase sole evidence.

### Recovery

Rebuild from same reviewed SHA, compare contents and digest, issue new version for published immutable mistakes.

### Pitfalls

- Hidden-file default change broke explicit dotfile upload use cases; plugin archives can silently lose .codex-plugin if blindly uploaded.
- Artifact download is untrusted data until origin and contents are verified.

### Official sources

- [Official sources 1](https://github.com/actions/upload-artifact)
- [Official sources 2](https://github.com/actions/download-artifact)
- [Official sources 3](https://docs.github.com/en/rest/actions/artifacts)

### Community reports

- [Community reports 1](https://github.com/actions/upload-artifact/issues/602)

## Cache keys, access and budgets

Group ID cache.

Capabilities actions-caches.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| lookup identity | path, key, restore-keys, OS/architecture/lockfile/toolchain salts; cache-version/ref scope | Do not mix incompatible binaries; restore prefixes trade hit rate for stale input risk. | Inspect exact key/ref/version and restored build behavior. |
| restore controls | lookup-only, fail-on-cache-miss, enableCrossOsArchive, supported restore/save actions | Fail on miss only when cache existence is an actual requirement; cache is ordinarily optional. | Test empty cache and prefix fallback; verify reproducible cold build. |
| write/eviction | immutable key entry; new key for changed content; retention/storage policies | Avoid secrets and release-only evidence; monitor eviction and thrashing. | Read usage, last_accessed_at, size and configured inherited limits. |
| trust boundary | fork/base/default-branch read visibility and write scope; workflow cache access restrictions | Treat cache as untrusted executable input; separate privileged/untrusted scopes. | Verify trust-specific keys/access plus authorized clean-cache build. |

### Project applicability

Small Python stdlib validation does not justify a cache unless measured runtime benefit exists.

### History and human interaction

Keep cache purge reason and old keys in issue/run evidence, never cache credential contents.

### Recovery

Delete only identified poisoned/stale keys; rerun cold, then change salt to prevent accidental reuse.

### Official sources

- [Official sources 1](https://github.com/actions/cache)
- [Official sources 2](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)
- [Official sources 3](https://docs.github.com/en/rest/actions/cache)

## Hosted, self-hosted and larger runner configuration

Group ID runners.

Capabilities actions-self-hosted-runners, actions-runner-groups, actions-hosted-runners.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| runs-on selection | hosted image/architecture/size; self-hosted label intersection; group plus labels | Use smallest suitable hosted runner; image labels can roll, so record actual image version. | Inspect job runner_name/group/labels/OS and setup image version. |
| self-hosted registration | repository/org scope; short-lived registration/removal tokens; JIT config; ephemeral flag | Use disposable isolated machines for untrusted work; registration is not host hardening. | Run benign job, confirm isolation and disposal/cleanup. |
| group access | all/selected repositories; public repo option; selected workflows/revisions; inherited org/enterprise policy | Restrict trusted runner group to known workflows and repos. | Read group repository IDs and allowed workflow refs; test excluded workflow refusal. |
| host lifecycle | runner version/update policy, online/busy, labels, proxy, workspace cleanup; ARC scale sets | Patch runner and images; bound queue and jobs; autoscaling requires separate infrastructure. | Check runner health and clean job-to-job environment. |
| larger runner settings | machine type/image/size/max parallelism, runner group, static IP/private networking where eligible | Enable only for a demonstrated workload and approved billing/network access. | Read saved runner config, network reachability and billed usage. |

### Project applicability

No current need for paid or self-hosted capacity in this plugin repository.

### History and human interaction

Capture operator registration/removal and host ownership, preserving relevant job logs before disposal.

### Recovery

Quarantine suspect runner, revoke credentials, replace image; never assume workspace deletion undoes compromise.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)
- [Official sources 2](https://docs.github.com/en/actions/reference/runners/self-hosted-runners)
- [Official sources 3](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access)
- [Official sources 4](https://docs.github.com/en/rest/actions/hosted-runners)

## OIDC claims and cloud trust

Group ID oidc.

Capabilities actions-oidc.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| issuance permission | id-token:write only on authenticating job | Token issuance grants no cloud resource permission by itself. | Inspect effective job permission and provider exchange result. |
| trust conditions | issuer, audience, repository identity, ref/environment, job_workflow_ref; provider-supported claims | Scope provider trust to exact owner/repo/workflow/target; avoid broad wildcard repo trust. | Inspect redacted claims and denied wrong-ref/target exchange. |
| subject template | repo use_default; org/repo include_claim_keys; supported custom properties | Stage cloud trust migration before changing sub format; org template requires correct repo adoption. | Read template and compare actual non-sensitive sub/claim values. |
| reusable workflow identity | caller repository context versus called job_workflow_ref; accessible trust claims | Require reviewed reusable workflow identity where provider supports it. | Inspect caller/callee SHAs and successful narrow provider action. |
| environment interaction | environment-based subject replaces ref-based shape; branch rules are separate gate | Configure both cloud subject and GitHub deployment branch policy. | Negative-test disallowed ref and unapproved environment job. |

### Project applicability

No cloud deploy target currently exists; do not create one to exercise OIDC.

### History and human interaction

Record cloud role/trust policy revision and migration review, never JWT contents.

### Recovery

Restore previous subject template or compatible provider trust; revoke exposed long-lived credentials separately.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/reference/security/oidc)
- [Official sources 2](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-with-reusable-workflows)
- [Official sources 3](https://docs.github.com/en/rest/actions/oidc)

## Environment protection and approvals

Group ID environment-approvals.

Capabilities deploy-environments, deploy-approval.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| required reviewers | eligible users/teams; one eligible approval suffices; prevent self-review; plan restrictions | Do not describe reviewer list as unanimous approval. Independent approval requires another eligible human. | Read reviewer IDs, prevent_self_review and actual approval actor. |
| wait timer | documented minute range; non-billable waiting; product/visibility gates | Use only for purposeful rollout delay; it does not inspect health. | Read wait duration and timestamps before job starts. |
| deployment branch policy | all; protected branches; selected branch/tag patterns | Gate deployment ref separately from repository branch protection; test tags explicitly. | Read protected_branches/custom_branch_policies and every branch/tag rule. |
| administrator bypass | allow/deny supported protection bypass setting | Keep bypass decision explicit and auditable; automation must not bypass its own gate. | Read saved option plus bypass actor/comment when used. |
| custom protection rules | installed GitHub App rules; enabled rules bounded by current platform limit | Verify app permission, external approval/health decision and failure handling. | Read rule integration IDs and actual requested/approved/rejected record. |
| environment configuration | name, URL, secrets, variables; create explicitly before referencing | A misspelled environment may be created without intended safeguards; exact name matters. | Read environment ID and settings before allowing workflow run. |
| approval operations | pending deployments approve/reject with comment; workflow gate differs from PR approval | Read artifact/SHA and change context before approval; never impersonate reviewer or weaken policy. | Record deployment IDs, reviewer, decision, comment and run continuation. |

### Project applicability

A single maintainer cannot manufacture independent peer approval. No deployable service exists; preserve zero required PR approvals as repository policy.

### History and human interaction

PR review, fork workflow execution approval and environment approval are distinct histories; record each real actor/decision.

### Recovery

Reject unsafe pending deployment, correct exact environment/ref and rerun; do not remove protection to unblock automation.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
- [Official sources 2](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)
- [Official sources 3](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments)
- [Official sources 4](https://docs.github.com/en/rest/deployments/environments)

## Deployment records, statuses and rollback

Group ID deployment-records.

Capabilities deploy-records.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| deployment request | ref, task, payload, environment, description, auto_merge, required_contexts, transient_environment, production_environment | Bind immutable SHA and required checks; deployment API is a record/request, not deployment engine. | Read record ID, sha, environment and exact request parameters. |
| status transitions | queued, pending, in_progress, success, failure, error, inactive; log_url, environment_url, auto_inactive | Report actual engine state and measured health. | Read ordered statuses and independently test application version/health. |
| cleanup/rollback | mark inactive; delete eligible deployment; external rollback to prior immutable artifact | Preserve operational trail; deactivate previews when removed. | Compare served SHA/digest before/after and status history. |

### Project applicability

Only create deployment records for an actual deployment; source/plugin release alone is not an application deployment.

### History and human interaction

Store approver, release artifact digest and rollback reason in deployment/linked issue history.

### Recovery

Deploy prior verified artifact with a new explicit rollback record; a green API status does not restore service.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/deployments/deployments)
- [Official sources 2](https://docs.github.com/en/rest/deployments/statuses)

## Security products, inheritance and enforcement

Group ID security-enablement.

Capabilities security-enablement, security-configurations, security-overview.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| product switches | dependency graph/submission; Dependabot alerts/security updates; Code Security; Secret Protection; private vulnerability reporting | Evaluate eligibility and actual need separately; security policy prose is not scanning enablement. | Read effective repository security_and_analysis and product-specific status. |
| configuration association | org/enterprise configuration ID; selected/all/new-repository defaults; enforcement | Preserve inherited policy; inspect asynchronous association failures and product entitlements. | Read configuration, repository association/application state and effective setting. |
| enforced controls | enabled/disabled/not-set where schema supports; enforcement mode; delegated dismissal/bypass | Validate current schema per field rather than applying one enum blindly. | Read exact serialized config plus repository lock state. |
| coverage/risk | repository filters, missing coverage, exclusions, alert severity/age; eligible plan | Report unknown/unavailable separately from clean or disabled. | Reconcile visible repo counts and excluded/failed scans with ledger. |

### Project applicability

Public plugin can use eligible free controls; do not activate a paid organizational product or change license policy without authorization.

### History and human interaction

Retain setting changes, application status, responsible security owner and policy exception explanation.

### Recovery

Correct failed association or incompatible config; preserve evidence before detaching and never silently relax enforcement.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/code-security/configurations)
- [Official sources 2](https://docs.github.com/en/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration)
- [Official sources 3](https://docs.github.com/en/code-security/getting-started/github-security-features)

## CodeQL, SARIF, Autofix and code quality

Group ID code-scanning.

Capabilities security-codeql, security-code-alerts, security-ai-autofix, security-code-quality.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| setup mode | default or advanced; language selection; query suite; supported runner | Choose default for supported uncomplicated builds; advanced for custom build/query needs. | Verify actual language database and completed analysis at intended SHA. |
| advanced options | matrix languages, build-mode none/autobuild/manual, paths/paths-ignore, queries/packs/model packs, config-file, category, schedule | Match build mode to language; path excludes can create blind spots. Keep category stable per analysis variant. | Read workflow/config at analyzed SHA and analysis category/language coverage. |
| blocking controls | security/quality severities, rule/tool selection, ruleset thresholds where supported | Pick actionable severity gates and require actual scan completion; empty upload is not clean coverage. | Inspect PR check result and corresponding alerts/instances. |
| SARIF upload | tool/category, commit_sha, ref, analysis_key, compressed payload; processing status | Validate SARIF and bind result to exact commit/ref; poll until processed. | Read sarif processing result and analysis commit/tool/category. |
| alert lifecycle | open/fixed/dismissed; allowed dismissal reason/comment; delegated review | Dismiss with evidence; reopen when premise fails. Deleting analysis is not remediation. | Read state, dismissing actor/time/reason and latest instance. |
| Autofix / AI Scan | available product switch; supported alert request; proposed patch/commit | Review generated diff and test before committing; do not equate generated fix with validated fix. | Rerun affected tests/scanner and inspect resolved finding. |
| variant databases / code quality | CodeQL database downloads/variant target scope; quality setup/findings supported schema | Use only for concrete cross-repository query/quality need; permissions differ from code scanning. | Read variant completion per repo and quality findings at target revision. |

### Project applicability

Analyze actual Python/scripts and workflow languages supported by selected tool; do not claim Markdown guidance has executable-language CodeQL coverage.

### History and human interaction

Preserve alert number, instance, reviewer rationale and scan SHA; approvals for dismissal remain separate from fix review.

### Recovery

Fix build/query/upload cause; rescan same intended revision; reopen unsupported dismissals and revert unsafe Autofix commit.

### Official sources

- [Official sources 1](https://docs.github.com/en/code-security/reference/code-scanning/workflow-configuration-options)
- [Official sources 2](https://docs.github.com/en/rest/code-scanning/code-scanning)
- [Official sources 3](https://docs.github.com/en/rest/code-quality/code-quality)
- [Official sources 4](https://docs.github.com/en/code-security/concepts/security-at-scale/delegated-alert-dismissal)

## Dependency graph, review, submission and SBOM

Group ID dependency-inventory.

Capabilities security-dependency-graph, security-sbom, security-global-advisories.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| inventory sources | supported manifests/lockfiles, automatic or explicit dependency submission; detector/job identity | Resolve build dependencies where manifests are insufficient; do not fabricate runtime dependencies. | Match graph snapshot detector and SHA to lockfile/build resolution. |
| dependency-review policy | base/head diff; fail-on-severity, allowed/denied licenses, scope, allowlisted advisories/packages; supported action options | Use narrow documented exceptions with owner/expiry; license policy requires owner decision. | Inspect newly introduced vulnerable/license entries and check failure. |
| SBOM | SPDX export; async report UUID where supported; snapshot date and included scopes | Treat as inventory snapshot bounded by graph completeness. | Parse SPDX and compare package counts/versions to manifests and submission. |
| advisory matching | GHSA/CVE, ecosystem/name, affected/fixed range, withdrawn/reviewed status | Match precise version and ecosystem; absence of advisory is not safety proof. | Read advisory update time, withdrawn state and installed resolved version. |

### Project applicability

No new runtime dependency is authorized. Track action dependencies and required tooling; owner has not selected project license.

### History and human interaction

Keep dated SBOM/diff, dependency exception reviewer and changed lockfiles with PR evidence.

### Recovery

Submit corrected snapshot and regenerate SBOM; fix affected version or record bounded reviewed exception.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/dependency-graph/dependency-review)
- [Official sources 2](https://docs.github.com/en/rest/dependency-graph/dependency-submission)
- [Official sources 3](https://docs.github.com/en/rest/dependency-graph/sboms)
- [Official sources 4](https://docs.github.com/en/rest/security-advisories/global-advisories)
- [Official sources 5](https://github.com/actions/dependency-review-action)

## Dependabot schedules, update strategy and runtime

Group ID dependabot.

Capabilities security-dependabot-alerts, security-dependabot-version, security-dependabot-runtime.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| update discovery | version:2; package-ecosystem; directory/directories; exclude-paths where supported | Configure every existing ecosystem, avoiding overlapping directory entries. | Inspect default-branch config and real job detected manifests. |
| schedule | daily/weekly/monthly/quarterly/semiannually/yearly/cron where current schema supports; day/time/timezone/cronjob | Choose workload-appropriate cadence; timezone explicit when needed. | Read actual scheduled job timestamps. |
| selection/strategy | allow; ignore dependency/version/update-types; versioning-strategy; target-branch; vendor; ecosystem-specific options | Review exclusions carefully: ignored vulnerable versions can block remediation. | Compare generated diff and job skipped-dependency reason. |
| groups | patterns/exclude-patterns, dependency-type, update-types, applies-to version-updates/security-updates; multi-ecosystem-groups | Use separate security/version intent; grouping failures need real job inspection. | Inspect generated PR members and applicable group. |
| cooldown | default-days; semver-major/minor/patch-days; include/exclude; default 3 days | Current 2026 default delays version updates even with no cooldown block; security updates are exempt. | Compare release publication, cooldown and PR creation time. |
| PR management | open-pull-requests-limit, labels, assignees, milestone, commit-message, branch separator, rebase-strategy; supported options per ecosystem | Preserve existing repository taxonomy; keep limits low enough for maintainable review. | Inspect generated PR metadata and rebase behavior. |
| registry/code execution | registries credential type/URL; selected registries; insecure-external-code-execution allow/deny | Allow external execution only for necessary reviewed ecosystem resolution; narrow registry credentials. | Read redacted registry resolution logs and execution settings. |
| runtime / repository access | standard/labeled runner, labels/group; org private-dependency repository allowlist/default access | Use labeled runner only on eligible repo; do not expand private repo access to fix typo. | Read effective runner settings and successful dependency resolution. |
| alerts/security PRs | severity/ecosystem/package/scope/state/EPSS filters; auto-triage rules and delegated dismissal if eligible | Prioritize real risk; dismissal requires reason and does not patch. | Read alert after merged fix and confirm installed version/checks. |

### Project applicability

Existing policy explicitly wants GitHub Actions updates. Add other ecosystems only if manifests exist.

### History and human interaction

Respond to supported @dependabot commands after reading bot status; human review remains required under repo rules, and bot actor restrictions affect secrets.

### Recovery

Read update log before rebase/recreate; remove obsolete ignore, fix registry access narrowly, rerun supported job and verify generated PR.

### Pitfalls

- Maintainer announcement July 14, 2026 confirms 3-day default version cooldown; older explanations assuming immediate version PRs are stale.
- Issue #16319 reports grouping failure in a particular non-root npm case; it is a reproduction lead, not proof all grouping is broken.

### Official sources

- [Official sources 1](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference)
- [Official sources 2](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/optimizing-pr-creation-version-updates)
- [Official sources 3](https://docs.github.com/en/rest/dependabot/alerts)
- [Official sources 4](https://docs.github.com/en/rest/dependabot/runner-settings)
- [Official sources 5](https://docs.github.com/en/rest/dependabot/repository-access)

### Community reports

- [Community reports 1](https://github.com/dependabot/dependabot-core/discussions/15582)
- [Community reports 2](https://github.com/dependabot/dependabot-core/issues/16319)

## Secret detection, push protection and exceptions

Group ID secret-scanning.

Capabilities security-secret-alerts, security-push-protection, security-custom-patterns.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| detection options | provider patterns, non-provider/generic/AI detection where eligible; validity checks; extended metadata | Enable supported useful detection; validity/metadata may contact provider and have product gates. | Read settings and scan history/coverage, not alert count alone. |
| push protection | repository protection versus personal protection; supported pattern participation | Do not mistake personal block for repository policy; repository scanning remains separate. | Read repository setting and safe documented test result. |
| custom patterns | name, secret regex, before/after context, additional match requirements; dry-run/publish; push protection | Use safe synthetic examples and negative corpus; dry-run before publishing noisy pattern. | Record pattern ID/version and positive/negative results. |
| bypass governance | test/false-positive/fix-later reasons where offered; delegated reviewers, expiry/review path | Never bypass a valid live credential; fix/revoke instead. Independent reviewer decision stays with reviewer. | Read request, actor, comment, expiry and resulting alert. |
| alert state | open/resolved; revoked, false_positive, used_in_tests, wont_fix or current schema reasons; location/history | Revoke with provider first; resolving UI alert does not revoke token or erase history. | Check provider revocation and read alert location/resolution metadata. |
| dismissal governance | direct or delegated dismissal; role eligibility; notification/review state | Confirm reviewer coverage before enforcing; preserve rationale even for test secrets. | Read request/outcome, reviewer and reopened state if rejected. |

### Project applicability

Useful for public repo; synthetic tests must not leak live values. Security setting read may itself contain secret values; redact outputs.

### History and human interaction

Retain private alert IDs, discovery/rotation timestamps and reviewed exception reasons; do not copy secret strings into public issues.

### Recovery

Revoke at provider, replace consumers and scan history; history rewriting is separate consequential work and does not invalidate copied credentials.

### Official sources

- [Official sources 1](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)
- [Official sources 2](https://docs.github.com/en/rest/secret-scanning/secret-scanning)
- [Official sources 3](https://docs.github.com/en/rest/secret-scanning/push-protection)
- [Official sources 4](https://docs.github.com/en/rest/secret-scanning/custom-patterns)
- [Official sources 5](https://docs.github.com/en/code-security/concepts/security-at-scale/delegated-alert-dismissal)

## Confidential reports, advisory publication and campaigns

Group ID security-coordination.

Capabilities security-advisories, security-campaigns.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| reporting policy | SECURITY.md supported versions/contact; private vulnerability reporting enabled/disabled | Provide confidential route and realistic response ownership. | Inspect rendered policy and actual reporting availability. |
| advisory content | draft/published/withdrawn, severity/CVSS/CWE, vulnerable ranges/patched versions, references, credit, CVE request | Keep report private until fix/disclosure agreement; verify affected ranges. | Read advisory state/collaborators and clean install of patched release. |
| collaboration | report triage, comments, invited collaborators, temporary private fix fork | Grant only necessary confidential access and retain reporter coordination. | Read actual collaborator identities and private fork/review history. |
| campaign setup | selected code alerts, repositories, managers/teams, contact, deadline; draft UI versus published API; optional generated issues | Use for multi-repository remediation requiring tracking; preserve private finding visibility. | Read published campaign scope/counts and corresponding resolved alerts. |
| publication / withdrawal | explicit publish/CVE disclosure; withdrawal constraints; notification effects | Publication is irreversible disclosure; prepare exact reviewed advisory/fix before authorized publish. | Read public GHSA/CVE and release timestamps; verify issue scope. |

### Project applicability

Confidential reporting is useful; campaigns require actual alert program and owner eligibility, not a placeholder.

### History and human interaction

Preserve reporter credits, embargo agreement, fix review and disclosure decision privately; public release notes must respect agreed timing.

### Recovery

Correct advisory affected ranges/notes and notify existing recipients; never claim withdrawal removes already disclosed information.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/security-advisories/repository-advisories)
- [Official sources 2](https://docs.github.com/en/rest/campaigns/campaigns)

## Drafts, generated notes, assets and immutability

Group ID release-lifecycle.

Capabilities releases-lifecycle, releases-assets, releases-immutable.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| release identity | tag_name, target_commitish for new tag, name, draft, prerelease, make_latest | Existing tag determines commit; target_commitish does not move it. Match plugin manifest version to v-tag. | Resolve tag object/commit, release ID and version file. |
| notes | body; generated notes; previous tag/configuration; categories/exclusions; discussion category where eligible | Review generated changelog; include install commands, validation evidence and limits. | Read rendered notes and linked issues/PRs against intended range. |
| asset upload | binary content type, filename/label; draft upload URL; per-asset ID/digest/size | Build deterministic installable archive, inspect hidden files and allowlist before attaching. | Download attached bytes and compare SHA-256/archive manifest. |
| immutability | repo/org policy; new release behavior; immutable flag | Create draft, attach every asset, then publish. Published assets/tag become locked; notes/title/latest/prerelease remain editable. | Read immutable flag, tag SHA, asset digest and release attestation. |
| publication/recovery | draft update versus publish; prerelease/stable; delete constraints; corrective next version | Do not publish from merely prepared source; irreversible distribution needs existing release authorization. | Read published_at, exact asset bytes, install from release and latest pointer. |

### Project applicability

Core delivery path: plugin version, v-tag, installation docs and validation evidence must agree. Immutability prevents patching published archive.

### History and human interaction

Record release preparer/reviewer/publisher, reviewed tag SHA and prior release comparison. Discussion and release notes carry human feedback/history.

### Recovery

For immutable wrong asset/tag, publish a new corrected version; editable notes cannot change locked bytes. Never force-move tag as an assumed recovery.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/releases/releases)
- [Official sources 2](https://docs.github.com/en/rest/releases/assets)
- [Official sources 3](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [Official sources 4](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases)

## Provenance, SBOM and linked artifact records

Group ID attestations.

Capabilities attestations-provenance, attestations-linked-artifacts.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| statement type | build provenance or SBOM attestation; artifact digest/name; supported registry publication | Attest exact distributed bytes; provenance says how/where built, not absence of bugs. | Verify subject digest and trusted repository/workflow identity. |
| workflow grants | id-token:write, attestations:write; contents/read and packages/write only when needed | Isolate attestation in trusted release job; eligibility varies with visibility/plan. | Inspect effective permissions and successful verify output. |
| verification constraints | trusted owner/repo/workflow, predicate type, signer identity, source ref/commit; offline/bundle modes where supported | Do not accept any valid GitHub signature; require intended producer. | Run gh attestation verify against downloaded exact asset and identity policy. |
| linked artifacts | storage metadata and artifact association using current endpoint schema | Distinguish storage record/link from uploaded file and signed attestation. | Read link identity, digest and referenced object existence. |

### Project applicability

Consider for installable release artifact when trusted workflow builds it; record unavailable eligibility instead of assuming.

### History and human interaction

Keep verifier command/policy/output and producing workflow SHA with release record; release attestation and custom build provenance are distinct.

### Recovery

Rebuild/re-attest correct bytes in trusted workflow; revoke trust in compromised producer and publish corrective version.

### Official sources

- [Official sources 1](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)
- [Official sources 2](https://docs.github.com/en/rest/repos/attestations)
- [Official sources 3](https://docs.github.com/en/rest/orgs/artifact-metadata)

## Registries, package ACL and trusted publishing

Group ID packages.

Capabilities packages-metadata, packages-registry, packages-access, packages-trusted-publishing.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| registry/form | OCI/GHCR, npm, NuGet, RubyGems granular; Maven/Gradle repository-scoped; host support | Choose only ecosystem actually distributed; REST metadata does not publish package bytes. | Install/pull exact version/digest from clean intended consumer. |
| authentication | GITHUB_TOKEN packages:read/write in workflow; supported classic PAT scopes for registry; registry-specific OIDC/trusted publishing | Prefer short-lived workflow credential; trusted-publishing support is registry-specific, not universal. | Verify exact registry trust configuration and authenticated clean install. |
| link and inheritance | repository link, inherited repository permissions, automatic inheritance org policy; explicit user/team ACL | Linked repo alone may not grant workflow access if ACL inheritance differs. | Read package settings/inheritance and intended principal access. |
| Actions access | selected repository access to granular package; separate Codespaces access | Grant only consumer/producer repos; token scope alone cannot override package ACL. | Test authorized workflow and excluded repo denial. |
| visibility | private/internal/public where supported; public transitions can be restricted/irreversible | Do not infer public package from public source repository. | Read package visibility and anonymous pull when intended. |
| versions/delete/restore | immutable consumer digest, tags, version metadata; package/version deletion; restoration eligibility/window | Do not delete versions still used; inspect downloads and restoration constraints first. | Read version ID and digest; restore and reinstall when authorized. |
| external trusted publisher | owner/repository/workflow/environment binding; OIDC permission and registry policy | For npm or other external registry, distinguish that registry from GitHub Packages. Verify registry official docs. | Perform registry-specific dry-run or publish only with release authorization; read resulting provenance. |

### Project applicability

GITHUB.md explicitly says no separate package artifact requirement. Plugin marketplace/source releases currently satisfy distribution; do not publish artificial package.

### History and human interaction

Retain package/version IDs, producer SHA, ACL reviewers and deprecation notices; preserve consumer compatibility.

### Recovery

Correct package ACL/link narrowly; rotate exposed tokens; publish corrected immutable version/digest instead of relying on mutable tags.

### Pitfalls

- Community reports show packages:write token permission alone did not fix missing package inheritance/Actions access; inspect both.
- Classic PAT restrictions and SSO can block registry auth despite scope. Do not respond by granting broader scopes blindly.

### Official sources

- [Official sources 1](https://docs.github.com/en/packages/learn-github-packages/about-permissions-for-github-packages)
- [Official sources 2](https://docs.github.com/en/packages/learn-github-packages/publishing-a-package)
- [Official sources 3](https://docs.github.com/en/packages/learn-github-packages/deleting-and-restoring-a-package)
- [Official sources 4](https://docs.npmjs.com/trusted-publishers/)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/32184)
- [Community reports 2](https://github.com/orgs/community/discussions/57809)

## Pages source, DNS, TLS and publication

Group ID pages.

Capabilities pages-settings, pages-builds.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| build_type / source | legacy branch path root/docs or workflow; branch; custom workflow upload/deploy | Use source matching actual site generator; branch commits using GITHUB_TOKEN do not trigger branch Pages build. | Read Pages configuration and actual successful build/deployment SHA. |
| workflow grants / target | contents:read, pages:write, id-token:write; github-pages environment and artifact | Scope deployment permissions to job and keep environment protections. | Read uploaded Pages artifact, deployment status and environment. |
| custom domain | CNAME, DNS A/AAAA/CNAME records, domain verification, protected domain ownership | Verify domain before linking and remove stale DNS when disabling. | Read DNS health, ownership record and served hostname. |
| HTTPS | certificate provisioning and https_enforced when available | Wait for valid certificate before enforcing; inspect mixed content. | Verify HTTPS chain/hostname and HTTP redirect. |
| visibility / path | project site base path, public/private enterprise entitlement; repository visibility differs | Do not publish private source content without intended audience decision. | Fetch as intended anonymous/authenticated user and inspect base-path assets. |
| build/history/recovery | branch build/request; workflow Pages deployment status/cancel; external health | A successful build does not prove correct public content. | Fetch expected marker/version, navigation/assets and custom-domain redirect. |

### Project applicability

No site requirement exists in GITHUB.md; keep Pages not-applicable until useful published site is requested.

### History and human interaction

Record domain owner authorization, workflow approval and deployed SHA; preserve previous successful deployment for rollback.

### Recovery

Redeploy prior verified site revision; correct source/base path/DNS, then recheck served bytes and TLS; deleting Pages alone leaves dangerous stale DNS.

### Official sources

- [Official sources 1](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Official sources 2](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Official sources 3](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages)
- [Official sources 4](https://docs.github.com/en/rest/pages/pages)

## Required check identity and review integration

Group ID checks-statuses.

Capabilities checks-runs, checks-suites, checks-commit-statuses.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| check run | name, head_sha, status/conclusion, started/completed timestamps, output/annotations, details_url; app identity | Stable unique names per required check; attach to exact tested SHA. | Read check name, app ID, head_sha and actual command evidence. |
| check suite | automatic creation preferences, rerequest, suite status | Suite success does not replace individual required checks; some writes are App-only. | Read suite and associated run conclusions. |
| commit status | context, state pending/success/failure/error, target_url, description | Keep context distinct from check-run names to avoid ambiguous requirement matching. | Read combined and individual statuses on intended SHA. |
| protection binding | required context/app, strict branch freshness, merge_group coverage; skipped/neutral semantics | Read rulesets and classic protection; require checks that actually test code. | Observe PR required check evaluation after latest push and merge-queue test commit. |

### Project applicability

Existing three validation commands remain authoritative. Peer approval count zero is deliberate single-maintainer policy.

### History and human interaction

Keep reviewer comments, check rerequest actor, force-push/stale-review history and final merge SHA; green unrelated SHA is insufficient.

### Recovery

Fix missing event/name/app permission and rerun actual required check; never spoof status or remove protection to merge.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/checks/runs)
- [Official sources 2](https://docs.github.com/en/rest/checks/suites)
- [Official sources 3](https://docs.github.com/en/rest/commits/statuses)
- [Official sources 4](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)

## Agentic workflows and constrained output

Group ID agentic-workflows.

Capabilities actions-agentic-workflows.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| definition / compilation | Markdown instructions plus frontmatter; generated workflow; gh aw compile | Review generated YAML after instruction change and keep compiled artifact synchronized. | Compile and compare source/generated diff; inspect actual workflow SHA. |
| engine / credentials | supported Copilot/Codex/Claude/Gemini engine; engine-specific secret and billing | Choose only an authorized available engine and narrow authentication. | Check engine initialization and approved usage budget without exposing keys. |
| guardrails | read-only runtime, firewall/network, tools, explicit safe-outputs and threat-detection gates | Allow only requested outputs; proposed issue/comment/PR is still external action requiring existing authorization. | Inspect generated downstream write job permissions and resulting object IDs. |
| review / triggers | schedule/dispatch/events; allowed actors; human-reviewed PR outputs | Treat repository text as untrusted prompt input; retain human review before merge/deploy. | Exercise controlled input and inspect output safety/review history. |

### Project applicability

Optional automation needs concrete recurring task, engine eligibility and authorized outputs; ordinary deterministic validation is sufficient now.

### History and human interaction

Retain prompts/config revisions, generated proposals, human acceptance/rejection and exact downstream writes; do not call model output an independent approval.

### Recovery

Disable affected workflow, stop pending writes and revoke compromised credentials; fix prompt/tool policy and inspect all emitted changes before reenable.

### Official sources

- [Official sources 1](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows)
- [Official sources 2](https://docs.github.com/en/actions/tutorials/develop-agentic-workflows-in-github-actions)
- [Official sources 3](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/about-github-agentic-workflows)

## Organization member privileges and effective access

Group ID organization-access-defaults.

Capabilities admin-organization-profile, admin-organization-policy-settings, admin-organization-members, admin-outside-collaborators.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Base repository permission | none \| read \| write \| admin; REST documented default read | Recommend none for private least-privilege organizations, then explicit teams; preserve existing grants. Internal repositories remain readable to enterprise members. | Read default_repository_permission and test effective access of a representative ordinary member. |
| Member repository creation | members_can_create_public_repositories/private_repositories/internal_repositories: boolean per visibility | Use separate visibility controls; enterprise may prohibit internal/public creation. Do not send closing-down members_allowed_repository_creation_type. | Read each flag and inherited enterprise constraint. |
| Member administrative powers | members_can_delete_repositories; members_can_change_repo_visibility; members_can_invite_outside_collaborators; members_can_create_teams; members_can_delete_issues: booleans | Choose each separately; broad repository admin authority does not authorize destructive actions in this session. | Read flags plus actual repository administrators; record inherited restrictions. |
| Public identity versus billing contact | name/company/blog/location/public email/description versus billing_email | Publish only owner-approved contact data; billing address stays private. | Inspect public profile signed out and billing contact through owner-only settings. |
| Invitation and membership | invitation pending/failed; organization role member/admin; member visibility private/public | Invite exact login/email and chosen role; wait for acceptance and required identity setup. Never infer full membership from public members. | Read invitations and authenticated membership; verify access after acceptance. |
| Outside collaborator conversion/removal | organization member versus outside collaborator; repository role per grant | Inventory team access and owned responsibilities first; explicit offboarding scope includes deploy keys/App access, not just user removal. | Read remaining direct/team/base grants and outstanding invitations after change. |
| Organization web commit signoff | web_commit_signoff_required boolean; documented default false | Apply an approved signoff agreement to web commits across organization repositories. Distinguish Signed-off-by from verified cryptographic signatures; CLI commits need --signoff. | Read organization and repository effective settings; inspect the web commit form and an authorized resulting trailer. Restore previous policy on error without rewriting earlier commits. |

### Pitfalls

- REST response examples are not tenant defaults. Base changes affect existing members too; private forks require separate inspection.
- A lower direct grant cannot subtract higher base/team/custom-role access.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/orgs/orgs)
- [Official sources 2](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/setting-base-permissions-for-an-organization)
- [Official sources 3](https://docs.github.com/en/rest/orgs/members)
- [Official sources 4](https://docs.github.com/en/rest/orgs/outside-collaborators)
- [Official sources 5](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-commit-signoff-policy-for-your-organization)

## Nested teams and delegated roles

Group ID teams-roles.

Capabilities admin-teams, admin-team-members, admin-team-idp-sync, admin-team-external-groups, admin-organization-role-assignments, admin-organization-custom-roles, admin-organization-custom-role-definitions, admin-enterprise-role-assignments, admin-organization-security-managers.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Team privacy | secret \| closed; new non-nested REST default secret, child default closed | Set explicitly: closed for discoverable normal teams; secret cannot have parent/children. | Read privacy and parent for every team, including secret teams through owner identity. |
| Hierarchy and identity | parent_team_id or parent_team_slug; ID takes precedence | Keep existing team IDs; resolve current slug after rename; verify inherited repository grants. | Read parent/children and effective repository access for child member. |
| Mention notifications | notifications_enabled \| notifications_disabled; default enabled | Disable only intentionally; CODEOWNERS/team mentions must reach responsible humans. | Read notification_setting; ask intended maintainers to verify receipt during authorized collaboration. |
| Team member authority | member \| maintainer; pending invitation versus active membership | Maintainer is team administration, not organization owner. Team creator becomes maintainer automatically. IdP-synced membership is changed at IdP. | Read team membership role/state and synchronization mapping. |
| Repository roles | read/triage/write/maintain/admin in UI; pull/push map to read/write in team REST; custom role name/ID | Assign the least role needed; check combined base/direct/team/custom permissions. | Read permission sources and a representative allowed/denied operation. |
| Custom role definition | base repository role plus additional permission identifiers; organization role permissions from fine-grained-permission discovery | Discover currently allowed identifiers, dependencies and plan; do not hard-code an old permission list. Separate definition from user/team assignment. | Read role definitions, assigned users/teams and inherited permissions before deleting or replacing a role. |
| Security manager migration | organization roles assignment; legacy security-managers routes retiring | Use current organization role discovery; preserve historical role-change evidence and existing assignments. | Read replacement role and exact affected users/teams; record unsupported legacy endpoint response. |

### Pitfalls

- Secret-team names can appear in mention text. A successful visible-team list does not prove no secret team exists.
- Do not remove a role as a shortcut to reconciling assignments; recover original role and grants first.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/teams/teams)
- [Official sources 2](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)
- [Official sources 3](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles)
- [Official sources 4](https://docs.github.com/en/rest/orgs/organization-roles)
- [Official sources 5](https://docs.github.com/en/rest/orgs/security-managers)

## SSO, provisioning, 2FA and account recovery

Group ID identity-recovery.

Capabilities admin-identity-policies, admin-organization-audit-and-sso, admin-organization-scim, admin-enterprise-scim, admin-enterprise-credentials.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Organization SAML connection | Sign on URL; Issuer; public certificate; enabled versus required | Configure/test first, authenticate owner at least once, preserve offline recovery codes; only then enforce. | Test IdP login and inspect list of members GitHub proposes removing before confirmation. |
| Enterprise SAML inheritance | enterprise enforced versus organization configuration | Enterprise enforcement overrides organization SAML; assess every organization and service credential before rollout. | Verify effective connection and representative member login across affected organizations. |
| Provisioning model | ordinary account invitations; organization SCIM; Enterprise Managed Users SCIM | Identify model before changing users. IdP governs managed-user lifecycle; ordinary local invitation is not an EMU substitute. | Read external identity, active state and group/team mapping with correct host API. |
| Authentication assurance | 2FA required yes/no; allowed 2FA methods per actual host policy; passkeys/security keys/recovery methods | Inventory impacted users and service accounts, notify humans, retain independent recovery methods; enforcement requires access-impact authorization. | Read requirement and member compliance; verify owners retain a tested recovery route. |
| Verified/approved domains | DNS verification record; verified domain; notification-domain restriction where available | Verify DNS ownership before restricting notifications; record DNS lifecycle owner. | Read verification and send destinations; do not confuse verified domain with automatic SSO provisioning. |
| Offboarding and recovery | suspend/deprovision; remove membership; revoke SSO credential; revoke token; delete account are distinct | Record actor/subject IDs, teams, grants and recovery constraints; choose reversible suspension when it meets request. | Check effective denial and preserved records; use documented recovery rather than recreating identity blindly. |
| IP allow-list entries and enforcement | organization/enterprise entries: IP or CIDR, description, enabled; allow-list enabled/disabled; inherited enterprise entries | Enterprise Cloud eligibility required. Inventory automation egress and IPv6, add the current administrator IP/range, and check address admission before enabling. Enforcement starts immediately; organization Codespaces becomes unavailable. Never remove the last working administrative route. | Read entries and inherited policy; use Check IP address before enabling, then verify representative user/App web/API/Git access. Preserve a working authorized admin session for recovery; restore prior entries or disable through that route if access breaks. Changes may take minutes to propagate. |
| Installed GitHub App IP inheritance | Enable IP allow list configuration for installed GitHub Apps boolean; App-managed entries | Enable only for approved installed Apps. Their registered addresses update automatically and apply to installation traffic, not ordinary users at those IPs. App-managed entries cannot be edited/deleted/disabled individually. | Read inheritance toggle and Managed by App entries, verify the intended installation access and user restrictions. Correct App registration or inheritance policy rather than broadening ordinary user CIDRs; recheck downstream access. |

### Pitfalls

- Enforcing organization SAML can remove members who have not authenticated with IdP. Downloading recovery codes into logs exposes recovery access.
- SCIM deprovisioning, IdP group deletion and GitHub membership removal are different effects; verify all required layers.

### Official sources

- [Official sources 1](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/enabling-and-testing-saml-single-sign-on-for-your-organization)
- [Official sources 2](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/enforcing-saml-single-sign-on-for-your-organization)
- [Official sources 3](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)
- [Official sources 4](https://docs.github.com/en/rest/scim)
- [Official sources 5](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)
- [Official sources 6](https://docs.github.com/en/apps/maintaining-github-apps/managing-allowed-ip-addresses-for-a-github-app)

## PAT and OAuth lifecycle

Group ID tokens-oauth.

Capabilities admin-organization-token-governance, admin-enterprise-token-inventory, admin-oauth-app-authorizations, admin-credential-revocation.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| PAT family and resource owner | fine-grained \| classic; one resource owner for fine-grained; all versus selected repositories | Prefer fine-grained when endpoint supports it, or installation App for long-lived automation. Check unsupported workflows before choosing token. | Inspect token family, owner, selected repositories and endpoint-specific permission without showing token. |
| Fine-grained approval | Require administrator approval (documented default) \| Do not require administrator approval | Keep approval unless owner explicitly chooses otherwise; owners own requests auto-approve. Pending tokens only read public resources. | Read pending requests, requested access/expiry and final request state; requester confirms operation after approval. |
| Classic access policy | allow versus restrict classic PAT access, separate from fine-grained approval | An approval rule does not control classic PATs; choose both policies and inherited enterprise restrictions. | Read both token-family policies and existing token inventory. |
| Maximum token lifetime | organization/enterprise configured maximum per token family; token expiration date | Use finite lifetime appropriate to workflow and rotation owner; read actual allowed range from current host rather than inventing universal default. | Check expiry and rotation reminder; verify replacement works before revoking old token. |
| Request decision API | action approve \| deny; optional reason max1024; GitHub App user/installation tokens only | Human reviews requested repositories and permissions; organization App token needs Personal access token requests write. PAT cannot approve itself through this API. | Read request ID/state; preserve reason and actor; requester gets notification. |
| OAuth app governance | authorized user grant; organization OAuth restrictions; approved/requested App access | Separate user authorization from organization approval and SSO authorization. Never assume OAuth install is GitHub App install. | Read app owner/client identity, scopes, organization authorization and last-use evidence. |
| Revocation | revoke organization access; revoke authorization; delete secret; emergency credential revocation | Record consequence and affected automation; revoke exposed credential and rotate consumers. Revocation cannot recover original secret. | Verify old credential fails and new scoped credential succeeds without logging either. |

### Pitfalls

- 403/404 may be SSO/resource-selection/approval restrictions, not absent repository. Changing token scope cannot add rights the token owner lacks.
- Do not paste credentials into issue reports, approval reasons, URLs or diagnostic artifacts.

### Official sources

- [Official sources 1](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [Official sources 2](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization)
- [Official sources 3](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/managing-requests-for-personal-access-tokens-in-your-organization)
- [Official sources 4](https://docs.github.com/en/rest/orgs/personal-access-tokens)
- [Official sources 5](https://docs.github.com/en/rest/apps/oauth-applications)

## App registration versus installation

Group ID app-registration.

Capabilities admin-github-apps, admin-github-app-installations, admin-enterprise-app-installations, admin-marketplace.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Registration owner/distribution | personal or organization owner; Only on this account \| Any account | Keep internal app private unless broader distribution requested. | Read App ID/slug/owner and installation availability. |
| User authorization flow | up to10 callback URLs; expiring user tokens selected by default; request OAuth during installation; device flow optional | Enable only needed flow; keep expiry. Setup URL cannot coexist with requesting user OAuth during installation. | Test exact redirect and expiration/refresh path without exposing secrets. |
| Post-install configuration | Setup URL; Redirect on update boolean | Use for required onboarding; installation repository selection changes can re-trigger setup. | Verify existing installation update preserves completed human configuration. |
| Permission/event selection | No access \| Read-only \| Read & write as offered; repository/organization/account permissions; events constrained by permissions | Choose endpoint minimum; expanded permissions require installation approval. | Compare requested registration permissions to currently approved installation permissions. |
| Installation repository scope | All repositories \| Only select repositories; installation ID; suspended state | Select only necessary repositories; registration, user consent and installation are separate. | Read installation repository list and mint a scoped token only for authorized operation. |
| Private keys and token lifecycle | App JWT; installation token; user token; private-key rotation | Store keys securely; install token may narrow approved permissions/repos. Rotate by adding replacement, verifying, then removing old key. | Verify App identity and token expiry/permissions; do not print PEM/JWT/token. |

### Pitfalls

- Uninstalling an external-property App removes its external custom properties; preserve values first.
- App permission change is not proof all existing installations accepted the expansion.

### Official sources

- [Official sources 1](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app)
- [Official sources 2](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party)
- [Official sources 3](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation)

## Webhook security and delivery recovery

Group ID webhook-delivery.

Capabilities admin-organization-webhooks, admin-github-app-webhooks.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Delivery configuration | active true/false; config.url HTTPS; content_type json/form; insecure_ssl 0/1; secret stored separately | Use HTTPS, verification enabled (0) and high-entropy secret; subscribe only needed events. | Read redacted configuration and selected events; validate signature on receiver. |
| Receiver behavior | X-GitHub-Event plus action; X-GitHub-Delivery; 2XX within10seconds | Durably enqueue, acknowledge quickly, process idempotently; unknown action is not assumed safe. | Inspect receipt, signature failure, queue processing and resulting business object. |
| Delivery recovery | ping; deliveries; delivery detail; redeliver attempt | Inspect failures before replay; replay same GUID must not duplicate side effects. | Read redelivery result and downstream state; POST acceptance alone is incomplete. |
| Retry credentials/runtime | organization/App/repository webhook permissions; installed runtime/module support | Use scope-correct credentials; GITHUB_TOKEN cannot redeliver repository webhooks. Validate sample runtime imports before deployment. | Run bounded redelivery test; check response status and error paths. |
| History and secret rotation | original delivery GUID plus attempt IDs/statuses; old/new verifier secret transition | Retain payload metadata only under approved data policy; coordinate producer/receiver rotation. | Verify latest signature and queue state, preserve original failed delivery and retry evidence. |

### Pitfalls

- OAuth-created hooks can be inaccessible to another credential type. Secret plaintext is not recoverable from readback.
- Community #126156 reports a stale CommonJS Octokit sample failing ERR_REQUIRE_ESM; current App guide uses .mjs. Verify installed package/runtime, do not cargo-cult old snippet.

### Official sources

- [Official sources 1](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks)
- [Official sources 2](https://docs.github.com/en/webhooks/using-webhooks/automatically-redelivering-failed-deliveries-for-a-repository-webhook)
- [Official sources 3](https://docs.github.com/en/webhooks/using-webhooks/automatically-redelivering-failed-deliveries-for-a-github-app-webhook)
- [Official sources 4](https://docs.github.com/en/rest/orgs/webhooks)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/126156)

## Audit history and incident evidence preservation

Group ID audit-history.

Capabilities admin-organization-audit-and-sso, admin-enterprise-audit, admin-organization-api-insights, admin-activity-events, admin-personal-data-export.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Read channel/time window | UI; JSON/CSV export; REST; stream; explicit created/date filters | UI default shows3months; enterprise web events180days and Git events7days. Export early; event channel determines completeness. | Record earliest/latest timestamps, filters, pages and counts for each channel. |
| Git versus API event evidence | Git clone/fetch/push; API requests; web-origin operations; SSO responses | Git REST events exclude some web/API initiated effects; do not equate Git event inventory with all mutations. | Correlate request IDs, actor/subject IDs, repository IDs and object timelines. |
| Streaming configuration | destination; active/paused; API request events opt-in; source IP disclosure; available Copilot agent events preview | Use enterprise stream for future retention; decide sensitive IP/log access and destination permissions with owner. | Verify receiver ingestion, last event time, health notifications and queryable retained sample. |
| Continuity and deduplication | at-least-once delivery;7day pause buffer; destination-specific acceptance window | Keep event IDs and deduplicate; repair misconfiguration within6days. Datadog can reject events older than18hours. | Monitor gaps and resume cursor; do not claim backfill predating stream enablement. |
| Preservation artifact | raw read-only export; capture timestamp/host/API version/filter; checksum; restricted storage; separate analysis | Preserve original evidence and write an additive change ledger; record renamed/deleted actor IDs. Export before destructive account/policy changes. | Verify archive readability and checksums; test incident-responder access without publishing private logs. |
| Account export | requested/in-progress/completed; expiring download link; revoke download link | Treat point-in-time personal metadata export separately from repository backup and audit stream. | Inspect completed archive structure privately and verify requested revocation. |

### Pitfalls

- An empty event slice can be retention, filter, permission or channel loss. GitHub Support does not preserve incident logs for you.
- API usage statistics, public Events and repository traffic are not substitutes for retained security audit evidence.

### Official sources

- [Official sources 1](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/accessing-the-audit-log-for-your-enterprise)
- [Official sources 2](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization)
- [Official sources 3](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)
- [Official sources 4](https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/requesting-an-archive-of-your-personal-accounts-data)

## Billing budgets, attribution and hard stops

Group ID billing-budget-options.

Capabilities admin-billing-budgets, admin-billing-usage, admin-billing-cost-centers, admin-billing-usage-reports, admin-enterprise-licensing.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Budget subject | budget_scope organization/repository/multi_user_customer/user; enterprise/cost_center on their supported scope endpoints | Match payer and subject; do not create a duplicate budget before reading existing overlapping controls. | Read budget IDs, scopes, product/SKU and payer; reconcile pages against total_count/has_next_page. |
| Pricing selector | BundlePricing + ai_credits; ProductPricing + product; SkuPricing + SKU | Use live supported billing schema, not retired product assumptions. | Read chosen selector and resulting budget; export actual SKU usage. |
| Amount/enforcement | budget_amount integer; prevent_further_usage boolean; user/universal must true | Set authorized cap; ordinary budget UI hard stop is off by default, alerts alone do not cap spend. | Read enforcement and applicable remaining capacity; never disable cap merely to clear an error. |
| User budget payload | user login required for user scope; budget_entity_name empty allowed; optional future expires_at YYYY-MM-DD | Explicit user field is required even where generated schema omits it. User budgets always stop usage. | Read subject/expiry and test affected user policy without incurring unauthorized charges. |
| Alerting | budget_alerting.will_alert; alert_recipients logins; user-scope alerting unavailable | Route supported alerts to responsible humans; distinguish budget notice from product-access or seat request. | Read alert recipients and supported scope; verify delivery through authorized process. |
| Cost center inclusion | usage counts toward enterprise by default; exclusion optional | Exclude only with approved independent spending authority; keep a cost-center cap. | Reconcile organization/user membership and exported attribution against invoice/usage. |
| Recovery from blocked usage | reset cycle; paid usage policy; user limit; organizational/cost-center/enterprise limit; account entitlement | Identify limiting layer first; request budget increase from budget owner or wait for reset. | Read all applicable controls and report exact failed endpoint/policy; use UI when API is unhealthy. |

### Pitfalls

- Community #166810 suggests disabling stop usage; this can permit uncapped charges and is not a safe default. Current official budget order/AI credits supersede old premium-only advice.
- Community #206489 reports organization budgets 400 with user-scoped budgets; unconfirmed globally. Preserve error and use UI, do not report zero budgets or delete seats as a workaround.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/billing/budgets)
- [Official sources 2](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/budgets)
- [Official sources 3](https://docs.github.com/en/copilot/how-tos/manage-and-track-spending/manage-company-spending)

### Community reports

- [Community reports 1](https://github.com/orgs/community/discussions/166810)
- [Community reports 2](https://github.com/orgs/community/discussions/206489)
- [Community reports 3](https://github.com/orgs/community/discussions/173899)

## Copilot seats, nested policy and client governance

Group ID copilot-governance.

Capabilities admin-copilot-seats, admin-copilot-usage-metrics, admin-copilot-agent-policy, admin-enterprise-ai-controls, admin-mcp-and-custom-agent-policy.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Access assignment | selected users/teams versus broader membership; organization seat versus enterprise-assigned access | Start with authorized pilot; identify payer and approval owner. A seat is not a feature policy or budget. | Read assigned seats/access and active entitlement for target human. |
| Enterprise enforcement | Enabled; Disabled; Let organizations decide/No policy; selected organizations where offered | Read inherited policy first; organization cannot override enterprise enforcement. | Inspect effective policy for each target organization and user. |
| Unconfigured defaults | separate default availability policies for GA features and GA models; enterprise-assigned user fallback policy | Choose future-feature/model defaults explicitly; do not invent one universal default for every product. | Read both defaults and explicit per-feature/model overrides. |
| Multiple license conflicts | same-enterprise usually least restrictive; cross-enterprise usually most restrictive; feature-specific exceptions | Evaluate paying org and exact conflict matrix: metrics/public-code privacy/non-GitHub semantic indexing differ. | Test target identity effective feature access, not only one organization settings page. |
| Separate feature/client switches | GitHub.com; CLI; Copilot app; cloud agent; review; model availability; preview; feedback; MCP in Copilot | Configure each applicable switch; Copilot MCP policy does not govern GitHub MCP in third-party hosts. | Read policy supported-surface matrix and verify actual client behavior. |
| Cloud-agent organization targeting | enabled everywhere/disabled/organization-delegated/selected organizations; selected IDs or organization properties | Property-based selection is evaluated at configuration time, not continuously on later property edits. | Re-read enabled org list after property changes; reconcile intentionally. |
| Human lifecycle and cost | access request; owner approval; onboarding; usage review; inactivity/offboarding | Give users instructions, responsible support contact and budget limit; usage metrics are not a productivity ranking. | Verify activation and failed access, record approved removal and effective date without deleting review history. |

### Pitfalls

- A toggle read is not a seat, model entitlement, client setting or billing verification.
- Do not assume organization policy applies to personal users merely accessing an organization repository; policy descriptions define audience.

### Official sources

- [Official sources 1](https://docs.github.com/en/copilot/concepts/enterprise/policies)
- [Official sources 2](https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/enterprise-administrators/policy-conflicts)
- [Official sources 3](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies)
- [Official sources 4](https://docs.github.com/en/copilot/concepts/enterprise/agent-management)
- [Official sources 5](https://docs.github.com/en/rest/copilot/copilot-user-management)

## Content exclusion, review and local agent controls

Group ID copilot-exclusions.

Capabilities admin-copilot-content-exclusions, admin-copilot-code-review, admin-copilot-cli-customization, admin-copilot-sdk.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Repository exclusion syntax | YAML list of path patterns; /scripts/** versus /scripts/*; case-insensitive fnmatch | Use patterns scoped to actual sensitive files; preserve inherited exclusions. | Test excluded file and nonexcluded control file for inline/chat/review behavior. |
| Organization/enterprise patterns | repository URL/name mapping to path list; wildcard repository key for filesystem-wide paths | Match intended clone URL and seat audience; enterprise and org scopes differ. | Inspect merged effective policies and actual resolved repository. |
| Propagation and supported clients | up to30minutes IDE propagation; reload client to refresh; current canonical support matrix | Recheck current canonical docs and installed client: older enterprise docs may still say CLI/agents unsupported. | Reload VS Code or restart supported IDE then test actual target client. |
| Exclusion boundary | guardrail; indirect access, symlinks, remote filesystems, third-party MCP exceptions | Use OS/tool permissions for hard boundaries; content exclusion cannot guarantee every access path. | Inspect tool permissions and avoid sensitive-file access in verification. |
| CLI/SDK execution | instructions/agents/skills/plugins/hooks/MCP/LSP; allowed tools/paths; permission handler; model/provider | Read installed runtime schema; installation of config does not authorize arbitrary hooks or tools. | Bounded session verifies loaded customizations, cancellation, error handling, cleanup and permission prompt. |

### Pitfalls

- Content exclusion is not a secret store or filesystem sandbox. Changing model/provider may change data handling and costs.

### Official sources

- [Official sources 1](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot)
- [Official sources 2](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion)
- [Official sources 3](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview)
- [Official sources 4](https://docs.github.com/en/copilot/get-started/sdk-quickstart)

## Codespaces policies and secrets

Group ID codespaces-options.

Capabilities admin-codespaces-lifecycle, admin-codespaces-machines, admin-codespaces-organization-access, admin-codespaces-organization-secrets, admin-codespaces-repository-secrets, admin-codespaces-user-secrets, admin-devcontainers.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Idle timeout | default30minutes; personal timeout plus org maximum; shortest applicable wins | Set maximum acceptable inactivity for organization-paid codespaces; terminal output can keep one active. | Read policy scope and inspect effective timeout after start/restart. |
| Policy targeting | All repositories \| Selected repositories; organization-paid codespaces only | Do not claim policy restricts personally paid codespaces. Maximum codespaces per user constraint is organization-wide. | Verify payer, targeted IDs and existing codespace next-start behavior. |
| Retention and lifecycle | default30days retention; stop/start/rebuild/delete; machine selection from available list | Save uncommitted work before destructive deletion/rebuild; stopping compute does not remove storage charges. | Read state, machine and storage; verify committed backup before deletion. |
| Additional constraints | allowed machine types; base-image restrictions; forwarded-port visibility; max codespaces per user | Configure individual constraints from real eligible plan UI; preserve intended developer functionality. | Create only an authorized bounded sample; verify restrictions and failure message. |
| Secret scope | organization all/private/selected repositories; repository; user selected repositories; encrypted value | Use narrowest scope and current public key; never log plaintext; explicitly grant needed additional repository access. | List names/scope and test authorized consumer; readback cannot reveal encrypted secret. |
| Prebuild branch, configuration and triggers | branch plus devcontainer.json; Every push default, On configuration change, Scheduled | Choose actual developer branch/configuration and authorized billing scope. Configuration-change mode watches supported devcontainer/Dockerfile paths and may leave dependencies stale; nested devcontainer changes do not all trigger it. | Read saved branch/configuration/schedule and latest Codespaces Prebuilds run SHA/conclusion; create an authorized sample to confirm Prebuilt codespace found. Correct configuration and rerun before relying on it. |
| Prebuild regions and template history | all available regions default; selected regions; retained versions 1..5, default 2 | Select used regions and justified history only; every region/version incurs storage charges. Older retained configurations support matching historical revisions. | Read regions/history and expected Prebuild Ready availability for region/configuration. Restore prior settings if intended developers lose coverage; disabling workflow updates leaves existing prebuilds usable and does not delete storage. |
| Prebuild commands and credential availability | onCreateCommand once per prebuild; updateContentCommand initially and on updates; repository/organization Codespaces secrets; no user secrets during prebuild | Put incremental source builds in updateContentCommand. Grant narrow repository access and credentials; prebuild secrets must not be embedded in resulting reusable files. User secrets become available only after codespace creation. | Read devcontainer commands and secret scope metadata; inspect redacted prebuild logs and an authorized clean codespace. Rotate exposed secrets at provider and replace consumers; fix command/configuration and rebuild affected prebuilds. |

### Pitfalls

- Deletion does not erase storage already accrued in the current billing cycle. Shared forwarded ports and terminal traffic can defeat expected idle savings.

### Official sources

- [Official sources 1](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period)
- [Official sources 2](https://docs.github.com/en/enterprise-cloud@latest/codespaces/troubleshooting/troubleshooting-included-usage)
- [Official sources 3](https://docs.github.com/en/rest/codespaces/organization-secrets)
- [Official sources 4](https://docs.github.com/en/rest/codespaces/codespaces)
- [Official sources 5](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds)
- [Official sources 6](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds)
- [Official sources 7](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-prebuilds)

## Custom properties, issue types and shared fields

Group ID classification-schema.

Capabilities admin-organization-properties, admin-enterprise-properties, admin-enterprise-organization-properties, admin-organization-issue-types, admin-organization-issue-fields.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Repository property schema | string/single_select/multi_select/true_false; required/default/allowed_values/values_editable_by as offered | Read existing schema and consumers first; preserve property names and values. | Read schema and values for new and existing customized repositories. |
| External property registration | installation_id; display_name1..15alphanumeric immutable; App-only namespace | Confirm installation permission and lifecycle owner; unregister/uninstall can destroy App-owned values. | Read registration as owner (installation token only sees itself); export values before uninstall. |
| Issue type | name; is_enabled boolean; description; gray/blue/green/yellow/orange/red/pink/purple/null color | Reuse type ID; disable obsolete type before deleting when preservation matters. | Read definitions and representative issue assignments. |
| Shared issue field datatype | text/date/single_select/multi_select/number | Choose native semantics; select types require options; not the same object as Project-only field. | Read field ID/type and issue values; test visibility with intended collaborator. |
| Shared field visibility/options | restricted \| all; organization_members_only deprecated; select option name/description/color/priority | Explicit restricted recommended for private metadata; all exposes to anyone able to see issue. Preserve option IDs during update. | Read effective visibility and existing values; check host visibility-feature support. |

### Pitfalls

- API docs currently default visibility to deprecated organization_members_only; explicitly use restricted on supported versions.
- Schema deletion/recreation can break ruleset targeting, reporting and historical issue field values.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/orgs/custom-properties)
- [Official sources 2](https://docs.github.com/en/rest/orgs/issue-types)
- [Official sources 3](https://docs.github.com/en/rest/orgs/issue-fields)
- [Official sources 4](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization)

## Personal identity, notifications and human action

Group ID personal-human-workflow.

Capabilities admin-account-profile, admin-account-emails, admin-account-keys, admin-account-gpg-keys, admin-account-ssh-signing-keys, admin-account-security-and-billing-ui, admin-notifications, admin-repository-watches, admin-account-blocking, admin-organization-blocking.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Email/privacy | primary/verified/public email; keep email private; block pushes exposing private email | Preserve verified recovery address; choose noreply Git identity when privacy requested. | Inspect public commit/profile and private verification state; never publish recovery address. |
| Key purpose | SSH authentication key versus SSH signing key versus GPG key; read-only/write deploy key separate | Keep purpose explicit; public key fingerprint identifies key, not private credential. | Read purpose/fingerprint and verify bounded auth or signature; inspect deploy-key grants on offboarding. |
| Recovery | passkeys/security keys/TOTP/recovery codes; active sessions; password reauthentication | Require human control of second factors and backup recovery; never save recovery material in shared docs. | Owner verifies independent recovery route; revoke only explicitly targeted session/credential. |
| Repository watch | Participating/@mentions; All activity; Ignore; Custom event types | Use releases/security/review signals needed by actual maintainer; automatically participating subscription can add noise. | Read subscription and intended event categories; intended human verifies notifications. |
| Delivery channels | On GitHub; email; Mobile; participating/watching categories; default/per-org verified email; working hours | Keep actionable maintainer notices; personal settings require account owner context. | Check inbox/email settings and representative received notification; a sent mention is not proof of delivery. |
| Moderation | block/unblock; organization block differs from personal block; interaction limits | Preserve abuse evidence privately; specify affected relationships and access before blocking. | Read current block/limit and verify intended scope; avoid unnecessary duplicate contact. |

### Pitfalls

- Email replies can create public comments. Notification privacy and contributor consent still matter.
- Removing a user does not revoke a deploy key whose private key they retained.

### Official sources

- [Official sources 1](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications)
- [Official sources 2](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [Official sources 3](https://docs.github.com/en/authentication/managing-commit-signature-verification)
- [Official sources 4](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa)
- [Official sources 5](https://docs.github.com/en/rest/users/blocking)

## Host-specific enterprise lifecycle and support

Group ID enterprise-host-lifecycle.

Capabilities admin-enterprise-accounts, admin-enterprise-organization-lifecycle, admin-enterprise-data-residency, admin-enterprise-server-admin, admin-github-connect, admin-organization-migrations, admin-user-migrations, admin-enterprise-importer, admin-support-entitlements, admin-support-tickets, admin-source-imports.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Hosting and identity | github.com \| tenant.ghe.com \| GHES version; ordinary identities versus managed users | Choose actual API/SSH host and product/version docs before credentials or network policy. | Read host /meta, enterprise identity and version; do not apply github.com IP/fingerprint snapshot blindly. |
| Organization lifecycle | create; invite existing; transfer; migration importer; pending acceptance | EMU cannot import an ordinary organization via simple enterprise invite; cross-host moves need supported migration. | Read destination ownership, inherited policy, billing and member access after completion. |
| Migration plan | source/export; destination; locks; import status; warnings; user attribution; redirect behavior | Preserve source and export; map humans and permissions; rehearse recovery before destructive cutover. | Inspect final migration log, counts, links and sampled historical issues/PR authors/files. |
| GHES administration | backup/restore; maintenance; upgrade; replica/HA; license; support bundle; GitHub Connect | Use instance version runbook and verified backups; repo admin is not appliance administrator. | Verify backup restore readiness, instance health/version and product connectivity after approved change. |
| Support interaction | entitlement; intended enterprise account; new/existing ticket; attachment; reply; status | Prepare redacted reproduction and preserve case history; submission/reply contacts another party and needs explicit instruction. | Read actual ticket ID/submitted content/status; form preparation alone is not submission. |

### Pitfalls

- Migration/API success does not prove review history, actor attribution or every product artifact migrated.
- Support attachments can have unauthenticated URLs; redact before upload.

### Official sources

- [Official sources 1](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/feature-overview-for-github-enterprise-cloud-with-data-residency)
- [Official sources 2](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/adding-organizations-to-your-enterprise)
- [Official sources 3](https://docs.github.com/en/migrations/using-github-enterprise-importer)
- [Official sources 4](https://docs.github.com/en/enterprise-server@latest/admin)
- [Official sources 5](https://docs.github.com/en/enterprise-cloud@latest/support/contacting-github-support/creating-a-support-ticket)

## Organization rules and hosted networking

Group ID rules-network.

Capabilities admin-organization-rulesets, admin-organization-rule-suites, admin-enterprise-rulesets, admin-organization-network-configurations, admin-enterprise-network-configurations.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Ruleset nested scope | target branch/tag/push where supported; enforcement disabled/active/evaluate; repository/ref include/exclude conditions; bypass actors/modes | Preserve target conditions and bypass IDs; evaluate mode measures without enforcement. Detail rule parameters in delivery-security reference. | Read each ruleset, inherited sources and rule suites for sample pushes; list alone proves little. |
| Network configuration | name1..100 letters/numbers/._-; compute_service none/actions; exactly one network_settings_ids entry | Use provisioned network resource and proper compute attachment; a configuration alone attaches no runner. | Read network setting and attached runner group plus actual connectivity. |
| Failover network | failover_network_settings_ids exactly one when configured; failover_network_enabled boolean | Choose failover only with independently tested connectivity and owner-approved network policy. | Read failover configuration; bounded connectivity/failover test and rollback route. |

### Pitfalls

- Push, branch and tag rules have different plan gates. Network API response examples showing multiple IDs conflict with current exactly-one request rule; current parameter constraint wins.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/orgs/rules)
- [Official sources 2](https://docs.github.com/en/rest/orgs/rule-suites)
- [Official sources 3](https://docs.github.com/en/rest/orgs/network-configurations)
- [Official sources 4](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/network-configurations)

## Agent automation, task execution and human handoff

Group ID agent-automation-options.

Capabilities admin-agent-automations, admin-agent-tasks, admin-agent-secrets, admin-agent-variables, admin-copilot-cloud-agent-sessions, admin-copilot-team-customizations.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Automation ownership | type personal/shared; enabled; require_actor_write_permission; continuous_history | Personal belongs to creator; shared is repository-readable and writer-manageable. Read repository allow-automations policy. | Read repository scope, creator and permitted actors; user-global list omits others shared automations. |
| Schedule and event triggers | cadence hourly/daily/weekly; hour_utc0..23; day_of_week0..6; minute_utc0/15/30/45 (omit with hourly); query/labels/workflow filters | Default daily/weekly midnight UTC, weekly Monday; choose explicitly with timezone conversion. | Read trigger fields and next/actual run time; preserve prior run history. |
| Trigger authority | write_scope trigger/repository; allow_copilot_triggers false default | Scheduled write_scope has no effect: scheduled runs can change entire repo. Keep Copilot-trigger loops disabled unless explicitly reviewed. | Read effective scope/policy; test trigger actor and targeted object. |
| Task request | prompt; model from current plan list; custom_agent filename stem; create_pull_request false default; base_ref/head_ref | Prompt must describe authorized work. Existing head_ref can receive commits; inspect branch/PR before start. | Read task/session/artifact and resulting diff; starting task is not completion. |
| Task states/history | queued/in_progress/completed/failed/idle/waiting_for_user/timed_out/cancelled; is_archived false default | Include archived records in history inventory; waiting_for_user needs actual human answer. | Read final state/output/errors and linked PR; retain original failed attempt before retry. |
| Secrets/variables/team customization | secret encryption key/value and repository visibility; plain variables; prompt/tool configuration | Never put secret in variable or prompt; preserve custom agents/tools and follow actual endpoint scope. | Read names/selection and bounded consumer output; no plaintext secret readback. |

### Pitfalls

- Public-preview surfaces change. App installation tokens support shared automations but not ordinary agent-task start/list; choose endpoint-specific authentication.
- No retry may silently create another billable task or duplicate PR; reread task/artifacts first.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/agent-automations/agent-automations)
- [Official sources 2](https://docs.github.com/en/rest/agent-tasks/agent-tasks)
- [Official sources 3](https://docs.github.com/en/rest/agents/secrets)
- [Official sources 4](https://docs.github.com/en/rest/agents/variables)
- [Official sources 5](https://docs.github.com/en/rest/copilot/copilot-cloud-agent-management)
- [Official sources 6](https://docs.github.com/en/rest/copilot/copilot-team-customizations)

## Copilot Spaces and private registry access

Group ID spaces-registry.

Capabilities admin-copilot-spaces, admin-copilot-space-collaborators, admin-copilot-space-resources, admin-private-registries.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Space default access | base_role no_access(default)/reader/writer/admin; name/description/general_instructions | Keep no_access until audience approved; discover direct collaborators separately. | Read default/direct roles and test intended audience. |
| Space resource types | repository/github_file/free_text/github_issue/github_pull_request/media_content/uploaded_text_file; type-specific metadata | Preserve resource IDs and private context; fine-grained/user tokens need every referenced repository. | Read resource details; list can omit whole Spaces with inaccessible resources, so incomplete list remains unknown. |
| Registry access | visibility all/private/selected; selected_repository_ids only with selected; replaces_base false default | Select repositories and decide whether public-registry fallback is acceptable. | Read visibility, selected IDs and successful bounded dependency resolution. |
| Registry authentication | token(default)/username_password/oidc_azure/oidc_aws/oidc_jfrog/oidc_cloudsmith/oidc_gcp/anonymous | Token/password require encrypted_value/key_id; OIDC omit them; anonymous also omits username. Use provider-specific fields from current schema. | Read redacted auth config and external trust mapping; verify authorized resolution, not secret plaintext. |
| Provider-specific identity | Azure tenant_id/client_id; AWS region/account/role/domain/domain_owner; JFrog provider/audience; Cloudsmith namespace/service_slug/audience; GCP workload_identity_provider/service_account | Grant narrow external trust; GCP service_account optional for direct WIF. Cloudsmith api_host defaults api.cloudsmith.io. | Verify actual issuer/audience/subject and repository binding with external administrator. |

### Pitfalls

- Space sharing and source repository access are distinct; do not widen source access to make inventory look complete.
- Credential rotation and trust-provider setup require both GitHub and registry-side verification.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/copilot-spaces/copilot-spaces)
- [Official sources 2](https://docs.github.com/en/rest/copilot-spaces/collaborators)
- [Official sources 3](https://docs.github.com/en/rest/copilot-spaces/resources)
- [Official sources 4](https://docs.github.com/en/rest/private-registries/organization-configurations)

## Organization defaults, repository history and storage

Group ID repository-community-lifecycle.

Capabilities admin-community-defaults, admin-organization-profile-content, admin-repository-lifecycle-admin, admin-repository-insights, admin-git-lfs, admin-archive-program, admin-github-models-retired.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Community defaults/profile | public .github defaults; repository-specific overrides; .github/profile/README.md and member profile where supported | Reuse organization defaults without overwriting repository custom documents; distinguish public/member audience. | Inspect rendered repository community profile and org profile with correct identity. |
| Repository lifecycle | visibility public/private/internal; archived; owner/name/default branch; delete versus archive | Check fork network, billing, actions/pages and collaborator consequences. Preserve history and transferable objects before move/delete. | Read metadata and history/redirect/access after change; archive is read-only, not backup. |
| LFS configuration | .gitattributes tracked patterns; LFS object store; pointers; quota/billing; migration rewritten history | Track only required files; git clone/mirror without LFS object fetch is insufficient backup. History rewrite requires coordinated human cutover. | Fetch/check LFS objects; verify fresh checkout and collaborators migration instructions. |
| Insights/preservation | traffic/clones/views; contributors/stats async response; Preserve this repository on/off | Capture ephemeral metric window before expiry. Archive Program opt-out only affects future preservation. | Read completed statistics and preservation setting; never equate UI archival, source export and long-term program. |
| Retired Models workflow | historical GitHub Models integration/configuration; retired endpoints | Preserve source/cost history, discover supported replacement only when requested; no new deployment against retired service. | Check endpoint retirement notice and installed integration; mark unavailable with dated evidence. |

### Pitfalls

- No repository deletion or history rewrite is implied by full setup. A metadata snapshot cannot restore repository/LFS/product history.

### Official sources

- [Official sources 1](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- [Official sources 2](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)
- [Official sources 3](https://docs.github.com/en/rest/repos/repos)
- [Official sources 4](https://docs.github.com/en/rest/metrics)
- [Official sources 5](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)
- [Official sources 6](https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/opting-into-or-out-of-the-github-archive-program-for-your-public-repository)
- [Official sources 7](https://docs.github.com/en/github-models)

## Human-facing sharing, Classroom and Spark

Group ID human-social-education.

Capabilities admin-account-following, admin-account-social-links, admin-gists, admin-gist-comments, admin-repository-stars, admin-activity-feeds, admin-classroom, admin-github-spark.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Social profile and subscriptions | follow/unfollow; social account URLs; star/unstar; public/private authenticated feeds | Only change owner-requested preferences; feed URLs can embed sensitive tokens. | Read actual relationship/profile/feed scope without logging private feed URLs. |
| Gist publication/history | public true/false on creation; description/files; file rename/delete; revisions/forks/comments | Secret gist is unlisted, not access-controlled private storage; never put secrets there. Preserve revision before edits. | Read visibility/files/history and comment IDs; inspect audience before publishing. |
| Classroom assignment | classroom/assignment ID; individual/group; accepted assignment repositories; students/teams; grades | Use teacher authority and preserve student privacy; acceptance and grading are separate human actions. | Read actual assignment, accepted repositories and grades with correct classroom scope. |
| Spark publishing/data | private/organization/all-GitHub-users where eligible; shared app data read-only/write; preview versus published version | Publication and data-write audience need explicit scope; managed users cannot publish to all GitHub users. | Read publication URL/version/audience and verify authorized viewer/data operation. |

### Pitfalls

- Commenting, following and invitations affect other humans. Read-only discovery is not permission to contact or publish.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/users/followers)
- [Official sources 2](https://docs.github.com/en/rest/users/social-accounts)
- [Official sources 3](https://docs.github.com/en/rest/gists/gists)
- [Official sources 4](https://docs.github.com/en/rest/gists/comments)
- [Official sources 5](https://docs.github.com/en/rest/activity/starring)
- [Official sources 6](https://docs.github.com/en/rest/activity/feeds)
- [Official sources 7](https://docs.github.com/en/rest/classroom/classroom)
- [Official sources 8](https://docs.github.com/en/copilot/tutorials/spark/your-first-spark)

## Platform diagnostics and templates

Group ID platform-diagnostics.

Capabilities admin-platform-meta, admin-platform-rate-limits, admin-platform-license-catalog, admin-platform-gitignore-templates, admin-platform-emojis, admin-platform-markdown-rendering.

| Setting | Values and defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Host metadata | GET /meta; API versions; SSH fingerprints; IP/domain lists | Use real host metadata and documented exceptions; avoid rewriting firewall from partial snapshot. | Verify host identity and freshness before applying any external network change. |
| Quota and retry | core/search/GraphQL resource budgets; x-ratelimit-*; retry-after; GraphQL cost/reset | Obey primary and secondary throttles; positive core remaining does not rule out secondary limit. | Record failed request/status/headers; retry under documented delay and verify object state first. |
| Catalog templates | SPDX license ID; detected license file; gitignore template name; emoji shortcode | Owner chooses license; preserve custom ignore rules; catalog discovery does not authorize relicensing. | Read actual committed license; git check-ignore plus tracked-file inspection; verify chosen shortcode. |
| Markdown rendering | mode markdown/gfm; repository context; raw rendering endpoint | Context changes issue/user link resolution; rendering POST does not publish comment or file. | Inspect returned HTML and context-sensitive links in intended renderer. |

### Pitfalls

- A successful render or catalog lookup proves only that lookup. It is not evidence of repository configuration or publication.

### Official sources

- [Official sources 1](https://docs.github.com/en/rest/meta)
- [Official sources 2](https://docs.github.com/en/rest/rate-limit)
- [Official sources 3](https://docs.github.com/en/rest/licenses)
- [Official sources 4](https://docs.github.com/en/rest/gitignore)
- [Official sources 5](https://docs.github.com/en/rest/emojis)
- [Official sources 6](https://docs.github.com/en/rest/markdown)

