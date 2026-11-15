# Delivery and security option decisions

Option-level companion to [delivery-security.md](delivery-security.md). Sources checked on 2026-11-15. This is a decision reference, not evidence that settings are enabled, available on every plan/host, or live-tested. Follow current endpoint schemas for every mutation; preview, retired and inherited controls need host-specific verification.

For every option record desired value, observed value, inheritance, applicability, plan/permission gate, exact object ID, SHA, actor, timestamp and evidence URL. Keep source-backed support, configuration read-back, execution success and independently verified outcome separate. An unavailable API field is unknown until host/version/role is established. Do not turn every option on.

The recommendations below preserve this repository's existing GITHUB.md: read-only CI, no new runtime dependency, zero required peer approvals for the single maintainer, owner-controlled license choice, and no fabricated Packages/Pages workload. They do not authorize deployment, publication, paid provisioning, access expansion or bypass. Existing session authorization controls those actions.

## History, people and evidence

Inspect prior workflow attempts, approvals, review comments, release assets, security exceptions and deployment statuses before retrying or replacing objects. Record the actual actor and SHA behind each decision. PR review, fork-run approval, environment approval and security dismissal/bypass approval are different decisions with different permissions. Preserve independent human review where configured; do not manufacture it with bot credentials or a changed policy.

Forum reports are troubleshooting leads. Prefer maintainer resolution and current official docs over old accepted answers. Notable 2026 drift: concurrency queue:max and Dependabot's three-day version cooldown. Current reusable workflow docs also clarify environment-secret forwarding; test absence safely.

## Option inventory

### Workflow triggers and typed inputs

Group: `workflow-events`. Capabilities: `actions-workflows`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| on / types | push, pull_request, pull_request_target, merge_group, schedule, workflow_dispatch, repository_dispatch, workflow_run, workflow_call, release; event-specific activity types | Choose the event whose code/ref and trust model match the job. Add merge_group when required checks serve a merge queue. | Exercise intended event; record event, actor, head_sha and workflow revision. |
| branches / tags / paths | positive/negative glob lists; branches-ignore/tags-ignore/paths-ignore alternatives | Protect required checks against path-filter skips; order negative patterns deliberately; branch and path filters combine. | Test included/excluded branch and file combinations; inspect check state. |
| schedule | POSIX cron; UTC; default-branch workflow | Use for tolerable delays, with manual recovery; scheduling is not a precise timer. | Compare scheduled event timestamp, branch and actual start. |
| workflow_dispatch.inputs | boolean, choice, environment, number, string; required/default/options | Validate enum and deployment target; environment input selects a value but does not gate a job without environment. | Run default and explicit input values; reject invalid target in job. |
| workflow_run | requested, in_progress, completed; workflows and branches | Treat upstream code/artifacts as untrusted; privileged follow-up must verify origin and SHA. | Read originating run ID, repository, event, conclusion, SHA and artifact provenance. |
| GITHUB_TOKEN event recursion | Most token-generated events do not launch another workflow; dispatch exceptions exist | Use explicit dispatch for intended chaining, with bounded recursion; do not broaden credentials just to trigger CI. | Match downstream run to dispatch; confirm no duplicate loop. |

Project applicability: Existing validation CI needs PR and default-branch coverage. Event expansion needs a concrete repository operation.

History and human interaction: Keep trigger edits in reviewed commits; retain event payload metadata without secrets and explain maintainer-triggered runs.

Recovery: Inspect event/ref/filters first; dispatch or rerun the exact intended revision only after correcting cause.

- Pitfall: A required workflow skipped by filters can leave a required check pending.
- Pitfall: pull_request_target operates in privileged base context; never checkout and execute untrusted PR code there.
- Pitfall: Schedule delays and dropped scheduling events require observability.

