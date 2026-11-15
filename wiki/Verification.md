# Verification record

## Version 0.3.1

Three fresh review agents examined runtime correctness, option/procedure coverage and publication/installation. The runtime reviewer found no actionable defect in the assigned execution/history scope. Twelve concrete review findings were corrected and verified, including two additional portability/policy cases from rechecking the first fixes.

- 65 tests cover tag/artifact/source mismatch, annotated tags, moved refs during upload, reviewed notes and preservation of existing prose, source/symlink portability, product policy shape and stale Wiki generation alongside prior runtime cases.
- Registry and generated-document checks cover both docs and Wiki catalogs. Every catalog capability retains concrete option decisions.
- The active release-tag ruleset blocks update/deletion with no bypass actors; its actual settings were read back.
- Existing runtime behavior and historical 0.3 evidence remain recorded below.

See [the review record](https://github.com/thinkhome-org/full-github/blob/main/docs/REVIEW-0.3.1.md) for findings, corrections and execution boundaries.

## Version 0.3.0

The configuration layer now maps every catalog capability to concrete choices and proof requirements. The full original OpenAPI document is preserved and validated against its recorded source digest. Nested references, defaults, enums, required fields, cardinality and response schemas are inspectable. Known current-documentation corrections are attached to operation descriptions.

Three domain research agents inspected official documentation and community incidents. The consolidated decision groups retain source distinctions and historical interpretation. CI rejects capabilities without mapped concrete option rules.

### Runtime and regression evidence

- 49 tests cover prior behavior plus full-schema integrity, nested reference traversal, per-capability option coverage, raw evidence retention, capped/absent-Link pagination, incomplete search, local concurrent history writers, privacy boundaries, committed hidden manifests, partial-draft retry and prerelease classification.
- A live page-based read requested 101 items from kubernetes/kubernetes and received pages of 100, 100, 16 and 0 items. The collector retained all 216 labels and exhausted continuation instead of treating the first capped response as complete.
- Actual issue mutation preserved its identity and existing labels, read back the resulting type/labels and appended a separate verification reference to local history.
- A public welcome Discussion was created and its pinned state verified in the GitHub UI. Question/proposal forms route real human participation into the correct native conversations.
- Independent runtime review found four defects in collection/publication edge cases. Regression tests now cover page-size caps, incomplete_results, raw-page preservation and RC prerelease state.
- Native repository release immutability was enabled and read back for future publications.
- The release environment was created and its v* tag policy read back. Tagged publication checks main ancestry and transferred checksums and uses a separate scoped GitHub Actions job, validated hidden manifests, SHA-256 checksums, provenance generation and byte-verified resumable drafts. Final release verification includes downloading the published artifact and gh attestation verify.

### Evidence boundaries

The local journal records executor attempts and caller-supplied read-back claims. It excludes bodies/header values and does not replace authenticated GitHub actors, audit records or required human approvals. No independent human approval is fabricated in the single-maintainer project.

The full schema and option decisions describe supported configurations and current source evidence. Actual entitlement, effective access and tenant-specific mutations still depend on the target host and credentials. Preserved historical failures below remain visible.

## Version 0.2.1

Verification date is 2026-11-15 on GitHub.com, repository thinkhome-org/full-github and organization Project 5.

## Inventory evidence

- Three independent research agents performed two completeness passes and inspected collaboration, delivery/security and administration using current official GitHub documentation.
- The combined catalog contains 261 feature families with operations, interfaces, sources, permissions/plan limits and verification requirements.
- The official OpenAPI snapshot contains 1,281 REST operations across 46 categories. The registry records its source digest and date.
- Live authenticated GraphQL introspection contains 32 query fields, 285 mutation fields including deprecated entries, and 1,881 schema types.
- Eighteen confirmed retired REST operations carry closure/replacement metadata and are blocked by the executor.
- Current Projects view CRUD and status-update CRUD were confirmed in the live schema. Earlier blanket UI-only guidance has been corrected.

Version 0.2.1 additionally preserves an explicit upload Content-Type header when a caller selects an asset MIME type.

## Automated checks

- 25 unit tests cover parameter boundaries, path/query encoding, body handling, binary upload host/media type, dry-run, remote exit status, retirement blocking, schema coverage, documented array filters, real-gh binary download byte preservation, pagination, empty responses, failures, classic branch protection and inaccessible Projects.
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
