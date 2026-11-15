# Independent review of 0.3.1

Three fresh agents separately inspected runtime behavior, feature-option guidance and release/installation correctness. Findings were reproduced or checked against current primary sources before implementation. Corrected release and validation paths were checked again by reviewers.

| Finding | Correction and proof |
| --- | --- |
| Required checks misclassified skipped jobs | Document success/skipped/neutral acceptance, pending workflow checks and an aggregate gate that evaluates prerequisite results. |
| IP allow-list options incomplete | Add entries/CIDRs, activation/enforcement, inheritance, App-specific IP behavior, IPv6, staged lockout avoidance and recovery. |
| PR contribution controls missing | Add has_pull_requests and all/collaborators_only policy, role impact and restoration checks. |
| Schedule timezone omitted | Add IANA timezone selection, UTC default and DST behavior. |
| Codespaces prebuild controls missing | Add branch/config selection, triggers, regions, retained versions, commands and prebuild secret availability. |
| Signoff policy missing | Add repository/org web signoff and distinguish DCO signoff from cryptographic signing. |
| Tag and artifact source not bound | Check HEAD versus peeled local tag, ZIP source comment versus build commit, and peeled remote tag before/resuming/finalizing publication. Add mismatch and annotated-tag regressions. |
| Marketplace accepted missing/invalid sources | Validate local relative paths, repository containment, plugin identity and policy enums with negative fixtures. |
| Automated notes omitted delivery information | Supply reviewed installation/verification/limitation notes alongside generated change history. Preserve existing human prose. |
| Generated Wiki copies could be stale | Render/check Wiki Capabilities and Configuration together with their repository counterparts. |
| Symlink sources could produce broken ZIPs | Reject lexical and archived symlink components and missing/mismatched referenced manifests; retain a valid nested-source case. |
| Marketplace product shape was unchecked | Validate optional product arrays and current upstream aliases while preserving omitted/null/empty supported forms. |

## Publication controls

The repository now has an active tag ruleset for refs/tags/v* that blocks update/deletion without bypass actors. This preserves tag identity while a build or draft is pending. Client-side read checks complement the server-side rule.

The workflow passes the build job's actual peeled commit to publication. New drafts receive reviewed notes from the tagged source plus generated change history. Drafts originating elsewhere require review of their delivery information; existing prose is preserved.

## Verification boundaries

The full regression suite has 65 tests. Registry validation and generated source/Wiki checks pass. Runtime public-provider checks and the verified immutable 0.3 release remain in the historical verification record.

The review establishes specific corrections and tested behavior. Target-account entitlements and high-impact administrative or paid operations retain their documented authorization and verification requirements.
