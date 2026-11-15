# Delivery, security and distribution

Practical capability reference for Full GitHub. Official GitHub documentation was checked on 2026-11-15. This is a capability map, not evidence that a particular account, token, repository, GitHub Enterprise Server version or connected tool supports every operation.

## How to use this reference

- First inspect the repository, host, plan, effective role, token permissions, inherited policy and installed `gh` version. Prefer connected GitHub tools when they expose the complete operation; otherwise use `gh`, `gh api`, Git, the native package client or the documented UI. A native Codex skill can orchestrate these tools; it cannot invent missing connector methods or credentials.
- REST paths below are templates, not shell-ready commands. `...` retains the preceding resource prefix. URL-encode environment names, refs, package names and IDs correctly. Consult each linked operation for its exact method, request schema, required API version and supported token type. Never infer a mutation from an analogous read path.
- For repository REST calls use `gh api --paginate repos/OWNER/REPO/...` where appropriate; choose `--method GET` explicitly when passing query fields, and send structured write payloads through `--input` files. Preserve pagination and partial-read errors. An empty authorized list differs from a failed read; 403/404 can mean permission, policy, plan, host or feature restrictions.
- Every write needs the user's existing authorization and a read-back. Destructive removal, publication, independent approval, paid provisioning and secret access have different consequences; do not infer authority for them from this catalog. Perform safe inspection/preparation while a consequential decision remains unresolved.
- Evidence must identify object IDs, repository, SHA/ref, scope and relevant timestamps. Distinguish configuration saved, job queued, execution completed, artifact verified and application healthy. Never mark security coverage complete from configuration files alone.

## Permission and availability checklist

Actions inspection usually needs Actions read; execution control needs Actions write. Configuration often needs Administration or organization Actions management. Secrets, Variables, Environments, Deployments, Code scanning alerts, Dependabot alerts, Secret scanning alerts, Repository security advisories, Attestations, Packages and Pages each have their own endpoint-specific permissions. A broad classic PAT scope is not interchangeable with a fine-grained permission or GitHub App grant. SSO authorization, organization approval, IP policy and enterprise inheritance can still block a nominally permitted request.

Public and private repositories have different security, environment, attestation and Pages entitlements. New or preview REST families listed below require current host/version verification. Never enable a paid product, change account ownership or broaden access solely to satisfy a checklist. The relevant read response/settings screen and linked official plan documentation are the evidence of availability.

## Actions

### Workflow definitions and dispatch

Capability ID: `actions-workflows`.

Operations:

