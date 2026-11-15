# GitHub capability directory

Reviewed 2026-11-15. 261 feature families.

Search using python3 scripts/operations.py capabilities TERM. Inspect a family using capability ID.

Each linked official source defines current permissions, product limits and operation details. The catalog records available interfaces and evidence requirements. Live verification is recorded separately in https://github.com/thinkhome-org/full-github/blob/main/docs/VERIFICATION.md.

## Actions

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| actions-workflows | Workflow definitions and dispatch | git; REST /repos/{owner}/{repo}/contents/.github/workflows, GET /repos/{owner}/{repo}/actions/workflows; GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}, PUT .../{workflow_id}/enable or /disable; POST .../{workflow_id}/dispatches, gh workflow list/view/run/enable/disable; repository Actions tab | [Docs 1](https://docs.github.com/en/rest/actions/workflows) |
| actions-runs | Workflow runs, attempts and execution control | GET /repos/{owner}/{repo}/actions/runs; GET .../actions/runs/{run_id}; GET .../{run_id}/attempts/{attempt_number}, POST .../{run_id}/rerun, /rerun-failed-jobs, /cancel, /force-cancel; POST .../actions/jobs/{job_id}/rerun; DELETE .../actions/runs/{run_id}, gh run list/view/watch/rerun/cancel/delete | [Docs 1](https://docs.github.com/en/rest/actions/workflow-runs) |
| actions-job-logs | Jobs, steps and logs | GET /repos/{owner}/{repo}/actions/runs/{run_id}/jobs; GET .../{run_id}/attempts/{attempt_number}/jobs, GET .../actions/jobs/{job_id}; GET .../actions/jobs/{job_id}/logs; GET .../actions/jobs/{job_id}/steps/{step_number}/logs, GET or DELETE .../actions/runs/{run_id}/logs; GET .../{run_id}/attempts/{attempt_number}/logs, gh run view RUN --job JOB --log; gh run view RUN --log-failed | [Docs 1](https://docs.github.com/en/rest/actions/workflow-jobs) |
| actions-artifacts | Workflow artifacts | GET /repos/{owner}/{repo}/actions/artifacts; GET .../actions/runs/{run_id}/artifacts, GET/DELETE .../actions/artifacts/{artifact_id}; GET .../{artifact_id}/zip, gh run download; actions/upload-artifact and actions/download-artifact | [Docs 1](https://docs.github.com/en/rest/actions/artifacts) |
| actions-caches | Dependency caches and cache limits | GET/DELETE /repos/{owner}/{repo}/actions/caches; DELETE .../caches/{cache_id}; GET .../actions/cache/usage, GET/PUT .../actions/cache/retention-limit and /storage-limit where documented; organization /organizations/{org}/actions/cache equivalents; enterprise /enterprises/{enterprise}/actions/cache equivalents, gh cache list/delete; actions/cache | [Docs 1](https://docs.github.com/en/rest/actions/cache) |
| actions-variables | Repository, environment and organization variables | REST /repos/{owner}/{repo}/actions/variables and /{name}, REST /repos/{owner}/{repo}/environments/{environment_name}/variables, REST /orgs/{org}/actions/variables and /{name}/repositories, gh variable list/get/set/delete --repo/--org/--env as supported | [Docs 1](https://docs.github.com/en/rest/actions/variables) |
| actions-secrets | Repository, environment and organization secrets | REST /repos/{owner}/{repo}/actions/secrets and /public-key, REST /repos/{owner}/{repo}/environments/{environment_name}/secrets, REST /orgs/{org}/actions/secrets and /{secret_name}/repositories, gh secret list/set/delete --repo/--org/--env; set via stdin or secure file | [Docs 1](https://docs.github.com/en/rest/actions/secrets) |
| actions-permissions | Actions access, allowed actions and default token policy | GET/PUT /repos/{owner}/{repo}/actions/permissions; .../permissions/selected-actions; .../permissions/workflow; .../permissions/access, GET/PUT /orgs/{org}/actions/permissions and /repositories; .../self-hosted-runners, Settings > Actions > General; workflow/job permissions YAML | [Docs 1](https://docs.github.com/en/rest/actions/permissions) |
| actions-fork-retention | Fork-run approvals and artifact/log retention policies | GET/PUT .../actions/permissions/fork-pr-contributor-approval; .../fork-pr-workflows-private-repos; .../artifact-and-log-retention at repository/organization scope, POST /repos/{owner}/{repo}/actions/runs/{run_id}/approve; GET .../{run_id}/approvals | [Docs 1](https://docs.github.com/en/rest/actions/permissions) |
| actions-policies | Actions policy objects | GET/POST /repos/{owner}/{repo}/actions/policies; GET/PUT/DELETE .../policies/{policy_id}, GET/POST /orgs/{org}/actions/policies; GET/PUT/DELETE .../policies/{policy_id} | [Docs 1](https://docs.github.com/en/rest/actions/policies) |
| actions-concurrency | Concurrency configuration and queue inspection | Git .github/workflows/*.yml concurrency; GET /repos/{owner}/{repo}/actions/concurrency_groups, GET .../actions/concurrency_groups/{group_name}; GET .../actions/runs/{run_id}/concurrency_groups | [Docs 1](https://docs.github.com/en/rest/actions/concurrency-groups) |
| actions-reusable | Reusable workflows, actions and templates | Git .github/workflows/*.yml, action.yml and organization .github/workflow-templates, GET/PUT /repos/{owner}/{repo}/actions/permissions/access; run referenced_workflows; Actions UI | [Docs 1](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations) |
| actions-oidc | OIDC cloud identity and subject customization | GET/PUT /repos/{owner}/{repo}/actions/oidc/customization/sub; /orgs/{org}/actions/oidc/customization/sub, REST organization/enterprise /actions/oidc/customization/properties/repo per current schema, Workflow YAML and cloud-provider IAM configuration | [Docs 1](https://docs.github.com/en/rest/actions/oidc) |
| actions-self-hosted-runners | Self-hosted and just-in-time runners | REST /repos/{owner}/{repo}/actions/runners and /{runner_id}/labels; /registration-token; /remove-token; /generate-jitconfig; /downloads, Organization /orgs/{org}/actions/runners equivalents; Settings > Actions > Runners; runner config/run scripts | [Docs 1](https://docs.github.com/en/rest/actions/self-hosted-runners) |
| actions-runner-groups | Runner groups and repository/workflow access | REST /orgs/{org}/actions/runner-groups and /{runner_group_id}, .../{runner_group_id}/repositories and /runners; organization Settings > Actions > Runner groups | [Docs 1](https://docs.github.com/en/rest/actions/self-hosted-runner-groups) |
| actions-hosted-runners | Managed larger runners, machine types and custom images | REST /orgs/{org}/actions/hosted-runners; /{hosted_runner_id}; /machine-sizes; /platforms; /limits, .../images/github-owned; /images/partner; /images/custom and /{image_definition_id}/versions, Organization Settings > Actions > Runners | [Docs 1](https://docs.github.com/en/rest/actions/hosted-runners) |
| actions-agentic-workflows | GitHub Agentic Workflows authoring and execution | Git .github/workflows/NAME.md and NAME.lock.yml; gh extension install github/gh-aw when authorized, gh aw init/add/compile/run/logs/audit/update; GitHub Actions UI and standard run/job APIs, Supported Copilot/Codex/Claude/Gemini engine identity and secure credential setup; frontmatter permissions, safe outputs and network controls | [Docs 1](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows) |

## Attestations

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| attestations-provenance | Build provenance and SBOM attestations | actions/attest or documented provenance/SBOM Actions; workflow id-token: write and attestations: write, POST /repos/{owner}/{repo}/attestations; GET .../attestations/{subject_digest}; organization/user digest lookup routes, gh attestation download/verify/trusted-root; OCI registry digest | [Docs 1](https://docs.github.com/en/rest/repos/attestations) |
| attestations-linked-artifacts | Linked artifact storage and deployment metadata | POST /orgs/{org}/artifacts/metadata/storage-record; POST .../metadata/deployment-record, GET /orgs/{org}/artifacts/{subject_digest}/metadata/storage-records or /deployment-records, POST .../metadata/deployment-record/cluster/{cluster}; POST .../cluster/{cluster}/jobs; GET .../jobs/{job_id}, Organization linked artifacts page | [Docs 1](https://docs.github.com/en/rest/orgs/artifact-metadata) |

## Checks

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| checks-runs | Check runs, output annotations and requested actions | GET /repos/{owner}/{repo}/commits/{ref}/check-runs; GET .../check-suites/{check_suite_id}/check-runs; GET .../check-runs/{check_run_id}/annotations, POST .../check-runs; GET/PATCH .../check-runs/{check_run_id}; POST .../check-runs/{check_run_id}/rerequest, GraphQL CheckRun/CheckAnnotation; createCheckRun and updateCheckRun; gh api; PR Checks tab | [Docs 1](https://docs.github.com/en/rest/checks/runs) |
| checks-suites | Check suites, preferences and rerequest | GET /repos/{owner}/{repo}/commits/{ref}/check-suites; GET .../check-suites/{check_suite_id}; POST .../check-suites, PATCH .../check-suites/preferences; POST .../check-suites/{check_suite_id}/rerequest, GraphQL Commit.checkSuites, CheckSuite.checkRuns; createCheckSuite, updateCheckSuitePreferences, rerequestCheckSuite | [Docs 1](https://docs.github.com/en/rest/checks/suites) |
| checks-commit-statuses | Commit status contexts and combined check visibility | POST /repos/{owner}/{repo}/statuses/{sha}; GET .../commits/{ref}/statuses; GET .../commits/{ref}/status, GraphQL Commit.status and statusCheckRollup.contexts with CheckRun/StatusContext fragments; gh pr checks; PR checks UI | [Docs 1](https://docs.github.com/en/rest/commits/statuses) |

## Deployments

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| deploy-environments | Environments, protection gates and branch/tag policies | REST /repos/{owner}/{repo}/environments and /{environment_name}, .../{environment_name}/deployment-branch-policies; .../deployment_protection_rules, Settings > Environments; workflow jobs.<id>.environment | [Docs 1](https://docs.github.com/en/rest/deployments/environments) |
| deploy-approval | Pending deployments and custom protection decisions | GET/POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments; GET .../{run_id}/approvals, POST .../{run_id}/deployment_protection_rule; Actions run > Review deployments | [Docs 1](https://docs.github.com/en/rest/actions/workflow-runs) |
| deploy-records | Deployment records and status history | REST /repos/{owner}/{repo}/deployments and /{deployment_id}, REST .../deployments/{deployment_id}/statuses and /{status_id}, Repository deployments UI; actual deployment engine/cloud CLI separately | [Docs 1](https://docs.github.com/en/rest/deployments/deployments) |

## Packages

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| packages-metadata | Packages and versions lifecycle | REST /orgs/{org}/packages and /{package_type}/{package_name}/versions; corresponding /users/{username} and /user routes, DELETE package/version route; POST .../restore; package settings UI | [Docs 1](https://docs.github.com/en/rest/packages/packages) |
| packages-registry | Registry publishing, installation and authentication | docker/podman for ghcr.io; npm for npm.pkg.github.com; gem for rubygems.pkg.github.com; mvn/gradle for maven.pkg.github.com; dotnet nuget for nuget.pkg.github.com, Workflow GITHUB_TOKEN with packages permissions or authorized classic PAT; ecosystem auth configuration | [Docs 1](https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages) |
| packages-access | Package visibility, linked repository and access control | Package page > Package settings > Manage access/Actions/Codespaces access; organization Settings > Packages, OCI org.opencontainers.image.source or ecosystem repository metadata for package linkage | [Docs 1](https://docs.github.com/en/packages/learn-github-packages/about-permissions-for-github-packages) |
| packages-trusted-publishing | Trusted publishing to external package registries | PyPI project Settings > Publishing; pypa/gh-action-pypi-publish; GitHub Actions release workflow and protected environment, npmjs.com package Settings > Trusted publishing; npm publish or supported npm trust CLI; https://docs.npmjs.com/trusted-publishers/, External registry-native API/UI; Git commits and Actions logs; no GitHub Packages trusted-publisher CRUD endpoint is implied | [Docs 1](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-pypi) |

## Pages

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| pages-settings | Pages source, custom domain, TLS and visibility | GET/POST/PUT/DELETE /repos/{owner}/{repo}/pages; GET .../pages/health, Settings > Pages; Git CNAME for applicable source; DNS provider and owner verified-domain settings | [Docs 1](https://docs.github.com/en/rest/pages/pages) |
| pages-builds | Pages builds and Actions deployments | GET/POST /repos/{owner}/{repo}/pages/builds; GET .../builds/latest and /{build_id}, POST .../pages/deployments; GET .../deployments/{pages_deployment_id}; POST .../{id}/cancel, actions/configure-pages, actions/upload-pages-artifact, actions/deploy-pages; github-pages environment | [Docs 1](https://docs.github.com/en/rest/pages/pages) |

## Releases

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| releases-lifecycle | Drafts, publication, prereleases and generated notes | REST /repos/{owner}/{repo}/releases; /latest; /tags/{tag}; /{release_id}; /generate-notes, gh release list/view/create/edit/delete; git tags; Releases UI | [Docs 1](https://docs.github.com/en/rest/releases/releases) |
| releases-assets | Release assets and binary integrity | REST /repos/{owner}/{repo}/releases/{release_id}/assets; /releases/assets/{asset_id}, POST returned upload_url on uploads.github.com with binary body and name; gh release upload/download/delete-asset, gh release verify-asset where supported | [Docs 1](https://docs.github.com/en/rest/releases/assets) |
| releases-immutable | Immutable releases and release attestations | Repository Settings > General > Releases > Enable release immutability, Organization Settings > Repository > General > Releases; GET/PUT/DELETE /repos/{owner}/{repo}/immutable-releases; GET/PUT /orgs/{org}/settings/immutable-releases and selected repositories routes, gh release verify; gh release verify-asset; release immutable field/badge | [Docs 1](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases) |

## Security

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| security-enablement | Repository security products and reporting policy | GET/PATCH /repos/{owner}/{repo}; GET/PUT/DELETE .../vulnerability-alerts; GET/PUT/DELETE .../automated-security-fixes, GET/PUT/DELETE .../private-vulnerability-reporting; Git SECURITY.md; Settings > Code security | [Docs 1](https://docs.github.com/en/rest/repos/repos) |
| security-configurations | Organization and enterprise security configurations | REST /orgs/{org}/code-security/configurations and /{configuration_id}; /defaults; /{configuration_id}/attach; /detach, Repository /repos/{owner}/{repo}/code-security-configuration; enterprise routes where documented, Organization Settings > Code security > Configurations | [Docs 1](https://docs.github.com/en/rest/code-security/configurations) |
| security-codeql | CodeQL setup, databases and variant analyses | GET/PATCH /repos/{owner}/{repo}/code-scanning/default-setup; Git advanced workflow, REST .../code-scanning/codeql/databases; /databases/{language}; /codeql/variant-analyses and result routes | [Docs 1](https://docs.github.com/en/rest/code-scanning/code-scanning) |
| security-code-alerts | Code scanning alerts, analyses and SARIF | REST /repos/{owner}/{repo}/code-scanning/alerts and /{alert_number}/instances; /analyses, POST .../code-scanning/sarifs; GET .../sarifs/{sarif_id}; organization alerts API | [Docs 1](https://docs.github.com/en/rest/code-scanning/code-scanning) |
| security-ai-autofix | AI Scan and Copilot Autofix | GET/PATCH /orgs/{org}/code-scanning/ai-scan and repository counterpart, GET/POST .../code-scanning/alerts/{alert_number}/autofix; POST .../autofix/commits | [Docs 1](https://docs.github.com/en/rest/code-scanning/code-scanning) |
| security-dependency-graph | Dependency submission and dependency review | GET /repos/{owner}/{repo}/dependency-graph/compare/{basehead}, POST /repos/{owner}/{repo}/dependency-graph/snapshots, Dependency review Action; Insights > Dependency graph; PR dependency review | [Docs 1](https://docs.github.com/en/rest/dependency-graph/dependency-review) |
| security-sbom | SBOM export and generated reports | GET /repos/{owner}/{repo}/dependency-graph/sbom, GET .../dependency-graph/sbom/generate-report; GET .../sbom/fetch-report/{sbom_uuid}, Insights > Dependency graph > Export SBOM | [Docs 1](https://docs.github.com/en/rest/dependency-graph/sboms) |
| security-dependabot-alerts | Dependabot alerts and security updates | GET /repos/{owner}/{repo}/dependabot/alerts; GET/PATCH .../{alert_number}, Organization/enterprise Dependabot alerts routes; repository automated-security-fixes endpoint; Security > Dependabot | [Docs 1](https://docs.github.com/en/rest/dependabot/alerts) |
| security-dependabot-version | Dependabot version updates and grouping | Git .github/dependabot.yml; Insights > Dependency graph > Dependabot, Dependabot PR comments for documented rebase/recreate commands; PR APIs | [Docs 1](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference) |
| security-dependabot-secrets | Dependabot registry credentials | REST /repos/{owner}/{repo}/dependabot/secrets and /public-key, REST /orgs/{org}/dependabot/secrets and selected repositories, gh secret --app dependabot list/set/delete; dependabot.yml registries | [Docs 1](https://docs.github.com/en/rest/dependabot/secrets) |
| security-dependabot-runtime | Dependabot runner and private repository access settings | GET/PUT /repos/{owner}/{repo}/dependabot/runner-settings, REST /orgs/{org}/dependabot/repository-access and /default-level; enterprise equivalents | [Docs 1](https://docs.github.com/en/rest/dependabot/runner-settings) |
| security-secret-alerts | Secret scanning alerts, locations and scan history | REST /repos/{owner}/{repo}/secret-scanning/alerts and /{alert_number}/locations, GET .../secret-scanning/scan-history; organization alerts endpoint; Settings > Code security | [Docs 1](https://docs.github.com/en/rest/secret-scanning/secret-scanning) |
| security-push-protection | Push protection and governed exceptions | PATCH /repos/{owner}/{repo} security_and_analysis; organization security configuration, POST .../secret-scanning/push-protection-bypasses; UI bypass/review flow, GET/PATCH /orgs/{org}/secret-scanning/pattern-configurations | [Docs 1](https://docs.github.com/en/rest/secret-scanning/push-protection) |
| security-custom-patterns | Secret custom patterns and validity controls | GET/POST/DELETE /orgs/{org}/secret-scanning/custom-patterns and repository counterparts; PATCH .../custom-patterns/{pattern_id}; Settings > Code security > Secret scanning, Organization security configurations for validity, extended metadata and generic/AI pattern options | [Docs 1](https://docs.github.com/en/rest/secret-scanning/custom-patterns) |
| security-advisories | Repository advisories, private reports and coordinated disclosure | REST /repos/{owner}/{repo}/security-advisories and /{ghsa_id}; /reports; /{ghsa_id}/forks; /{ghsa_id}/cve, Advisory comment routes; organization advisory listing; Security > Advisories | [Docs 1](https://docs.github.com/en/rest/security-advisories/repository-advisories) |
| security-global-advisories | GitHub Advisory Database lookup | GET /advisories; GET /advisories/{ghsa_id}; GitHub Advisory Database UI | [Docs 1](https://docs.github.com/en/rest/security-advisories/global-advisories) |
| security-overview | Security coverage, campaigns, bypass and dismissal review | Organization Security > Overview; security configurations and documented product APIs, UI for campaign/delegated-review controls without a verified public mutation; export available reports | [Docs 1](https://docs.github.com/en/code-security/getting-started/github-security-features) |
| security-campaigns | Published security campaigns | GET/POST /orgs/{org}/campaigns; GET/PATCH/DELETE /orgs/{org}/campaigns/{campaign_number}, Organization Security > Campaigns | [Docs 1](https://docs.github.com/en/rest/campaigns/campaigns) |
| security-code-quality | Code quality findings and setup | GET /repos/{owner}/{repo}/code-quality/findings; GET .../findings/{finding_number}, GET/PATCH /repos/{owner}/{repo}/code-quality/setup; repository code quality UI | [Docs 1](https://docs.github.com/en/rest/code-quality/code-quality) |

## administration

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| admin-organization-profile | Organization identity, repository defaults, security toggles and immutable releases | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/orgs) |
| admin-organization-members | Invitations, failed/pending invitations, membership roles and public membership | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/members) |
| admin-teams | Team lifecycle, hierarchy and repository access | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/teams/teams) |
| admin-team-members | Team member and maintainer roles and pending invitations | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/teams/members) |
| admin-outside-collaborators | List/remove external collaborators and convert members | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/outside-collaborators) |
| admin-organization-role-assignments | Organization roles and user/team assignments | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/organization-roles) |
| admin-organization-custom-roles | Custom repository roles and their definitions | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/orgs/custom-roles) |
| admin-organization-custom-role-definitions | Custom organization role definitions | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/orgs/organization-roles) |
| admin-organization-security-managers | Retired legacy security-manager team API | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/security-managers) |
| admin-organization-blocking | Blocked-user inspection and block/unblock | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/blocking) |
| admin-organization-properties | Repository custom-property schema, values and external App-owned properties | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/custom-properties) |
| admin-organization-rulesets | Organization branch/tag/push rulesets and history | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/rules) |
| admin-organization-rule-suites | Rule evaluation results | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/rule-suites) |
| admin-organization-issue-types | Organization issue type definitions | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/issue-types) |
| admin-organization-issue-fields | Organization issue field definitions | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/issue-fields) |
| admin-organization-webhooks | Webhook configuration, ping, deliveries and redelivery | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/webhooks) |
| admin-organization-token-governance | Fine-grained token requests, approvals, access inventory and revocation | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/personal-access-tokens) |
| admin-organization-api-insights | API usage by route, actor, user, subject and time | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/api-insights) |
| admin-organization-network-configurations | Hosted-compute network configurations and settings | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/orgs/network-configurations) |
| admin-team-idp-sync | Identity-provider group mappings to teams | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/teams/team-sync) |
| admin-team-external-groups | External group discovery and team connections | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/teams/external-groups) |
| admin-organization-audit-and-sso | Organization audit events and SAML credential authorizations | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/orgs/orgs) |
| admin-enterprise-accounts | Enterprise discovery and access-verification restrictions | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/enterprises) |
| admin-enterprise-audit | Enterprise audit queries and streaming configuration | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/audit-log) |
| admin-enterprise-role-assignments | Enterprise role catalog and user/team assignments | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/enterprise-roles) |
| admin-enterprise-ai-controls | Enterprise/team model policies, agent app models and AI feature policies | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/ai-controls) |
| admin-enterprise-credentials | Enterprise-delegated credential grants and selective/bulk revocation | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/credential-authorizations) |
| admin-enterprise-token-inventory | Enterprise token inventory and token owner lookup | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/token-inventory) |
| admin-enterprise-licensing | Consumed licenses, sync state, active committers and Visual Studio matches | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/licensing) |
| admin-enterprise-properties | Enterprise repository custom-property schema and promotion | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/custom-properties) |
| admin-enterprise-organization-properties | Custom-property schema and values on organizations | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/custom-properties-for-orgs) |
| admin-enterprise-rulesets | Enterprise repository rulesets and versions | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/rules) |
| admin-enterprise-network-configurations | Enterprise hosted-compute network configurations | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/network-configurations) |
| admin-enterprise-app-installations | Install/uninstall Apps and change organization installation repository access | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/organization-installations) |
| admin-enterprise-scim | Managed-user/group lifecycle and provisioning | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/scim) |
| admin-organization-scim | Organization SCIM identities | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/scim/scim) |
| admin-billing-usage | Organization/user/enterprise metered and AI-credit usage | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/billing/usage) |
| admin-billing-budgets | Budget inspection, creation, update and deletion | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/billing/budgets) |
| admin-billing-cost-centers | Cost center lifecycle, resource assignment and membership lookup | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/billing/cost-centers) |
| admin-billing-usage-reports | Asynchronous enterprise billing report generation and retrieval | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/billing/usage-reports) |
| admin-codespaces-lifecycle | Codespace creation, configuration, start/stop, export and deletion | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/codespaces/codespaces) |
| admin-codespaces-machines | Available machine types | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/codespaces/machines) |
| admin-codespaces-organization-access | Organization-paid Codespaces access and organization lifecycle operations | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/codespaces/organizations) |
| admin-codespaces-organization-secrets | Encrypted organization Codespaces secrets and selected-repository access | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/codespaces/organization-secrets) |
| admin-codespaces-repository-secrets | Encrypted repository Codespaces secrets | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/codespaces/repository-secrets) |
| admin-codespaces-user-secrets | Encrypted personal Codespaces secrets and repository grants | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/codespaces/secrets) |
| admin-copilot-seats | Copilot billing settings, seat inventory and team/user seat assignment | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot/copilot-user-management) |
| admin-copilot-usage-metrics | Organization/team/enterprise/user usage reports | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot/copilot-usage-metrics) |
| admin-copilot-agent-policy | Cloud-agent enablement and selected organizations/repositories | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-coding-agent-management) |
| admin-copilot-cloud-agent-sessions | Cloud-agent task/session creation | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot/copilot-cloud-agent-management) |
| admin-copilot-code-review | Copilot review policy and review usage settings | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot/copilot-code-review) |
| admin-copilot-content-exclusions | Copilot content-exclusion configuration | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot/copilot-content-exclusion-management) |
| admin-copilot-team-customizations | Team-level Copilot customization settings | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot/copilot-team-customizations) |
| admin-github-apps | App identity, manifest conversion, installations, token mint/revoke and suspension | REST API, gh api | [Docs 1](https://docs.github.com/rest/apps/apps) |
| admin-github-app-installations | Installation repository visibility, grants and token revocation | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/apps/installations) |
| admin-github-app-webhooks | App webhook config, delivery inspection and redelivery | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/apps/webhooks) |
| admin-oauth-app-authorizations | Check, reset or revoke App token/authorization | REST API, gh api | [Docs 1](https://docs.github.com/rest/apps/oauth-applications) |
| admin-marketplace | App plan, customer and authenticated-user subscription inspection | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/apps/marketplace) |
| admin-organization-migrations | Organization migration archives and repository locks | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/migrations/orgs) |
| admin-user-migrations | Personal repository migration archives and locks | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/migrations/users) |
| admin-source-imports | Closed legacy source-import API (historical coverage) | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/migrations/source-imports) |
| admin-account-profile | Public/authenticated account profile inspection and update | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/users/users) |
| admin-account-emails | Personal email addresses and visibility | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/users/emails) |
| admin-account-keys | SSH authentication public keys | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/users/keys) |
| admin-account-gpg-keys | GPG public signing keys | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/users/gpg-keys) |
| admin-account-ssh-signing-keys | SSH public signing keys | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/users/ssh-signing-keys) |
| admin-account-following | Follower discovery and follow/unfollow | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/users/followers) |
| admin-account-blocking | Personal blocked-user management | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/users/blocking) |
| admin-account-social-links | Personal profile social links | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/users/social-accounts) |
| admin-gists | Gist lifecycle, files, history, forks and stars | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/gists/gists) |
| admin-gist-comments | Gist comment lifecycle | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/gists/comments) |
| admin-repository-stars | Star/unstar repositories and list stars/stargazers | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/activity/starring) |
| admin-repository-watches | Repository subscribers and personal watch subscriptions | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/activity/watching) |
| admin-notifications | Personal notification inbox, thread state and subscriptions | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/activity/notifications) |
| admin-activity-events | Public/private activity event feeds | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/activity/events) |
| admin-activity-feeds | Account feed links | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/activity/feeds) |
| admin-agent-automations | Agent automation lifecycle, runs and scheduling | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/agent-automations/agent-automations) |
| admin-agent-tasks | Agent task creation, status and task lifecycle | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/agent-tasks/agent-tasks) |
| admin-agent-secrets | Agent organization/repository encrypted secrets and repository selection | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/agents/secrets) |
| admin-agent-variables | Agent organization/repository variables and repository selection | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/agents/variables) |
| admin-copilot-spaces | Copilot Space lifecycle and discovery | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot-spaces/copilot-spaces) |
| admin-copilot-space-collaborators | Copilot Space user/team collaborators | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot-spaces/collaborators) |
| admin-copilot-space-resources | Copilot Space attached repository/file/text resources | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/copilot-spaces/resources) |
| admin-private-registries | Organization private-registry authentication configurations | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/private-registries/organization-configurations) |
| admin-classroom | Closed GitHub Classroom API (historical coverage) | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/classroom/classroom) |
| admin-credential-revocation | Revocation of exposed supported GitHub credentials | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/rest/credentials/revoke) |
| admin-identity-policies | Organization/enterprise SAML SSO, 2FA, SSH CA, IP allow lists and domain verification | GitHub web UI, GraphQL API, DNS provider | [Docs 1](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization) |
| admin-organization-policy-settings | Organization/enterprise policy inheritance and defaults | GitHub web UI, REST API, GraphQL API | [Docs 1](https://docs.github.com/en/organizations/managing-organization-settings) |
| admin-community-defaults | Account/organization shared community files and templates | Git, Contents REST API, GitHub web UI | [Docs 1](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file) |
| admin-organization-profile-content | Organization public/member profile and pinned repositories | Git, Contents REST API, GitHub web UI | [Docs 1](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile) |
| admin-enterprise-importer | GitHub Enterprise Importer migrations | GitHub CLI GEI extension, GraphQL API, GitHub web UI | [Docs 1](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-between-github-products/migrating-repositories-from-githubcom-to-github-enterprise-cloud) |
| admin-repository-lifecycle-admin | Repository transfer, archive/unarchive, deletion and restoration | REST API, gh repo, GitHub web UI | [Docs 1](https://docs.github.com/en/rest/repos/repos) |
| admin-repository-insights | Repository traffic, statistics and community health | REST API, gh api, GitHub web UI | [Docs 1](https://docs.github.com/en/rest/metrics) |
| admin-devcontainers | Devcontainer configuration and Codespaces prebuild/policy settings | Git, Codespaces REST API, GitHub web UI, devcontainer CLI when installed | [Docs 1](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces) |
| admin-mcp-and-custom-agent-policy | Copilot MCP controls, registries, custom agents and managed client settings | GitHub web UI, Git, supported policy REST API, managed client configuration | [Docs 1](https://docs.github.com/en/copilot/concepts/enterprise/agent-management) |
| admin-git-lfs | Git LFS tracking, migration, verification, archive and billing behavior | Git LFS CLI, Git, GitHub web UI, billing REST API | [Docs 1](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) |
| admin-account-security-and-billing-ui | Personal account security, billing and recovery boundaries | GitHub web UI, documented REST API for narrow supported operations | [Docs 1](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure) |
| admin-enterprise-server-admin | GitHub Enterprise Server appliance administration | GHES REST API, Management Console API, SSH administrative shell, GitHub web UI | [Docs 1](https://docs.github.com/en/enterprise-server@latest/admin) |
| admin-github-models-retired | Retired GitHub Models playground, catalog, inference and BYOK | Historical product documentation, Git repository inspection | [Docs 1](https://docs.github.com/en/github-models) |
| admin-github-connect | GitHub Connect between Enterprise Server and Enterprise Cloud | GHES enterprise/site administration UI, GitHub Enterprise Cloud UI, documented instance APIs | [Docs 1](https://docs.github.com/en/enterprise-server@3.22/admin/configuring-settings/configuring-github-connect) |
| admin-support-entitlements | Enterprise support entitlements and access | GitHub enterprise settings UI, GitHub Support portal | [Docs 1](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-support-entitlements-for-your-enterprise) |
| admin-support-tickets | GitHub Support tickets, attachments and ongoing case management | GitHub Support portal, authorized browser interaction | [Docs 1](https://docs.github.com/en/enterprise-cloud@latest/support/contacting-github-support/creating-a-support-ticket) |
| admin-enterprise-organization-lifecycle | Enterprise organization creation, invitations and transfers | GitHub enterprise settings UI, documented GraphQL enterprise mutations | [Docs 1](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/adding-organizations-to-your-enterprise) |
| admin-enterprise-data-residency | Enterprise Cloud data residency and host-specific feature/network compatibility | Enterprise settings UI, host-specific REST/GraphQL APIs, GitHub Enterprise Importer, IdP/network administration | [Docs 1](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/feature-overview-for-github-enterprise-cloud-with-data-residency) |
| admin-personal-data-export | Personal account data export and expiring archive access | GitHub account settings UI, User Migration REST API, authenticated download | [Docs 1](https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/requesting-an-archive-of-your-personal-accounts-data) |
| admin-archive-program | Public repository participation in the GitHub Archive Program | Repository settings UI | [Docs 1](https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/opting-into-or-out-of-the-github-archive-program-for-your-public-repository) |
| admin-platform-meta | GitHub platform API discovery, host metadata and operational diagnostics | REST API, gh api, GitHub Status web UI | [Docs 1](https://docs.github.com/en/rest/meta) |
| admin-platform-rate-limits | REST/GraphQL rate-limit budgets and respectful retry behavior | REST API, GraphQL API, gh api response headers | [Docs 1](https://docs.github.com/en/rest/rate-limit) |
| admin-platform-license-catalog | License catalog and detected repository license metadata | REST API, gh api | [Docs 1](https://docs.github.com/en/rest/licenses) |
| admin-platform-gitignore-templates | GitHub gitignore template catalog | REST API, gh api, Git | [Docs 1](https://docs.github.com/en/rest/gitignore) |
| admin-platform-emojis | GitHub emoji catalog | REST API, gh api | [Docs 1](https://docs.github.com/en/rest/emojis) |
| admin-platform-markdown-rendering | GitHub Markdown and GFM rendering utilities | REST API, gh api, GitHub rendered UI | [Docs 1](https://docs.github.com/en/rest/markdown) |
| admin-github-spark | GitHub Spark app creation, iteration, publishing and data-access controls | GitHub Spark web UI, deployed Spark site, linked Git repository when available | [Docs 1](https://docs.github.com/en/copilot/tutorials/spark/your-first-spark) |
| admin-copilot-cli-customization | Copilot CLI local sessions, instructions, skills, plugins, hooks, LSP and permission settings | Copilot CLI, Git repository files, user-local CLI configuration, organization/enterprise policy UI | [Docs 1](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview) |
| admin-copilot-sdk | Copilot SDK application integration, sessions, tools and lifecycle control | Official Copilot SDK, Copilot CLI JSON-RPC runtime, application source and tests | [Docs 1](https://docs.github.com/en/copilot/get-started/sdk-quickstart) |

## branches-rules

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| branch-protection | Classic branch protection | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/branches/branch-protection) |
| repository-rulesets | Branch/tag/push rulesets and effective rules | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/repos/rules) |
| ruleset-insights | Rule evaluation and enforcement evidence | REST, UI | [Docs 1](https://docs.github.com/en/rest/repos/rule-suites) |
| repository-merge-policy | Repository merge methods and branch cleanup policy | REST, gh repo edit, UI | [Docs 1](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges) |

## community

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| community-comment-minimization | Hide and restore off-topic or disruptive comments | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/issues#minimizecomment) |
| community-interaction-limits | Temporary interaction restrictions | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/interactions) |
| community-saved-replies | Personal saved replies and reusable response insertion | UI | [Docs 1](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies) |

## discussions

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| discussions-lifecycle | Repository and organization Discussions | GraphQL, REST repository feature toggle, UI | [Docs 1](https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-discussions) |
| discussions-answers | Answers, reactions and community feedback | GraphQL, UI | [Docs 1](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/participating-in-a-discussion) |
| discussions-organization | Categories, forms, polls and moderation | UI, GraphQL where mutation documented, git forms | [Docs 1](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions) |

## issues

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| issue-lifecycle | Issue lifecycle and completion reasons | REST, GraphQL, gh issue, UI | [Docs 1](https://docs.github.com/en/rest/issues/issues) |
| issue-metadata | Labels, assignees and milestones | REST, gh label, gh issue, UI | [Docs 1](https://docs.github.com/en/rest/issues/labels) |
| issue-assignees | Assignable users and assignment validation | REST, gh issue edit, gh pr edit, UI | [Docs 1](https://docs.github.com/en/rest/issues/assignees) |
| issue-milestones | Milestone planning and progress | REST, gh api, UI | [Docs 1](https://docs.github.com/en/rest/issues/milestones) |
| issue-types | Owner issue types and per-issue type assignment | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/repos/issue-types) |
| issue-types-owner | Organization and personal issue type administration | REST, UI | [Docs 1](https://docs.github.com/en/rest/orgs/issue-types) |
| issue-fields | Owner-wide structured issue fields | REST, UI | [Docs 1](https://docs.github.com/en/rest/orgs/issue-fields) |
| issue-field-values | Per-issue structured field values | REST, UI | [Docs 1](https://docs.github.com/en/rest/issues/issue-field-values) |
| issue-forms-templates | Issue forms, templates and contact routing | git, REST contents, UI | [Docs 1](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) |
| issue-subissues | Parent/sub-issue hierarchy and ordering | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/issues/sub-issues) |
| issue-dependencies | Blocking and blocked-by relationships | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/issues/issue-dependencies) |
| issue-related | Related issues and suggested relationships | REST, UI | [Docs 1](https://docs.github.com/en/rest/issues/issues#list-issues-related-to-an-issue) |
| issue-comments | Conversation comments, pinned comments and reactions | REST, GraphQL, gh issue comment, UI | [Docs 1](https://docs.github.com/en/rest/issues/comments) |
| issue-artifacts | Issue-attached artifacts | REST | [Docs 1](https://docs.github.com/en/rest/issues/artifacts) |
| issue-timeline | Timeline, audit context and cross references | REST, GraphQL, gh api | [Docs 1](https://docs.github.com/en/rest/issues/timeline) |
| issue-transfer-pin-duplicate | Transfer, pinning and duplicate triage | GraphQL, gh issue transfer, gh issue pin, UI | [Docs 1](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository) |
| issue-saved-views | Issue dashboard and advanced triage views | UI, REST search, GraphQL search, gh search issues | [Docs 1](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests) |
| issue-linked-branches | Issue-linked development branches | GraphQL, gh issue develop, git, UI | [Docs 1](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) |
| issue-planning-status | Native issue planning statuses (preview) | GraphQL, UI where enrolled | [Docs 1](https://docs.github.com/en/graphql/reference/issues#setissuestatus) |

## profiles-social

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| profile-status | Personal availability status | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/users#changeuserstatus) |
| profile-star-lists | Named lists of starred repositories | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/users#createuserlist) |
| profile-content-pins | Personal profile README, pins and contribution display | git, REST contents, GraphQL read, UI | [Docs 1](https://docs.github.com/en/account-and-profile/how-tos/profile-customization) |
| profile-follow-organizations | Follow organization activity | GraphQL, UI | [Docs 1](https://docs.github.com/en/get-started/exploring-projects-on-github/following-organizations) |

## projects

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| projects-lifecycle | Projects v2 discovery, lifecycle and repository links | REST, GraphQL, gh project, UI | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects) |
| projects-items | Project issue/PR items and drafts | REST, GraphQL, gh project item-*, UI | [Docs 1](https://docs.github.com/en/rest/projects/items) |
| projects-fields | Project custom fields and built-in metadata | REST, GraphQL, gh project field-*, UI | [Docs 1](https://docs.github.com/en/rest/projects/fields) |
| projects-field-values | Typed Project field values and clearing | REST, GraphQL, gh project item-edit, UI | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects) |
| projects-iterations | Iteration planning, schedules and breaks | GraphQL, gh project item-edit, UI | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-iteration-fields) |
| projects-views | Saved table, board and roadmap views | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/projects) |
| projects-layout | Grouping, slicing, sorting and field visibility | UI, REST view creation, GraphQL read | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/changing-the-layout-of-a-view) |
| projects-filters | Project filters and saved-view item retrieval | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/projects/items#list-items-for-an-organization-project-view) |
| projects-insights | Current and historical insights charts | UI | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects) |
| projects-workflows | Built-in Project status workflows | GraphQL read/delete, UI configuration | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations) |
| projects-auto-add | Automatic item intake | UI, Actions with GraphQL | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically) |
| projects-auto-archive | Automatic archival and retention | UI, GraphQL, gh project item-archive | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically) |
| projects-actions | Project automation through Actions and webhooks | Actions, GraphQL, REST, webhooks | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions) |
| projects-templates | Organization Project templates and copying | GraphQL, gh project copy, UI | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-project-templates-in-your-organization) |
| projects-updates | Project status updates and subscriptions | GraphQL, UI | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/sharing-project-updates) |
| projects-access | Project visibility, access and linking | GraphQL, UI | [Docs 1](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects) |
| projects-issue-fields | Reuse owner issue fields in Projects | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/projects) |
| projects-multiselect | Multiple-choice Project fields | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/projects) |

## pull-requests

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| pr-lifecycle | Pull request lifecycle, drafts and base/head management | REST, GraphQL, gh pr, git | [Docs 1](https://docs.github.com/en/rest/pulls/pulls) |
| pr-linking | Linked issues and automatic closure | GraphQL, gh pr, UI | [Docs 1](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) |
| pr-templates | PR templates and contribution checklist | git, REST contents, gh pr create, UI | [Docs 1](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository) |
| pr-review-requests | Reviewer requests and rerequests | REST, GraphQL, gh pr edit, UI | [Docs 1](https://docs.github.com/en/rest/pulls/review-requests) |
| pr-reviews | Review submission and dismissal | REST, GraphQL, gh pr review, UI | [Docs 1](https://docs.github.com/en/rest/pulls/reviews) |
| pr-review-comments | Inline review comments, suggestions and threads | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/pulls/comments) |
| pr-merge | Guarded merge and asynchronous merge results | REST, GraphQL, gh pr merge, UI | [Docs 1](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request) |
| pr-auto-merge | Auto-merge scheduling | GraphQL, gh pr merge --auto, UI | [Docs 1](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/automatically-merging-a-pull-request) |
| pr-merge-queue | Merge queue configuration and enrollment | REST rules, GraphQL, gh pr merge, UI | [Docs 1](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) |
| pr-update-revert-cleanup | Update branch, revert and branch cleanup | REST, git, gh pr update-branch, gh pr revert, UI | [Docs 1](https://docs.github.com/en/rest/pulls/pulls#update-a-pull-request-branch) |
| pr-stacks | Native stacked pull requests | REST, UI | [Docs 1](https://docs.github.com/en/rest/pulls/stacks) |
| pr-agent-merge | Agent Merge enrollment and allowed automation actions | REST, UI | [Docs 1](https://docs.github.com/en/rest/pulls/agent-merge) |
| pr-file-view-state | Per-viewer reviewed-file state | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/pulls#markfileasviewed) |
| pr-archival | Native pull request archiving | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/pulls#archivepullrequest) |

## repositories

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| repository-lifecycle | Repository lifecycle and metadata | REST, GraphQL, gh repo, UI | [Docs 1](https://docs.github.com/en/rest/repos/repos) |
| repository-templates | Template repositories and generated repositories | REST, gh repo create --template, UI | [Docs 1](https://docs.github.com/en/rest/repos/repos#create-a-repository-using-a-template) |
| repository-forks | Fork networks and upstream synchronization | REST, gh repo fork, gh repo sync, git, UI | [Docs 1](https://docs.github.com/en/rest/repos/forks) |
| repository-content | Contents, README, archives and immutable source reads | REST, GraphQL, gh api, git | [Docs 1](https://docs.github.com/en/rest/repos/contents) |
| repository-git-objects | Git blobs, trees, commits, refs and annotated tags | REST, GraphQL, git | [Docs 1](https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-your-git-database) |
| repository-history | History, compare, blame and commit verification | REST, GraphQL, git log, git blame, gh api | [Docs 1](https://docs.github.com/en/rest/commits/commits) |
| repository-branches | Branch management and synchronization | REST, gh api, git, UI | [Docs 1](https://docs.github.com/en/rest/branches/branches) |
| repository-community | Community standards and shared contribution files | REST, git, UI | [Docs 1](https://docs.github.com/en/rest/metrics/community) |
| repository-autolinks | External tracker autolinks | REST, UI | [Docs 1](https://docs.github.com/en/rest/repos/autolinks) |
| repository-codeowners | Ownership and review routing | REST, git, UI | [Docs 1](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) |
| repository-lfs-submodules | Large files, submodules and checkout fidelity | git, git lfs, REST | [Docs 1](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) |
| repository-commit-comments | Commit discussion comments | REST, GraphQL read, UI | [Docs 1](https://docs.github.com/en/rest/commits/comments) |

## search-notifications

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| search-cross-github | Cross-GitHub discovery and search coverage | REST, GraphQL, gh search, UI | [Docs 1](https://docs.github.com/en/rest/search/search) |
| search-code | Code search versus local source inspection | UI, REST, gh search code, rg, git | [Docs 1](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax) |
| search-issues-prs | Issue and PR search qualifiers | REST, GraphQL, gh search issues, gh search prs, UI | [Docs 1](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests) |
| notifications-inbox | Notification inbox and thread state | REST, UI | [Docs 1](https://docs.github.com/en/rest/activity/notifications) |
| notifications-watch | Repository watches, stars and subscriptions | REST, GraphQL, UI | [Docs 1](https://docs.github.com/en/rest/activity/watching) |
| activity-events | Repository and user activity feeds | REST, UI | [Docs 1](https://docs.github.com/en/rest/activity/events) |

## sponsors

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| sponsors-listing | Sponsors eligibility and listing setup | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/sponsors#createsponsorslisting) |
| sponsors-tiers | Sponsorship tiers and benefits | GraphQL, UI | [Docs 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers) |
| sponsors-transactions | Individual and bulk sponsorship commitments | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/sponsors#createsponsorship) |
| sponsors-preferences | Sponsorship privacy and connected platform preferences | GraphQL, UI | [Docs 1](https://docs.github.com/en/graphql/reference/sponsors#updatesponsorshippreferences) |
| sponsors-analytics | Sponsor activity, lifetime value and exports | GraphQL, UI | [Docs 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/viewing-your-sponsors-and-sponsorships) |
| sponsors-newsletters | Sponsor newsletters and tier-targeted updates | GraphQL read, UI | [Docs 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/contacting-your-sponsors) |
| sponsors-payouts | Payout status and receipts | UI, GraphQL permitted metadata | [Docs 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-payouts-from-github-sponsors) |
| sponsors-goals | Sponsorship goals and progress | UI, GraphQL read | [Docs 1](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-goal) |

## wiki

| ID | Capability | Interfaces | Official source |
| --- | --- | --- | --- |
| wiki-pages | Wiki publishing and independent Git history | git, UI, REST repository feature toggle | [Docs 1](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis) |
| wiki-navigation | Wiki sidebar, footer, assets and navigation | git, UI | [Docs 1](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content) |

