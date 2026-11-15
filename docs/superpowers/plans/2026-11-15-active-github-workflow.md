# Active GitHub workflow implementation plan

> For agentic workers use the existing scoped agent assignments. Continue authorized autonomous execution.

**Goal** Make full-profile decisions and native issue conversations observable and required during delivery.

**Architecture** Keep the existing skill, gh executor and catalog. Add one read-only ledger gate and extend the existing audit to issue-level objects. Use native comment creation for chronology rather than introducing a second posting client. Preserve descriptions, existing views and restricted fields.

**Tech stack** Python standard library, gh, Git, native GitHub APIs and UI.

**User specification** Existing autonomous Full GitHub request plus screenshots of issue metadata/actions, comments and Wiki footer. All eligible capabilities must be actively assessed; missing rights and inapplicability remain explicit decisions.

## Tasks

- [x] Inspect current repository and official issue/Wiki procedures, reproduce absent comments.
- [x] Require kickoff, changed findings/decisions, verification and release comments; document concurrency, retry and no overwrite semantics.
- [x] Add failing tests then issue-level audit probes and metadata/conversation attention checks. Preserve unknown permission failures.
- [x] Add tested full-profile completion gate rejecting missing or unfinished capability decisions.
- [x] Reconcile actual issue types, shared vs Project fields, parent/subissues, real dependency, priority, dates and Project README/status update without fabricating history or deadlines.
- [x] Add issue-form native types, Wiki lifecycle page/footer and links from the skill and installed user documentation.
- [x] Review changes, run all regression/registry/generated checks and exercise live issue comments and inspection.
- [ ] Merge via linked PR, publish and install a new version, verify provenance/bytes and document final release evidence in native comments and Wiki.

## Review focus

- Failed reads never mean absent settings.
- Comments are new chronological entries; independent workers never replace a shared comment.
- Newer CLI commands have API/UI fallback on installed gh2.96.
- Full-profile gate validates evidence claims; actual read-back remains required.
- Private shared fields and personal views never become public merely to fill a UI slot.
