# Verification record

## Version 0.2.0

Verification date is 2026-11-15 on GitHub.com, repository thinkhome-org/full-github and organization Project 5.

## Inventory evidence

- Three independent research agents performed two completeness passes and inspected collaboration, delivery/security and administration using current official GitHub documentation.
- The combined catalog contains 261 feature families with operations, interfaces, sources, permissions/plan limits and verification requirements.
- The official OpenAPI snapshot contains 1,281 REST operations across 46 categories. The registry records its source digest and date.
- Live authenticated GraphQL introspection contains 32 query fields, 285 mutation fields including deprecated entries, and 1,881 schema types.
- Eighteen confirmed retired REST operations carry closure/replacement metadata and are blocked by the executor.
- Current Projects view CRUD and status-update CRUD were confirmed in the live schema. Earlier blanket UI-only guidance has been corrected.

## Automated checks

- 24 unit tests cover parameter boundaries, path/query encoding, body handling, binary upload host/media type, dry-run, remote exit status, retirement blocking, schema coverage, documented array filters, real-gh binary download byte preservation, pagination, empty responses, failures, classic branch protection and inaccessible Projects.
- Manifest, capability schema, unique IDs, retired metadata and GraphQL root/type consistency are validated.
- Generated capability and operation directories are checked for drift.

## Live execution

- The REST executor read repository metadata through repos/get and downloaded a live source ZIP with verified archive integrity.
- It created the capability-coverage label and read back its ID and custom description.
- It created the Capabilities Project view through projects/create-view-for-org with a repository/label filter. A GraphQL read confirmed the view.
- GraphQL updateProjectV2View renamed existing views to Overview, Workflow and Roadmap. A subsequent read confirmed all four saved views and layouts.
- The expanded audit executed 55 repository, organization and Project probes. 48 returned observed data and seven remained unknown. Project fields/items/views were paginated. Classic branch protection was inspected separately from rulesets.
- Two reconciliation passes preserved all label/view IDs and content, retained the new objects, created no duplicates and performed zero repeat writes. This verifies the exercised label/view scope.
- Independent code review found binary-response wrapping and administrative array-filter defects. Regression tests reproduce the relevant request/output behavior and both fixes passed.
- Initial 0.1 acceptance already exercised issue → PR → merged → automatic Project Done, Wiki publication, marketplace installation and fresh Codex skill discovery. The 0.2 release uses the same distribution route.

## Unresolved live reads

| Probe | Evidence |
| --- | --- |
| dependabot_runner_settings | gh: Not Found (HTTP 404) |
| pages | gh: Not Found (HTTP 404) |
| license | gh: Not Found (HTTP 404) |
| organization_roles | gh: Not Found (HTTP 404) gh: This API operation needs the "admin:org" scope. To request it, run:  gh auth refresh -h github.com -s admin:org |
| organization_rulesets | gh: Not Found (HTTP 404) gh: This API operation needs the "admin:org" scope. To request it, run:  gh auth refresh -h github.com -s admin:org |
| organization_actions_permissions | gh: You must be an org admin or have the actions policies fine-grained permission. (HTTP 403) gh: This API operation needs the "admin:org" scope. To request it, run:  gh auth refresh -h github.com -s admin:org |
| organization_runner_groups | gh: You must be an org admin or have the runners and runner groups fine-grained permission. (HTTP 403) gh: This API operation needs the "admin:org" scope. To request it, run:  gh auth refresh -h github.com -s admin:org |

These failures are preserved as unknown. A 404 alone cannot establish absence, plan exclusion or missing permission. Organization admin scope was not expanded during verification.

## Limits of the evidence

The catalog documents supported interfaces. The generic executor exposes indexed REST operations and native gh executes GraphQL. Only the named operations above were mutated live. Most security-sensitive, paid, enterprise and account operations were verified against official schemas/documentation, with live execution gated by the target account's rights and policy.

The expanded audit is configuration discovery, followed by feature-specific object and UI inspection. It cannot independently prove every capability is configured. Exhaustive mutation testing of every API operation is outside this verification record.

Original plugin content still awaits the owner's license decision. NOTICE.md preserves the third-party OpenAPI license.
