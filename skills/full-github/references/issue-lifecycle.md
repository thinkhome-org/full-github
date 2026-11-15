# Issues as an ongoing collaboration record

Reviewed against GitHub.com documentation on 2026-11-15. Read this before creating or updating tracked work, together with [history-interaction.md](history-interaction.md) and [collaboration-options.md](collaboration-options.md). A catalog entry proves discovery; it does not prove this workflow was followed.

## Required operating behavior

Use a live issue for substantial work. Read its description, all relevant comments and complete timeline before acting. Preserve the reporter's words, evidence, authorship and existing links. Inspect current owner/type/labels, shared field values, Project items/status, milestone, parent/children, dependencies, artifacts and linked development before filling gaps. Read every page or record the inventory as incomplete.

Keep the description as the current scope and acceptance criteria. **Add a new comment for each material progress checkpoint, changed decision, blocker, review response and delivery result. Do not repeatedly replace the issue body or the first comment to simulate a conversation.** A summary edit can accompany a comment, but cannot replace it. Fix small typos in your own text when useful; preserve consequential changes with a new explanation and source link. Never edit another person's comment as routine progress reporting.

Use these checkpoints when their event occurs; combine adjacent events into one useful update instead of posting empty heartbeat comments.

| Event | New timeline comment must contain |
| --- | --- |
| Work starts | Agreed scope, proposed steps, ownership and intended acceptance evidence. |
| Material finding or scope change | What was observed, its evidence, consequence and superseded decision if any. |
| Blocked or needing a human decision | Exact blocker, attempted recovery, focused question and independently continuing work. |
| Ready for review | Linked PR/commit, tests, remaining limits and what reviewers should inspect. |
| Delivered | Actual merged commit/release/deployment/docs links, verification result and unfinished work. |