Official sources: [reference 1](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [reference 2](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [reference 3](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

### Jobs, matrices, conditions and run history

Group: `workflow-execution`. Capabilities: `actions-workflows`, `actions-runs`, `actions-job-logs`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| needs / if | DAG dependencies; success(), failure(), cancelled(), always(); expressions | Use explicit terminal handling. Reserve always() for bounded cleanup; avoid making cancellation ineffective. | Inspect skipped and failed upstream cases plus cancellation. |
| strategy | matrix axes/include/exclude, fail-fast, max-parallel | Test supported platforms; fail-fast false retains all diagnostics at higher cost. | Inspect complete matrix job set and all conclusions. |
| step execution | run/uses, id, with, env, shell, working-directory, outputs, defaults | Pass untrusted strings through environment or typed inputs rather than shell interpolation. | Read exact workflow SHA, command results and produced outputs. |
| timeouts / tolerated failures | job and step timeout-minutes; continue-on-error; retry in command/action | Bound resource use; do not mark safety or release validation optional. | Force representative failure; ensure required job fails and cleanup completes. |
| services / containers | image, credentials, env, volumes, ports, options; supported runner OS | Use when integration tests require services; pin trusted images and isolate credentials. | Health-check service and inspect exact image digest. |
| attempt operations | rerun all, failed jobs, one job, debug logging, cancel/force-cancel; delete logs/run | Rerun after diagnosis. Capture current attempt; debug logs increase disclosure risk. | Record run ID, attempt, job IDs, SHA, conclusion and redacted log URL. |

Project applicability: Keep the existing small validation workflow unless real platform differences justify a matrix.

History and human interaction: Preserve previous attempts and reviewer explanation; canceled or deleted logs are not proof of an earlier success.

Recovery: Read the current attempt before retrying; cancel normally first; force-cancel only after identifying stuck run and external side effects.

- Pitfall: A maintainer investigation of discussion #206259 attributed apparent queue blocking to other group jobs and always() preventing cancellation; initial bug claims were incomplete.

Official sources: [reference 1](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [reference 2](https://docs.github.com/en/rest/actions/workflow-runs), [reference 3](https://docs.github.com/en/rest/actions/workflow-jobs).

Community / maintainer evidence: [discussion 1](https://github.com/orgs/community/discussions/206259).

### Actions availability, allowed code and token defaults

Group: `actions-policy`. Capabilities: `actions-permissions`, `actions-policies`, `actions-fork-retention`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| Actions enabled scope | disabled, all eligible repositories, selected repositories; inherited org/enterprise constraints | Read inheritance before changing repository settings. | Read all controlling scopes and repository eligibility. |
| allowed actions/reusable workflows | all, local-only, selected; GitHub-owned, verified Marketplace, explicit patterns; SHA-pinning policy where supported | Pin reviewed actions; allow only required external automation. | Read selected-action patterns and inspect each uses reference. |
| default_workflow_permissions | read or write; per-workflow/per-job permission map | Keep repository default read; grant needed write permissions only in responsible job. | Inspect setup log effective GITHUB_TOKEN permissions. |
| token permission map | actions, artifact-metadata, attestations, checks, contents, deployments, discussions, id-token, issues, models, packages, pages, pull-requests, security-events, statuses; supported read/write/none values | Once any permission is specified, unspecified permissions become none; metadata/scopes and availability differ. | Compare permissions to each operation schema and actual run grants. |
| PR creation / approval by Actions | allow or deny workflow PR creation/approval | Creation may help automation; automated approval is not independent review and must not satisfy a human governance intent. | Read can_approve_pull_request_reviews and inspect actor of resulting review. |
| fork policy | first-time/first-time-with-new-account/all external contributor approval; private-fork run/read-token/write-token/secrets options | Run contributions without secrets/write token; approval authorizes code execution and consumes resources. | Read fork policy plus run approval actor and effective token. |
| policy objects and retention | schema-defined action policy rules; artifact/log days bounded by parent policy | Inspect current rule schema and inherited maximums; retain enough release evidence without storing sensitive logs. | Read policy IDs/rules and expiry dates on actual run/artifact. |

Project applicability: Repository rules require read-only CI. Do not enable write or fork secrets merely for fuller coverage.

History and human interaction: Record who approved contributed code, which SHA was inspected and whether a later update needs review again.

Recovery: Revert an allowlist through reviewed policy change; preserve run evidence before lowering retention or deleting logs.

Official sources: [reference 1](https://docs.github.com/en/rest/actions/permissions), [reference 2](https://docs.github.com/en/rest/actions/policies), [reference 3](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

### Reusable workflows, actions and templates

Group: `reusable-contract`. Capabilities: `actions-reusable`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| sharing and reference | same-repo path; owner/repo workflow@SHA/tag/branch; private/internal sharing | Prefer exact reviewed SHA; access/allowed-actions policies must permit every nested workflow. | Read referenced_workflows SHAs and effective access policy. |
| workflow_call contract | boolean/number/string inputs, required/default; explicit secrets; outputs mapped job to workflow | Treat inputs/outputs as an API; avoid stringly typed booleans. | Run caller with omitted/default/explicit values and check outputs. |
| secret forwarding | named secrets or inherit for supported org/enterprise relationship; forwarding at every nested hop | Forward only required names; inheritance is wider. Current docs require passing environment secrets as well. | Fail safely when required secret is empty without printing it. |
| environment scope | environment on called job; same-name environment secret wins | Caller cannot put environment on a reusable-workflow call job. Pass environment identifier as input and bind it inside called workflow. | Observe called job gate and selected environment; verify secret presence only. |
| env and outputs | caller env is not general callee env; job/workflow outputs; reusable matrix output semantics | Pass configuration explicitly; use artifacts for files. | Assert outputs on representative matrix and nested caller. |
| nesting / permissions / concurrency | supported host nesting limit; accessible chain; permissions can only remain or decrease; caller/callee group IDs | Avoid same concurrency key accidentally canceling caller; inspect current host limits rather than hard-code historical limits. | Execute complete chain and inspect grants/group. |
| action forms and templates | composite steps, JavaScript runtime, Docker action; organization workflow-templates metadata | Use a template for copied starting files; reusable workflow for centrally maintained behavior. | Check action.yml inputs/runtime and actual consumer run. |

Project applicability: Use only if repeated workflows merit a shared contract; small single-repo CI does not need a new abstraction.

History and human interaction: Version contract changes, review all callers and record actual called SHA rather than mutable tag only.

Recovery: Pin consumer to prior known SHA; restore compatible input/output contract and test caller before broader rollout.

- Pitfall: Issue #4453 reports empty environment secrets without forwarding; current official documentation explicitly requires passing or inherit. required:true checks passing, not non-empty value.

Official sources: [reference 1](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows), [reference 2](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations), [reference 3](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

Community / maintainer evidence: [discussion 1](https://github.com/actions/runner/issues/4453).

### Variables, credentials and precedence

Group: `configuration-secrets`. Capabilities: `actions-variables`, `actions-secrets`, `security-dependabot-secrets`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| scope / selected repositories | organization all/private/selected; repository; environment; Actions versus Dependabot secret stores | Place credentials in narrowest necessary scope; variables are public-to-readers configuration. | Read names/metadata and selected repository IDs. |
| same-name precedence | environment over repository over organization; runtime availability/context restrictions | Avoid collisions; check when the job evaluates variables versus when environment values are available. | Inspect effective non-sensitive variable and secret-presence check in bound job. |
| write protocol | scope public key plus encrypted_value; gh secret via stdin/secure file | Never put secret in arguments, source or issue; encrypted API field is not a retrieval path. | Read updated_at/name; exercise minimal authorized operation. |
| fork / Dependabot / reusable contexts | secrets withheld for untrusted fork runs; Dependabot uses its dedicated store; explicit reusable forwarding | Do not duplicate broad credentials to fix a context error. | Read event actor and correct credential store; negative test unauthorized use. |
| rotation / expiry / redaction | provider revoke/reissue, key owner/expiry metadata outside secret value; add-mask for derived values | Rotate at provider; log masking is best effort, not access control. | Confirm old credential rejection and new credential operation without outputting either. |

Project applicability: Validation should need no repository secret. Dependabot private registries need separate credentials only if present.

History and human interaction: Record credential purpose, owner, consumer and rotation date; never plaintext values in historical evidence.

Recovery: Revoke exposed credential first; replace narrow secret and rerun safely; remove/redact logs separately.

Official sources: [reference 1](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets), [reference 2](https://docs.github.com/en/actions/reference/workflows-and-actions/variables), [reference 3](https://docs.github.com/en/rest/actions/secrets), [reference 4](https://docs.github.com/en/rest/dependabot/secrets).

### Concurrency and queue policy

Group: `concurrency-queues`. Capabilities: `actions-concurrency`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| group | workflow/job scope; expression; repository-wide case-insensitive group name | Include workflow/ref for isolated CI; use environment-specific shared key for deployment serialization. | Read evaluated group and all related pending/running jobs. |
| queue | single default; max permits up to 100 pending | Use single for latest-state jobs; max when every item matters and host supports it. | Queue a bounded test and inspect pending replacements/overflow. |
| cancel-in-progress | false/default; true; allowed expression | Cancel stale CI; avoid interrupting releases or migrations. queue:max plus true is invalid. | Read old run conclusion and ensure side effects stopped. |
| ordering | FIFO by entering concurrency wait, not original dispatch time; no universal dispatch ordering guarantee | Do not use queue as a transactional ledger; record intended sequence separately if needed. | Compare queue-entry and execution history with expected deployment revisions. |

Project applicability: CI can cancel outdated branch checks; release and Wiki publication must preserve sequence and existing content.

History and human interaction: Attach cancellation reason to run history and preserve prior attempt IDs; an operator retry does not establish queue order.

Recovery: Inspect every workflow sharing the key and always() conditions before calling a queue bug; check runner availability and status incident history.

- Pitfall: 2021–2025 complaints about a single pending slot do not describe current queue:max behavior; maintainer announced shipping April 17, 2026.
- Pitfall: The control-concurrency page contains broad examples implying unconditional cancellation; use its explicit queue/cancel policy definitions.

Official sources: [reference 1](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency), [reference 2](https://docs.github.com/en/rest/actions/concurrency-groups).

Community / maintainer evidence: [discussion 1](https://github.com/orgs/community/discussions/5435), [discussion 2](https://github.com/orgs/community/discussions/12835), [discussion 3](https://github.com/orgs/community/discussions/206259).

### Workflow artifact contents and lifecycle

Group: `artifacts`. Capabilities: `actions-artifacts`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| upload contract | name, path/globs/exclusions, if-no-files-found warn/error/ignore, retention-days | Require expected files; choose unique artifact name per matrix job. | Download exact artifact ID and inspect archive manifest. |
| hidden and file metadata | include-hidden-files false by default; ZIP changes permission fidelity; tar when metadata matters | Include required dotfiles explicitly after excluding credentials; tar executable-sensitive bundles. | Check .codex-plugin files and executable bits in extracted release bundle. |
| compression / overwrite | compression-level supported range; overwrite false default; upload version semantics | Favor low compression for precompressed assets; overwrite deletes old artifact identity. | Record artifact ID, digest, size and expiration after upload. |
| download selection | ID/name/pattern, merge-multiple, path; repository/run/token for cross-run access | Bind release input to trusted run and SHA, never latest name alone. | Verify source run, digest and expected file allowlist. |
| host and action compatibility | supported major/runtime/backend; GHES support differs from GitHub.com | Read current action README and installed runner minimum; do not blindly copy a dot-com major. | Run on target host and inspect resulting artifact/download. |

Project applicability: Inspect installable plugin archive before release; preservation of hidden plugin metadata is essential.

History and human interaction: Keep archive manifest, digest and trusted producing SHA with release evidence; retention expiry must not erase sole evidence.

Recovery: Rebuild from same reviewed SHA, compare contents and digest, issue new version for published immutable mistakes.

- Pitfall: Hidden-file default change broke explicit dotfile upload use cases; plugin archives can silently lose .codex-plugin if blindly uploaded.
- Pitfall: Artifact download is untrusted data until origin and contents are verified.

Official sources: [reference 1](https://github.com/actions/upload-artifact), [reference 2](https://github.com/actions/download-artifact), [reference 3](https://docs.github.com/en/rest/actions/artifacts).

Community / maintainer evidence: [discussion 1](https://github.com/actions/upload-artifact/issues/602).

### Cache keys, access and budgets

Group: `cache`. Capabilities: `actions-caches`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| lookup identity | path, key, restore-keys, OS/architecture/lockfile/toolchain salts; cache-version/ref scope | Do not mix incompatible binaries; restore prefixes trade hit rate for stale input risk. | Inspect exact key/ref/version and restored build behavior. |
| restore controls | lookup-only, fail-on-cache-miss, enableCrossOsArchive, supported restore/save actions | Fail on miss only when cache existence is an actual requirement; cache is ordinarily optional. | Test empty cache and prefix fallback; verify reproducible cold build. |
| write/eviction | immutable key entry; new key for changed content; retention/storage policies | Avoid secrets and release-only evidence; monitor eviction and thrashing. | Read usage, last_accessed_at, size and configured inherited limits. |
| trust boundary | fork/base/default-branch read visibility and write scope; workflow cache access restrictions | Treat cache as untrusted executable input; separate privileged/untrusted scopes. | Verify trust-specific keys/access plus authorized clean-cache build. |

Project applicability: Small Python stdlib validation does not justify a cache unless measured runtime benefit exists.

History and human interaction: Keep cache purge reason and old keys in issue/run evidence, never cache credential contents.

Recovery: Delete only identified poisoned/stale keys; rerun cold, then change salt to prevent accidental reuse.

Official sources: [reference 1](https://github.com/actions/cache), [reference 2](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching), [reference 3](https://docs.github.com/en/rest/actions/cache).

### Hosted, self-hosted and larger runner configuration

Group: `runners`. Capabilities: `actions-self-hosted-runners`, `actions-runner-groups`, `actions-hosted-runners`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| runs-on selection | hosted image/architecture/size; self-hosted label intersection; group plus labels | Use smallest suitable hosted runner; image labels can roll, so record actual image version. | Inspect job runner_name/group/labels/OS and setup image version. |
| self-hosted registration | repository/org scope; short-lived registration/removal tokens; JIT config; ephemeral flag | Use disposable isolated machines for untrusted work; registration is not host hardening. | Run benign job, confirm isolation and disposal/cleanup. |
| group access | all/selected repositories; public repo option; selected workflows/revisions; inherited org/enterprise policy | Restrict trusted runner group to known workflows and repos. | Read group repository IDs and allowed workflow refs; test excluded workflow refusal. |
| host lifecycle | runner version/update policy, online/busy, labels, proxy, workspace cleanup; ARC scale sets | Patch runner and images; bound queue and jobs; autoscaling requires separate infrastructure. | Check runner health and clean job-to-job environment. |
| larger runner settings | machine type/image/size/max parallelism, runner group, static IP/private networking where eligible | Enable only for a demonstrated workload and approved billing/network access. | Read saved runner config, network reachability and billed usage. |

Project applicability: No current need for paid or self-hosted capacity in this plugin repository.

History and human interaction: Capture operator registration/removal and host ownership, preserving relevant job logs before disposal.

Recovery: Quarantine suspect runner, revoke credentials, replace image; never assume workspace deletion undoes compromise.

Official sources: [reference 1](https://docs.github.com/en/actions/reference/runners/github-hosted-runners), [reference 2](https://docs.github.com/en/actions/reference/runners/self-hosted-runners), [reference 3](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access), [reference 4](https://docs.github.com/en/rest/actions/hosted-runners).

### OIDC claims and cloud trust

Group: `oidc`. Capabilities: `actions-oidc`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| issuance permission | id-token:write only on authenticating job | Token issuance grants no cloud resource permission by itself. | Inspect effective job permission and provider exchange result. |
| trust conditions | issuer, audience, repository identity, ref/environment, job_workflow_ref; provider-supported claims | Scope provider trust to exact owner/repo/workflow/target; avoid broad wildcard repo trust. | Inspect redacted claims and denied wrong-ref/target exchange. |
| subject template | repo use_default; org/repo include_claim_keys; supported custom properties | Stage cloud trust migration before changing sub format; org template requires correct repo adoption. | Read template and compare actual non-sensitive sub/claim values. |
| reusable workflow identity | caller repository context versus called job_workflow_ref; accessible trust claims | Require reviewed reusable workflow identity where provider supports it. | Inspect caller/callee SHAs and successful narrow provider action. |
| environment interaction | environment-based subject replaces ref-based shape; branch rules are separate gate | Configure both cloud subject and GitHub deployment branch policy. | Negative-test disallowed ref and unapproved environment job. |

Project applicability: No cloud deploy target currently exists; do not create one to exercise OIDC.

History and human interaction: Record cloud role/trust policy revision and migration review, never JWT contents.

Recovery: Restore previous subject template or compatible provider trust; revoke exposed long-lived credentials separately.

Official sources: [reference 1](https://docs.github.com/en/actions/reference/security/oidc), [reference 2](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-with-reusable-workflows), [reference 3](https://docs.github.com/en/rest/actions/oidc).

### Environment protection and approvals

Group: `environment-approvals`. Capabilities: `deploy-environments`, `deploy-approval`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| required reviewers | eligible users/teams; one eligible approval suffices; prevent self-review; plan restrictions | Do not describe reviewer list as unanimous approval. Independent approval requires another eligible human. | Read reviewer IDs, prevent_self_review and actual approval actor. |
| wait timer | documented minute range; non-billable waiting; product/visibility gates | Use only for purposeful rollout delay; it does not inspect health. | Read wait duration and timestamps before job starts. |
| deployment branch policy | all; protected branches; selected branch/tag patterns | Gate deployment ref separately from repository branch protection; test tags explicitly. | Read protected_branches/custom_branch_policies and every branch/tag rule. |
| administrator bypass | allow/deny supported protection bypass setting | Keep bypass decision explicit and auditable; automation must not bypass its own gate. | Read saved option plus bypass actor/comment when used. |
| custom protection rules | installed GitHub App rules; enabled rules bounded by current platform limit | Verify app permission, external approval/health decision and failure handling. | Read rule integration IDs and actual requested/approved/rejected record. |
| environment configuration | name, URL, secrets, variables; create explicitly before referencing | A misspelled environment may be created without intended safeguards; exact name matters. | Read environment ID and settings before allowing workflow run. |
| approval operations | pending deployments approve/reject with comment; workflow gate differs from PR approval | Read artifact/SHA and change context before approval; never impersonate reviewer or weaken policy. | Record deployment IDs, reviewer, decision, comment and run continuation. |

Project applicability: A single maintainer cannot manufacture independent peer approval. No deployable service exists; preserve zero required PR approvals as repository policy.

History and human interaction: PR review, fork workflow execution approval and environment approval are distinct histories; record each real actor/decision.

Recovery: Reject unsafe pending deployment, correct exact environment/ref and rerun; do not remove protection to unblock automation.

Official sources: [reference 1](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments), [reference 2](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments), [reference 3](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments), [reference 4](https://docs.github.com/en/rest/deployments/environments).

### Deployment records, statuses and rollback

Group: `deployment-records`. Capabilities: `deploy-records`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| deployment request | ref, task, payload, environment, description, auto_merge, required_contexts, transient_environment, production_environment | Bind immutable SHA and required checks; deployment API is a record/request, not deployment engine. | Read record ID, sha, environment and exact request parameters. |
| status transitions | queued, pending, in_progress, success, failure, error, inactive; log_url, environment_url, auto_inactive | Report actual engine state and measured health. | Read ordered statuses and independently test application version/health. |
| cleanup/rollback | mark inactive; delete eligible deployment; external rollback to prior immutable artifact | Preserve operational trail; deactivate previews when removed. | Compare served SHA/digest before/after and status history. |

Project applicability: Only create deployment records for an actual deployment; source/plugin release alone is not an application deployment.

History and human interaction: Store approver, release artifact digest and rollback reason in deployment/linked issue history.

Recovery: Deploy prior verified artifact with a new explicit rollback record; a green API status does not restore service.

Official sources: [reference 1](https://docs.github.com/en/rest/deployments/deployments), [reference 2](https://docs.github.com/en/rest/deployments/statuses).

### Security products, inheritance and enforcement

Group: `security-enablement`. Capabilities: `security-enablement`, `security-configurations`, `security-overview`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| product switches | dependency graph/submission; Dependabot alerts/security updates; Code Security; Secret Protection; private vulnerability reporting | Evaluate eligibility and actual need separately; security policy prose is not scanning enablement. | Read effective repository security_and_analysis and product-specific status. |
| configuration association | org/enterprise configuration ID; selected/all/new-repository defaults; enforcement | Preserve inherited policy; inspect asynchronous association failures and product entitlements. | Read configuration, repository association/application state and effective setting. |
| enforced controls | enabled/disabled/not-set where schema supports; enforcement mode; delegated dismissal/bypass | Validate current schema per field rather than applying one enum blindly. | Read exact serialized config plus repository lock state. |
| coverage/risk | repository filters, missing coverage, exclusions, alert severity/age; eligible plan | Report unknown/unavailable separately from clean or disabled. | Reconcile visible repo counts and excluded/failed scans with ledger. |

Project applicability: Public plugin can use eligible free controls; do not activate a paid organizational product or change license policy without authorization.

History and human interaction: Retain setting changes, application status, responsible security owner and policy exception explanation.

Recovery: Correct failed association or incompatible config; preserve evidence before detaching and never silently relax enforcement.

Official sources: [reference 1](https://docs.github.com/en/rest/code-security/configurations), [reference 2](https://docs.github.com/en/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration), [reference 3](https://docs.github.com/en/code-security/getting-started/github-security-features).

### CodeQL, SARIF, Autofix and code quality

Group: `code-scanning`. Capabilities: `security-codeql`, `security-code-alerts`, `security-ai-autofix`, `security-code-quality`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| setup mode | default or advanced; language selection; query suite; supported runner | Choose default for supported uncomplicated builds; advanced for custom build/query needs. | Verify actual language database and completed analysis at intended SHA. |
| advanced options | matrix languages, build-mode none/autobuild/manual, paths/paths-ignore, queries/packs/model packs, config-file, category, schedule | Match build mode to language; path excludes can create blind spots. Keep category stable per analysis variant. | Read workflow/config at analyzed SHA and analysis category/language coverage. |
| blocking controls | security/quality severities, rule/tool selection, ruleset thresholds where supported | Pick actionable severity gates and require actual scan completion; empty upload is not clean coverage. | Inspect PR check result and corresponding alerts/instances. |
| SARIF upload | tool/category, commit_sha, ref, analysis_key, compressed payload; processing status | Validate SARIF and bind result to exact commit/ref; poll until processed. | Read sarif processing result and analysis commit/tool/category. |
| alert lifecycle | open/fixed/dismissed; allowed dismissal reason/comment; delegated review | Dismiss with evidence; reopen when premise fails. Deleting analysis is not remediation. | Read state, dismissing actor/time/reason and latest instance. |
| Autofix / AI Scan | available product switch; supported alert request; proposed patch/commit | Review generated diff and test before committing; do not equate generated fix with validated fix. | Rerun affected tests/scanner and inspect resolved finding. |
| variant databases / code quality | CodeQL database downloads/variant target scope; quality setup/findings supported schema | Use only for concrete cross-repository query/quality need; permissions differ from code scanning. | Read variant completion per repo and quality findings at target revision. |

Project applicability: Analyze actual Python/scripts and workflow languages supported by selected tool; do not claim Markdown guidance has executable-language CodeQL coverage.

History and human interaction: Preserve alert number, instance, reviewer rationale and scan SHA; approvals for dismissal remain separate from fix review.

Recovery: Fix build/query/upload cause; rescan same intended revision; reopen unsupported dismissals and revert unsafe Autofix commit.

Official sources: [reference 1](https://docs.github.com/en/code-security/reference/code-scanning/workflow-configuration-options), [reference 2](https://docs.github.com/en/rest/code-scanning/code-scanning), [reference 3](https://docs.github.com/en/rest/code-quality/code-quality), [reference 4](https://docs.github.com/en/code-security/concepts/security-at-scale/delegated-alert-dismissal).

### Dependency graph, review, submission and SBOM

Group: `dependency-inventory`. Capabilities: `security-dependency-graph`, `security-sbom`, `security-global-advisories`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| inventory sources | supported manifests/lockfiles, automatic or explicit dependency submission; detector/job identity | Resolve build dependencies where manifests are insufficient; do not fabricate runtime dependencies. | Match graph snapshot detector and SHA to lockfile/build resolution. |
| dependency-review policy | base/head diff; fail-on-severity, allowed/denied licenses, scope, allowlisted advisories/packages; supported action options | Use narrow documented exceptions with owner/expiry; license policy requires owner decision. | Inspect newly introduced vulnerable/license entries and check failure. |
| SBOM | SPDX export; async report UUID where supported; snapshot date and included scopes | Treat as inventory snapshot bounded by graph completeness. | Parse SPDX and compare package counts/versions to manifests and submission. |
| advisory matching | GHSA/CVE, ecosystem/name, affected/fixed range, withdrawn/reviewed status | Match precise version and ecosystem; absence of advisory is not safety proof. | Read advisory update time, withdrawn state and installed resolved version. |

Project applicability: No new runtime dependency is authorized. Track action dependencies and required tooling; owner has not selected project license.

History and human interaction: Keep dated SBOM/diff, dependency exception reviewer and changed lockfiles with PR evidence.

Recovery: Submit corrected snapshot and regenerate SBOM; fix affected version or record bounded reviewed exception.

Official sources: [reference 1](https://docs.github.com/en/rest/dependency-graph/dependency-review), [reference 2](https://docs.github.com/en/rest/dependency-graph/dependency-submission), [reference 3](https://docs.github.com/en/rest/dependency-graph/sboms), [reference 4](https://docs.github.com/en/rest/security-advisories/global-advisories), [reference 5](https://github.com/actions/dependency-review-action).

### Dependabot schedules, update strategy and runtime

Group: `dependabot`. Capabilities: `security-dependabot-alerts`, `security-dependabot-version`, `security-dependabot-runtime`.

| Option | Values / default | Decision rule | Verification |
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

Project applicability: Existing policy explicitly wants GitHub Actions updates. Add other ecosystems only if manifests exist.

History and human interaction: Respond to supported @dependabot commands after reading bot status; human review remains required under repo rules, and bot actor restrictions affect secrets.

Recovery: Read update log before rebase/recreate; remove obsolete ignore, fix registry access narrowly, rerun supported job and verify generated PR.

- Pitfall: Maintainer announcement July 14, 2026 confirms 3-day default version cooldown; older explanations assuming immediate version PRs are stale.
- Pitfall: Issue #16319 reports grouping failure in a particular non-root npm case; it is a reproduction lead, not proof all grouping is broken.

Official sources: [reference 1](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference), [reference 2](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/optimizing-pr-creation-version-updates), [reference 3](https://docs.github.com/en/rest/dependabot/alerts), [reference 4](https://docs.github.com/en/rest/dependabot/runner-settings), [reference 5](https://docs.github.com/en/rest/dependabot/repository-access).

Community / maintainer evidence: [discussion 1](https://github.com/dependabot/dependabot-core/discussions/15582), [discussion 2](https://github.com/dependabot/dependabot-core/issues/16319).

### Secret detection, push protection and exceptions

Group: `secret-scanning`. Capabilities: `security-secret-alerts`, `security-push-protection`, `security-custom-patterns`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| detection options | provider patterns, non-provider/generic/AI detection where eligible; validity checks; extended metadata | Enable supported useful detection; validity/metadata may contact provider and have product gates. | Read settings and scan history/coverage, not alert count alone. |
| push protection | repository protection versus personal protection; supported pattern participation | Do not mistake personal block for repository policy; repository scanning remains separate. | Read repository setting and safe documented test result. |
| custom patterns | name, secret regex, before/after context, additional match requirements; dry-run/publish; push protection | Use safe synthetic examples and negative corpus; dry-run before publishing noisy pattern. | Record pattern ID/version and positive/negative results. |
| bypass governance | test/false-positive/fix-later reasons where offered; delegated reviewers, expiry/review path | Never bypass a valid live credential; fix/revoke instead. Independent reviewer decision stays with reviewer. | Read request, actor, comment, expiry and resulting alert. |
| alert state | open/resolved; revoked, false_positive, used_in_tests, wont_fix or current schema reasons; location/history | Revoke with provider first; resolving UI alert does not revoke token or erase history. | Check provider revocation and read alert location/resolution metadata. |
| dismissal governance | direct or delegated dismissal; role eligibility; notification/review state | Confirm reviewer coverage before enforcing; preserve rationale even for test secrets. | Read request/outcome, reviewer and reopened state if rejected. |

Project applicability: Useful for public repo; synthetic tests must not leak live values. Security setting read may itself contain secret values; redact outputs.

History and human interaction: Retain private alert IDs, discovery/rotation timestamps and reviewed exception reasons; do not copy secret strings into public issues.

Recovery: Revoke at provider, replace consumers and scan history; history rewriting is separate consequential work and does not invalidate copied credentials.

Official sources: [reference 1](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning), [reference 2](https://docs.github.com/en/rest/secret-scanning/secret-scanning), [reference 3](https://docs.github.com/en/rest/secret-scanning/push-protection), [reference 4](https://docs.github.com/en/rest/secret-scanning/custom-patterns), [reference 5](https://docs.github.com/en/code-security/concepts/security-at-scale/delegated-alert-dismissal).

### Confidential reports, advisory publication and campaigns

Group: `security-coordination`. Capabilities: `security-advisories`, `security-campaigns`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| reporting policy | SECURITY.md supported versions/contact; private vulnerability reporting enabled/disabled | Provide confidential route and realistic response ownership. | Inspect rendered policy and actual reporting availability. |
| advisory content | draft/published/withdrawn, severity/CVSS/CWE, vulnerable ranges/patched versions, references, credit, CVE request | Keep report private until fix/disclosure agreement; verify affected ranges. | Read advisory state/collaborators and clean install of patched release. |
| collaboration | report triage, comments, invited collaborators, temporary private fix fork | Grant only necessary confidential access and retain reporter coordination. | Read actual collaborator identities and private fork/review history. |
| campaign setup | selected code alerts, repositories, managers/teams, contact, deadline; draft UI versus published API; optional generated issues | Use for multi-repository remediation requiring tracking; preserve private finding visibility. | Read published campaign scope/counts and corresponding resolved alerts. |
| publication / withdrawal | explicit publish/CVE disclosure; withdrawal constraints; notification effects | Publication is irreversible disclosure; prepare exact reviewed advisory/fix before authorized publish. | Read public GHSA/CVE and release timestamps; verify issue scope. |

Project applicability: Confidential reporting is useful; campaigns require actual alert program and owner eligibility, not a placeholder.

History and human interaction: Preserve reporter credits, embargo agreement, fix review and disclosure decision privately; public release notes must respect agreed timing.

Recovery: Correct advisory affected ranges/notes and notify existing recipients; never claim withdrawal removes already disclosed information.

Official sources: [reference 1](https://docs.github.com/en/rest/security-advisories/repository-advisories), [reference 2](https://docs.github.com/en/rest/campaigns/campaigns).

### Drafts, generated notes, assets and immutability

Group: `release-lifecycle`. Capabilities: `releases-lifecycle`, `releases-assets`, `releases-immutable`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| release identity | tag_name, target_commitish for new tag, name, draft, prerelease, make_latest | Existing tag determines commit; target_commitish does not move it. Match plugin manifest version to v-tag. | Resolve tag object/commit, release ID and version file. |
| notes | body; generated notes; previous tag/configuration; categories/exclusions; discussion category where eligible | Review generated changelog; include install commands, validation evidence and limits. | Read rendered notes and linked issues/PRs against intended range. |
| asset upload | binary content type, filename/label; draft upload URL; per-asset ID/digest/size | Build deterministic installable archive, inspect hidden files and allowlist before attaching. | Download attached bytes and compare SHA-256/archive manifest. |
| immutability | repo/org policy; new release behavior; immutable flag | Create draft, attach every asset, then publish. Published assets/tag become locked; notes/title/latest/prerelease remain editable. | Read immutable flag, tag SHA, asset digest and release attestation. |
| publication/recovery | draft update versus publish; prerelease/stable; delete constraints; corrective next version | Do not publish from merely prepared source; irreversible distribution needs existing release authorization. | Read published_at, exact asset bytes, install from release and latest pointer. |

Project applicability: Core delivery path: plugin version, v-tag, installation docs and validation evidence must agree. Immutability prevents patching published archive.

History and human interaction: Record release preparer/reviewer/publisher, reviewed tag SHA and prior release comparison. Discussion and release notes carry human feedback/history.

Recovery: For immutable wrong asset/tag, publish a new corrected version; editable notes cannot change locked bytes. Never force-move tag as an assumed recovery.

Official sources: [reference 1](https://docs.github.com/en/rest/releases/releases), [reference 2](https://docs.github.com/en/rest/releases/assets), [reference 3](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository), [reference 4](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases).

### Provenance, SBOM and linked artifact records

Group: `attestations`. Capabilities: `attestations-provenance`, `attestations-linked-artifacts`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| statement type | build provenance or SBOM attestation; artifact digest/name; supported registry publication | Attest exact distributed bytes; provenance says how/where built, not absence of bugs. | Verify subject digest and trusted repository/workflow identity. |
| workflow grants | id-token:write, attestations:write; contents/read and packages/write only when needed | Isolate attestation in trusted release job; eligibility varies with visibility/plan. | Inspect effective permissions and successful verify output. |
| verification constraints | trusted owner/repo/workflow, predicate type, signer identity, source ref/commit; offline/bundle modes where supported | Do not accept any valid GitHub signature; require intended producer. | Run gh attestation verify against downloaded exact asset and identity policy. |
| linked artifacts | storage metadata and artifact association using current endpoint schema | Distinguish storage record/link from uploaded file and signed attestation. | Read link identity, digest and referenced object existence. |

Project applicability: Consider for installable release artifact when trusted workflow builds it; record unavailable eligibility instead of assuming.

History and human interaction: Keep verifier command/policy/output and producing workflow SHA with release record; release attestation and custom build provenance are distinct.

Recovery: Rebuild/re-attest correct bytes in trusted workflow; revoke trust in compromised producer and publish corrective version.

Official sources: [reference 1](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds), [reference 2](https://docs.github.com/en/rest/repos/attestations), [reference 3](https://docs.github.com/en/rest/orgs/artifact-metadata).

### Registries, package ACL and trusted publishing

Group: `packages`. Capabilities: `packages-metadata`, `packages-registry`, `packages-access`, `packages-trusted-publishing`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| registry/form | OCI/GHCR, npm, NuGet, RubyGems granular; Maven/Gradle repository-scoped; host support | Choose only ecosystem actually distributed; REST metadata does not publish package bytes. | Install/pull exact version/digest from clean intended consumer. |
| authentication | GITHUB_TOKEN packages:read/write in workflow; supported classic PAT scopes for registry; registry-specific OIDC/trusted publishing | Prefer short-lived workflow credential; trusted-publishing support is registry-specific, not universal. | Verify exact registry trust configuration and authenticated clean install. |
| link and inheritance | repository link, inherited repository permissions, automatic inheritance org policy; explicit user/team ACL | Linked repo alone may not grant workflow access if ACL inheritance differs. | Read package settings/inheritance and intended principal access. |
| Actions access | selected repository access to granular package; separate Codespaces access | Grant only consumer/producer repos; token scope alone cannot override package ACL. | Test authorized workflow and excluded repo denial. |
| visibility | private/internal/public where supported; public transitions can be restricted/irreversible | Do not infer public package from public source repository. | Read package visibility and anonymous pull when intended. |
| versions/delete/restore | immutable consumer digest, tags, version metadata; package/version deletion; restoration eligibility/window | Do not delete versions still used; inspect downloads and restoration constraints first. | Read version ID and digest; restore and reinstall when authorized. |
| external trusted publisher | owner/repository/workflow/environment binding; OIDC permission and registry policy | For npm or other external registry, distinguish that registry from GitHub Packages. Verify registry official docs. | Perform registry-specific dry-run or publish only with release authorization; read resulting provenance. |

Project applicability: GITHUB.md explicitly says no separate package artifact requirement. Plugin marketplace/source releases currently satisfy distribution; do not publish artificial package.

History and human interaction: Retain package/version IDs, producer SHA, ACL reviewers and deprecation notices; preserve consumer compatibility.

Recovery: Correct package ACL/link narrowly; rotate exposed tokens; publish corrected immutable version/digest instead of relying on mutable tags.

- Pitfall: Community reports show packages:write token permission alone did not fix missing package inheritance/Actions access; inspect both.
- Pitfall: Classic PAT restrictions and SSO can block registry auth despite scope. Do not respond by granting broader scopes blindly.

Official sources: [reference 1](https://docs.github.com/en/packages/learn-github-packages/about-permissions-for-github-packages), [reference 2](https://docs.github.com/en/packages/learn-github-packages/publishing-a-package), [reference 3](https://docs.github.com/en/packages/learn-github-packages/deleting-and-restoring-a-package), [reference 4](https://docs.npmjs.com/trusted-publishers/).

Community / maintainer evidence: [discussion 1](https://github.com/orgs/community/discussions/32184), [discussion 2](https://github.com/orgs/community/discussions/57809).

### Pages source, DNS, TLS and publication

Group: `pages`. Capabilities: `pages-settings`, `pages-builds`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| build_type / source | legacy branch path root/docs or workflow; branch; custom workflow upload/deploy | Use source matching actual site generator; branch commits using GITHUB_TOKEN do not trigger branch Pages build. | Read Pages configuration and actual successful build/deployment SHA. |
| workflow grants / target | contents:read, pages:write, id-token:write; github-pages environment and artifact | Scope deployment permissions to job and keep environment protections. | Read uploaded Pages artifact, deployment status and environment. |
| custom domain | CNAME, DNS A/AAAA/CNAME records, domain verification, protected domain ownership | Verify domain before linking and remove stale DNS when disabling. | Read DNS health, ownership record and served hostname. |
| HTTPS | certificate provisioning and https_enforced when available | Wait for valid certificate before enforcing; inspect mixed content. | Verify HTTPS chain/hostname and HTTP redirect. |
| visibility / path | project site base path, public/private enterprise entitlement; repository visibility differs | Do not publish private source content without intended audience decision. | Fetch as intended anonymous/authenticated user and inspect base-path assets. |
| build/history/recovery | branch build/request; workflow Pages deployment status/cancel; external health | A successful build does not prove correct public content. | Fetch expected marker/version, navigation/assets and custom-domain redirect. |

Project applicability: No site requirement exists in GITHUB.md; keep Pages not-applicable until useful published site is requested.

History and human interaction: Record domain owner authorization, workflow approval and deployed SHA; preserve previous successful deployment for rollback.

Recovery: Redeploy prior verified site revision; correct source/base path/DNS, then recheck served bytes and TLS; deleting Pages alone leaves dangerous stale DNS.

Official sources: [reference 1](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), [reference 2](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), [reference 3](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [reference 4](https://docs.github.com/en/rest/pages/pages).

### Required check identity and review integration

Group: `checks-statuses`. Capabilities: `checks-runs`, `checks-suites`, `checks-commit-statuses`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| check run | name, head_sha, status/conclusion, started/completed timestamps, output/annotations, details_url; app identity | Stable unique names per required check; attach to exact tested SHA. | Read check name, app ID, head_sha and actual command evidence. |
| check suite | automatic creation preferences, rerequest, suite status | Suite success does not replace individual required checks; some writes are App-only. | Read suite and associated run conclusions. |
| commit status | context, state pending/success/failure/error, target_url, description | Keep context distinct from check-run names to avoid ambiguous requirement matching. | Read combined and individual statuses on intended SHA. |
| protection binding | required context/app, strict branch freshness, merge_group coverage; skipped/neutral semantics | Read rulesets and classic protection; require checks that actually test code. | Observe PR required check evaluation after latest push and merge-queue test commit. |

Project applicability: Existing three validation commands remain authoritative. Peer approval count zero is deliberate single-maintainer policy.

History and human interaction: Keep reviewer comments, check rerequest actor, force-push/stale-review history and final merge SHA; green unrelated SHA is insufficient.

Recovery: Fix missing event/name/app permission and rerun actual required check; never spoof status or remove protection to merge.

Official sources: [reference 1](https://docs.github.com/en/rest/checks/runs), [reference 2](https://docs.github.com/en/rest/checks/suites), [reference 3](https://docs.github.com/en/rest/commits/statuses), [reference 4](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks).

### Agentic workflows and constrained output

Group: `agentic-workflows`. Capabilities: `actions-agentic-workflows`.

| Option | Values / default | Decision rule | Verification |
| --- | --- | --- | --- |
| definition / compilation | Markdown instructions plus frontmatter; generated workflow; gh aw compile | Review generated YAML after instruction change and keep compiled artifact synchronized. | Compile and compare source/generated diff; inspect actual workflow SHA. |
| engine / credentials | supported Copilot/Codex/Claude/Gemini engine; engine-specific secret and billing | Choose only an authorized available engine and narrow authentication. | Check engine initialization and approved usage budget without exposing keys. |
| guardrails | read-only runtime, firewall/network, tools, explicit safe-outputs and threat-detection gates | Allow only requested outputs; proposed issue/comment/PR is still external action requiring existing authorization. | Inspect generated downstream write job permissions and resulting object IDs. |
| review / triggers | schedule/dispatch/events; allowed actors; human-reviewed PR outputs | Treat repository text as untrusted prompt input; retain human review before merge/deploy. | Exercise controlled input and inspect output safety/review history. |

Project applicability: Optional automation needs concrete recurring task, engine eligibility and authorized outputs; ordinary deterministic validation is sufficient now.

History and human interaction: Retain prompts/config revisions, generated proposals, human acceptance/rejection and exact downstream writes; do not call model output an independent approval.

Recovery: Disable affected workflow, stop pending writes and revoke compromised credentials; fix prompt/tool policy and inspect all emitted changes before reenable.

Official sources: [reference 1](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows), [reference 2](https://docs.github.com/en/actions/tutorials/develop-agentic-workflows-in-github-actions), [reference 3](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/about-github-agentic-workflows).

## Completeness and live verification boundary

This inventory decomposes the capability families listed in delivery-security.md into concrete choice groups. It is not a claim to mirror every field of every future REST/GraphQL schema, action input, cloud IAM provider, ecosystem registry or UI preview. Before acting, enumerate the current object schema and UI subsettings for the target host, compare every returned writable field against the desired configuration, and record omitted/unavailable fields explicitly. Link new material options here rather than hiding them behind a top-level enabled flag.

No external state was changed to produce this reference. Live reads/mutations, billing/entitlement checks, real approval interactions, provider access, package installs, release publication and deployment health checks require separate evidence in the task coverage ledger.
