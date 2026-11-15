# Collaboration: option-level setup and operating policy

Research date: 2026-11-15. Read this with [collaboration.md](collaboration.md), [operations.md](operations.md) and the capability catalog. This document decomposes settings and decisions inside those families; it does not replace operation discovery, owner policy or a live audit. Sources describe GitHub.com unless a host/version is identified. No external mutations or target-account feature tests were performed for this research.

## How to apply the options

For each applicable group, record observed object/field/option IDs, exact current values, the desired values and reason, supported execution surface, required permission/plan, and evidence after reconciliation. Inspect every existing customized object before creating or replacing one. A group is not configured merely because its parent capability is readable. A missing API setting requires current UI/schema inspection, not an invented default or a skipped nested option.

“Prefer”, “default to” and “use” below are recommended project policies. Actual GitHub defaults are identified explicitly; owner/repository decisions override recommendations. The listed values describe the documented surface, not a promise every value is available on every plan/host. For a newly discovered nested control, extend the ledger and inspect its semantics before declaring the group complete. Counts of groups or settings do not prove exhaustive coverage.

Choose applicability from the real workflow: a single-maintainer library can have zero required peer approvals with passing checks and owner routing; a busy team may need queue/review freshness; a deployed service needs QA/release semantics beyond merge. Cross-repository planning justifies shared fields and owner Projects. Date commitments justify roadmap/iterations; unsupported plans are unavailable with evidence rather than silently approximated. Community support needs staffed Q&A/routing; enabling every category creates no response ownership.

## Human interaction through the lifecycle

1. **Before work:** read instructions, issue body, relevant complete timeline/comments and linked decisions; search for duplicates; inspect Project status, ownership, blockers and any existing PR. Record current IDs and SHAs.
2. **Triage:** reuse existing native type/labels/fields; agree what completion means; preserve reporter evidence. Distinguish an actionable defect, unanswered question, early design discussion and declined proposal. Reopen the same unfinished work rather than fragmenting its history.
3. **While implementing:** add new chronological issue comments for meaningful progress, changed decisions, blockers, review readiness and delivery. Keep the description as current scope/acceptance criteria; description edits or repeatedly updating the first comment never replace progress comments. Follow the project's actual status transitions and notify only relevant people when authorized. Use [issue-lifecycle.md](issue-lifecycle.md) for mandatory checkpoints, sidebar reconciliation and native relationship/artifact procedures.
4. **Review:** read summary and inline threads, including outdated/resolved threads when relevant. Reply at the original finding with the implementing commit, reasoned disagreement or a linked follow-up. Submit pending reviews intentionally. Resolve only addressed/agreed findings and re-request review when appropriate and authorized.
5. **Delivery:** compare reviewed/current head; satisfy effective checks/review/queue rules; wait for actual merge and inspect resulting commit, issue closure and Project automations. A green enqueue or closed issue does not establish release/deployment.
6. **After delivery:** publish affected docs/Wiki only through the configured publication path, verify the remote rendered result, and retain issue→PR→commit→release/documentation links. Report partial/gated work precisely and retain previous decisions and unsuccessful attempts when they explain the final state.

Writing comments, assigning reviewers, converting discussions, subscriptions, announcements and personal votes affect people. This reference describes their correct operation; it does not itself authorize posting, access expansion, irreversible deletion or financial commitments.

## Settings and decisions

Each row gives accepted choices, a decision rule and owning-object verification. Each group carries official sources; forum observations are separately labeled and can prompt checks but never overrule current official behavior or actual target evidence.

### `repository-collaboration-settings` — Repository identity, defaults and collaboration surfaces

**Capability IDs:** `repository-lifecycle`, `repository-branches`, `repository-autolinks`, `repository-community`.

**Applicability:** Every repository; preserve owner decisions about visibility, licensing and audience.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| visibility / private | public; private; internal where eligible | Preserve observed visibility; assess access and discoverability before a requested change, never make a private project public as routine setup. | Re-read visibility and intended reader access; inspect fork implications before changing. |
| default_branch | existing branch name | Retain the current branch unless migration is required; discover branch names before configuring CI, templates or closing links. | Read repository default_branch, ref SHA and PR bases after any authorized rename. |
| has_issues / has_projects / has_wiki / has_discussions | independent booleans | Enable the surfaces the project will actively use; enabling a repository Projects tab does not create or configure an owner Project. | Read each flag and follow the actual tab and linked owner Project. |
| description / homepage / topics | text; HTTPS URL; topic list | Use concise purpose and a working primary documentation URL; preserve unrelated topics and owner-defined metadata. | Read metadata and open rendered links; check topic replacement semantics before writing. |
| autolinks.key_prefix / url_template / is_alphanumeric | tracker prefix; URL with <num>; boolean | Add only for a real external tracker; choose a non-colliding prefix and correct numeric versus alphanumeric matching. | Read rule IDs and test a harmless rendered example without sending a comment. |
| archived / disabled | repository lifecycle flags | Archive only when work truly ends; do not archive to represent a finished milestone or Project. | Re-read flags, open work and expected read-only behavior; record unarchive recovery path. |
| has_pull_requests / pull_request_creation_policy | has_pull_requests boolean; documented default true; pull_request_creation_policy: all or collaborators_only | Preserve contribution access unless a restriction is intended. Organization collaborators for this setting have write, maintain or admin access; personal collaborators are invited users. Disabling hides existing PRs rather than deleting them. | Read both settings and intended contributor eligibility; inspect PR visibility. Re-enable to restore existing PR availability; restore prior policy if legitimate contributions are blocked. |
| web_commit_signoff_required | boolean; documented default false; effective organization policy also applies | Choose only an owner-approved signoff agreement. This adds author signoff to web commits, differs from cryptographic signing, and does not enforce CLI signoffs; CLI authors use --signoff. | Read repository and organization policies; inspect the Sign off and commit changes form and resulting Signed-off-by trailer on an authorized commit. Restore prior setting if misconfigured; retain existing commit history. |

Option review: 2026-11-15. [official source 1](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/disabling-pull-requests), [official source 2](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-commit-signoff-policy-for-your-repository). Provider defaults above are separate from observed tenant values.

