# History and human interaction

Every configuration decision needs a reason, ownership and evidence that survives the current chat. Use GitHub's native records and the local execution journal together.

## Before changing state

Identify the actual repository and people affected. Read current configuration and its effective inherited policy. Link substantial changes to an issue or discussion, milestone and Project. Put the proposed values, rationale, affected people, compatibility and read-back checks into the issue/PR. Preserve earlier decisions and link a superseding decision when requirements change.

Use the configuration option groups to distinguish provider defaults from a recommendation for this project. Check nested enum, type, required, cardinality and nullable constraints using the full schema inspector and current official documentation. Read operational errata before applying a generated schema literally.

## Native history

- Git commits, branches, reviews and PR conversations explain implementation and acceptance. Preserve review threads and authorship. Add a comment explaining changed intent instead of replacing the historical discussion.
- Issues retain timeline events, labels, assignees, types, shared fields, dependencies and completion reason. Use closing references and verify Project automation. A transfer, conversion, archival or deletion changes what readers can find; preserve source links and verify comments/metadata before calling it complete.
- Project status updates explain progress. Items, field values, saved views, chart scope and automation must be checked separately. A successful write does not prove persistence or backfill.
- Wiki history is a separate Git repository. Pull before edits, preserve pages and navigation, commit with a reason, push and read the remote commit back.
- Release tags, notes, checksums and attestations connect published bytes to source and CI. Preserve released tags and existing asset bytes. Resume a partial draft using read-back comparison.
- Organization audit logs and webhook delivery logs have provider retention limits. Use authorized streaming/export for longer history. The Events API has limits and latency and cannot substitute for the audit log.

## Local execution journal

REST call and collect record started and terminal events in CODEX_HOME/full-github/history.sqlite3, defaulting to ~/.codex/full-github/history.sqlite3. The private file uses mode 0600. SQLite commits preserve independent concurrent requests. Records contain operation/method, selected target identifiers, time, optional context URL and exit status.

Request bodies, header values and response payloads are excluded. Review target metadata before sharing history because repository identities may be private. The journal covers this executor. Native gh/GraphQL/UI operations retain their GitHub records and should link to the same issue or PR.

```sh
python3 scripts/operations.py call issues/update --params '{"owner":"OWNER","repo":"REPO","issue_number":NUMBER}' --body-file change.json --context https://github.com/OWNER/REPO/issues/NUMBER
python3 scripts/operations.py history --limit 100
python3 scripts/operations.py verify-event RUN_ID --outcome matched --evidence https://github.com/OWNER/REPO/issues/NUMBER
```

Use --limit 0 to read all local events. --no-history is available for explicitly ephemeral inspection. Dry-run, schema and option discovery create no execution history. A query string or embedded credential is rejected in context/evidence links.

command_succeeded records the CLI result. It does not certify the desired setting or a human review. verification_recorded stores the caller's later read-back claim and evidence link. An interrupted started event or outcome_unknown requires reconciliation against GitHub before retrying. A transport failure may follow a server-side change. Re-read by known identity and apply only the remaining delta.

This local history is editable by the account owner and is not a cryptographically tamper-evident audit service. Use GitHub's authenticated audit/review records and provenance verification when that assurance is required.

## Real human participation

Use Issues for actionable defects, Q&A Discussions for questions, Ideas for proposals and PR review threads for code review. Publish clear forms and links. Keep meaningful status and ownership visible. Convert accepted proposals into linked work while preserving the original discussion.

A human approval must come from an authorized actor through the required GitHub control. Never manufacture a second reviewer, approval, reaction, vote or answered question. A bot's own review and a local verification event cannot satisfy a policy requiring an independent reviewer. Use actual requested reviewers and record unresolved approvals.

Ask one focused question in the relevant GitHub conversation when a material decision cannot be inferred. Continue independent authorized work. Do not repeatedly ask for a choice already recorded. Never automatically send private data, expand access, commit spending or moderate another person's content merely because a full profile includes that feature.

## Failure and recovery

Reconcile partial operations using IDs, content and GitHub history. Preserve unknown outcomes and observed errors. Missing Link headers, capped search results, incomplete_results, changing totals or repeated pages invalidate an all-items claim. collect verifies page-based reads and keeps received pages on failure. For cursor APIs paginate each connection and compare declared counts where available.

Official behavior and community incident reports may differ by date, host and rollout. Read the supplied community report as incident evidence, then verify its current applicability. Record the actual choice and proof for this repository.

Sources include GitHub's [REST integration practices](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api), [pagination documentation](https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api), [PR reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews), [audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization) and [artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations).

The Full GitHub plugin repository enables native release immutability. Future published tags/assets are frozen, and corrections are issued as a new release.