Use `issues/create-comment` with a JSON body file containing `body`, or `gh issue comment ISSUE --body-file FILE`. Read back the returned comment ID/body/author/URL. After a timeout, look for the attempted comment before retrying. Do not use `issues/update-comment`, `gh issue comment --edit-last`, or an upserted bot summary for progress checkpoints. Stable bot summaries may coexist only when separately identified and chronological updates remain intact. [REST issue comments](https://docs.github.com/en/rest/issues/comments).

Issue comments are a chronological conversation; the issue-comment API has no nested `reply_to` or thread-parent argument. Link the exact comment being answered and quote only the relevant sentence. Use a separate linked issue for independently owned work, a Discussion with replies for open-ended topics, and PR review threads for line-specific review. Preserve their links in the issue. Do not claim nested issue reply threads were configured. [Comment API](https://docs.github.com/en/rest/issues/comments), [Discussion participation](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/collaborating-with-maintainers-using-discussions).

## Reconcile every sidebar control

For every row, use it when it serves this work; otherwise retain an explicit reason in the work's applicability record. Blank controls alone do not prove an omission, but an unexamined control cannot be marked complete. Do not invent dates, severity, ownership or relationships to make a sidebar look full.

| Control | Required decision and read-back |
| --- | --- |
| Assignees | Identify the actual accountable actor; use only assignable users and verify returned logins. Delegated agent execution does not imply assigning unrelated humans. |
| Labels and type | Read available owner/repository taxonomy. Set the appropriate native type in addition to relevant labels; a bug label is not an issue type. Preserve unrelated labels and existing type choices unless correcting them with a reason. |
| Shared issue fields | Read definitions/options and existing issue values; choose valid native Priority/Effort/date values when the work provides a basis. Use field IDs and exact option names for REST, node/option IDs for GraphQL as the schema requires. Record a genuine unknown instead of inventing a commitment. |
| Projects | Add the actual issue to the intended owner Project; read its item ID and field values, then maintain Status with real progress. A repository Project tab and issue open/closed state are separate. |
| Milestone | Use an existing delivery milestone when a real release/scope exists. Verify the issue's milestone number and target; do not fabricate a release/date for unplanned intake. |
| Relationships | Check parent, children, blocking and blocked-by separately. Add native relationships for actual decomposition/order. A mention or checklist is not a configured relationship. |
| Development | Link an issue branch and closing/reference PR as appropriate; read `linkedBranches`, actual ref SHA and PR linkage. A branch-name convention alone is not native issue linkage. |
| Notifications | Preserve viewer subscriptions. Use relevant mentions only when necessary within authorized collaboration; do not subscribe users or generate notification spam to demonstrate a feature. |

Shared issue fields and Project-local fields have different storage and visibility. Read both before choosing a source of truth; do not accidentally maintain two contradictory Priority fields. Values cannot currently be prefilled by issue templates or URL query parameters. Use the issue sidebar/API or a supported automation and read back. [Issue field values](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-and-managing-issue-fields), [field administration](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-fields).

Use `issues/list-issue-field-values-for-issue` and `issues/add-issue-field-values` for a targeted change. Read the full schema before `issues/set-issue-field-values`: replacement must preserve unrelated values. Do not delete shared field definitions or options as routine issue completion. Check restricted/public visibility as the intended reader. [REST field values](https://docs.github.com/en/rest/issues/issue-field-values).

## Native sub-issues and dependency ordering

Break independent deliverables into native children with their own acceptance criteria, type, ownership and timeline. Reuse an existing matching issue rather than duplicating it. Inventory the existing parent and child list first, including cross-repository visibility. Limits documented for GitHub.com are 100 sub-issues per parent and eight nesting levels; permission/host limits still apply. [Sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues).

- Create an ordinary issue, read its global numeric `id`, then call `issues/add-sub-issue` on the parent with `sub_issue_id`. The payload ID is not the repository issue number. Inspect `replace_parent` before moving a child; do not silently detach existing work.
- Use `issues/get-parent` and `issues/list-sub-issues` to verify both directions. `issues/reprioritize-sub-issue` accepts a child ID plus `before_id` or `after_id`; use observed sibling IDs and verify resulting order.
- A parent/child relationship describes decomposition. An issue dependency describes required ordering. If B is blocked by A, call `issues/add-blocked-by-dependency` on B with A's global numeric `issue_id`; read both `issues/list-dependencies-blocked-by` and `issues/list-dependencies-blocking`. Reject self/cyclic intent and reconcile provider errors rather than creating reciprocal blockers.
- Remove only an obsolete relationship, with a timeline explanation when consequential. Removing a child relation does not delete or complete the child. Parent progress does not establish release delivery.

The exact indexed REST routes are documented by [sub-issue endpoints](https://docs.github.com/en/rest/issues/sub-issues) and [dependency endpoints](https://docs.github.com/en/rest/issues/issue-dependencies). Current GitHub CLI also documents `--parent`, `--add-sub-issue`, `--blocked-by` and `--blocking`; first inspect installed `gh issue create/edit --help`. Older CLI versions can use the REST executor instead of inventing unsupported flags. [Dependency usage](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies).

## Artifacts, plans and evidence

Use a native issue artifact for a substantial implementation plan, research/decision document or useful prototype; a comment links the artifact and explains the decision. Keep artifacts distinct from Actions workflow artifacts and release assets. Discover current list and names before creation. Supported issue types include `plan`, `generic`, `link` and `embedded_html`; inspect current endpoint schema before choosing the payload. Create/read/update through `issues/*-issue-artifact` operations and verify the actual artifact number, type, name, content and URL.

An edit creates another artifact version; keep this intentional version history while comments preserve progress chronology. Deleting an artifact also deletes its history and is not routine cleanup. HTML previews execute provided code; inspect trusted source before rendering. `gh issue artifact` requires CLI 2.103.0 or newer; older clients can use the indexed REST API where the target host permits it. [Artifacts with issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/using-artifacts-with-issues).

## Completion and the issue menu

| Operation | Procedure and proof |
| --- | --- |
| Completed | Add delivery evidence, then close according to project policy or verify the closing PR's merge automation. Read `state` and `state_reason`; completion must satisfy acceptance criteria. |
| Not planned | Explain the actual disposition and alternatives in a comment; use `state: closed`, `state_reason: not_planned`. Do not classify an unresolved implementation failure as completed. |
| Duplicate | Confirm the canonical target and preserve unique evidence by linking it. On supported REST use `state: closed`, `state_reason: duplicate`, `duplicate_issue_id` with the canonical global numeric ID. GraphQL `closeIssue` takes node IDs. Inspect live schema/host, then verify closure reason and canonical timeline relation. A duplicate label alone is insufficient. |
| Reopen | Explain remaining scope, reopen the same work when appropriate and reconcile Project status and any duplicate relation. Do not create a new issue solely to conceal an unsuccessful attempt. |
| Clone | Use the native Clone issue UI for a separate similar task. Check the draft before creation; verify target metadata, new URL and unchanged original. Manual API recreation must be described as recreation, since native cloning has special notification/prefill behavior. |
| Transfer | Use `gh issue transfer` or GraphQL `transferIssue` after checking destination access and owner compatibility. Verify new URL, old redirect, comments and retained/missing metadata; record affected notification/access implications. |
| Convert to Discussion | Use the native UI when the work is an open-ended question/proposal. Select the appropriate category, preserve original references, then verify destination content/comments and source state. Do not copy/delete the issue and call it a native conversion. |
| Pin/unpin | Use `gh issue pin/unpin` or GraphQL `pinIssue/unpinIssue` for a real repository entry point. Preserve existing pins and read the list afterward. Pinning a comment uses a separate comment endpoint/node. |
| Lock/unlock | Use `issues/lock` or `issues/unlock` only for an actual authorized moderation need; read lock state/reason and affected participation. Completion alone is not a reason to prevent follow-up. |
| Delete | Permanent deletion is destructive and removes history. Keep completed/rejected work closed and searchable; deletion needs an explicit valid reason and applicable authorization. |
| Open in Copilot / reactions / feedback | These are optional handoff, personal reaction and product feedback actions. A handoff requires account/tool eligibility and approved scope; reactions are not acceptance evidence. Do not trigger them merely to fill a coverage row. |

[Closing](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/closing-an-issue), [REST update schema](https://docs.github.com/en/rest/issues/issues#update-an-issue), [duplicate reference events](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/marking-issues-or-pull-requests-as-a-duplicate), [native cloning](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/cloning-an-issue), [transfer constraints](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository), [Discussion conversion](https://docs.github.com/en/discussions/managing-discussions-for-your-community/moderating-discussions).

## Views and final acceptance

Inspect repository Issues filters, personal dashboard saved Views and owner Project views separately. The same label in the navigation does not imply shared settings. Use meaningful filters for untriaged, blocked, active, review and completed work where relevant; verify the saved query as its actual audience. Personal dashboard views are viewer-specific UI state. Share useful query links or Project views for team workflows; do not claim a personal saved view configures everyone's dashboard. [Issue filters](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests), [dashboard saved views](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/viewing-all-of-your-issues-and-pull-requests).

Before completion, verify the new chronological comments and preserved earlier comments, actual type/labels/shared values, Project item/status, milestone, native relationships, development links, artifact and acceptance evidence. Record unavailable controls with host/permission evidence and unused controls with a concrete applicability reason. Re-read representative rendered issue and linked destinations. Never report a supported endpoint as proof that the issue was populated correctly.