**Official sources:** [repos](https://docs.github.com/en/rest/repos/repos), [autolinks](https://docs.github.com/en/rest/repos/autolinks).

**Pitfall:** Repository flag defaults vary with creation path and owner settings; never infer actual configuration from product availability.

### `source-and-history-policy` — Source changes, history and repository derivation

**Capability IDs:** `repository-content`, `repository-git-objects`, `repository-history`, `repository-lfs-submodules`, `repository-templates`, `repository-forks`, `repository-commit-comments`.

**Applicability:** Every code repository; LFS/submodules/templates/forks only where present.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| content.ref / expected sha | immutable commit SHA; branch; tag; update blob SHA | Read immutable refs for evidence; use Git for multi-file work and expected old SHAs for API writes. | Inspect resulting commit tree and parents plus changed-file list; reconcile timeout before retry. |
| ref.force / git push strategy | non-force; force-with-lease when explicitly justified | Preserve human commits; default to non-force updates, compare remote head and use a lease only for authorized history rewrite. | Fetch and compare old/new ref OIDs; stop if remote changed unexpectedly. |
| merge history | merge commit; squash; rebase | Follow repository policy; merge preserves branch commits, squash gives one logical commit, rebase rewrites commit identities. | Match resulting base-branch commit and PR merge metadata; keep issue/PR links as decision history. |
| template.include_all_branches / fork.default_branch_only | boolean choices | Template copies start a separate history; forks preserve an upstream relationship. Choose based on contribution versus new-project intent. | Inspect parent/source or is_template relationship and compare expected branches/files. |
| LFS / submodule checkout | pointer versus object; pinned SHA; recursive checkout | Fetch only required objects and pinned submodules; never treat an LFS pointer or gitlink as tested source content. | Verify actual object bytes, submodule OIDs and executable/symlink modes. |
| comment anchor | commit SHA; file path; valid line | Commit comments discuss a specific historical revision; use a PR review thread for an actionable PR finding. | Read returned comment ID, commit_id and line metadata; retain URL when following up. |

**Official sources:** [contents](https://docs.github.com/en/rest/repos/contents), [refs](https://docs.github.com/en/rest/git/refs), [pull-request-merges](https://docs.github.com/en/pull-requests/reference/pull-request-merges).

**Pitfall:** A Git clone does not contain issues, review conversations, Project configuration or Wiki history. Separate evidence stores are needed for those records.

### `codeowner-routing` — Who receives review and when

**Capability IDs:** `repository-codeowners`, `pr-review-requests`.

**Applicability:** Repositories accepting PRs; stricter ownership only with available qualified reviewers.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| CODEOWNERS location / matching order | .github/CODEOWNERS; root CODEOWNERS; docs/CODEOWNERS; last matching pattern | Use one authoritative file on the PR base branch, broad ownership first and narrow overrides later; list multiple owners together. | Read actual base-branch file, query CODEOWNERS errors and map representative changed paths. |
| owner eligibility | user with write; visible team with explicit write | Reuse real maintainers; do not invent a reviewer or broaden team visibility/access to make routing work. | Verify team visibility and repository role; inspect requests on a matching ready PR. |
| requested_reviewers / requested_teams | user logins; organization team slugs | Request the smallest relevant set; requests notify people, so repository setup alone is not authority to send them. | Read outstanding review requests and submitted reviews separately; a removed request may mean review completed. |
| draft to ready | draft; ready for review | Keep incomplete work draft; move ready when description, diff and checks support review. CODEOWNERS automatic requests happen on readiness. | Re-read isDraft and automatic requests; explain review scope in the authorized PR description. |
| require_code_owner_reviews | false; true through branch policy | Routing alone never enforces approval; enable enforcement where actual independent owners exist and repository rules call for it. | Read effective protection/ruleset plus PR reviewDecision; avoid self-approval deadlock. |

**Official sources:** [about-code-owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [review-requests](https://docs.github.com/en/rest/pulls/review-requests).

**Pitfall:** The author cannot approve their own PR. A single-maintainer repository may deliberately require zero peer approvals while retaining routing and required checks.

### `issue-intake-routing` — Issue chooser and PR template routing

**Capability IDs:** `issue-forms-templates`, `pr-templates`.

**Applicability:** User-facing or collaborative repositories; lightweight internal projects can use fewer forms.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| chooser.blank_issues_enabled / contact_links | true; false; name/url/about entries | Keep an accessible path for unusual reports; route support and private vulnerabilities to actual staffed destinations. | Render chooser as intended contributor; open every contact URL without submitting. |
| form.name / description / title | unique chooser name; purpose text; optional title prefix | Separate reproducible defects from proposals only when triage differs; avoid prefixes duplicating structured type. | Open every template on default branch and check readable chooser order and defaults. |
| form.labels / assignees / type | existing labels; assignable users; existing owner issue type | Reuse taxonomy; default assignees only when maintainers accept that responsibility; labels must already exist. | Check available labels/types/assignees and inspect a permitted representative result. |
| form.projects | OWNER/NUMBER list | For external reporters prefer Project auto-add because template project insertion needs the submitter's write access to that Project. | Verify with relevant contributor permission context; do not use maintainer success as outsider proof. |
| PR template selection | .github/pull_request_template.md; PULL_REQUEST_TEMPLATE/name.md and template query | Use concise purpose/validation/risk prompts; multiple templates need an actual selection link/process, not an assumed automatic chooser. | Open new-PR draft composer and test the intended template URL without posting. |
| inheritance / placement | repository templates; owner .github defaults | Inventory inherited files before adding duplicates; default-branch placement controls normal chooser availability. | Compare effective chooser and local/owner file sources, including casing and extension. |

**Official sources:** [syntax-for-issue-forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms), [configuring-issue-templates-for-your-repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository).

**Pitfall:** Issue forms become editable Markdown; required form controls are intake aids, not permanent structured-field enforcement. Issue forms are not PR forms.

### `form-controls` — Nested form controls and validation

**Capability IDs:** `issue-forms-templates`.

**Applicability:** For every configured YAML issue form; discussion forms reuse supported controls with their own top-level schema.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| body[].type / id | markdown; input; textarea; dropdown; checkboxes; upload; unique alphanumeric/-/_ IDs | Pick the control matching the answer; use stable unique IDs for supported prefills and future maintenance. | Validate schema and render each control on the target host; require a non-markdown control. |
| input.attributes | label; description; placeholder; value; validations.required | Require actionable minimum information, not optional diagnostics; placeholders are examples, values are submitted defaults. | Clear required inputs in preview and inspect validation behavior without posting. |
| textarea.attributes | label; description; placeholder; value; render; validations.required | Use render for literal logs/code only; omit it when Markdown editing or attachment affordances are needed. | Check code-fence output and attachment/Markdown behavior in composer. |
| dropdown.attributes | options[]; multiple true/false; default index; validations.required | Default only when the common choice is safe; use no default when choosing version/platform must be deliberate. | Check unique options, index bounds, single versus multiple selection and empty validation. |
| checkboxes.attributes.options[] | label; required true/false | Require only a meaningful acknowledgement; individual required flags differ from an optional checklist. | Test unchecked required item and check rendered links and separate labels. |
| markdown / upload | markdown.value; upload label/description/required where supported | Markdown guidance is not submitted content; keep critical reporting requirements in actual controls. Upload only needed files with privacy guidance. | Preview target schema support; inspect attachment expectations and avoid requesting secrets. |

**Official sources:** [syntax-for-githubs-form-schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema), [common-validation-errors-when-creating-issue-forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/common-validation-errors-when-creating-issue-forms).

**Pitfall:** Do not invent regex validators, conditional controls or arbitrary client logic; unsupported YAML keys can prevent the form appearing.

### `issue-taxonomy` — Types, labels, owners and milestone planning

**Capability IDs:** `issue-metadata`, `issue-assignees`, `issue-milestones`, `issue-types`, `issue-types-owner`.

**Applicability:** Every tracked work item; owner-wide definitions only with owner-level applicability.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| issue.type / owner definition | enabled type ID; null; name/description/color/is_enabled | Prefer the owner's existing Bug/Task/Feature equivalents; types describe work kind rather than transient status. Owner edits affect other repositories. | List owner and repository types, then read the issue's assigned type ID. |
| labels[] / label color-description | names and IDs; six-digit color; explanatory description | Labels serve useful cross-cutting queries; preserve customized names/colors and add/remove narrowly instead of replacing all. | Compare before/after label ID sets and rendered descriptions; check saved filters still match renamed labels. |
| assignees[] | eligible user logins; empty list | Assign a responsible person only when the task or project convention authorizes it; assignment does not mean acceptance. | Check assignability then re-read the exact assignee set; do not confuse PR reviewer and assignee. |
| milestone.title / description / due_on / state | repository milestone; ISO8601 date; open/closed | Use milestones for real releases/deadlines, not arbitrary duplicates of Project iterations; dates are targets. | Read milestone counters and all included open/closed issues and PRs; closing milestone does not close work. |
| metadata mutation mode | add; remove; replace | Use delta mutations for focused edits; reserve replace for an explicitly reconciled full desired set. | Re-read concurrent metadata before write and confirm unrelated labels/assignees remain. |

**Official sources:** [labels](https://docs.github.com/en/rest/issues/labels), [assignees](https://docs.github.com/en/rest/issues/assignees), [milestones](https://docs.github.com/en/rest/issues/milestones), [issue-types](https://docs.github.com/en/rest/orgs/issue-types).

**Pitfall:** Do not create a new taxonomy each run or use a label named Feature as proof native issue type is configured.

### `shared-issue-fields` — Shared issue definitions and Project-local fields

**Capability IDs:** `issue-fields`, `issue-field-values`, `projects-issue-fields`, `projects-multiselect`.

**Applicability:** Cross-repository structured facts use owner issue fields; Project-only estimates/status use Project fields. Preview/host gates must be inspected.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| field scope / applicability | owner issue field; Project field; same-owner issues only | Put reusable facts on the issue; Project issue-field cells are empty for PRs, draft items and issues from other owners. | Read owner definition, issue sidebar and Project column as intended audience; missing applicability is not missing data. |
| visibility / API enum | Restricted/Public in UI; restricted/all in REST; deprecated organization_members_only | Retain restricted default for nonpublic planning facts; public/internal Projects expose only Public issue fields. Changing to Restricted removes the field from those Projects. | Read exact API visibility and inspect viewer/sidebar/timeline/Project behavior; do not change visibility merely to display a column. |
| pin to types / field limits | selected issue type IDs; Issues without a type; no pins; current 25 owner fields/100 select options/10 pins per type/50 total Project fields | Pin relevant fields so creation/view surfaces show them automatically; unpinned fields remain available through Add field and Projects. Limits differ from Project single-select options. | Read pin mapping for typed and untyped issues and count all system/issue/local Project fields; verify target-host limits before creating. |
| data_type / typed value | text; number; date; single_select; multi_select where supported | Select type from actual schema; use date for dates and number for arithmetic, not formatted strings. | Inspect supported owner and Project types separately; round-trip one permitted value of the selected type. |
| select options | stable ID; name; description; color; default where supported | Reuse IDs; rename in place when supported, never recreate populated options just to reorder or recolor. | Export affected values before change and compare option IDs and representative assignments afterward. |
| issue field values operation | add; set; delete; typed scalar or option IDs | Preserve unrelated values and distinguish adding multi-select members from replacing the selected set. | Read all current issue-field-values and compare exact changed field and option IDs. |
| intake population | sidebar; API; Actions; supported Project column | Do not promise template or URL prefill of native issue fields; those are currently unsupported in the consulted product guide. | Verify creation path then read the issue fields, not Markdown text that happens to have the same heading. |

**Official sources:** [adding-and-managing-issue-fields](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-and-managing-issue-fields), [issue-field-values](https://docs.github.com/en/rest/issues/issue-field-values), [issue-fields](https://docs.github.com/en/rest/orgs/issue-fields), [about-issue-fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-issue-fields), [managing-issue-fields](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-fields).

**Pitfall:** A community preview announcement is not proof of API type support or entitlement. Inspect the exact host schema and actual rendered field.

**Community observation** (not current-platform proof): [202760](https://github.com/orgs/community/discussions/202760) — July 2026 community post describes multi-select preview; treat as discovery, not authority for every host or endpoint. **Official/current check:** Current issue-field-values examples include multi_select; bundled UpdateProjectV2FieldInput also exposes multiSelectOptions. Live entitlement remains untested.

### `issue-state-and-relations` — Completion, hierarchy, blockers and identity

**Capability IDs:** `issue-lifecycle`, `issue-subissues`, `issue-dependencies`, `issue-related`, `issue-transfer-pin-duplicate`, `issue-linked-branches`, `issue-planning-status`.

**Applicability:** Issues with meaningful lifecycle; hierarchy/dependencies only where real decomposition/order exists.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| state / state_reason | open; closed; completed; not_planned; reopened where accepted | Close completed only with acceptance evidence; not-planned needs a decision reason; reopen the original issue for the same unfinished work. | Read state/state_reason and timeline; closing is not deployment verification. |
| parent / child order | issue database IDs; parent relationship; ordered sub-issues | Use one parent for decomposition, preserve child identity and ordering; avoid manufacturing hierarchy for unrelated work. | Read parent and child sides, all pages and final sibling order; current product limits are 100 children and eight levels. |
| blocked_by / blocking | directed native issue dependencies | Record A blocked by B when B must finish first; parenthood and a mention do not establish dependency. | Query both directions and verify no self/cyclic/duplicate relationship accepted by the host. |
| related / duplicate | related edge; duplicate_of; mark/unmark duplicate | Link peers as related; point duplicates to the canonical issue and retain the reporter's reproduction details there by reference. | Read canonical URLs and relationship timeline; do not delete duplicate history. |
| transfer / pin | destination repository; pinned/unpinned | Transfer only after access/ownership consequences are understood; use pins for durable current entry points, not every issue. | Follow old URL, read new repository/number/ID, metadata and relationship preservation. |
| linkedBranch.repositoryId / name / oid | chosen repository; branch name; base commit | Start from observed default/base SHA unless task needs a release branch; link existing work before creating duplicate branches. | Read actual ref OID and issue linkedBranches; link does not substitute for a closing PR. |
| planning status | discovered status ID; duplicate reference where supported | Preview planning statuses may transition issue state; use only after discovering viewerCanSetStatus and available statuses. | Read status plus open/closed state and duplicate target; do not equate it to Project Status. |

**Official sources:** [issues](https://docs.github.com/en/rest/issues/issues), [adding-sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues), [issue-dependencies](https://docs.github.com/en/rest/issues/issue-dependencies), [creating-a-branch-for-an-issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue).

**Pitfall:** Removal of a hierarchy/dependency edge is not deletion of either issue. Native relationships need actual API/UI evidence, not a checklist in the body.

### `timeline-and-conversation-preservation` — Human conversation and durable evidence

**Capability IDs:** `issue-comments`, `issue-timeline`, `issue-artifacts`, `repository-history`.

**Applicability:** Every task involving past decisions, edits, triage or review follow-up.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| read model | issue body; paginated comments; timeline events; reviews and threads | Read all relevant streams before replying; issue body and last few visible comments omit decisions, force pushes, transfers and prior review outcomes. | Independently paginate nested connections; reconcile IDs/timestamps and retrieve referenced objects. |
| edit versus append | correct current body; new progress/decision comment; retain superseded links | Edit the canonical description to reflect current scope; append material decisions and corrections when authorized so reasoning remains chronological. | Compare prior content and edit history where available; retain earlier evidence URLs and authorship. |
| comment/reply location | issue conversation; PR summary; review thread reply; Discussion answer | Reply in the thread containing the question; distinguish implemented fix, justified disagreement, unresolved question and deferred follow-up. | Read thread root/reply IDs and resulting thread state; never claim a pending review was delivered. |
| notifications / mentions | direct mention; team mention; no mention; user subscription | Mention only relevant people when an authorized message needs their attention; do not silently change watch/subscription settings. | Inspect recipient and final posted location; API success is not proof the user read the message. |
| attachments / artifacts | canonical ID; immutable URL/ref; access-restricted resource | Preserve attachment identity and permissions; reference existing logs/files instead of re-uploading private content publicly. | Verify readable content with permitted audience and identify expiry; attachment presence is not content validation. |
| recovery after ambiguous write | reconcile by ID/body/context; retry missing write only | Avoid duplicate posts after timeouts; inspect recent author/timestamp/body and relationship events before retry. | Capture canonical ID/URL and distinguish already-applied from unapplied writes. |

**Official sources:** [timeline](https://docs.github.com/en/rest/issues/timeline), [comments](https://docs.github.com/en/rest/issues/comments), [users#usercontentedit](https://docs.github.com/en/graphql/reference/users#usercontentedit).

**Pitfall:** Git history is not conversation history; activity feeds are not complete audit logs. Loading an old thread in UI may collapse large portions.

**Community observation** (not current-platform proof): [5119](https://github.com/orgs/community/discussions/5119) — Long-running reports describe collapsed older activity and difficult navigation; exact UI behavior has changed over time. **Official/current check:** REST timeline and comment endpoints are separately paginated, so use their complete relevant pages rather than infer completeness from the rendered screen.

**Community observation** (not current-platform proof): [33551](https://github.com/orgs/community/discussions/33551) — Users seek issue/comment edit history through APIs and point to GraphQL. **Official/current check:** Inspect UserContentEdit connections and viewer permissions on the current schema; do not claim a comments list contains every revision.

### `pr-creation-and-linking` — PR intent, comparison base and connected work

**Capability IDs:** `pr-lifecycle`, `pr-linking`, `pr-templates`, `pr-stacks`, `pr-archival`.

**Applicability:** All code changes delivered through PRs; native stacks/archival only on supported hosts.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| head / base / draft | owner:branch; repository base branch; boolean | Discover existing PR before creating; choose correct target release/default branch and draft state from readiness. | Read head repo/ref/SHA, base ref/SHA and isDraft; inspect full diff against merge base. |
| title / body / maintainer_can_modify | current problem and result; validation and limits; boolean | Describe final scope and evidence; allow fork-maintainer edits only when contributor intent and repository trust permit. | Re-read rendered description and fork edit permission; retain rationale and linked decisions. |
| closing keyword / manual development link | closes/fixes/resolves #N; OWNER/REPO#N; manual same-repo link | Use closing intent only for fully satisfied issues targeting default branch; use plain references for partial work or release-target PRs. | Check development links before merge, issue state and timeline after merge; commit-only closing may omit PR sidebar linkage. |
| base retarget / branch rewrite | new base; merge update; rebase update | Recheck scope before retargeting; changing base can remove visible commits and make inline comments outdated. Preserve decision URLs and communicate material scope changes in authorized flow. | Compare old/new base/head SHAs, diff, review freshness and unresolved/outdated threads. |
| native stack / archival | detected stack relationship; archive/unarchive | Use native stack support only where available; archive is distinct from close, branch deletion and Project archive. | Read actual stack/base relationships or archived/state fields and timeline; do not simulate support with text and label it configured. |

**Official sources:** [pulls](https://docs.github.com/en/rest/pulls/pulls), [linking-a-pull-request-to-an-issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue), [changing-the-base-branch-of-a-pull-request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/changing-the-base-branch-of-a-pull-request).

**Pitfall:** A PR references the live head branch; pushing after review changes the material under review. Closing without merge does not mean delivered.

### `review-submission-and-threads` — Review decisions, anchors, pending state and resolution

**Capability IDs:** `pr-reviews`, `pr-review-comments`, `pr-file-view-state`.

**Applicability:** All review work; submitted comments are external messages and require task authorization.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| review.commit_id / event | observed head SHA; omitted event=PENDING; COMMENT; APPROVE; REQUEST_CHANGES | Bind evidence to the reviewed head. Draft/pending reviews are private; submit only the intended decision and explain actionable findings. | Read review ID, commit_id, state, submitted_at and comments; author cannot approve own PR. |
| inline anchor | commit_id; path; line/side; start_line/start_side; subject_type line/file | Anchor to an actual diff on the observed SHA; prefer current line/side coordinates, not deprecated positional guessing. | Re-read comment diff_hunk, original/current line and commit IDs; wrong anchor requires correction, not silent relocation. |
| reply and suggestion | in_reply_to root ID; suggestion block; batched application | Preserve original conversation; inspect suggestions as code, batch related accepted edits and verify new commits. | Read replies and resulting branch SHA; rerun affected checks after applying suggestions. |
| viewed files / diff settings | mark/unmark viewed; unified/split; ignore whitespace | Viewed is personal progress, not approval; inspect whitespace when meaningful and unmark changed files requiring another pass. | Read viewerViewedState as same viewer and current path/head; record what was actually reviewed. |
| thread.resolve / reopen | resolved; unresolved; outdated | Resolve after code/evidence addresses the finding or recorded agreement; outdated merely means anchor drift, not fixed. | Read isResolved/isOutdated and implementing commit or linked follow-up; preserve unresolved material objections. |
| dismissal.message / restrictions | required rationale; eligible actor | Dismiss only invalidated/unavailable-reviewer feedback with an explicit reason and policy authority; do not erase dissent to unblock merge. | Read dismissed review state and timeline rationale plus remaining effective review requirements. |

**Official sources:** [reviews](https://docs.github.com/en/rest/pulls/reviews), [comments](https://docs.github.com/en/rest/pulls/comments), [reviewing-proposed-changes-in-a-pull-request](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request), [dismissing-a-pull-request-review](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/dismissing-a-pull-request-review).

**Pitfall:** Review comments, issue-style PR comments and commit comments are different stores. Never respond to only the summary while missing inline threads.

### `merge-options-and-delivery` — Merge settings and asynchronous delivery

**Capability IDs:** `pr-merge`, `pr-auto-merge`, `pr-merge-queue`, `pr-update-revert-cleanup`, `pr-agent-merge`.

**Applicability:** Repositories accepting merges; queue/auto-merge/Agent Merge only where supported and justified by throughput.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| allow_merge_commit / allow_squash_merge / allow_rebase_merge | independent booleans | Follow existing history policy and effective branch rules; retain squash-only delivery where the repository policy requires it. Avoid introducing several methods without a reason. | Read repository flags and allowed methods in effective rules; inspect actual resulting commit topology. |
| squash_merge_commit_title / message | PR_TITLE or COMMIT_OR_PR_TITLE; PR_BODY or COMMIT_MESSAGES or BLANK | Prefer stable PR title plus reviewed useful body for a one-change PR; inspect generated message for accidental skip directives or sensitive diagnostics. | Preview final message and read resulting commit; verify expected CI ran on the merged SHA. |
| merge_commit_title / message | PR_TITLE or MERGE_MESSAGE; PR_BODY or PR_TITLE or BLANK | If merge commits are enabled, choose a useful durable description without dumping transient logs. | Read supported enum payload and final commit message; no configuration claim from preview alone. |
| merge.sha / merge_method | exact reviewed head SHA; merge/squash/rebase | Guard the merge against concurrent head changes; do not override required checks, outstanding review or queue to satisfy a local plan. | Re-read current head and gate state, then resulting merged flag, merge_commit_sha and base ref. |
| auto-merge / queue entry | enabled/disabled; selected allowed merge method; queued state | Enable only for reviewed intent and qualifying rules; enqueue/enable is pending work, not completion. | Poll meaningful state changes until merge/failure or handoff; inspect queue removal reason and merged commit checks. |
| update_branch.expected_head_sha / delete_branch_on_merge / revert | expected head guard; boolean; revert PR | Update only after inspecting divergence; delete truly merged disposable branches, retain long-lived branches. Revert through a tracked PR rather than history rewrite. | Confirm head after update, branch absent only when intended, and revert result against merged commit. |

**Official sources:** [configuring-commit-squashing-for-pull-requests](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests), [pull-request-merges](https://docs.github.com/en/pull-requests/reference/pull-request-merges), [pulls](https://docs.github.com/en/rest/pulls/pulls), [skip-workflow-runs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs).

**Pitfall:** Squash of a reused long-lived branch can replay prior commits in later PRs; start a fresh branch. Agent-merge eligibility must be checked separately.

**Community observation** (not current-platform proof): [179965](https://github.com/orgs/community/discussions/179965) — A path-trigger investigation traced missing Actions runs to skip directives copied into a squash commit message. **Official/current check:** Official skip-workflow and squash-message documentation explains the mechanism. Inspect final message and run checks; do not conclude squash inherently breaks path filters.

### `project-identity-access` — Project scope, access and item identity

**Capability IDs:** `projects-lifecycle`, `projects-access`, `projects-items`.

**Applicability:** Use Projects where the repository workflow calls for planning/tracking; public/private and organization/user ownership remain explicit choices.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| owner / number / node ID | organization Project; user Project; stable project ID | Reuse an existing matching Project; store owner/number/URL and node ID, never treat repository Projects flag as owner Project setup. | Read Project owner/ID/title/closed/public and linked repository list. |
| visibility / base permission / explicit collaborators | public/private; none/read/write/admin where available; users/teams | Choose least privilege for the real audience; repository access and Project access are separate. Draft titles and custom data can expose information. | Read base/explicit grants and inspect as intended reader; do not broaden repo access to make a Project readable. |
| item content type / IDs | Issue; PullRequest; DraftIssue; item ID distinct from content ID | Keep tracked work as native issues/PRs; draft ideas are appropriate before a repository is selected. Reuse existing item for content ID. | Paginate items and match content node ID/URL, including archived entries. |
| draft conversion | destination repository; issue metadata | Convert when the work has a responsible repository; preserve draft body, relevant fields and links, and check access before conversion. | Read returned issue URL and item content type/field values; do not create a second item for the same work. |
| item reorder / archive / delete | relative item order; archived flag; remove from Project | Use archive for recoverable history; deletion removes membership/field data, not the underlying issue. | Compare item IDs and saved values; restore archive when needed and verify representative fields. |

**Official sources:** [managing-access-to-your-projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects), [managing-visibility-of-your-projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-visibility-of-your-projects), [adding-items-to-your-project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project).

**Pitfall:** Successful item-add is not proof that every view will show it: filters, archives, pagination, permissions or a service incident can hide the item.

**Community observation** (not current-platform proof): [193194](https://github.com/orgs/community/discussions/193194) — April 2026 report shows successful CLI add and issue association while list/UI omit the item. **Official/current check:** Treat as incident evidence, not a current general guarantee. Read actual item by ID, paginate, inspect archive/filter and relevant repository access before retrying.

### `project-field-schema` — Project field configuration and value integrity

**Capability IDs:** `projects-fields`, `projects-field-values`, `projects-issue-fields`, `projects-multiselect`.

**Applicability:** Every Project; additional fields only when a real view, query or decision uses them.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| field data type / semantic scope | text; number; date; single select; iteration; supported multi-select; built-in issue fields | Reuse built-in title/assignee/type/milestone and shared issue facts; create local fields only for Project-specific planning. | Inventory field IDs/types and example values; distinguish issue fields from similar-name local fields. |
| Status options / order / default | discovered IDs; e.g. Todo/In Progress/Done; optional default | Retain established names/IDs and explicitly define completion. Default to intake/Todo only if all newly added work is truly queued. | Read options/default and a newly added versus existing item; default changes must not silently rewrite old work. |
| select label / description / color | option ID; label; meaning; available color enum | Give ambiguous statuses a usable entry/exit definition; preserve IDs across cosmetic changes. Colors supplement text, never replace meaning. | Compare option IDs before/after, sampled assignments and UI descriptions; inspect schema before option-list replacement. |
| field mutation payload | typed text/number/date/singleSelectOptionId/iterationId; supported multi-select values | Send exactly the relevant value member using discovered IDs; clearing a field is a separate intentional action. | Read the changed field value and verify unrelated values remain; preserve zero versus unset. |
| field deletion / option removal | keep; migrate; delete with affected-value inventory | Migrate populated values before any authorized deletion; export mapping because recreating the same name may not recover identity. | Compare all affected item values and saved-view/filter/workflow references; never prove safety using only one empty item. |

**Official sources:** [about-single-select-fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields), [about-text-and-number-fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-text-and-number-fields), [projects](https://docs.github.com/en/graphql/reference/projects).

**Pitfall:** Current single-select guide documents at most 50 options and an optional default for newly added items; target API/UI default support still requires discovery.

### `project-iterations` — Iteration schedules and rollover

**Capability IDs:** `projects-iterations`.

**Applicability:** Only projects with real cadence; continuous-flow work does not need artificial sprints.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| iteration configuration | start date; duration number; days/weeks | Match the actual team's planning cadence and timezone assumptions; do not auto-create indefinite schedules. | Read configuration plus automatically created iterations and exact IDs/dates. |
| iteration instance | title; startDate; duration; completed/active iteration ID | Preserve completed iteration identity and assignments; amend future dates deliberately rather than shifting historical interpretation. | Compare old/new date ranges and representative assigned work. |
| breaks | insertion point; break date range | Reflect actual holidays/pauses; inspect generated dates after insertion rather than assuming later schedule is unchanged. | Re-read all affected intervals and check no unintended overlap or shifted promised dates. |
| rollover | selected unfinished items; target iteration ID; preserve completed assignments | Move only unfinished selected work when agreed; keep prior commitment context in authorized update/history instead of silently rewriting all scope. | Compare item IDs/status and previous/target iteration assignments, including nonselected completed work. |

**Official sources:** [about-iteration-fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-iteration-fields).

**Pitfall:** An iteration field initially creates three iterations; a break initially follows the prior duration. Product defaults are starting data, not a planning decision.

### `project-saved-views` — View identity, shared configuration and safe filters

**Capability IDs:** `projects-views`, `projects-layout`, `projects-filters`.

**Applicability:** Every Project with distinct intake, execution or reporting audiences; avoid duplicate views with no distinct purpose.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| view name / layout / position | table; board; roadmap; saved view ID/order | Name views by the decision they support, e.g. Intake, Active work, Release roadmap; set default/first useful view for readers. | Read every saved view and reload shared URL, including ordering and unsaved-change indicators. |
| filter scope | repo/is/reason/assignee/label/type and custom field qualifiers supported in view | Store exact query, not a prose claim; include explicit repo/type/state where needed and quote multiword names. | Check representative included/excluded items and zero-value/unassigned cases; a filter is not an access boundary. |
| number/date/iteration comparison | > >= < <=; ranges; @current/@next where supported | Use date/iteration semantics of this surface, not issue-search syntax; check boundary and timezone behavior with known values. | Inspect edge dates and missing values; compare returned content IDs to expected fixtures/current known items. |
| view save / duplicate / reset / delete | saved shared changes; duplicate; discard unsaved; remove view | Save intended shared configuration explicitly; use a duplicate for experimentation and do not delete a view with active shared links casually. | Reopen as reader/new session and check persistent configuration and old navigation links. |
| API versus UI | current REST view endpoints; GraphQL view mutations; UI advanced controls | Discover actual supported request fields; REST creation and GraphQL view CRUD exist, so avoid blanket UI-only claims. | Read saved configuration through supported surface; use rendered verification for unsupported controls. |

**Official sources:** [managing-your-views](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/managing-your-views), [filtering-projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects), [views](https://docs.github.com/en/rest/projects/views).

**Pitfall:** Auto-add and auto-archive have narrower filter grammars than views. A valid view query cannot be copied blindly into automation.

### `project-layout-controls` — Table and board nested controls

**Capability IDs:** `projects-layout`, `projects-views`.

**Applicability:** For every table or board view that is part of the project workflow.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| visible fields / column order / card fields | selected field IDs; ordering; shown/hidden fields | Show owner, status and the facts needed for this view; hide unused noise while preserving stored data. | Reload saved view and inspect expected header/card fields and order. |
| board column field / visible columns / limits | single-select or iteration field; displayed values; column limit where offered | Use Status for execution, iteration for planning; hide columns only with an alternate way to find excluded work. Column limits are planning signals, not enforcement. | Verify field ID and value-to-column mapping; inspect hidden/no-value work and displayed limits. |
| group by / vertical_group_by | supported field; no grouping | Group by responsible person, parent or priority for a real triage question; dragging across groups can edit underlying fields. | Read fields after an authorized drag and verify parent/assignee effects rather than assuming presentation-only movement. |
| slice by | supported field; no slicing | Use for fast per-team/repository focus; title/reviewers/linked PRs are not supported slice fields in current guide. | Check slice plus saved filter intersection and clear selection to recover full view. |
| sort primary/secondary / direction | field IDs; ascending/descending; no sorting | Use priority/date order when that drives work, manual order for explicit ranking; sorted boards disallow manual ordering within columns. | Read saved sorting and known equal-value tie examples; distinguish drag-to-column mutation from reorder. |
| field sums | count; selected numeric fields | Sum only compatible measures; points are estimates and mixed currencies/units must not be combined. | Recompute a representative group from actual item values and compare displayed aggregate. |

**Official sources:** [customizing-the-table-layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-table-layout), [customizing-the-board-layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-board-layout).

**Pitfall:** Grouping a multi-assignee issue can show it in several groups; avoid interpreting row/card counts as unique work without checking IDs.

### `project-roadmap-controls` — Roadmap dates, markers and time windows

**Capability IDs:** `projects-layout`, `projects-views`.

**Applicability:** Projects with dates or iteration commitments; omit when no credible schedule exists.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| Date fields.Start date / Target date | chosen date or iteration field IDs | Bind to explicit planning fields, not guessed names; distinguish planned dates from actual completion evidence. | Read both mappings and compare bar boundaries to item values; inspect undated work separately. |
| Markers | iterations; milestone dates; item dates | Display only useful commitment/reference markers to avoid implying every date is a release deadline. | Inspect labels and actual source milestone/date values. |
| Zoom | Month; Quarter; Year | Choose the smallest window supporting the planning decision; preserve a useful shared overview. | Reload view and inspect expected time window and clipped/offscreen work. |
| roadmap drag / resize | changes start/target dates or selected iteration | Treat dragging as a real scheduling mutation; avoid accidental date changes during inspection. | Read changed field values and affected automation afterward; restore exact original values on accidental edit. |
| group / slice / sort / sums | supported fields and order; none | Apply the same data-integrity rules as other layouts; maintain access to ungrouped/undated items through a table view. | Compare item IDs across roadmap and table to explain omissions without inventing missing work. |

**Official sources:** [customizing-the-roadmap-layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout).

**Pitfall:** A visually complete roadmap can exclude undated items; never equate visible bars with all project scope.

### `project-event-workflows` — Event-driven Status transitions and issue closure

**Capability IDs:** `projects-workflows`, `projects-field-values`.

**Applicability:** Every Project, including apparently unconfigured Projects; defaults can already be active.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| workflow enabled / target field-option | per-workflow enabled flag; discovered Status option ID | Inventory every built-in event workflow before manual reconciliation; retain behavior only when transition matches the project's definition. | Read workflow trigger/enabled/target and verify a permitted representative transition. |
| item added → Status | disabled; intake/Todo option | Default new work to intake if untriaged; do not overwrite imported/customized existing work as a setup side effect. | Observe new item value, existing populated item and applicable field default together. |
| issue/PR closed → Done | enabled default; disabled; alternative supported option | Closed-not-planned is not successful delivery; decide whether one Done column intentionally includes cancellation or needs separate reporting. | Check reason and resulting Status for completed and not-planned examples; correct mismatches without reopening rejected work. |
| PR merged → Done | enabled default; disabled; supported option | Merge may be completion for library work, but deployed systems may still require QA/release. Define that boundary explicitly. | Read merged commit, item Status and downstream release/deployment evidence separately. |
| Status change → issue state | disabled; close issue on configured transition where supported | Enable only when board transitions truly authorize closing the issue; avoid circular/competing automation. | Read issue state/reason and both directions of workflow behavior; identify unexpected loops or last-writer wins. |
| reopen / ready / review-related events | discovered host workflows | Inventory actual available triggers and decide each applicability rather than assume all event workflows exist everywhere. | Read current workflow list/schema/UI and verify exact resulting option IDs after relevant event. |

**Official sources:** [using-the-built-in-automations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations).

**Pitfall:** Initialization enables closed→Done and merged→Done. A successful Status write can be immediately changed by another workflow; verify after automation settles.

### `project-auto-add` — Auto-add filters, backfill and execution identity

**Capability IDs:** `projects-auto-add`, `projects-actions`.

**Applicability:** For repository intake needing reliable Project membership; custom Actions only for unsupported native needs.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| auto-add.repository / filter | per-repository selector; is/label/reason/assignee/no subset | Scope to intended repository and item kind; exclude automation noise deliberately. Validate native grammar independently of view query. | Read enabled workflow and exact filter; inspect a matching and a nonmatching permitted item. |
| filter values / negation | is:open/closed/merged/draft/issue/pr; label names; reason; assignee; no:label/assignee/reason | Use supported values and negation (no does not support negation); quote labels. Do not invent arbitrary custom-field auto-add filters. | Preview/save and confirm actual matching content IDs; compare available grammar with current official guide. |
| workflow count / duplicate | plan-dependent 1/5/20 limits currently documented; unique filters | Reuse existing workflows; Free has one, Pro/Team five, Enterprise twenty in current guide. Record plan gate rather than adding a token workaround silently. | Read actual count and entitlement; verify each repository selector and duplicate filter. |
| existing backlog | explicit paginated backfill; future matching creates/updates | Enabling auto-add does not backfill existing matches; reconcile backlog as a separate authorized operation preserving item values. | List source issues/PRs, compare content IDs to active/archive membership and add only missing items. |
| custom Action identity | installation token or authorized user credential; least Project/repository permissions | Repository GITHUB_TOKEN generally cannot stand in for owner Project write access; prefer a scoped App only when native workflow is insufficient. | Inspect workflow/token permissions without exposing secrets; verify membership and typed field values after execution. |

**Official sources:** [adding-items-automatically](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically), [automating-projects-using-actions](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions).

**Pitfall:** Creating a dummy issue to test automation sends real notifications and is not a read-only check; use existing evidence or an explicitly authorized representative fixture.

### `project-auto-archive` — Retention filters, existing matches and restoration

**Capability IDs:** `projects-auto-archive`, `projects-items`.

**Applicability:** Projects with a defined retention policy; keep disabled if release/QA remains open after issue closure.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| auto-archive.enabled / filter | disabled; enabled; is/reason/updated only | Prefer disabled until retention criteria are agreed; custom Status is not supported in this automation grammar. | Read exact saved filter and enabled state; enumerate matching existing items before enable. |
| retention clock | updated relative-date expression supported by current surface | Do not call last-updated age closed-age; comments/labels/assignees/milestones/field changes can reset update time. | Test known boundary examples in this automation surface; record literal filter rather than translating comparator from memory. |
| existing matches | immediately eligible after enable, potentially delayed processing | Inventory affected IDs/values first; unlike auto-add, auto-archive also processes old matching items. | Compare before/after active and archive IDs and counts until processing settles. |
| archive versus capacity | recoverable archive; Project membership deletion | Archive keeps custom data and supports restore but still counts toward current 50,000 combined item limit. Deletion needs a separate retention decision. | Read archive entries and restored values; verify underlying issue remains unchanged. |
| recovery | disable workflow; restore selected archived item IDs | Stop faulty automation first, restore exact affected items and values, then correct filter before re-enabling. | Re-read saved filter and representative restored fields; inspect re-archival to detect remaining bad criteria. |

**Official sources:** [archiving-items-automatically](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically), [archiving-items-from-your-project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/archiving-items-from-your-project).

**Pitfall:** Historical Community reports describe invalid filters partly executing; do not present that old bug as current. Validate native grammar and preserve a restoration inventory.

**Community observation** (not current-platform proof): [36466](https://github.com/orgs/community/discussions/36466) — Historical reports include unsupported Status filters, unexpected archive effects and confusing recovery. **Official/current check:** Current guide restricts filters to is/reason/updated and documents preservation/restoration. Use those verified limits rather than obsolete 1,200-item claims.

**Community observation** (not current-platform proof): [17085](https://github.com/orgs/community/discussions/17085) — Users ask for closed-date retention and suggest updated-based workarounds. **Official/current check:** Updated and closed time are different clocks; do not repeat a community workaround as exact closure retention.

### `project-insights-and-updates` — Charts, historical interpretation and project health

**Capability IDs:** `projects-insights`, `projects-updates`.

**Applicability:** Projects where someone consumes the report; do not create decorative metrics or post updates without authorization.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| chart filter / layout / X-axis / group | supported chart types; selected category field; Time for historical chart; group or None | Name the actual decision and denominator; chart filters are their own saved configuration, not inherited proof from an open view. | Open saved chart and compare included content IDs/known sample; verify reader access. |
| Y-axis / numeric field | count; sum; average; minimum; maximum; selected numeric field | Count unique work or aggregate compatible numeric units; never equate estimate sums with actual labor or outcome value. | Recompute sample groups including missing/zero values and inspect saved aggregate and field mapping. |
| historical chart state / retention | Time axis; Open/Completed/Closed pull requests/Not planned | Historical charts track native issue/PR states, not arbitrary local Status history. Insights does not track archived or deleted items, so retention affects reporting. | Compare known state transitions and active/archive membership; do not report archive-filtered history as all-time delivery. |
| status update.status | ON_TRACK; AT_RISK; OFF_TRACK; INACTIVE; COMPLETE | Set overall project health from evidence, separately from issue open/closed and item Status; meaningful bad news must remain visible. | Read saved update ID/status and chronological update history. |
| status update.startDate / targetDate / body | dates; Markdown message; prior values as form defaults | Include reason, evidence and next decision; inspect inherited previous dates rather than republish stale commitments. Append meaningful updates, edit only corrections. | Read resulting dates/body and prior entries; templates cannot receive updates and subscriptions can notify readers. |

**Official sources:** [configuring-charts](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/configuring-charts), [about-insights-for-projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects), [sharing-project-updates](https://docs.github.com/en/issues/planning-and-tracking-with-projects/sharing-project-updates), [projects](https://docs.github.com/en/graphql/reference/projects).

**Pitfall:** Chart controls may require UI even when field/view APIs exist. Do not claim chart configuration from project item listing or API capability indexing.

### `project-copy-template` — Template/copy fidelity and initial conditions

**Capability IDs:** `projects-templates`, `projects-lifecycle`, `projects-access`, `projects-workflows`.

**Applicability:** Repeated project patterns; do not create a template where one Project already suffices.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| copy owner / title / draft selection | organization/user owner; new title; copy draft issues checkbox | Choose destination deliberately and copy example drafts only when useful; inspect template contents for confidential planning text. | Read new owner/title/ID and copied draft bodies/values. |
| copied configuration | views; custom fields; draft field values; workflows except auto-add; insights | Treat copied settings as a starting point, not desired final state; inherited automation can immediately affect new work. | Compare each copied component and field-option mappings independently with source snapshot. |
| not copied | original issue/PR items; collaborators; team/repository links; auto-add workflows | Recreate only applicable omitted relationships and intake workflow under authorized access scope; backfill existing work separately. | Read membership, grants, links and enabled auto-add on destination; source configuration proves nothing about destination completion. |
| organization template / recommendations | mark/unmark template; recommended template list | Curate only usable templates with documented fields and workflow expectations; avoid promoting an unverified personal experiment. | Read template status and organization recommendation visibility as intended member. |

**Official sources:** [copying-an-existing-project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/copying-an-existing-project), [managing-project-templates-in-your-organization](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-project-templates-in-your-organization).

**Pitfall:** Copied field/option IDs are destination identities; never apply source item/field IDs to the new Project by name alone.

### `discussion-categories-and-forms` — Discussion purposes, category formats and intake

**Capability IDs:** `discussions-lifecycle`, `discussions-organization`.

**Applicability:** Public/community projects or genuinely cross-repository decisions; small internal work can stay in issues.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| repository versus organization source | repository Discussions; designated organization source repository | Keep repo-specific support near code; organization-wide discussions need explicit source-repository governance and access review. | Read enabled surface, source repository and moderator roles; inspect audience before publishing. |
| category.name / emoji / description / format | open-ended; Q&A; announcement; Polls where offered | Use Q&A for answerable support, open-ended for design, announcement for maintainer-origin updates. Inspect current Polls control rather than treating docs prose inconsistencies as universal support. | Read category IDs and actual format/answerability; announcement posting has stricter permissions than replies. |
| section membership / category rename/delete | one section per category; rename in place; Delete & Move target | Reuse category IDs; preserve navigation and discussion history. Deleting a category moves discussions to a chosen existing category. | Compare IDs/format and counts, destination and old shared links; inspect forms after slug changes. |
| category form path / top-level schema | .github/DISCUSSION_TEMPLATE/<category-slug>.yml; body/labels/title | Match category slug exactly; use supported controls, not issue-form assignee/projects/type top-level keys. | Open actual category composer on default branch and validate required/non-Markdown fields without posting. |
| labels / pins | existing repository labels; global/category pins; four per scope | Pin actionable entry points with a moderator/response owner; avoid a duplicate label taxonomy. | Read pin location, appearance and rendered routing links; global pins and category pins are distinct. |
| category movement / poll intake | recategorize eligible discussion; Polls category cannot move to/from | Select a valid format before intake; do not promise migration of a normal topic into a poll by changing category. | Read current category/format and eligible destinations; preserve original topic links. |

**Official sources:** [managing-categories-for-discussions](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions), [syntax-for-discussion-category-forms](https://docs.github.com/en/discussions/managing-discussions-for-your-community/syntax-for-discussion-category-forms), [about-discussions](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions), [managing-discussions](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions).

**Pitfall:** Enabling Discussions creates a surface, not a staffed support process. Define who monitors unanswered questions and how decisions become tracked work.

### `discussion-response-and-moderation` — Answers, polls, conversions and moderation history

**Capability IDs:** `discussions-lifecycle`, `discussions-answers`.

**Applicability:** Every authorized discussion interaction; high-impact moderation requires exact task scope.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| answer selection | mark answer; unmark; Q&A eligible comment | Mark a correct reusable solution with supporting explanation; an accepted answer is not proof a linked implementation shipped. | Read answer ID/body/author and category answerability; retain unresolved follow-up. |
| reply hierarchy / poll vote | replyToId; pollOptionId; viewerCanVote/viewerHasVoted | Respond to the right question; inspect existing viewer vote and options. Voting is personal participation, not setup. | Read reply parent and viewer vote state/counts; never cast a vote merely to test a feature. |
| poll content | discussion title/body; question; at least two options in Polls composer | Choose clear distinct options and explain how feedback informs a decision; do not invent supported close dates, anonymity or binding voting rules. | Preview composer and read poll question/options/order after an authorized creation; creation API support needs its own discovery. |
| lock / close / reason / allow reactions | lock/unlock; close/reopen; reason supported by host; reaction toggle | Prefer explanation and narrow moderation; lock restricts interaction while preserving content. Do not silence technical disagreement. | Read locked/closed/reason and rendered notice; confirm permitted moderators and reactions separately. |
| issue → discussion conversion | category ID; original issue and resulting discussion IDs | Use only when conversation rather than committed work is appropriate; explain routing when messaging is authorized and snapshot original history first. | Read both objects, canonical links, authors, all comment/reaction pages and issue closure/lock behavior; reconcile timeout before retry. |
| create issue from discussion | linked new issue in responsible repository | Track accepted actionable work while retaining the discussion decision trail; do not assume participants/subscriptions or every metadata field move. | Read both cross-links and preserve original authors and decision context. |
| transfer discussion | eligible same-owner destination repository or organization source repo | Destination creation permission is required; private-to-public and announcement transfers are unsupported. Review audience before any allowed transfer. | Read destination repository/category/access and retained comments/links; reconcile original and returned discussion IDs. |
| minimize / delete | classification and restore; irreversible deletion | Use least destructive appropriate moderation with reason; deletion is not a substitute for marking superseded information. | Read minimized state or exact deleted ID and preserve required moderation rationale without redistributing sensitive content. |

**Official sources:** [moderating-discussions](https://docs.github.com/en/discussions/managing-discussions-for-your-community/moderating-discussions), [participating-in-a-discussion](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/participating-in-a-discussion), [managing-discussions](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions), [discussions](https://docs.github.com/en/graphql/reference/discussions).

**Pitfall:** Community conversion threads contain conflicting claims and historical incidents. Current official conversion flow exists; do not repeat a claim that conversion is universally unavailable.

**Community observation** (not current-platform proof): [152627](https://github.com/orgs/community/discussions/152627) — February 2025 conversion-to-404 incident was reported fixed by GitHub staff in March 2025. **Official/current check:** Current moderation docs describe conversion; verify each resulting object and retained comments rather than treat this as a present platform outage.

**Community observation** (not current-platform proof): [3197](https://github.com/orgs/community/discussions/3197) — Maintainers describe user confusion about converted issues becoming closed/locked and request clearer traceability. **Official/current check:** Use current official flow plus actual post-conversion reads; communicate destination and preserve the old decision trail when authorized.

**Community observation** (not current-platform proof): [2952](https://github.com/orgs/community/discussions/2952) — Long history includes contradictory conversion advice and assumptions about participant/watch preservation. **Official/current check:** Official current docs, not a recent unverified forum reply, determine supported flow; inspect destination authors/comments/access independently.

### `wiki-publication-history` — Wiki content, publication, permissions and discoverability

**Capability IDs:** `wiki-pages`, `wiki-navigation`.

**Applicability:** Projects needing a Wiki; separate site/Pages only when user need justifies it.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| enabled / editing audience | has_wiki; collaborators-only; public editing on eligible public repos | Default to repository writers for project policy/docs; public editing is a governance choice, not a completeness requirement. | Read repository flag and actual Wiki access control; public/private visibility follows repository audience. |
| source repository / publication ref | OWNER/REPO.wiki.git; actual wiki branch and SHA | Clone/fetch Wiki separately; preserve other contributors' commits and compare source wiki/ files before publishing. | Compare remote before/after commit SHA and rendered pages; source files alone are not proof of publication. |
| page title / filename / markup | supported file extension; stable page slug; relative links | Keep page naming stable and explicit; avoid filesystem case collisions and check renamed-page backlinks. | Render pages and follow links on GitHub, inspect separate Wiki Git log and page history. |
| navigation | Home; _Sidebar.<ext>; _Footer.<ext> | Provide install/use/config/troubleshooting navigation based on actual project scope; footer can carry source/version context. | Open every navigation destination, heading anchor and asset as intended reader. |
| change message / correction / recovery | meaningful commit; revert commit; merge remote changes | Record what changed and why; recover with a new corrective commit rather than force-overwrite others' Wiki work. | Read remote ancestry and page revision, compare preserved unrelated pages and restored content. |
| indexing / size constraints | search-engine eligibility; current soft file limit | Do not promise search-engine discovery for a small Wiki; current guide requires 500 stars and restricted public editing, with soft 5,000-file limit. | Inspect actual audience/search behavior; consider Pages only if indexing or size is an actual requirement. |

**Official sources:** [about-wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis), [adding-or-editing-wiki-pages](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages), [creating-a-footer-or-sidebar-for-your-wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis/creating-a-footer-or-sidebar-for-your-wiki), [viewing-a-wikis-history-of-changes](https://docs.github.com/en/communities/documenting-your-project-with-wikis/viewing-a-wikis-history-of-changes).

**Pitfall:** A main-repository pull request does not review/enforce separate Wiki pushes automatically; document the publication check and do not conflate branches.

### `search-and-discovery` — Search surfaces, query semantics and completeness

**Capability IDs:** `search-cross-github`, `search-code`, `search-issues-prs`, `issue-saved-views`.

**Applicability:** Discovery before every duplicate-sensitive operation; authoritative owning endpoints for final facts.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| code search surface | browser Code Search; REST legacy code search; local rg/git grep | Choose syntax for the actual engine; browser Boolean/regex/symbol features do not imply equivalent REST support. Use local Git for exact nondefault-revision inspection. | Record engine, repository and revision; retrieve matched file at immutable SHA before acting. |
| modern code query | repo/org/user; path/language/symbol/content; quoted strings; /regex/; AND/OR/NOT | Scope narrowly and escape literals correctly; a bare term can match path or content. Inspect actual engine limits before assuming exhaustive indexing. | Reproduce match locally at known revision and inspect excluded files/ref; empty search is not absence proof. |
| issue/PR query | is:issue/is:pr; state/reason; author/assignee; review/review-requested; linked; dates | Use explicit type and repository scope, native review qualifiers for review queues and dates for bounded investigations. | Retrieve every consequential issue/PR by ID and paginate authoritative collection for completeness. |
| Discussion query | repo/org; in:title/body/comments; category; is:answered/unanswered where supported; dates | Search existing answers/decisions before creating a new topic; category and issue-search grammars differ. | Open original discussion, current answer and full relevant replies; check date of claim and superseding staff response. |
| REST search result limits | per_page/page; incomplete_results; capped result windows | Treat results as indexed discovery; split disjoint date/repository ranges and reconcile total counts when cap or incompleteness appears. | Inspect incomplete_results and available pages, deduplicate IDs; use owning lists/GraphQL/Git if a full inventory is required. |
| saved queries / issue views | name/query; personal versus shared saved surface | Save useful triage/review queries with explicit audience; a personal saved search is not a shared Project view. | Reload as same viewer, inspect exact query and validate known expected item membership. |

**Official sources:** [understanding-github-code-search-syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax), [searching-code](https://docs.github.com/en/search-github/searching-on-github/searching-code), [searching-issues-and-pull-requests](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests), [searching-discussions](https://docs.github.com/en/search-github/searching-on-github/searching-discussions), [search](https://docs.github.com/en/rest/search/search).

**Pitfall:** Masked private objects, indexing lag, engine-specific limits and search caps mean zero results cannot establish absence or permission. Never use obsolete legacy limits as modern Code Search limits.

### `ruleset-targets-and-insights` — Ruleset scope, bypass and evaluation evidence

**Capability IDs:** `repository-rulesets`, `ruleset-insights`.

**Applicability:** Every repository audit; enforce only with repository policy, eligible plan and a tested contribution path.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| target / conditions | branch; tag; push; ref_name include/exclude; repository targeting at owner scope | Inspect inherited rules and select exact intended ref patterns, including default-branch symbolic selectors when supported; exclusion can silently remove protection. | Read ruleset IDs/source/enforcement plus effective rules for a representative matching and excluded ref. |
| enforcement | disabled; active; evaluate on eligible Enterprise plans | Disabled protects nothing; evaluate observes without blocking and needs a plan check. Preview broad new policy in evaluate where available before enforcement. | Read saved mode and rule-suite results; do not report evaluate as protected. |
| bypass_actors.actor_type / actor_id / bypass_mode | eligible role/team/App IDs; always; pull_request; exempt where supported | Preserve existing authorized exceptions and choose the narrowest useful mode; exempt does not run rules or create a bypass audit entry. | Read actor identity/mode and confirm no accidental broad role exception or App removal. |
| rule suite filters | ref; actor_name; rule_suite_result; time_period; pass/fail/bypass | Inspect operational failures and bypass use, not merely policy JSON. Check current endpoint filter enums and retention before querying. | Read suite ID, actor, ref, evaluation time and per-rule result; distinguish evaluate failures from blocked writes. |
| ruleset history / import-export | ruleset ID/version; export JSON; reviewed imported settings | Preserve baseline/version and review imported selectors/actor IDs; source owner IDs do not automatically mean destination identities. | Compare saved ruleset history, exact imported payload and effective target rules; revert with a corrective version. |

**Official sources:** [rules](https://docs.github.com/en/rest/repos/rules), [managing-rulesets-for-a-repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository).

**Pitfall:** Multiple rulesets can apply together with classic protection. A clear ruleset read does not prove the actor had no bypass or that another inherited rule did not apply.

### `branch-and-merge-gates` — Effective review/check requirements and compatible merge behavior

**Capability IDs:** `branch-protection`, `repository-merge-policy`.

**Applicability:** All protected default/release branches; single-maintainer workflows must not require impossible self-approval.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| required_pull_request_reviews | required_approving_review_count; dismiss_stale_reviews; require_code_owner_reviews; require_last_push_approval | Choose actual independent reviewer availability; stale/last-push rules must match team workflow. Zero peer approval may be intentional with required checks. | Read effective rules and representative current-head review states; inspect reviewer eligibility and outstanding changes requests. |
| review dismissal / bypass restrictions | dismissal_restrictions; bypass_pull_request_allowances; users/teams/apps | Retain narrowly justified emergency routes; never add the running agent as bypass to complete setup. | Compare actor IDs and enabled restrictions, and inspect subsequent dismissal/bypass evidence. |
| required_status_checks | strict; checks context/app_id; legacy contexts | Bind stable check names to expected Apps where supported; strict requires up-to-date branch, queue needs merge_group CI support. GitHub accepts success, skipped and neutral conclusions; a skipped required job does not prove its validation ran. | Compare rules to check-run names/App IDs and results on the relevant PR/test-merge or merge-group SHA. Whole-workflow filter skips leave checks pending; conditional/dependent job skips can allow merging. Require a terminal aggregate gate that evaluates prerequisite results and fails for missing or failed required validation; verify failure and skip cases before relying on it. |
| enforce_admins / restrictions | admin enforcement boolean; allowed users/teams/apps; block_creations where supported | Decide administrator policy deliberately; push allowlists are not equivalent to review bypass. Preserve existing emergency ownership. | Read protection and ruleset bypass together; verify effective actor rights without making a disruptive test push. |
| history / signatures / deletion | require_linear_history; required_signatures; allow_force_pushes; allow_deletions; lock_branch | Match legitimate release workflow and retain no-force/no-delete for protected history unless specifically justified. Locked branches and fork-sync settings need separate intent. | Read all flags and branch status; verify merge methods remain compatible with linear history. |
| conversation/deployment/security gates | required_conversation_resolution; required deployments; required code/secret/quality rules where supported | Require gates only when their producer/workflow exists and can complete; determine exact environment/tool thresholds from the schema and project policy. | Read named environments/tool thresholds and current-head gate results; do not disable failing gates as recovery. |
| repository merge flags | allow_merge_commit/squash/rebase; allow_auto_merge; allow_update_branch; delete_branch_on_merge | Keep methods compatible with effective rules; auto-update visibility is not auto-merge or branch freshness. Clean only disposable merged heads. | Read repository flags and PR merge box/effective rule methods; inspect final merge topology and branch cleanup. |
| merge queue parameters | check timeout; minimum/maximum group size; grouping strategy; merge method where offered | Use only when contention justifies it; inspect current host schema for exact names/enums and ensure queue check triggers exist. | Read queue rule payload and representative merge_group results, queue removal reasons and merged SHA. |

Option review: 2026-11-15. [official source 1](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks). Provider defaults above are separate from observed tenant values.

**Official sources:** [branch-protection](https://docs.github.com/en/rest/branches/branch-protection), [available-rules-for-rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets), [repos](https://docs.github.com/en/rest/repos/repos).

**Pitfall:** Classic protection update endpoints can replace nested objects and clear omitted policy. Snapshot and merge intended changes; one protected-branch endpoint cannot establish full ruleset enforcement.

### `notification-and-activity-state` — Personal watch choices, inbox triage and feed limitations

**Capability IDs:** `notifications-watch`, `notifications-inbox`, `activity-events`.

**Applicability:** Only the authenticated user’s authorized personal preferences; repository setup does not authorize following/watching or marking inbox items done.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| repository subscription | subscribed; ignored; custom event selection through supported UI | Preserve user preference; watch only requested event categories and distinguish ignored from simply not subscribed. Stars bookmark rather than subscribe. | Read subscription as same user plus UI custom categories; subscribers_count differs from legacy watchers_count/stargazers_count. |
| watcher list restrictions | admin/collaborator-only listing; deprecated user watched-repo endpoint | Current docs describe July 2026 restrictions and deprecated endpoint empty responses; do not infer nobody watches from an empty legacy list. | Check endpoint status/auth identity and direct repository subscription state. |
| inbox query | all; participating; since; before; repository; reason; UI custom filters | Choose smallest needed read window and paginate; inspect reason such as mention/review_request/assign rather than treating all notifications equally. | Read thread ID/subject/reason/unread/last_read_at and canonical owning object. |
| triage operation | read/unread; done; saved; unsubscribe | Read acknowledges visibility; done hides completed notifications, save retains attention, unsubscribe changes future delivery. Apply only explicitly intended selected threads. | Re-read selected thread and UI saved/done state; compare unaffected threads, and reconcile ambiguous writes before retry. |
| retention / subscription recovery | done retained five months; saved indefinitely; resubscribe | Inbox is not permanent project history; unsaving old notifications can make them disappear. Unsubscribe can be superseded by later mention or review request. | Preserve canonical issue/PR URLs for durable context and verify subscription after authorized recovery. |
| authentication / polling | classic PAT notifications/repo scopes per current notification docs; Last-Modified/ETag; X-Poll-Interval | Do not assume fine-grained/App tokens support notification endpoints. Respect server polling interval and conditional requests. | Inspect authentication compatibility and 304 semantics without exposing credentials; permission failure remains unknown state. |
| activity feed window | up to 300 events; past 30 days; latency 30 seconds to six hours | Use feeds for discovery, not real-time completion or complete audit history. Prefer owning issue/PR/commit state for consequential facts. | Record event ID/time and owning object evidence; honor ETag and X-Poll-Interval. |

**Official sources:** [watching](https://docs.github.com/en/rest/activity/watching), [notifications](https://docs.github.com/en/rest/activity/notifications), [events](https://docs.github.com/en/rest/activity/events), [managing-notifications-from-your-inbox](https://docs.github.com/en/subscriptions-and-notifications/how-tos/viewing-and-triaging-notifications/managing-notifications-from-your-inbox).

**Pitfall:** Personal inbox Done is unrelated to issue closure or Project Done; never complete work by clearing its notification.

### `community-personal-replies-and-moderation` — Reusable drafts, reversible hiding and temporary interaction limits

**Capability IDs:** `community-saved-replies`, `community-comment-minimization`, `community-interaction-limits`.

**Applicability:** Community repositories with real support/moderation needs; personal replies and broad restrictions require explicit scope.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| saved reply title / body / selection | personal title; Markdown body; create/edit/delete; insert and customize | Store generic accurate routing text and customize to the actual report; inserting a draft does not authorize sending. Current documented cap is 100 replies. | Reload personal reply settings and preview inserted draft; do not post a test reply. |
| minimizeComment.subjectId / classifier | ABUSE; OFF_TOPIC; OUTDATED; RESOLVED; DUPLICATE; SPAM | Pick a justified classification and preserve the discussion; disagreement or inconvenient findings are not abuse. Check actor/type eligibility first. | Read viewerCanMinimize/isMinimized/minimizedReason plus original comment link and rendered visibility. |
| unminimize / deletion distinction | restore hidden comment; delete separately authorized content | Use restoration when hiding was mistaken; minimized content still exists and cannot be treated as erased sensitive data. | Read restored state and inspect full thread; handle actual secret exposure through the applicable security process. |
| interaction scope / inheritance | repository; organization public repositories; user-owned public repositories | Choose the narrowest incident scope and inspect inherited limits before overriding; broad owner controls affect uninvolved contributors. | Read effective repo and owner restrictions and record actor, scope and expiry. |
| interaction limit / expiry | existing_users; contributors_only; collaborators_only; one_day/three_days/one_week/one_month/six_months | Prefer the shortest effective restriction consistent with authorized moderation; do not silently block ordinary reporters for routine setup. | Read limit and expires_at from owning endpoint and inspect class semantics; never validate by posting disruption. |
| remove / expire / blocked users | remove temporary limit; automatic expiry; separate account blocking | Restore normal participation after incident and keep rationale; removing a repository limit does not remove an inherited owner restriction. | Re-read repo/owner limit state and separate block lists where authorized; distinguish expired from inaccessible. |

**Official sources:** [about-saved-replies](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies), [issues](https://docs.github.com/en/graphql/reference/issues), [repos](https://docs.github.com/en/rest/interactions/repos), [orgs](https://docs.github.com/en/rest/interactions/orgs), [user](https://docs.github.com/en/rest/interactions/user).

**Pitfall:** No stable saved-reply CRUD API is established here; inspect current UI. Comment minimization, conversation lock, interaction limit and account blocking are separate controls.

### `profile-personal-presence` — Personal availability, bookmarks, featured work and following

**Capability IDs:** `profile-status`, `profile-star-lists`, `profile-content-pins`, `profile-follow-organizations`.

**Applicability:** Personal-account actions only when the user requests them; not mandatory repository setup.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| status content / scope | emoji; message; organizationId or public null | Preserve user wording and audience; avoid publishing private project details as status. Organization-scoped status is not an organization announcement. | Read emoji/message/organization and inspect rendering as intended audience. |
| status availability / expiration | limitedAvailability boolean; expiresAt timestamp; clear status | Set busy only for requested availability; use intended timezone converted to exact expiry rather than leave a temporary absence indefinitely. | Read indicatesLimitedAvailability/expiresAt and verify removal/expiry; personal status is unrelated to work-item Status. |
| star list name / description / membership | create/update/delete list; repository membership IDs; starring independently | Keep bookmark organization separate from follow/watch; preserve unrelated list memberships in updateUserListsForItem replacement operations. | Read list ID/content and repository star state separately; list deletion is not repository deletion. |
| profile README / pins | USER/USER README; up to six repositories/gists combined; pin order | Publish only user-approved profile content and intended public featured work; use valid account-named repository for README. | Read immutable README commit and public rendered profile/pin order; preserve existing selections. |
| contribution/profile visibility | public/private profile; private contribution display; achievements/activity options where offered | Treat as personal privacy choice; anonymized private activity is not permission to reveal private repository names. | Inspect profile as owner and public viewer; verify current UI rather than assume profile REST edits cover these settings. |
| organization following | follow/unfollow org; viewerIsFollowing | Follow only requested organizations; preview feature supplies public activity, not membership or repository access. | Read following relation as same viewer and inspect dashboard; no requirement to generate activity for a test. |

**Official sources:** [users](https://docs.github.com/en/graphql/reference/users), [personal-profile](https://docs.github.com/en/account-and-profile/concepts/personal-profile), [pinning-items-to-your-profile](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile), [following-organizations](https://docs.github.com/en/get-started/exploring-projects-on-github/following-organizations).

**Pitfall:** Personal starring, following, availability and profile changes can reveal preferences and should not be silently bundled with a repository audit.

### `sponsors-listing-onboarding` — Sponsors identity, eligibility and public listing

**Capability IDs:** `sponsors-listing`.

**Applicability:** Only an owner requesting fundraising; a public/open-source repository does not establish Sponsors eligibility or authorize enrollment.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| listing identity | authenticated personal account; sponsorableLogin organization | Select the actual beneficiary, authority and supported region/fiscal-host route; do not create an organization listing for a similarly named repository owner by assumption. | Read listing/account IDs, owner/admin role and enrollment/approval state. |
| profile fields / featured opt-in | bio; introduction; featured work; matching/featured preferences where eligible | Prepare accurate public purpose and benefits; owner decides marketing consent and funding language. | Read rendered listing and saved preferences; unpublished/draft differs from publicly approved listing. |
| onboarding personal/legal fields | residence; billing/tax/provider verification; fiscal-host details | Let account owner handle required legal/banking attestations and credentials; never infer those from GitHub profile geography or commit email. | Report exact outstanding setup gate without exposing tax/bank data; listing mutation alone is not completed onboarding. |
| publication / funding link | approved listing; draft setup; FUNDING.yml sponsor button | Add funding links only to real intended supported beneficiaries; distinguish external funding URLs from an active GitHub Sponsors listing. | Open public listing and repository sponsor target as intended reader; retain owner decision about platform selection. |

**Official sources:** [setting-up-github-sponsors-for-your-personal-account](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/setting-up-github-sponsors-for-your-personal-account), [setting-up-github-sponsors-for-your-organization](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/setting-up-github-sponsors-for-your-organization), [sponsors](https://docs.github.com/en/graphql/reference/sponsors).

**Pitfall:** Enrollment/profile setup does not authorize a payment, bank change, tier publication or newsletter.

### `sponsors-tier-configuration` — Amounts, recurrence, publication and benefit access

**Capability IDs:** `sponsors-tiers`.

**Applicability:** Approved Sponsors owner with a concrete benefit/price policy; tier creation is optional.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| amount / recurrence | amount in US dollars; isRecurring boolean; documented API range 1–12000 | Choose explicitly approved price and monthly versus one-time meaning; never confuse dollars with cents or interpret isRecurring as an arbitrary billing scheduler. | Read amount/currency/recurrence from returned tier and actual checkout; current API schema defines valid range. |
| description / welcome message | public perks; post-payment instructions | Promise only deliverable benefits, avoid private credentials in broad welcome text, and document entitlement expectations. | Preview public and purchaser-facing text and check instructions/links. |
| publish / retire | draft by default in createSponsorsTier; publish true/false; retire tier | Review concrete tier before publication. Published prices cannot be edited; retire and create a new tier for a new price. | Read published/retired state and remaining active sponsorships; retirement does not cancel existing sponsors. |
| repository benefit | organization-owned private repository ID/name; no repository benefit | Adding a benefit grants read-only access to sponsors and requires explicit access authorization; do not attach source or customer data accidentally. | Verify exact repository owner/visibility and tier benefit, plus current entitlement policy without creating a paid test sponsorship. |
| tier limits | up to ten published one-time; up to ten published monthly | Reuse meaningful existing offers rather than create redundant tiers; keep retired options visible in historical reporting. | Count active published tiers by recurrence and inspect retired-tier subscribers separately. |

**Official sources:** [managing-your-sponsorship-tiers](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers), [sponsors](https://docs.github.com/en/graphql/reference/sponsors).

**Pitfall:** Existing sponsors can remain on a retired tier. Do not delete/replace historical tier identity to make the public price list look tidy.

### `sponsors-commitments-and-preferences` — Payer intent, bulk partial outcomes and sponsorship privacy

**Capability IDs:** `sponsors-transactions`, `sponsors-preferences`.

**Applicability:** Only explicit sponsorship instructions naming payer, beneficiary, amount, recurrence and intended visibility.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| sponsorship payer / beneficiary / tier | sponsorId/login; sponsorableId/login; tierId or allowed custom amount | Resolve exact accounts and a current valid offer; do not charge a personal account when organization funding was intended. | Read account/tier IDs and current sponsorship before mutation; checkout fees/tax/payment details require current verification. |
| one-time / recurring commitment | approved amount; recurrence; payment/renewal state | Repository setup and recommendation do not authorize spending. Match the explicitly requested commitment and inspect immediate/prorated effects before submission. | Read resulting amount, recurrence, payer, beneficiary and active/pending status; financial mutation timeout requires reconcile-before-retry. |
| bulk sponsorship results | per-beneficiary input; individual success/error results | Treat batch as potentially partial, never all-or-nothing; preserve successful commitments and retry only missing authorized ones. | Read every beneficiary relationship and error individually, compare total approved versus committed amounts. |
| change / cancel | upgrade; downgrade; cancelSponsorship; retired tier retained | Apply requested effective change with current billing semantics; cancellation does not prove refund or immediate entitlement end. | Read resulting tier/state and billing effective date; preserve history of previous commitments. |
| privacy / email preferences | PUBLIC; PRIVATE where current schema supports; receive email updates boolean | Make public identity and update consent deliberate personal choices; private sponsorship does not mean beneficiary sees no information. | Read actual sponsorship preference fields and public appearance; never publish identity merely to test visibility. |
| connected platform | Patreon linkage or documented connected sponsorability preference | Connect only an explicitly selected owned account and inspect permission scope; linkage does not create a paid sponsorship. | Read linkage/preference state and retain external-provider limitations; do not claim payment from a connected badge. |

**Official sources:** [sponsors](https://docs.github.com/en/graphql/reference/sponsors), [about-sponsorships-fees-and-taxes](https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/about-sponsorships-fees-and-taxes), [managing-your-sponsorship](https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/managing-your-sponsorship).

**Pitfall:** Current billing/provider terms are changeable. Read the actual checkout/account flow before any authorized commitment and keep sensitive financial data out of public issues.

### `sponsors-reporting-and-campaigns` — Sponsor history, exports and referral metadata

**Capability IDs:** `sponsors-analytics`.

**Applicability:** Sponsors owners requesting financial/activity reporting; exports contain personal/financial information.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| sponsor filters / activity window | active or retired tiers; date range; new/change/cancellation activity | Separate active sponsors, past sponsors, payments and payouts; distinguish cumulative commitment from settled receipts. | Read account/timezone/date/currency and reconcile paginated source rows to displayed totals. |
| export format / date / delivery | CSV; JSON; supported date window and delivery destination | Export only requested scope to intended private destination; initiating emailed export is an external delivery action requiring authorization. | Verify requested export fields/window, actual received file and row totals; record pending versus completed export. |
| referral metadata syntax | metadata_KEY=value; alphanumeric/dash/underscore; at most ten pairs | Use non-sensitive short campaign codes, never email addresses or secret identifiers in public URLs. Whitespace/invalid characters can produce 404. | Check resulting URL and export metadata key after permitted transaction; keys truncate at 25 chars and values at 100 per current guide. |
| lifetime / revenue interpretation | authorized lifetime value; currency; transaction/payment status | Use financial definitions explicitly; sponsorship totals and estimated next payout are not recognized revenue or a tax report. | Reconcile refunds/fees/date window with account dashboard and payout receipts when applicable. |

**Official sources:** [viewing-your-sponsors-and-sponsorships](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/viewing-your-sponsors-and-sponsorships), [sponsors](https://docs.github.com/en/graphql/reference/sponsors).

**Pitfall:** Export access does not authorize publishing sponsor identities or payment details in a public Wiki/Project.

### `sponsors-newsletters-and-delivery` — Recipient scope, sender identity and publish boundary

**Capability IDs:** `sponsors-newsletters`.

**Applicability:** Only explicit instructions to contact sponsors; preparing a draft alone does not authorize sending.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| recipients | opted-in sponsors; all eligible tiers; selected tier IDs | Match requested audience and current opt-in; do not bypass consent with copied sponsor email lists. | Read selected tier recipients and current eligibility before publish; distinguish tier names from stable IDs. |
| subject / body / sender | draft subject/message; personal primary email or noreply based on privacy; organization noreply | Prepare concrete reviewed content and working links; note personal sender exposure when email privacy is off. | Preview sender/subject/body/links and target account in dashboard without sending test mail. |
| draft versus Publish | unsent draft; published email update | Publish sends mail and needs an explicit messaging instruction; repository release/setup authority alone is insufficient. | Read publication/sent history and exact target scope; absence of send evidence must remain draft/unknown. |
| ambiguous delivery recovery | inspect newsletter history first; avoid duplicate Publish | A timeout can occur after sending; do not retry the broadcast before reconciling history and timestamps. | Capture update ID, publication time and recipient tier scope; report uncertainty rather than claim all recipients received/read mail. |

**Official sources:** [contacting-your-sponsors](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/contacting-your-sponsors).

**Pitfall:** Published/sent means provider acceptance/history, not proof every recipient received or read the message.

### `sponsors-payouts-and-goals` — Banking boundaries, estimated payouts and fundraising targets

**Capability IDs:** `sponsors-payouts`, `sponsors-goals`.

**Applicability:** Sponsors owners managing their own fundraising; goals are public owner decisions and bank changes require exact authority.

| Nested setting / operation choice | Values | Decision rule | Verification / recovery |
| --- | --- | --- | --- |
| payout account / status | past payout; estimated next payout; holds/provider state | Read correct beneficiary/provider and distinguish estimated, pending and paid; never equate incoming sponsorship with completed payout. | Match amount/date/currency and account history to actual receipt where available. |
| bank/fiscal-host management | supported Stripe Connect flow; fiscal-host support route | Owner handles bank/legal verification; fiscal-host accounts cannot directly edit payout information through the same control. Never paste bank/tax data into repository logs. | Inspect provider/account gate and resulting secure status only; record support handoff as unresolved. |
| receipt export | PDF payout receipts for supported Stripe Connect accounts | Export only required receipt to the authorized private destination; respect provider-specific availability. | Open actual receipt and match account/payout amount/date; dashboard display alone is not exported file evidence. |
| goal type / target / description | Number of monthly sponsors; Sponsorships a month; one active goal | Select an owner-approved measurable target and explain funded work accurately; avoid implying contribution guarantees. | Read live goal type/target/text and public progress; only one simultaneous goal is supported in current guide. |
| goal edit / remove / share | update target/text; remove goal; copy/embed link | Preserve rationale for target changes and publish/share externally only when requested; progress is not recognized revenue. | Re-read public goal after update/removal and inspect embed destination; do not send promotion as setup. |

**Official sources:** [managing-your-payouts-from-github-sponsors](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-payouts-from-github-sponsors), [managing-your-sponsorship-goal](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-goal).

**Pitfall:** Payout management is provider/account work, not repository administration. Do not claim settled revenue, tax treatment or completed banking verification from GraphQL metadata.

## Recovery and evidence contract

Before consequential bulk changes, snapshot IDs, selected values, associations, applicable filters and current head/revision. Re-read on ambiguous failure; do not repeat a successful create/post merely because a subsequent read used the wrong filter or identity. If automation changed too much, disable it before restoring data. Never delete/recreate populated fields/options to make a desired-state script look idempotent.

For setup acceptance, compare an existing customized object and a newly created object when creation is authorized, including unchanged unrelated content. Without authorized mutations, report the corresponding write/read-back scenario as untested. Include a new item, old matching item and excluded item in automation reasoning: auto-add and archive deliberately have different backlog semantics. Verify closed-not-planned, merged-but-not-released, reopen, missing metadata and archived-item cases when they apply.

Official-documentation support, indexed operation/schema support, live read evidence, live mutation evidence and human acceptance are separate evidence levels. This research supplies the first two selectively; it supplies no target mutation evidence. Advanced/preview controls, personal saved surfaces, chart mutation APIs and rendered UI persistence still require host-specific inspection. Preserve these gaps explicitly instead of claiming every option is configured.