- Read/create/edit/delete .github/workflows/*.yml through Git commits or Contents API; inspect events, inputs, matrices, services, containers, permissions, timeouts and concurrency.
- List/get workflows; enable/disable; dispatch workflow_dispatch with ref and typed inputs.

Execution paths:

- `git; REST /repos/{owner}/{repo}/contents/.github/workflows`
- `GET /repos/{owner}/{repo}/actions/workflows; GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}`
- `PUT .../{workflow_id}/enable or /disable; POST .../{workflow_id}/dispatches`
- `gh workflow list/view/run/enable/disable; repository Actions tab`

Verification: Read committed YAML and workflow state; locate dispatched run by workflow/ref/event/SHA and inspect conclusion.

Constraints: Actions read/write permissions vary by operation. Workflow file writes require Contents and appropriate Workflows permission; dispatch must be configured and present on default branch. Dispatch acceptance is not execution success.

[Official documentation](https://docs.github.com/en/rest/actions/workflows).

### Workflow runs, attempts and execution control

Capability ID: `actions-runs`.

Operations:

- List/filter runs and attempts; read head SHA, event, status, conclusion and referenced workflows.
- Re-run all/failed jobs or one job and dependent jobs; enable debug; cancel/force cancel; delete runs.

Execution paths:

- `GET /repos/{owner}/{repo}/actions/runs; GET .../actions/runs/{run_id}; GET .../{run_id}/attempts/{attempt_number}`
- `POST .../{run_id}/rerun, /rerun-failed-jobs, /cancel, /force-cancel; POST .../actions/jobs/{job_id}/rerun; DELETE .../actions/runs/{run_id}`
- `gh run list/view/watch/rerun/cancel/delete`

Verification: Match current attempt, head_sha and required checks; record final conclusion and run URL.

Constraints: Actions read for inspection, write for control. Re-running may execute code and spend resources; deleted runs/logs cannot prove prior results.

[Official documentation](https://docs.github.com/en/rest/actions/workflow-runs).

### Jobs, steps and logs

Capability ID: `actions-job-logs`.

Operations:

- List jobs per run or attempt; inspect steps, runner assignment and timestamps.
- Download job, step, run and attempt logs; delete run logs.

Execution paths:

- `GET /repos/{owner}/{repo}/actions/runs/{run_id}/jobs; GET .../{run_id}/attempts/{attempt_number}/jobs`
- `GET .../actions/jobs/{job_id}; GET .../actions/jobs/{job_id}/logs; GET .../actions/jobs/{job_id}/steps/{step_number}/logs`
- `GET or DELETE .../actions/runs/{run_id}/logs; GET .../{run_id}/attempts/{attempt_number}/logs`
- `gh run view RUN --job JOB --log; gh run view RUN --log-failed`

Verification: Inspect actual failed step and current attempt; retain redacted evidence and log expiration status.

Constraints: Actions read; write for log deletion. Download redirects expire. Logs may contain secrets; redact output and do not treat masking as a complete security boundary.

[Official documentation](https://docs.github.com/en/rest/actions/workflow-jobs).

### Workflow artifacts

Capability ID: `actions-artifacts`.

Operations:

- List repository/run artifacts; inspect digest, expiration, size and associated run; download ZIP; delete.
- Upload/download in workflow with supported actions; set retention.

Execution paths:

- `GET /repos/{owner}/{repo}/actions/artifacts; GET .../actions/runs/{run_id}/artifacts`
- `GET/DELETE .../actions/artifacts/{artifact_id}; GET .../{artifact_id}/zip`
- `gh run download; actions/upload-artifact and actions/download-artifact`

Verification: Download intended run artifact, verify digest and archive contents, check expired=false.

Constraints: Actions read/write; retention/storage limits apply. REST management is not an arbitrary artifact-upload API; workflow artifact upload uses Actions tooling.

[Official documentation](https://docs.github.com/en/rest/actions/artifacts).

### Dependency caches and cache limits

Capability ID: `actions-caches`.

Operations:

- List by key/ref; inspect last access, size and usage; delete by ID/key.
- Get/set cache retention/storage limits at documented repository, organization or enterprise scope; inspect organization usage per repository.

Execution paths:

- `GET/DELETE /repos/{owner}/{repo}/actions/caches; DELETE .../caches/{cache_id}; GET .../actions/cache/usage`
- `GET/PUT .../actions/cache/retention-limit and /storage-limit where documented; organization /organizations/{org}/actions/cache equivalents; enterprise /enterprises/{enterprise}/actions/cache equivalents`
- `gh cache list/delete; actions/cache`

Verification: Read limits/usage after write; inspect a real cache restore/save in workflow logs.

Constraints: Write/admin permissions depend on scope and limit endpoint; inherited limits and billing apply. Cache is untrusted reusable input, not a release artifact or secret store.

[Official documentation](https://docs.github.com/en/rest/actions/cache).

### Repository, environment and organization variables

Capability ID: `actions-variables`.

Operations:

- List/get/create/update/delete variables.
- List/set/add/remove selected repository access for organization variables; inspect inherited organization variables.

Execution paths:

- `REST /repos/{owner}/{repo}/actions/variables and /{name}`
- `REST /repos/{owner}/{repo}/environments/{environment_name}/variables`
- `REST /orgs/{org}/actions/variables and /{name}/repositories`
- `gh variable list/get/set/delete --repo/--org/--env as supported`

Verification: Read effective scope, value and repository selection; verify vars consumption in the intended job.

Constraints: Variables are plaintext configuration. Variables read/write and environment/organization administrative authority depend on endpoint; plan and visibility affect organization access.

[Official documentation](https://docs.github.com/en/rest/actions/variables).

### Repository, environment and organization secrets

Capability ID: `actions-secrets`.

Operations:

- List/get metadata; encrypt and create/update using scope public key; delete.
- Manage organization secret visibility and selected repositories; list inherited organization secrets.

Execution paths:

- `REST /repos/{owner}/{repo}/actions/secrets and /public-key`
- `REST /repos/{owner}/{repo}/environments/{environment_name}/secrets`
- `REST /orgs/{org}/actions/secrets and /{secret_name}/repositories`
- `gh secret list/set/delete --repo/--org/--env; set via stdin or secure file`

Verification: Read metadata and selected repositories; use a minimal authorized workflow without echoing secret values.

Constraints: Secret values cannot be retrieved. Use Secrets read/write or scope-specific authority. Forks and Dependabot have distinct secret contexts; environment secrets require the environment gate. Never put plaintext secrets in issues, logs or command arguments.

[Official documentation](https://docs.github.com/en/rest/actions/secrets).

### Actions access, allowed actions and default token policy

Capability ID: `actions-permissions`.

Operations:

- Get/set organization/repository Actions enabled state, allowed actions/reusable workflows, selected repositories, workflow-token default permissions and PR creation/approval policy.
- Configure sharing of private reusable actions/workflows and organization self-hosted runner access.

Execution paths:

- `GET/PUT /repos/{owner}/{repo}/actions/permissions; .../permissions/selected-actions; .../permissions/workflow; .../permissions/access`
- `GET/PUT /orgs/{org}/actions/permissions and /repositories; .../self-hosted-runners`
- `Settings > Actions > General; workflow/job permissions YAML`

Verification: Re-read policy and inherited constraints; inspect actual GITHUB_TOKEN permissions in run setup.

Constraints: Administration or organization Actions permissions apply. Repository policy cannot loosen enterprise/organization restrictions. Keep read-only defaults and grant individual write permissions only for needed jobs.

[Official documentation](https://docs.github.com/en/rest/actions/permissions).

### Fork-run approvals and artifact/log retention policies

Capability ID: `actions-fork-retention`.

Operations:

- Get/set fork PR contributor approval and private-fork workflow settings.
- Get/set organization/repository artifact-and-log retention; inspect approval history and approve eligible fork run.

Execution paths:

- `GET/PUT .../actions/permissions/fork-pr-contributor-approval; .../fork-pr-workflows-private-repos; .../artifact-and-log-retention at repository/organization scope`
- `POST /repos/{owner}/{repo}/actions/runs/{run_id}/approve; GET .../{run_id}/approvals`

Verification: Read persisted settings; inspect approval actor and subsequent run with intended token/secret scope.

Constraints: Admin/policy rights and plan restrictions apply. Approval executes contributed code; inspect changes first. Never use pull_request_target to execute untrusted PR code with privileged secrets.

[Official documentation](https://docs.github.com/en/rest/actions/permissions).

### Actions policy objects

Capability ID: `actions-policies`.

Operations:

- List/get/create/update/delete repository and organization policy objects using documented rule schema.

Execution paths:

- `GET/POST /repos/{owner}/{repo}/actions/policies; GET/PUT/DELETE .../policies/{policy_id}`
- `GET/POST /orgs/{org}/actions/policies; GET/PUT/DELETE .../policies/{policy_id}`

Verification: Read returned policy, target scope and inheritance; check its effect in a relevant run.

Constraints: Policy administration permission and current rollout apply. This is separate from the established Actions permissions endpoints; do not invent rule fields or assume a GHES version supports it.

[Official documentation](https://docs.github.com/en/rest/actions/policies).

### Concurrency configuration and queue inspection

Capability ID: `actions-concurrency`.

Operations:

- Configure workflow/job concurrency groups and cancellation behavior.
- List repository/run concurrency groups; inspect one group.

Execution paths:

- `Git .github/workflows/*.yml concurrency; GET /repos/{owner}/{repo}/actions/concurrency_groups`
- `GET .../actions/concurrency_groups/{group_name}; GET .../actions/runs/{run_id}/concurrency_groups`

Verification: Compare configured group with observed pending/running work and cancellation conclusions.

Constraints: Inspection requires Actions read; changes go through workflow YAML. Do not assume a group cancellation mutation exists; cancel the identified runs via run API.

[Official documentation](https://docs.github.com/en/rest/actions/concurrency-groups).

### Reusable workflows, actions and templates

Capability ID: `actions-reusable`.

Operations:

- Create workflow_call inputs/secrets/outputs; invoke reusable workflow at job level; maintain shared workflow templates and composite/container/JavaScript action metadata.
- Pin caller uses to reviewed SHA; configure sharing; inspect called workflow references and permission propagation.

Execution paths:

- `Git .github/workflows/*.yml, action.yml and organization .github/workflow-templates`
- `GET/PUT /repos/{owner}/{repo}/actions/permissions/access; run referenced_workflows; Actions UI`

Verification: Run a real caller and verify inputs, outputs, called SHA, runner and least-privilege token.

Constraints: Nested workflows cannot elevate token permissions. Caller/called repositories must be accessible and allowed by policy; environment secrets and caller env do not automatically pass as workflow secrets/env.

[Official documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations).

### OIDC cloud identity and subject customization

Capability ID: `actions-oidc`.

Operations:

- Get/set repository/organization OIDC subject template; list/create/delete organization/enterprise custom property inclusion.
- Configure id-token: write and cloud trust for exact repository/ref/environment or workflow identity.

Execution paths:

- `GET/PUT /repos/{owner}/{repo}/actions/oidc/customization/sub; /orgs/{org}/actions/oidc/customization/sub`
- `REST organization/enterprise /actions/oidc/customization/properties/repo per current schema`
- `Workflow YAML and cloud-provider IAM configuration`

Verification: Verify non-sensitive token claims and a narrowly scoped cloud operation from intended job/environment.

Constraints: GitHub subject-template admin rights do not configure cloud IAM. id-token: write permits token issuance, not resource access. Changing subject shape can break existing trust; never print the JWT.

[Official documentation](https://docs.github.com/en/rest/actions/oidc).

### Self-hosted and just-in-time runners

Capability ID: `actions-self-hosted-runners`.

Operations:

- List/get runners, OS, online/busy state, applications and version EOL; issue registration/removal tokens or JIT configuration; remove runner.
- List/add/set/remove labels; configure ephemeral process and runner host.

Execution paths:

- `REST /repos/{owner}/{repo}/actions/runners and /{runner_id}/labels; /registration-token; /remove-token; /generate-jitconfig; /downloads`
- `Organization /orgs/{org}/actions/runners equivalents; Settings > Actions > Runners; runner config/run scripts`

Verification: Read online/label state and execute a harmless job on intended isolated runner; inspect cleanup.

Constraints: Administration or organization Self-hosted runners permissions; registration tokens are sensitive and temporary. API registration does not provision hardware or isolate untrusted workloads.

[Official documentation](https://docs.github.com/en/rest/actions/self-hosted-runners).

### Runner groups and repository/workflow access

Capability ID: `actions-runner-groups`.

Operations:

- List/get/create/update/delete runner groups.
- Manage selected repository access and runner membership; inspect hosted runners in group and selected workflow restrictions.

Execution paths:

- `REST /orgs/{org}/actions/runner-groups and /{runner_group_id}`
- `.../{runner_group_id}/repositories and /runners; organization Settings > Actions > Runner groups`

Verification: Re-read membership, visibility and allowed workflows; verify target repository can schedule an intended job.

Constraints: Organization authority and runner-group plan availability apply; inherited enterprise groups may be read-only. Group membership alone does not establish secure host isolation.

[Official documentation](https://docs.github.com/en/rest/actions/self-hosted-runner-groups).

### Managed larger runners, machine types and custom images

Capability ID: `actions-hosted-runners`.

Operations:

- List/create/get/update/delete configured hosted runners; inspect platforms, sizes, image choices and limits.
- List/get/delete custom image definitions/versions; build new images using documented image workflow.

Execution paths:

- `REST /orgs/{org}/actions/hosted-runners; /{hosted_runner_id}; /machine-sizes; /platforms; /limits`
- `.../images/github-owned; /images/partner; /images/custom and /{image_definition_id}/versions`
- `Organization Settings > Actions > Runners`

Verification: Read persisted runner/image version and run a representative job on the selected runner.

Constraints: Organization runner-management authority; supported paid plans, metered compute, platform and region limits. Custom image API management does not imply a generic image-upload endpoint.

[Official documentation](https://docs.github.com/en/rest/actions/hosted-runners).

## Deployments

### Environments, protection gates and branch/tag policies

Capability ID: `deploy-environments`.

Operations:

- List/get/create/update/delete environments; configure reviewers, wait timers, self-review prevention and bypass policy.
- List/create/update/delete deployment branch/tag policies; list/enable/disable custom GitHub App protection rules.

Execution paths:

- `REST /repos/{owner}/{repo}/environments and /{environment_name}`
- `.../{environment_name}/deployment-branch-policies; .../deployment_protection_rules`
- `Settings > Environments; workflow jobs.<id>.environment`

Verification: Re-read environment and rules; inspect a real job blocked/allowed by intended gate.

Constraints: Repository Administration read/write. Public repositories support environments across current plans; private/internal require an eligible paid plan. Reviewer/wait/custom-rule availability is narrower; inspect exact plan before promising support.

[Official documentation](https://docs.github.com/en/rest/deployments/environments).

### Pending deployments and custom protection decisions

Capability ID: `deploy-approval`.

Operations:

- List pending deployments and review history; approve/reject eligible environments with reason.
- Submit custom protection-rule result using the authorized GitHub App integration.

Execution paths:

- `GET/POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments; GET .../{run_id}/approvals`
- `POST .../{run_id}/deployment_protection_rule; Actions run > Review deployments`

Verification: Read approval actor/reason and subsequent job/deployment conclusion.

Constraints: Reviewer eligibility and prevent-self-review rules apply. Custom rule review must use authorized integration; an agent must not impersonate an independent required reviewer.

[Official documentation](https://docs.github.com/en/rest/actions/workflow-runs).

### Deployment records and status history

Capability ID: `deploy-records`.

Operations:

- List/get/create/delete deployments for ref, task and environment.
- Create/list/get deployment statuses with state, log/environment URLs, inactive/production flags.

Execution paths:

- `REST /repos/{owner}/{repo}/deployments and /{deployment_id}`
- `REST .../deployments/{deployment_id}/statuses and /{status_id}`
- `Repository deployments UI; actual deployment engine/cloud CLI separately`

Verification: Match deployment SHA/environment; inspect final status and visit deployed application with a meaningful health check.

Constraints: Deployments read/write; inactive-state deletion constraints apply. A deployment API record does not execute a deployment; success status alone is not application verification.

[Official documentation](https://docs.github.com/en/rest/deployments/deployments).

## Security

### Repository security products and reporting policy

Capability ID: `security-enablement`.

Operations:

- Inspect/update security_and_analysis, vulnerability-alert and automated-security-fixes settings; enable private vulnerability reporting where supported.
- Maintain SECURITY.md and security reporting route; inspect inherited organization configuration.

Execution paths:

- `GET/PATCH /repos/{owner}/{repo}; GET/PUT/DELETE .../vulnerability-alerts; GET/PUT/DELETE .../automated-security-fixes`
- `GET/PUT/DELETE .../private-vulnerability-reporting; Git SECURITY.md; Settings > Code security`

Verification: Read actual settings using eligible token; verify SECURITY.md rendered and private report entry point.

Constraints: Administration/security-manager authority; public/free and private paid Code Security/Secret Protection eligibility differ. SECURITY.md is policy text and does not enable scanning.

[Official documentation](https://docs.github.com/en/rest/repos/repos).

### Organization and enterprise security configurations

Capability ID: `security-configurations`.

Operations:

- List/get/create/update/delete configurations; inspect defaults; attach/detach repositories; set defaults.
- Select dependency graph/submission, Dependabot, Code Security, Secret Protection, reporting, delegated dismissal/bypass, validity/metadata and enforcement options.

Execution paths:

- `REST /orgs/{org}/code-security/configurations and /{configuration_id}; /defaults; /{configuration_id}/attach; /detach`
- `Repository /repos/{owner}/{repo}/code-security-configuration; enterprise routes where documented`
- `Organization Settings > Code security > Configurations`

Verification: Read configuration, associated repository application status and effective settings; asynchronous attachment must complete.

Constraints: Organization owner/security manager and Administration permission. Product licenses and enterprise policy constrain options; enabling paid products may consume licenses. Prefer individual code_security and secret_protection fields over deprecated combined values.

[Official documentation](https://docs.github.com/en/rest/code-security/configurations).

### CodeQL setup, databases and variant analyses

Capability ID: `security-codeql`.

Operations:

- Read/update default setup; alternatively maintain advanced CodeQL workflow/query packs/build mode.
- List/download/delete language databases; create/read variant analysis and per-repository result.

Execution paths:

- `GET/PATCH /repos/{owner}/{repo}/code-scanning/default-setup; Git advanced workflow`
- `REST .../code-scanning/codeql/databases; /databases/{language}; /codeql/variant-analyses and result routes`

Verification: Verify intended SHA/language/query suite produced a completed analysis.

Constraints: Security events/administrative rights; Code Security entitlement for private repositories. Default/advanced setup and language support constrain configuration.

[Official documentation](https://docs.github.com/en/rest/code-scanning/code-scanning).

### Code scanning alerts, analyses and SARIF

Capability ID: `security-code-alerts`.

Operations:

- List/filter/get/update alerts and instances; dismiss/reopen with reason; list/get/delete analyses.
- Upload compressed SARIF; poll processing.

Execution paths:

- `REST /repos/{owner}/{repo}/code-scanning/alerts and /{alert_number}/instances; /analyses`
- `POST .../code-scanning/sarifs; GET .../sarifs/{sarif_id}; organization alerts API`

Verification: Match processed SARIF/analysis to commit and tool; re-read alert state.

Constraints: Code scanning alerts read/write; SARIF validation/size limits and enabled product required. Accepted upload is not completed analysis.

[Official documentation](https://docs.github.com/en/rest/code-scanning/code-scanning).

### AI Scan and Copilot Autofix

Capability ID: `security-ai-autofix`.

Operations:

- Read/update organization/repository AI Scan enablement where available.
- Request/read autofix; commit reviewed fix.

Execution paths:

- `GET/PATCH /orgs/{org}/code-scanning/ai-scan and repository counterpart`
- `GET/POST .../code-scanning/alerts/{alert_number}/autofix; POST .../autofix/commits`

Verification: Inspect generated diff; run tests and re-scan.

Constraints: Product entitlement, policy, supported alert/language and extra commit permissions apply. Generated fixes require review; API presence does not guarantee account availability.

[Official documentation](https://docs.github.com/en/rest/code-scanning/code-scanning).

### Dependency submission and dependency review

Capability ID: `security-dependency-graph`.

Operations:

- Inspect dependency changes between base/head, vulnerabilities and licensing.
- Submit dependency snapshots for dependencies missing from supported manifests; configure automatic submission where supported.

Execution paths:

- `GET /repos/{owner}/{repo}/dependency-graph/compare/{basehead}`
- `POST /repos/{owner}/{repo}/dependency-graph/snapshots`
- `Dependency review Action; Insights > Dependency graph; PR dependency review`

Verification: Match resolved dependency diff/snapshot to commit and ecosystem; inspect review check.

Constraints: Dependency review private repositories requires eligible Code Security plan; graph must be enabled. Submission uses Contents write; incomplete manifests/build resolution produce incomplete inventory.

[Official documentation](https://docs.github.com/en/rest/dependency-graph/dependency-review).

### SBOM export and generated reports

Capability ID: `security-sbom`.

Operations:

- Export current dependency graph as SPDX SBOM.
- Request asynchronous report generation and fetch by returned UUID where available.

Execution paths:

- `GET /repos/{owner}/{repo}/dependency-graph/sbom`
- `GET .../dependency-graph/sbom/generate-report; GET .../sbom/fetch-report/{sbom_uuid}`
- `Insights > Dependency graph > Export SBOM`

Verification: Parse returned SPDX; inspect repository identity, generation time, package versions and coverage.

Constraints: Repository read/Contents read as documented; graph coverage bounds SBOM completeness. An SBOM is inventory, not a clean vulnerability scan or provenance attestation.

[Official documentation](https://docs.github.com/en/rest/dependency-graph/sboms).

### Dependabot alerts and security updates

Capability ID: `security-dependabot-alerts`.

Operations:

- List/get/filter alerts at repository/organization/enterprise scope; dismiss/reopen with documented reason.
- Inspect reachability/EPSS where returned; enable security updates and review remediation PRs.

Execution paths:

- `GET /repos/{owner}/{repo}/dependabot/alerts; GET/PATCH .../{alert_number}`
- `Organization/enterprise Dependabot alerts routes; repository automated-security-fixes endpoint; Security > Dependabot`

Verification: Re-read alert state; verify lockfile upgrade, passing PR checks and resolved alert after merge.

Constraints: Dependabot alerts read/write; organization/enterprise visibility limited by role. API documented as public preview. Dismissal does not remediate a vulnerability; update availability depends on ecosystem and fix.

[Official documentation](https://docs.github.com/en/rest/dependabot/alerts).

### Dependabot version updates and grouping

Capability ID: `security-dependabot-version`.

Operations:

- Create/edit dependabot.yml for ecosystem, directories, schedule, groups/multi-ecosystem groups, allow/ignore, cooldowns, registries, labels/assignees/reviewers and target branch where supported.
- Inspect update jobs/logs; trigger manual update and supported @dependabot PR commands.

Execution paths:

- `Git .github/dependabot.yml; Insights > Dependency graph > Dependabot`
- `Dependabot PR comments for documented rebase/recreate commands; PR APIs`

Verification: Read default-branch config; inspect actual update job and generated PR for each intended ecosystem.

Constraints: Per-ecosystem option support differs. Do not invent a generic REST create-version-update job endpoint. Version updates differ from vulnerability-triggered security updates; maintain both explicitly.

[Official documentation](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference).

### Dependabot registry credentials

Capability ID: `security-dependabot-secrets`.

Operations:

- List/get metadata, encrypt/create/update/delete repository/organization Dependabot secrets.
- Manage organization secret repository access and configure private registry references.

Execution paths:

- `REST /repos/{owner}/{repo}/dependabot/secrets and /public-key`
- `REST /orgs/{org}/dependabot/secrets and selected repositories`
- `gh secret --app dependabot list/set/delete; dependabot.yml registries`

Verification: Read secret metadata and repository selection; inspect authorized registry resolution without logging credentials.

Constraints: Dependabot secrets permissions; distinct from Actions secrets and unavailable for plaintext retrieval. Organization private repository access and plan restrictions apply.

[Official documentation](https://docs.github.com/en/rest/dependabot/secrets).

### Dependabot runner and private repository access settings

Capability ID: `security-dependabot-runtime`.

Operations:

- Read/set standard or labeled runner settings, labels and runner group.
- List/update organization/enterprise repository access list and default access level.

Execution paths:

- `GET/PUT /repos/{owner}/{repo}/dependabot/runner-settings`
- `REST /orgs/{org}/dependabot/repository-access and /default-level; enterprise equivalents`

Verification: Read effective runner settings and inspect dependency-update job on intended runner; check allowed private repository dependency resolution.

Constraints: Labeled runners only take effect for private/internal repositories with Actions enabled. Repository-access management has separate owner/token requirements; inspect its official endpoint documentation before writes.

[Official documentation](https://docs.github.com/en/rest/dependabot/runner-settings).

### Secret scanning alerts, locations and scan history

Capability ID: `security-secret-alerts`.

Operations:

- List/get/filter alerts and locations; resolve/reopen with documented reason; inspect validity and push-protection context.
- Inspect repository scan history; enable scanning through repository security settings.

Execution paths:

- `REST /repos/{owner}/{repo}/secret-scanning/alerts and /{alert_number}/locations`
- `GET .../secret-scanning/scan-history; organization alerts endpoint; Settings > Code security`

Verification: Re-read alert/resolution; verify leaked credentials revoked with provider and inspect relevant scan coverage.

Constraints: Secret scanning alerts read/write and product eligibility. Responses can include secret values; redact them. Resolving an alert never revokes a credential.

[Official documentation](https://docs.github.com/en/rest/secret-scanning/secret-scanning).

### Push protection and governed exceptions

Capability ID: `security-push-protection`.

Operations:

- Inspect/enable repository push protection, delegated bypass and dismissal policy.
- Use documented bypass request/review path only for explicitly authorized false positive/test secret; inspect pattern configurations.

Execution paths:

- `PATCH /repos/{owner}/{repo} security_and_analysis; organization security configuration`
- `POST .../secret-scanning/push-protection-bypasses; UI bypass/review flow`
- `GET/PATCH /orgs/{org}/secret-scanning/pattern-configurations`

Verification: Read policy and actual reviewed bypass record; test safe non-sensitive detection only when authorized.

Constraints: Secret Protection/plan and delegated reviewer eligibility apply. User-level push protection differs from repository-level scanning. Never bypass a real leaked secret to make a push succeed.

[Official documentation](https://docs.github.com/en/rest/secret-scanning/push-protection).

### Secret custom patterns and validity controls

Capability ID: `security-custom-patterns`.

Operations:

- List/create/update/delete organization/repository custom patterns through documented bulk APIs.
- Configure push-protection participation; use supported dry-run/publish and validity/metadata settings.

Execution paths:

- `GET/POST/DELETE /orgs/{org}/secret-scanning/custom-patterns and repository counterparts; PATCH .../custom-patterns/{pattern_id}; Settings > Code security > Secret scanning`
- `Organization security configurations for validity, extended metadata and generic/AI pattern options`

Verification: Inspect returned pattern IDs/version and test safe positive/negative examples; verify published detection.

Constraints: Pattern and product permissions apply; some controls require UI or current schema-specific endpoints. Extended metadata requires validity checks. Do not send live credentials as pattern test samples.

[Official documentation](https://docs.github.com/en/rest/secret-scanning/custom-patterns).

### Repository advisories, private reports and coordinated disclosure

Capability ID: `security-advisories`.

Operations:

- List/get/create/update advisories, draft/publish/withdraw where allowed; privately report vulnerabilities.
- Read/create/edit comments; create temporary private fix fork; request CVE.

Execution paths:

- `REST /repos/{owner}/{repo}/security-advisories and /{ghsa_id}; /reports; /{ghsa_id}/forks; /{ghsa_id}/cve`
- `Advisory comment routes; organization advisory listing; Security > Advisories`

Verification: Read advisory state, vulnerable/fixed ranges, collaborators, CVE and publication URL; verify fix release exists.

Constraints: Repository security advisory permission and collaborator role govern confidential data; private reporting must be enabled. Publishing discloses details publicly; scope authorization separately from drafting.

[Official documentation](https://docs.github.com/en/rest/security-advisories/repository-advisories).

### GitHub Advisory Database lookup

Capability ID: `security-global-advisories`.

Operations:

- Search/filter/list reviewed and unreviewed advisories; get GHSA details and affected package versions.

Execution paths:

- `GET /advisories; GET /advisories/{ghsa_id}; GitHub Advisory Database UI`

Verification: Match ecosystem/package/version and patched range to actual dependency graph.

Constraints: Lookup is evidence, not an exploitability assessment; absent advisory does not establish safety. Respect pagination and update timestamps.

[Official documentation](https://docs.github.com/en/rest/security-advisories/global-advisories).

### Security coverage, campaigns, bypass and dismissal review

Capability ID: `security-overview`.

Operations:

- Inspect organization security coverage/risk and prioritize alerts; manage delegated review where the account exposes it.
- Track fixes via issues/PRs and re-read security state.

Execution paths:

- `Organization Security > Overview; security configurations and documented product APIs`
- `UI for campaign/delegated-review controls without a verified public mutation; export available reports`

Verification: Record account-visible coverage/review and individual resolved findings, including exclusions.

Constraints: Organization security-manager rights and product/preview availability. Do not claim every UI control has REST/GraphQL write support; record unsupported mutations as UI handoff.

[Official documentation](https://docs.github.com/en/code-security/getting-started/github-security-features).

### Published security campaigns

Capability ID: `security-campaigns`.

Operations:

- List/get/create/update/delete published campaigns; configure managers/teams, deadline, contact and code scanning alert selection; optionally generate issues.
- Use UI for draft campaigns and inspect remediation progress.

Execution paths:

- `GET/POST /orgs/{org}/campaigns; GET/PATCH/DELETE /orgs/{org}/campaigns/{campaign_number}`
- `Organization Security > Campaigns`

Verification: Read campaign state, managers, deadline and alert counts; confirm actual alert remediation and generated issues.

Constraints: Organization owner/security manager; Campaigns read/write and Code scanning alerts read for included repositories. Draft campaigns cannot be read or managed through these REST endpoints; product eligibility applies.

[Official documentation](https://docs.github.com/en/rest/campaigns/campaigns).

### Code quality findings and setup

Capability ID: `security-code-quality`.

Operations:

- List/filter/get findings; inspect locations, rules and severity.
- Get/update setup configuration through documented schema; verify intended analysis coverage.

Execution paths:

- `GET /repos/{owner}/{repo}/code-quality/findings; GET .../findings/{finding_number}`
- `GET/PATCH /repos/{owner}/{repo}/code-quality/setup; repository code quality UI`

Verification: Read configured setup and findings for intended revision; inspect resulting analysis/checks.

Constraints: Use endpoint-specific Code quality permissions and current product eligibility. Findings API is read-only; do not invent finding-dismissal or fix-commit mutation from code scanning equivalents.

[Official documentation](https://docs.github.com/en/rest/code-quality/code-quality).

## Releases

### Drafts, publication, prereleases and generated notes

Capability ID: `releases-lifecycle`.

Operations:

- List/get latest/by-tag releases; create draft, edit title/body/target, publish, mark prerelease/latest, delete where allowed.
- Generate notes and maintain .github/release.yml categorization; link discussion category where supported.

Execution paths:

- `REST /repos/{owner}/{repo}/releases; /latest; /tags/{tag}; /{release_id}; /generate-notes`
- `gh release list/view/create/edit/delete; git tags; Releases UI`

Verification: Read published release, exact tag/commit, draft/prerelease/latest state and release notes; compare version source.

Constraints: Contents write and repository policy; release creation can create a tag. A Git tag and a GitHub Release are distinct. Published latest excludes drafts/prereleases by semantics; do not infer from sorted tags.

[Official documentation](https://docs.github.com/en/rest/releases/releases).

### Release assets and binary integrity

Capability ID: `releases-assets`.

Operations:

- List/get/download/upload assets; rename/relabel/delete where mutable.
- Inspect digest/content type/size and exact archive contents before publication.

Execution paths:

- `REST /repos/{owner}/{repo}/releases/{release_id}/assets; /releases/assets/{asset_id}`
- `POST returned upload_url on uploads.github.com with binary body and name; gh release upload/download/delete-asset`
- `gh release verify-asset where supported`

Verification: Download published bytes and verify expected checksum/content/version; re-read asset metadata and download URL.

Constraints: Contents read/write. Asset uploads are separate from creating release; partial uploads need reconciliation. Immutable published releases prohibit asset modification/deletion.

[Official documentation](https://docs.github.com/en/rest/releases/assets).

### Immutable releases and release attestations

Capability ID: `releases-immutable`.

Operations:

- Enable repository or organization immutability policy for future releases; create draft, attach complete assets, then publish.
- Verify release attestation/tag/assets; edit allowed title/notes/prerelease/latest metadata.

Execution paths:

- `Repository Settings > General > Releases > Enable release immutability`
- `Organization Settings > Repository > General > Releases; GET/PUT/DELETE /repos/{owner}/{repo}/immutable-releases; GET/PUT /orgs/{org}/settings/immutable-releases and selected repositories routes`
- `gh release verify; gh release verify-asset; release immutable field/badge`

Verification: Read immutable state; verify attestation, locked tag commit and downloaded asset digests.

Constraints: Only future releases are affected. Published tag/assets are protected; do not promise replacing assets or reusing protected tag names. Confirm installed gh supports verification commands; policy configuration UI is the documented fallback.

[Official documentation](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases).

## Attestations

### Build provenance and SBOM attestations

Capability ID: `attestations-provenance`.

Operations:

- Generate signed provenance/SBOM attestations in Actions; associate Sigstore bundle with repository.
- Get/download attestations by subject digest; verify binary or OCI image against expected repo/workflow/identity.

Execution paths:

- `actions/attest or documented provenance/SBOM Actions; workflow id-token: write and attestations: write`
- `POST /repos/{owner}/{repo}/attestations; GET .../attestations/{subject_digest}; organization/user digest lookup routes`
- `gh attestation download/verify/trusted-root; OCI registry digest`

Verification: Verify downloaded bytes/digest, certificate identity, workflow/ref and transparency/issuer policy, not merely bundle presence.

Constraints: Public repositories on current plans; private/internal need Enterprise Cloud. Creating needs repository write/Attestations write; OIDC is needed for workflow identity. Provenance is not a vulnerability guarantee.

[Official documentation](https://docs.github.com/en/rest/repos/attestations).

### Linked artifact storage and deployment metadata

Capability ID: `attestations-linked-artifacts`.

Operations:

- Record artifact storage/deployment information keyed by digest; list known records.
- Set cluster deployment records directly or create asynchronous cluster records job and poll status.

Execution paths:

- `POST /orgs/{org}/artifacts/metadata/storage-record; POST .../metadata/deployment-record`
- `GET /orgs/{org}/artifacts/{subject_digest}/metadata/storage-records or /deployment-records`
- `POST .../metadata/deployment-record/cluster/{cluster}; POST .../cluster/{cluster}/jobs; GET .../jobs/{job_id}`
- `Organization linked artifacts page`

Verification: Read digest-associated records and completed job; cross-check actual registry bytes and deployed workload digest.

Constraints: Repository Artifact metadata permission and linked-artifact product/rollout eligibility. Metadata does not push a binary or deploy it; only record actual observed storage/deployment facts.

[Official documentation](https://docs.github.com/en/rest/orgs/artifact-metadata).

## Packages

### Packages and versions lifecycle

Capability ID: `packages-metadata`.

Operations:

- List/get packages and versions by organization/user; inspect metadata/digests.
- Delete/restore packages or versions where supported; inspect migration conflicts if relevant.

Execution paths:

- `REST /orgs/{org}/packages and /{package_type}/{package_name}/versions; corresponding /users/{username} and /user routes`
- `DELETE package/version route; POST .../restore; package settings UI`

Verification: Read version/digest/visibility and test installation before declaring delivery; verify deletion or restoration state.

Constraints: Management REST requires documented classic PAT scopes; GITHUB_TOKEN has supported package workflow exceptions. Admin permission required for destructive operations; retention/restoration limits and download-count safeguards apply.

[Official documentation](https://docs.github.com/en/rest/packages/packages).

### Registry publishing, installation and authentication

Capability ID: `packages-registry`.

Operations:

- Build and publish/install OCI/container, npm, RubyGems, Maven/Gradle and NuGet packages with ecosystem tools.
- Configure namespace, package/repository link, immutable version/digest and workflow package permissions.

Execution paths:

- `docker/podman for ghcr.io; npm for npm.pkg.github.com; gem for rubygems.pkg.github.com; mvn/gradle for maven.pkg.github.com; dotnet nuget for nuget.pkg.github.com`
- `Workflow GITHUB_TOKEN with packages permissions or authorized classic PAT; ecosystem auth configuration`

Verification: Install/pull exact published version/digest from a clean consumer and run a meaningful smoke check.

Constraints: Supported registries differ by host/plan. REST package metadata management is not a generic publishing API. Never expose registry tokens in source/config logs; storage/data-transfer billing applies.

[Official documentation](https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages).

### Package visibility, linked repository and access control

Capability ID: `packages-access`.

Operations:

- Inspect/configure granular user/team/repository access, inherited repository access, Actions/Codespaces access, visibility and linked repository.
- Reconcile organization package creation/visibility policy.

Execution paths:

- `Package page > Package settings > Manage access/Actions/Codespaces access; organization Settings > Packages`
- `OCI org.opencontainers.image.source or ecosystem repository metadata for package linkage`

Verification: Inspect effective package ACL and test consumer/workflow access using intended principal.

Constraints: Registry permissions differ: granular versus repository-scoped. Public repository does not necessarily make its package public. Visibility transitions and inherited ACL have restrictions; unverified UI mutations remain handoff.

[Official documentation](https://docs.github.com/en/packages/learn-github-packages/about-permissions-for-github-packages).

## Pages

### Pages source, custom domain, TLS and visibility

Capability ID: `pages-settings`.

Operations:

- Get/create/update/delete site; choose branch/path or Actions build source; set custom domain/HTTPS where supported.
- Inspect DNS health; configure domain verification/DNS and access policy through authorized owning service.

Execution paths:

- `GET/POST/PUT/DELETE /repos/{owner}/{repo}/pages; GET .../pages/health`
- `Settings > Pages; Git CNAME for applicable source; DNS provider and owner verified-domain settings`

Verification: Read site source/domain/HTTPS state and DNS health; request public/authorized URL and verify content, certificate and redirects.

Constraints: Pages permissions plus repository admin/Contents rights for some writes. Private repository source does not guarantee a private site; private publishing/access control requires eligible Enterprise Cloud configuration.

[Official documentation](https://docs.github.com/en/rest/pages/pages).

### Pages builds and Actions deployments

Capability ID: `pages-builds`.

Operations:

- List/get/request legacy Pages builds and inspect latest status.
- Upload Pages artifact in Actions; create/get/cancel Pages deployment; inspect environment status and deployed SHA.

Execution paths:

- `GET/POST /repos/{owner}/{repo}/pages/builds; GET .../builds/latest and /{build_id}`
- `POST .../pages/deployments; GET .../deployments/{pages_deployment_id}; POST .../{id}/cancel`
- `actions/configure-pages, actions/upload-pages-artifact, actions/deploy-pages; github-pages environment`

Verification: Require completed build/deployment for intended SHA and inspect rendered site/assets at site URL.

Constraints: Workflow deploy needs pages: write and id-token: write plus environment policy. Accepted deployment is not live success; custom workflow artifacts must satisfy Pages packaging constraints.

[Official documentation](https://docs.github.com/en/rest/pages/pages).

## Additional delivery capability families

### Check runs, output annotations and requested actions

Capability ID: `checks-runs`.

Operations:

- List runs by ref/suite; get run and paginated annotations; create/update run name, head SHA, state/conclusion, details URL, output, images and requested-action buttons.
- Append line annotations in batches; rerequest run and handle check_run webhook requested_action/rerequested.

Execution paths:

- `GET /repos/{owner}/{repo}/commits/{ref}/check-runs; GET .../check-suites/{check_suite_id}/check-runs; GET .../check-runs/{check_run_id}/annotations`
- `POST .../check-runs; GET/PATCH .../check-runs/{check_run_id}; POST .../check-runs/{check_run_id}/rerequest`
- `GraphQL CheckRun/CheckAnnotation; createCheckRun and updateCheckRun; gh api; PR Checks tab`

Verification: Read run head_sha, owning App, conclusion, output and annotation locations; verify execution independently before reporting success.

Constraints: Checks read/write and operation-specific App/token eligibility. Creation requires GitHub App identity; do not infer create rights from a token that can rerequest. Maximum 50 annotations per request; updates append. Rerequest emits event and does not itself update the run. Never manufacture passing checks.

[Official documentation](https://docs.github.com/en/rest/checks/runs).

### Check suites, preferences and rerequest

Capability ID: `checks-suites`.

Operations:

- List/get suites for Git ref and associated runs; inspect App, branch, SHA, status and conclusion.
- Create suite where manual flow is needed; update automatic suite-creation preferences by App; rerequest suite.

Execution paths:

- `GET /repos/{owner}/{repo}/commits/{ref}/check-suites; GET .../check-suites/{check_suite_id}; POST .../check-suites`
- `PATCH .../check-suites/preferences; POST .../check-suites/{check_suite_id}/rerequest`
- `GraphQL Commit.checkSuites, CheckSuite.checkRuns; createCheckSuite, updateCheckSuitePreferences, rerequestCheckSuite`

Verification: Inspect latest suite for intended SHA and actual constituent runs; after rerequest observe new execution and resulting conclusion.

Constraints: Checks read/write; suite creation is GitHub App-only; each operation lists supported token types. App ownership and repository push visibility apply. Fork-only pushes may return empty matching PR data. Rerequest queues an event, not successful execution.

[Official documentation](https://docs.github.com/en/rest/checks/suites).

### Commit status contexts and combined check visibility

Capability ID: `checks-commit-statuses`.

Operations:

- Create pending/success/failure/error commit status with context, description and target URL; list history and combined latest state by ref.
- Inspect combined Checks and StatusContext rollup for exact PR head or merge-group SHA and compare required checks/rules.

Execution paths:

- `POST /repos/{owner}/{repo}/statuses/{sha}; GET .../commits/{ref}/statuses; GET .../commits/{ref}/status`
- `GraphQL Commit.status and statusCheckRollup.contexts with CheckRun/StatusContext fragments; gh pr checks; PR checks UI`

Verification: Read back latest status for the exact SHA/context and expected creator; inspect Checks separately and compare required-check source App where configured.

Constraints: Commit statuses read/write permission; checks are distinct objects and combined-status REST excludes check runs. Status creation appends history; there is no arbitrary status edit/delete API. A pending/success rollup is not independent proof that a required trusted check executed.

[Official documentation](https://docs.github.com/en/rest/commits/statuses).

### Trusted publishing to external package registries

Capability ID: `packages-trusted-publishing`.

Operations:

- Configure a registry trusted publisher bound to GitHub repository/workflow and optional environment; grant job id-token: write and publish validated package without long-lived publishing token.
- Support PyPI trusted publishing and npm trusted publishers through their native registry configuration; inspect provenance, version and published bytes.

Execution paths:

- `PyPI project Settings > Publishing; pypa/gh-action-pypi-publish; GitHub Actions release workflow and protected environment`
- `npmjs.com package Settings > Trusted publishing; npm publish or supported npm trust CLI; https://docs.npmjs.com/trusted-publishers/`
- `External registry-native API/UI; Git commits and Actions logs; no GitHub Packages trusted-publisher CRUD endpoint is implied`

Verification: Read registry trust binding, run authorized release workflow, download/install exact published distribution and inspect registry provenance with intended repository/workflow identity.

Constraints: External registry package-owner authorization and current runner/CLI limits apply. npm trusted publishing currently requires supported cloud-hosted runners and modern npm/Node versions; install/private dependency access may still require separate credentials. Registry trust is not configured by editing GitHub YAML; GitHub Packages uses its documented authentication instead.

[Official documentation](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-pypi).

### GitHub Agentic Workflows authoring and execution

Capability ID: `actions-agentic-workflows`.

Operations:

- Author Markdown workflow with triggers, permissions, engine and safe outputs; compile .lock.yml and commit both files; import/update reviewed upstream workflow with source reference.
- Run workflow; inspect logs/audit/token usage and estimated inference cost; adjust prompts/configuration and recompile.

Execution paths:

- `Git .github/workflows/NAME.md and NAME.lock.yml; gh extension install github/gh-aw when authorized`
- `gh aw init/add/compile/run/logs/audit/update; GitHub Actions UI and standard run/job APIs`
- `Supported Copilot/Codex/Claude/Gemini engine identity and secure credential setup; frontmatter permissions, safe outputs and network controls`

Verification: Review compiled workflow and declared outputs; run a narrowly scoped task and inspect actual issue/PR/comment, run logs, safe-output decisions and cost.

Constraints: Requires Actions, repository write, installed gh aw and selected engine entitlement/credential; Actions and inference incur separate costs. Imports/initialization modify repository files and may create PRs; inspect first. Untrusted repository text remains untrusted; engine availability does not imply write authorization. GitHub Models is retired and is not this feature.

[Official documentation](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows).

Additional references: [GraphQL Checks](https://docs.github.com/en/graphql/reference/checks), [GraphQL commits and status rollups](https://docs.github.com/en/graphql/reference/commits), [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/), [agentic workflow architecture and billing](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-github-agentic-workflows). GitHub Models retirement is covered by the administration reference; do not use its historical catalog/inference APIs to implement these workflows.

## Additional official operation references

Use these when a row spans more than one endpoint family:

- [Deployment protection rules](https://docs.github.com/en/rest/deployments/protection-rules), [branch policies](https://docs.github.com/en/rest/deployments/branch-policies), and [deployment statuses](https://docs.github.com/en/rest/deployments/statuses).
- [Dependabot private repository access](https://docs.github.com/en/rest/dependabot/repository-access), [dependency submission](https://docs.github.com/en/rest/dependency-graph/dependency-submission), and [Dependabot options](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference).
- [Secret alert and bypass operations](https://docs.github.com/en/rest/secret-scanning/secret-scanning), [custom patterns](https://docs.github.com/en/rest/secret-scanning/custom-patterns), and [pattern push-protection configuration](https://docs.github.com/en/rest/secret-scanning/push-protection).
- [Enable release immutability](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes), [repository immutable-release API](https://docs.github.com/en/rest/repos/repos#check-if-immutable-releases-are-enabled-for-a-repository), [organization immutable-release API](https://docs.github.com/en/rest/orgs/orgs#get-immutable-releases-settings-for-an-organization), [attestation verification](https://cli.github.com/manual/gh_attestation_verify), and [release CLI](https://cli.github.com/manual/gh_release).
- [Package permissions](https://docs.github.com/en/packages/learn-github-packages/about-permissions-for-github-packages) and [package registries](https://docs.github.com/en/packages/working-with-a-github-packages-registry).

## Required recorded gaps

A feature is **unsupported**, **unavailable**, **not applicable** or **unverified** only with its reason recorded. Keep separate gaps for connector surface, CLI version, missing permission, plan restriction, inherited policy, unavailable preview and uninspected UI. For UI-managed controls, give the exact owning settings page and a concrete verification step; a README instruction does not configure that page. Cloud IAM, DNS, package consumers and runner hardware require evidence from those external systems. Nothing in this reference claims live settings, tests, publication or account availability were verified.
