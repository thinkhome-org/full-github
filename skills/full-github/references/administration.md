# Organization, enterprise, account and development administration

This is a capability map, not a claim that the current token can administer every account. Checked against current official GitHub documentation and [GitHub-maintained OpenAPI descriptions](https://github.com/github/rest-api-description) on 2026-11-15. Operation inventory below omits deprecated numeric-team aliases; it includes separate Enterprise Cloud routes and explicitly marked closed historical families. Current host/version endpoint documentation wins over older cached guidance.

## Access and execution contract

- Establish whether the object belongs to a **personal account**, **organization**, **enterprise**, or **Enterprise Server instance**. Repository admin does not imply organization owner; organization owner does not imply enterprise owner; none implies appliance administrator.
- Record caller identity, token type, resource selection, granted permission, SSO authorization, inherited enterprise policy, plan and feature availability. An App installation token is limited by both installation selection and approved App permissions. A fine-grained PAT is not supported by every endpoint. The per-endpoint permission table is authoritative, even where a read unusually requires a write/admin grant.
- Use `gh api` for supported REST endpoints, `gh api graphql` for supported GraphQL operations, Git for repository files, and browser controls for remaining settings. A connected GitHub tool is an alternative only when it exposes the actual operation. `gh api` does not bypass authentication or plan restrictions.
- Fetch every page. Interpret 403/404 as unknown until permission and product availability are checked. Preserve the failure and exact endpoint; do not claim missing membership, policies or licenses from inaccessible data.
- Read before writing; preserve unrelated settings and inheritances. Use exact IDs, least privilege, structured JSON/file bodies and the documented API version. Re-read the changed resource. For async operations, wait for completed status and inspect output, errors and live effects.
- Access changes, account ownership/visibility, billing limits, destructive lifecycle operations, identity policy, token issuance and external integrations require authorization covering those consequences. Documentation coverage never grants that authorization. Do not print secrets, private feed URLs, App keys or exported private archives.
- Authentication support is changing: current [Copilot policy docs](https://docs.github.com/en/rest/copilot/copilot-coding-agent-management) include App tokens with enterprise permissions. Do not generalize the older enterprise-admin landing page's classic-PAT restriction to every enterprise endpoint. [Organization PAT governance](https://docs.github.com/en/rest/orgs/personal-access-tokens) specifically requires GitHub App token support, not an ordinary PAT.

## Coverage and operation routes

Each family lists representative documented routes (closed families are marked unavailable), access requirements and limits. Use the [complete REST operation registry](../data/rest-operations.json) and linked endpoint documentation for every operation and exact request schema. Verification rules above apply to every family. `GET` is inspection; mutation verbs perform writes. POST may start an asynchronous operation or mint a credential. This reference does not run any of them automatically.

### Organization identity, repository defaults, security toggles and immutable releases

Coverage ID: `admin-organization-profile`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization owner; Administration read for private settings/write for updates. Public profile reads may be anonymous. Account deletion is irreversible. Some policies inherit enterprise restrictions. Immutable releases are a distinct setting, not a Git tag convention.

Example routes (14 documented in this family):

```text
GET /organizations
GET /orgs/{org}
PATCH /orgs/{org}
DELETE /orgs/{org}
```

[Official documentation](https://docs.github.com/rest/orgs/orgs).

### Invitations, failed/pending invitations, membership roles and public membership

Coverage ID: `admin-organization-members`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Members read/write as documented; invitations require organization owner. Self public-membership operations act only for authenticated user. Enterprise Managed Users use IdP provisioning rather than ordinary invitations. Removal revokes access; public-member lists are incomplete membership evidence.

Example routes (18 documented in this family):

```text
GET /orgs/{org}/failed_invitations
GET /orgs/{org}/invitations
POST /orgs/{org}/invitations
DELETE /orgs/{org}/invitations/{invitation_id}
```

[Official documentation](https://docs.github.com/rest/orgs/members).

### Team lifecycle, hierarchy and repository access

Coverage ID: `admin-teams`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Members read/write; repository grants additionally require appropriate repository Administration and authority. Prefer organization/slug routes over legacy numeric-team APIs. Secret-team visibility is restricted; inherited grants survive removing a direct grant.

Example routes (11 documented in this family):

```text
GET /orgs/{org}/teams
POST /orgs/{org}/teams
PATCH /orgs/{org}/teams/{team_slug}
DELETE /orgs/{org}/teams/{team_slug}
```

[Official documentation](https://docs.github.com/rest/teams/teams).

### Team member and maintainer roles and pending invitations

Coverage ID: `admin-team-members`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Members read/write; organization owner or permitted team maintainer. Identity-provider synchronized memberships cannot be treated as independent local grants.

Example routes (5 documented in this family):

```text
GET /orgs/{org}/teams/{team_slug}/invitations
GET /orgs/{org}/teams/{team_slug}/members
PUT /orgs/{org}/teams/{team_slug}/memberships/{username}
DELETE /orgs/{org}/teams/{team_slug}/memberships/{username}
```

[Official documentation](https://docs.github.com/rest/teams/members).

### List/remove external collaborators and convert members

Coverage ID: `admin-outside-collaborators`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Members read/write; organization owner for membership conversion/removal. Conversion can strip organization and team access; ordinary repository collaborator grants are a separate operation.

Example routes (3 documented in this family):

```text
GET /orgs/{org}/outside_collaborators
PUT /orgs/{org}/outside_collaborators/{username}
DELETE /orgs/{org}/outside_collaborators/{username}
```

[Official documentation](https://docs.github.com/rest/orgs/outside-collaborators).

### Organization roles and user/team assignments

Coverage ID: `admin-organization-role-assignments`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Custom organization roles read for role discovery; Members write for assignment; owners for writes. Custom-role creation and updates require Enterprise Cloud surfaces; built-in roles do not imply arbitrary custom permissions.

Example routes (10 documented in this family):

```text
GET /orgs/{org}/organization-roles
DELETE /orgs/{org}/organization-roles/teams/{team_slug}
PUT /orgs/{org}/organization-roles/teams/{team_slug}/{role_id}
DELETE /orgs/{org}/organization-roles/teams/{team_slug}/{role_id}
```

[Official documentation](https://docs.github.com/rest/orgs/organization-roles).

### Custom repository roles and their definitions

Coverage ID: `admin-organization-custom-roles`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud; owners or delegated custom-role authority; Custom repository roles read/write. Org-wide roles and repository roles are distinct. Deleting a role affects current assignments.

Example routes (12 documented in this family):

```text
GET /organizations/{organization_id}/custom_roles
GET /orgs/{org}/custom-repository-roles
POST /orgs/{org}/custom-repository-roles
PATCH /orgs/{org}/custom-repository-roles/{role_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/orgs/custom-roles).

### Custom organization role definitions

Coverage ID: `admin-organization-custom-role-definitions`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud; Custom organization roles read/write and permitted owner/delegated manager. Inspect exact role-definition routes and assignment permissions independently.

Example routes (4 documented in this family):

```text
GET /orgs/{org}/organization-fine-grained-permissions
POST /orgs/{org}/organization-roles
PATCH /orgs/{org}/organization-roles/{role_id}
DELETE /orgs/{org}/organization-roles/{role_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/orgs/organization-roles).

### Retired legacy security-manager team API

Coverage ID: `admin-organization-security-managers`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Retirement begins 2026-01-01 according to current official endpoint notices; these three routes must not be presented as current supported setup. Use Organization Roles discovery and assignment endpoints for security-manager roles instead. Eligible security features and owner/delegated assignment authority still apply.

Example routes (3 documented in this family):

```text
GET /orgs/{org}/security-managers
PUT /orgs/{org}/security-managers/teams/{team_slug}
DELETE /orgs/{org}/security-managers/teams/{team_slug}
```

[Official documentation](https://docs.github.com/rest/orgs/security-managers).

### Blocked-user inspection and block/unblock

Coverage ID: `admin-organization-blocking`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization owner; Blocking users read/write. Blocking can remove collaboration access; record intended scope and existing relationships.

Example routes (4 documented in this family):

```text
GET /orgs/{org}/blocks
GET /orgs/{org}/blocks/{username}
PUT /orgs/{org}/blocks/{username}
DELETE /orgs/{org}/blocks/{username}
```

[Official documentation](https://docs.github.com/rest/orgs/blocking).

### Repository custom-property schema, values and external App-owned properties

Coverage ID: `admin-organization-properties`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Custom properties read/write/admin according to schema versus value operation; external registration requires External custom properties for repositories admin. Schema admin and per-repository value editing differ. App tokens can see only their own external-property registration.

Example routes (13 documented in this family):

```text
GET /orgs/{org}/properties/installations
POST /orgs/{org}/properties/installations
PATCH /orgs/{org}/properties/installations/values
PATCH /orgs/{org}/properties/installations/values/{property_name}
```

[Official documentation](https://docs.github.com/rest/orgs/custom-properties).

### Organization branch/tag/push rulesets and history

Coverage ID: `admin-organization-rulesets`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Administration organization write is required even for listed ruleset reads in current endpoint docs; owner or authorized role. Plan and rule-type gates apply; push rulesets, evaluate mode and repository targeting are not interchangeable. Preserve bypass actors.

Example routes (7 documented in this family):

```text
GET /orgs/{org}/rulesets
POST /orgs/{org}/rulesets
PUT /orgs/{org}/rulesets/{ruleset_id}
DELETE /orgs/{org}/rulesets/{ruleset_id}
```

[Official documentation](https://docs.github.com/rest/orgs/rules).

### Rule evaluation results

Coverage ID: `admin-organization-rule-suites`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Endpoint-specific organization Administration access. Results are evidence of evaluated pushes, not proof that every repository is covered.

Example routes (2 documented in this family):

```text
GET /orgs/{org}/rulesets/rule-suites
GET /orgs/{org}/rulesets/rule-suites/{rule_suite_id}
```

[Official documentation](https://docs.github.com/rest/orgs/rule-suites).

### Organization issue type definitions

Coverage ID: `admin-organization-issue-types`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization owner or delegated issue-type management; read/write according to endpoint. Issue types differ from labels and Projects single-select fields. Deletion affects assignments.

Example routes (4 documented in this family):

```text
GET /orgs/{org}/issue-types
POST /orgs/{org}/issue-types
PUT /orgs/{org}/issue-types/{issue_type_id}
DELETE /orgs/{org}/issue-types/{issue_type_id}
```

[Official documentation](https://docs.github.com/rest/orgs/issue-types).

### Organization issue field definitions

Coverage ID: `admin-organization-issue-fields`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization owner/delegated authority and endpoint-specific issue-field permissions. Availability can vary by rollout and plan; do not fabricate support on an older GitHub host.

Example routes (4 documented in this family):

```text
GET /orgs/{org}/issue-fields
POST /orgs/{org}/issue-fields
PATCH /orgs/{org}/issue-fields/{issue_field_id}
DELETE /orgs/{org}/issue-fields/{issue_field_id}
```

[Official documentation](https://docs.github.com/rest/orgs/issue-fields).

### Webhook configuration, ping, deliveries and redelivery

Coverage ID: `admin-organization-webhooks`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Owner; Webhooks read/write; classic scope admin:org_hook. OAuth Apps cannot inspect/edit hooks they did not create, and users cannot inspect/edit OAuth-created hooks. Secrets are not readable plaintext.

Example routes (11 documented in this family):

```text
GET /orgs/{org}/hooks
POST /orgs/{org}/hooks
PATCH /orgs/{org}/hooks/{hook_id}
DELETE /orgs/{org}/hooks/{hook_id}
```

[Official documentation](https://docs.github.com/rest/orgs/webhooks).

### Fine-grained token requests, approvals, access inventory and revocation

Coverage ID: `admin-organization-token-governance`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** GitHub App user or installation token; Personal access token requests read/write and Personal access tokens read/write for corresponding endpoints. These APIs are not supported by fine-grained PATs. Revoking organization access does not reveal or recreate token secrets.

Example routes (8 documented in this family):

```text
GET /orgs/{org}/personal-access-token-requests
POST /orgs/{org}/personal-access-token-requests
POST /orgs/{org}/personal-access-token-requests/{pat_request_id}
POST /orgs/{org}/personal-access-tokens
```

[Official documentation](https://docs.github.com/rest/orgs/personal-access-tokens).

### API usage by route, actor, user, subject and time

Coverage ID: `admin-organization-api-insights`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization owner/delegated API-insights authority; check endpoint token permissions. Enterprise Cloud availability and retention/window constraints apply; API activity is different from repository traffic.

Example routes (9 documented in this family):

```text
GET /orgs/{org}/insights/api/route-stats/{actor_type}/{actor_id}
GET /orgs/{org}/insights/api/subject-stats
```

[Official documentation](https://docs.github.com/rest/orgs/api-insights).

### Hosted-compute network configurations and settings

Coverage ID: `admin-organization-network-configurations`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Owner/network-configuration authority; endpoint-specific organization network configuration permission. Eligible hosted compute and Azure/network prerequisites apply; a configuration does not by itself attach every runner or codespace.

Example routes (6 documented in this family):

```text
GET /orgs/{org}/settings/network-configurations
POST /orgs/{org}/settings/network-configurations
PATCH /orgs/{org}/settings/network-configurations/{network_configuration_id}
DELETE /orgs/{org}/settings/network-configurations/{network_configuration_id}
```

[Official documentation](https://docs.github.com/rest/orgs/network-configurations).

### Identity-provider group mappings to teams

Coverage ID: `admin-team-idp-sync`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud organization owner; supported SAML provider and team synchronization. IdP is authoritative; never replace synchronized membership with direct user changes.

Example routes (3 documented in this family):

```text
GET /orgs/{org}/team-sync/groups
GET /orgs/{org}/teams/{team_slug}/team-sync/group-mappings
PATCH /orgs/{org}/teams/{team_slug}/team-sync/group-mappings
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/teams/team-sync).

### External group discovery and team connections

Coverage ID: `admin-team-external-groups`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Managed Users; owner or appropriate identity-management authority. Separate from ordinary team-sync APIs. Provisioning and group membership remain IdP-managed.

Example routes (5 documented in this family):

```text
GET /orgs/{org}/external-group/{group_id}
GET /orgs/{org}/external-groups
PATCH /orgs/{org}/teams/{team_slug}/external-groups
DELETE /orgs/{org}/teams/{team_slug}/external-groups
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/teams/external-groups).

### Organization audit events and SAML credential authorizations

Coverage ID: `admin-organization-audit-and-sso`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud; owner or audit-log reader; read:audit_log for supported classic reads, endpoint-specific authority for credential revocation. Only enterprise-specific extra routes are included here. Audit retention and credentials differ from repository events.

Example routes (7 documented in this family):

```text
GET /orgs/{org}/audit-log
GET /orgs/{org}/credential-authorizations
POST /orgs/{org}/credential-authorizations/revoke-all
POST /orgs/{org}/credential-authorizations/revoke-credential-type
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/orgs/orgs).

### Enterprise discovery and access-verification restrictions

Coverage ID: `admin-enterprise-accounts`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise owner/authorized enterprise role; Enterprise Cloud and endpoint-specific token support. Enterprise is not an organization. Changing access restrictions can affect every linked organization.

Example routes (2 documented in this family):

```text
POST /enterprises/{enterprise}/access-restrictions/disable
POST /enterprises/{enterprise}/access-restrictions/enable
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/enterprises).

### Enterprise audit queries and streaming configuration

Coverage ID: `admin-enterprise-audit`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise owner/delegated audit authority; classic read:audit_log where documented; inspect current per-endpoint App support. Streams require supported destination and secret encryption; query pagination, retention and event selection matter.

Example routes (7 documented in this family):

```text
GET /enterprises/{enterprise}/audit-log
GET /enterprises/{enterprise}/audit-log/stream-key
POST /enterprises/{enterprise}/audit-log/streams
PUT /enterprises/{enterprise}/audit-log/streams/{stream_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/audit-log).

### Enterprise role catalog and user/team assignments

Coverage ID: `admin-enterprise-role-assignments`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise owner/delegated enterprise role authority; enterprise role and membership permissions vary by operation. Enterprise roles and organization roles are independent; plan and enterprise membership prerequisites apply.

Example routes (10 documented in this family):

```text
GET /enterprises/{enterprise}/enterprise-roles
DELETE /enterprises/{enterprise}/enterprise-roles/teams/{team_slug}
PUT /enterprises/{enterprise}/enterprise-roles/teams/{team_slug}/{role_id}
DELETE /enterprises/{enterprise}/enterprise-roles/teams/{team_slug}/{role_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/enterprise-roles).

### Enterprise/team model policies, agent app models and AI feature policies

Coverage ID: `admin-enterprise-ai-controls`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud; enterprise owner/AI manager; Enterprise AI controls read/write where supported. A client may impose additional controls; policy availability depends on licensed products. Use endpoint docs rather than old blanket PAT-only guidance.

Example routes (10 documented in this family):

```text
GET /enterprises/{enterprise}/copilot/apps/model-policies
PATCH /enterprises/{enterprise}/copilot/apps/model-policies
PATCH /enterprises/{enterprise}/copilot/feature-policies
PATCH /enterprises/{enterprise}/copilot/fusion/model-policies
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/ai-controls).

### Enterprise-delegated credential grants and selective/bulk revocation

Coverage ID: `admin-enterprise-credentials`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise owner/delegated credential authority and exact endpoint token permissions. Bulk revocation can interrupt many users/integrations. Authorizations are not raw secrets.

Example routes (6 documented in this family):

```text
POST /enterprises/{enterprise}/credential-authorizations
DELETE /enterprises/{enterprise}/credential-authorizations
POST /enterprises/{enterprise}/credential-authorizations/revoke-all
POST /enterprises/{enterprise}/credential-authorizations/revoke-credential-type
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/credential-authorizations).

### Enterprise token inventory and token owner lookup

Coverage ID: `admin-enterprise-token-inventory`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud; security/enterprise authority and token-inventory permissions per endpoint. Inventory is sensitive metadata; no token-secret retrieval.

Example routes (4 documented in this family):

```text
GET /enterprises/{enterprise}/credentials
POST /enterprises/{enterprise}/credentials/exports
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/token-inventory).

### Consumed licenses, sync state, active committers and Visual Studio matches

Coverage ID: `admin-enterprise-licensing`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise owner/billing manager or endpoint-authorized role. License/seat counts and billable consumption differ; product and server synchronization prerequisites vary.

Example routes (6 documented in this family):

```text
GET /enterprises/{enterprise}/consumed-licenses
GET /enterprises/{enterprise}/license-sync-status
PUT /enterprises/{enterprise}/visual-studio-subscriptions/{visual_studio_subscription_id}
DELETE /enterprises/{enterprise}/visual-studio-subscriptions/{visual_studio_subscription_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/licensing).

### Enterprise repository custom-property schema and promotion

Coverage ID: `admin-enterprise-properties`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud; enterprise custom-properties management authority. Inherited definitions can constrain organization overrides; promoting a property changes ownership.

Example routes (6 documented in this family):

```text
GET /enterprises/{enterprise}/properties/schema
PATCH /enterprises/{enterprise}/properties/schema
PUT /enterprises/{enterprise}/properties/schema/organizations/{org}/{custom_property_name}/promote
PUT /enterprises/{enterprise}/properties/schema/{custom_property_name}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/custom-properties).

### Custom-property schema and values on organizations

Coverage ID: `admin-enterprise-organization-properties`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud; enterprise organization-property permissions by read/write/admin operation. Properties of organizations are separate from properties of repositories.

Example routes (7 documented in this family):

```text
GET /enterprises/{enterprise}/org-properties/schema
PATCH /enterprises/{enterprise}/org-properties/schema
PUT /enterprises/{enterprise}/org-properties/schema/{custom_property_name}
DELETE /enterprises/{enterprise}/org-properties/schema/{custom_property_name}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/custom-properties-for-orgs).

### Enterprise repository rulesets and versions

Coverage ID: `admin-enterprise-rulesets`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud owner/delegated enterprise ruleset management authority. Inspect inherited org/repository rules together; enterprise mutation support differs from repository-level API.

Example routes (6 documented in this family):

```text
POST /enterprises/{enterprise}/rulesets
GET /enterprises/{enterprise}/rulesets/{ruleset_id}
PUT /enterprises/{enterprise}/rulesets/{ruleset_id}
DELETE /enterprises/{enterprise}/rulesets/{ruleset_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/rules).

### Enterprise hosted-compute network configurations

Coverage ID: `admin-enterprise-network-configurations`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise owner/network authority; supported Enterprise Cloud hosted networking. Requires supported network resources and applicable hosted-compute licensing.

Example routes (6 documented in this family):

```text
GET /enterprises/{enterprise}/network-configurations
POST /enterprises/{enterprise}/network-configurations
PATCH /enterprises/{enterprise}/network-configurations/{network_configuration_id}
DELETE /enterprises/{enterprise}/network-configurations/{network_configuration_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/network-configurations).

### Install/uninstall Apps and change organization installation repository access

Coverage ID: `admin-enterprise-app-installations`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud owner/authorized enterprise App-installation authority. This is an enterprise installation API, not a general permission for any token to install arbitrary Apps on any account.

Example routes (9 documented in this family):

```text
GET /enterprises/{enterprise}/apps/installable_organizations
GET /enterprises/{enterprise}/apps/installable_organizations/{org}/accessible_repositories
POST /enterprises/{enterprise}/apps/organizations/{org}/installations
DELETE /enterprises/{enterprise}/apps/organizations/{org}/installations/{installation_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/organization-installations).

### Managed-user/group lifecycle and provisioning

Coverage ID: `admin-enterprise-scim`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Managed Users with supported IdP; provisioning credentials and SCIM endpoint permissions. Use IdP-led provisioning. Deprovisioning/suspension can remove enterprise access; normal personal-account creation APIs do not substitute.

Example routes (12 documented in this family):

```text
GET /scim/v2/enterprises/{enterprise}/Groups
POST /scim/v2/enterprises/{enterprise}/Groups
PUT /scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}
PATCH /scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/enterprise-admin/scim).

### Organization SCIM identities

Coverage ID: `admin-organization-scim`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise Cloud SAML/SCIM-supported organization; provisioning credentials. Not interchangeable with enterprise-managed-user SCIM; supported IdPs and token rules apply.

Example routes (6 documented in this family):

```text
GET /scim/v2/organizations/{org}/Users
POST /scim/v2/organizations/{org}/Users
PUT /scim/v2/organizations/{org}/Users/{scim_user_id}
PATCH /scim/v2/organizations/{org}/Users/{scim_user_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/scim/scim).

### Organization/user/enterprise metered and AI-credit usage

Coverage ID: `admin-billing-usage`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Account owner/billing manager or authorized billing role; organization Administration read on documented org usage routes. Use the account that is actually billed; organization-funded user usage is absent from personal-account reports. No fixed pricing assumptions.

Example routes (12 documented in this family):

```text
GET /organizations/{org}/settings/billing/ai_credit/usage
GET /organizations/{org}/settings/billing/premium_request/usage
```

[Official documentation](https://docs.github.com/rest/billing/usage).

### Budget inspection, creation, update and deletion

Coverage ID: `admin-billing-budgets`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Billing authority; Administration org read for documented org reads; write permissions and account eligibility per endpoint. Budget deletion can remove a spending limit. Alert-only and stop-usage budgets differ; changes can create costs or interrupt service.

Example routes (11 documented in this family):

```text
GET /organizations/{org}/settings/billing/budgets
POST /organizations/{org}/settings/billing/budgets
PATCH /organizations/{org}/settings/billing/budgets/{budget_id}
DELETE /organizations/{org}/settings/billing/budgets/{budget_id}
```

[Official documentation](https://docs.github.com/rest/billing/budgets).

### Cost center lifecycle, resource assignment and membership lookup

Coverage ID: `admin-billing-cost-centers`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise owner/billing manager or delegated enterprise billing read/write access. Org owners/delegated readers can be limited to accessible resources; cost centers are enterprise billing objects.

Example routes (8 documented in this family):

```text
GET /enterprises/{enterprise}/settings/billing/cost-centers
POST /enterprises/{enterprise}/settings/billing/cost-centers
PATCH /enterprises/{enterprise}/settings/billing/cost-centers/{cost_center_id}
DELETE /enterprises/{enterprise}/settings/billing/cost-centers/{cost_center_id}
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/billing/cost-centers).

### Asynchronous enterprise billing report generation and retrieval

Coverage ID: `admin-billing-usage-reports`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise billing access; enterprise owner/billing manager/delegated billing role. Inspect report completion and download; report request acceptance is not a completed report.

Example routes (3 documented in this family):

```text
GET /enterprises/{enterprise}/settings/billing/reports
POST /enterprises/{enterprise}/settings/billing/reports
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/billing/usage-reports).

### Codespace creation, configuration, start/stop, export and deletion

Coverage ID: `admin-codespaces-lifecycle`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated user and Codespaces permissions; repository access and accepted devcontainer permissions. Compute/storage may be billed; deleting a codespace can lose unpushed work. Export is asynchronous.

Example routes (16 documented in this family):

```text
GET /repos/{owner}/{repo}/codespaces
POST /repos/{owner}/{repo}/codespaces
POST /repos/{owner}/{repo}/pulls/{pull_number}/codespaces
POST /user/codespaces
```

[Official documentation](https://docs.github.com/rest/codespaces/codespaces).

### Available machine types

Coverage ID: `admin-codespaces-machines`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Repository/codespace read access; Codespaces metadata permission as documented. Machine choices depend on region, repository policy and billing entitlement.

Example routes (2 documented in this family):

```text
GET /repos/{owner}/{repo}/codespaces/machines
GET /user/codespaces/{codespace_name}/machines
```

[Official documentation](https://docs.github.com/rest/codespaces/machines).

### Organization-paid Codespaces access and organization lifecycle operations

Coverage ID: `admin-codespaces-organization-access`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization owner; organization Codespaces read/write and Codespaces lifecycle admin permissions as required. Organization management applies to qualifying organization-billed codespaces; do not assume authority over all user-owned codespaces. Three access-control endpoints are marked deprecated in the current spec without a definite closure date; inspect live supported replacements before mutation.

Example routes (7 documented in this family):

```text
GET /orgs/{org}/codespaces
PUT /orgs/{org}/codespaces/access
POST /orgs/{org}/codespaces/access/selected_users
DELETE /orgs/{org}/codespaces/access/selected_users
```

[Official documentation](https://docs.github.com/rest/codespaces/organizations).

### Encrypted organization Codespaces secrets and selected-repository access

Coverage ID: `admin-codespaces-organization-secrets`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization Codespaces secrets read/write; organization owner/delegated secret authority. Reads expose metadata only. Encrypt to retrieved public key; never log supplied plaintext.

Example routes (9 documented in this family):

```text
GET /orgs/{org}/codespaces/secrets
GET /orgs/{org}/codespaces/secrets/public-key
PUT /orgs/{org}/codespaces/secrets/{secret_name}
DELETE /orgs/{org}/codespaces/secrets/{secret_name}
```

[Official documentation](https://docs.github.com/rest/codespaces/organization-secrets).

### Encrypted repository Codespaces secrets

Coverage ID: `admin-codespaces-repository-secrets`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Repository Codespaces secrets read/write and repository admin/delegated authority. Secret value cannot be read back; verify name/scope metadata after a write.

Example routes (5 documented in this family):

```text
GET /repos/{owner}/{repo}/codespaces/secrets
GET /repos/{owner}/{repo}/codespaces/secrets/public-key
PUT /repos/{owner}/{repo}/codespaces/secrets/{secret_name}
DELETE /repos/{owner}/{repo}/codespaces/secrets/{secret_name}
```

[Official documentation](https://docs.github.com/rest/codespaces/repository-secrets).

### Encrypted personal Codespaces secrets and repository grants

Coverage ID: `admin-codespaces-user-secrets`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated user and Codespaces user secrets permission. Personal secrets differ from Actions, Dependabot and organization secret stores.

Example routes (9 documented in this family):

```text
GET /user/codespaces/secrets
GET /user/codespaces/secrets/public-key
PUT /user/codespaces/secrets/{secret_name}
DELETE /user/codespaces/secrets/{secret_name}
```

[Official documentation](https://docs.github.com/rest/codespaces/secrets).

### Copilot billing settings, seat inventory and team/user seat assignment

Coverage ID: `admin-copilot-seats`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Copilot Business/Enterprise and owner/billing authority; manage_billing:copilot or documented fine-grained permission. Seat assignment and removal affect billing/access. Plan-specific endpoints and cancellation semantics apply.

Example routes (7 documented in this family):

```text
GET /orgs/{org}/copilot/billing
GET /orgs/{org}/copilot/billing/seats
POST /orgs/{org}/copilot/billing/selected_teams
DELETE /orgs/{org}/copilot/billing/selected_teams
```

[Official documentation](https://docs.github.com/rest/copilot/copilot-user-management).

### Organization/team/enterprise/user usage reports

Coverage ID: `admin-copilot-usage-metrics`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Copilot entitlement, enabled metrics collection and owner/billing/delegated metrics authority; current enterprise App permission Enterprise Copilot metrics read where documented. Aggregation thresholds, date windows and privacy constraints apply. Legacy metrics and current downloadable usage reports differ.

Example routes (12 documented in this family):

```text
GET /enterprises/{enterprise}/copilot/metrics/reports/enterprise-1-day
GET /enterprises/{enterprise}/copilot/metrics/reports/enterprise-28-day/latest
```

[Official documentation](https://docs.github.com/rest/copilot/copilot-usage-metrics).

### Cloud-agent enablement and selected organizations/repositories

Coverage ID: `admin-copilot-agent-policy`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Enterprise AI controls read/write for supported App tokens; enterprise owners control enterprise policy; org owners control delegated org policy. Current general docs support App user/installation tokens for enterprise controls while older versioned pages can differ. Verify exact host/version. Product/plan policy applies.

Example routes (9 documented in this family):

```text
PUT /enterprises/{enterprise}/copilot/policies/coding_agent
POST /enterprises/{enterprise}/copilot/policies/coding_agent/organizations
DELETE /enterprises/{enterprise}/copilot/policies/coding_agent/organizations
PUT /orgs/{org}/copilot/coding-agent/permissions
```

[Official documentation](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-coding-agent-management).

### Cloud-agent task/session creation

Coverage ID: `admin-copilot-cloud-agent-sessions`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Supported Copilot plan; repository access and endpoint-specific agent permissions. Starting an agent consumes compute/AI allowance and may produce writes/PRs; review resulting work.

Example routes (1 documented in this family):

```text
GET /repos/{owner}/{repo}/copilot/cloud-agent/configuration
```

[Official documentation](https://docs.github.com/rest/copilot/copilot-cloud-agent-management).

### Copilot review policy and review usage settings

Coverage ID: `admin-copilot-code-review`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Copilot entitlement and repository/organization/enterprise policy authority per endpoint. Policy enablement does not guarantee a review occurred or that its findings are correct.

Example routes (10 documented in this family):

```text
GET /enterprises/{enterprise}/copilot/policies/code-review
PUT /enterprises/{enterprise}/copilot/policies/code-review
PUT /orgs/{org}/copilot/code-review/runner
PATCH /orgs/{org}/copilot/code-review/settings
```

[Official documentation](https://docs.github.com/rest/copilot/copilot-code-review).

### Copilot content-exclusion configuration

Coverage ID: `admin-copilot-content-exclusions`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Licensed organization/enterprise; owner or delegated content-exclusion authority. Exclusions are product/client-specific, not a universal data-access or secret-protection boundary.

Example routes (2 documented in this family):

```text
GET /orgs/{org}/copilot/content_exclusion
PUT /orgs/{org}/copilot/content_exclusion
```

[Official documentation](https://docs.github.com/rest/copilot/copilot-content-exclusion-management).

### Team-level Copilot customization settings

Coverage ID: `admin-copilot-team-customizations`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Copilot plan and team/org customization authority per endpoint. Team customization does not override stronger enterprise restrictions.

Example routes (3 documented in this family):

```text
GET /orgs/{org}/teams/{team_slug}/copilot/customizations
PUT /orgs/{org}/teams/{team_slug}/copilot/customizations
DELETE /orgs/{org}/teams/{team_slug}/copilot/customizations
```

[Official documentation](https://docs.github.com/rest/copilot/copilot-team-customizations).

### App identity, manifest conversion, installations, token mint/revoke and suspension

Coverage ID: `admin-github-apps`. Surfaces: REST API, gh api.

**Access and limits:** App JWT for App-owned routes; authorized App owner/user for relevant routes; narrowed installation permissions. App creation from a manifest needs the interactive manifest handshake. Installation requires authorized account approval except documented enterprise routes. Never expose private keys or minted tokens.

Example routes (14 documented in this family):

```text
GET /app
POST /app-manifests/{code}/conversions
DELETE /app/installations/{installation_id}
POST /app/installations/{installation_id}/access_tokens
```

[Official documentation](https://docs.github.com/rest/apps/apps).

### Installation repository visibility, grants and token revocation

Coverage ID: `admin-github-app-installations`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Installation token for installation reads; appropriate authenticated user token/admin authority for repository selection. Token cannot exceed installation grants; adding repositories does not add unapproved permissions.

Example routes (6 documented in this family):

```text
GET /installation/repositories
DELETE /installation/token
PUT /user/installations/{installation_id}/repositories/{repository_id}
DELETE /user/installations/{installation_id}/repositories/{repository_id}
```

[Official documentation](https://docs.github.com/rest/apps/installations).

### App webhook config, delivery inspection and redelivery

Coverage ID: `admin-github-app-webhooks`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated App JWT and App ownership. Distinct from organization/repository hooks. Delivery acceptance is not receiver-side processing proof.

Example routes (5 documented in this family):

```text
GET /app/hook/config
PATCH /app/hook/config
POST /app/hook/deliveries/{delivery_id}/attempts
```

[Official documentation](https://docs.github.com/rest/apps/webhooks).

### Check, reset or revoke App token/authorization

Coverage ID: `admin-oauth-app-authorizations`. Surfaces: REST API, gh api.

**Access and limits:** Owning OAuth/GitHub App client credentials where endpoint documents them. Cannot enumerate or mint arbitrary users' personal tokens. Reset invalidates existing credentials; do not log client secret or tokens.

Example routes (4 documented in this family):

```text
DELETE /applications/{client_id}/grant
POST /applications/{client_id}/token
PATCH /applications/{client_id}/token
DELETE /applications/{client_id}/token
```

[Official documentation](https://docs.github.com/rest/apps/oauth-applications).

### App plan, customer and authenticated-user subscription inspection

Coverage ID: `admin-marketplace`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** App JWT or authenticated user according to seller versus customer endpoint; Marketplace listing eligibility. APIs inspect subscriptions/plans; stub endpoints are test fixtures and not proof of paid purchase.

Example routes (8 documented in this family):

```text
GET /marketplace_listing/accounts/{account_id}
GET /marketplace_listing/plans
```

[Official documentation](https://docs.github.com/rest/apps/marketplace).

### Organization migration archives and repository locks

Coverage ID: `admin-organization-migrations`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization owner with documented migration scopes/token; supported source and target. Archive export APIs target specific migration paths, not a complete backup of every GitHub feature. Lock/unlock and archive deletion require care.

Example routes (7 documented in this family):

```text
GET /orgs/{org}/migrations
POST /orgs/{org}/migrations
DELETE /orgs/{org}/migrations/{migration_id}/archive
DELETE /orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock
```

[Official documentation](https://docs.github.com/rest/migrations/orgs).

### Personal repository migration archives and locks

Coverage ID: `admin-user-migrations`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated owner and documented migration token scopes. Source/target product and archive contents are restricted; verify downloaded archive and protect private content.

Example routes (7 documented in this family):

```text
GET /user/migrations
POST /user/migrations
DELETE /user/migrations/{migration_id}/archive
DELETE /user/migrations/{migration_id}/repos/{repo_name}/lock
```

[Official documentation](https://docs.github.com/rest/migrations/users).

### Closed legacy source-import API (historical coverage)

Coverage ID: `admin-source-imports`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** UNAVAILABLE on GitHub.com since 2024-04-12; these retained OpenAPI routes are historical, not executable capabilities. Use supported Git import/push or Enterprise Importer for eligible migrations; do not try to restore this closed API by broadening token privileges.

Example routes (8 documented in this family):

```text
GET /repos/{owner}/{repo}/import
PUT /repos/{owner}/{repo}/import
PATCH /repos/{owner}/{repo}/import
DELETE /repos/{owner}/{repo}/import
```

[Official documentation](https://docs.github.com/rest/migrations/source-imports).

### Public/authenticated account profile inspection and update

Coverage ID: `admin-account-profile`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public reads may be anonymous; authenticated profile changes require user-account profile permission. User account signup, password, 2FA and recovery are not ordinary REST profile writes; managed-user constraints apply.

Example routes (6 documented in this family):

```text
GET /user
PATCH /user
```

[Official documentation](https://docs.github.com/rest/users/users).

### Personal email addresses and visibility

Coverage ID: `admin-account-emails`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated account; email-addresses read/write or documented classic user:email scope. Email verification still requires user interaction; never promise API-only verification or add another person's address.

Example routes (5 documented in this family):

```text
PATCH /user/email/visibility
GET /user/emails
POST /user/emails
DELETE /user/emails
```

[Official documentation](https://docs.github.com/rest/users/emails).

### SSH authentication public keys

Coverage ID: `admin-account-keys`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated account Git SSH keys read/write; public-key listing can be anonymous. Public keys only; private keys are never retrievable. Adding a key grants authentication capability.

Example routes (5 documented in this family):

```text
GET /user/keys
POST /user/keys
DELETE /user/keys/{key_id}
```

[Official documentation](https://docs.github.com/rest/users/keys).

### GPG public signing keys

Coverage ID: `admin-account-gpg-keys`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated account GPG keys read/write. Key publication does not create a private signing key or prove commit verification for every signature.

Example routes (5 documented in this family):

```text
GET /user/gpg_keys
POST /user/gpg_keys
DELETE /user/gpg_keys/{gpg_key_id}
```

[Official documentation](https://docs.github.com/rest/users/gpg-keys).

### SSH public signing keys

Coverage ID: `admin-account-ssh-signing-keys`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated account SSH signing keys read/write. Signing keys and SSH authentication keys are separate stores.

Example routes (5 documented in this family):

```text
GET /user/ssh_signing_keys
POST /user/ssh_signing_keys
DELETE /user/ssh_signing_keys/{ssh_signing_key_id}
```

[Official documentation](https://docs.github.com/rest/users/ssh-signing-keys).

### Follower discovery and follow/unfollow

Coverage ID: `admin-account-following`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public reads; authenticated follower-management permission for writes. Social following creates notifications and is not repository watching.

Example routes (8 documented in this family):

```text
GET /user/followers
GET /user/following
PUT /user/following/{username}
DELETE /user/following/{username}
```

[Official documentation](https://docs.github.com/rest/users/followers).

### Personal blocked-user management

Coverage ID: `admin-account-blocking`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated account Blocking users read/write. User block and organization block are separate actions with different scope.

Example routes (4 documented in this family):

```text
GET /user/blocks
GET /user/blocks/{username}
PUT /user/blocks/{username}
DELETE /user/blocks/{username}
```

[Official documentation](https://docs.github.com/rest/users/blocking).

### Personal profile social links

Coverage ID: `admin-account-social-links`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public reads; authenticated user profile write for changes. Publicly exposes supplied profile links.

Example routes (4 documented in this family):

```text
GET /user/social_accounts
POST /user/social_accounts
DELETE /user/social_accounts
```

[Official documentation](https://docs.github.com/rest/users/social-accounts).

### Gist lifecycle, files, history, forks and stars

Coverage ID: `admin-gists`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public reads; authenticated Gists write permission or classic gist scope for writes. Secret gists are unlisted, not access-controlled private repositories. Deleted files/revisions can remain in history.

Example routes (15 documented in this family):

```text
GET /gists
POST /gists
PATCH /gists/{gist_id}
DELETE /gists/{gist_id}
```

[Official documentation](https://docs.github.com/rest/gists/gists).

### Gist comment lifecycle

Coverage ID: `admin-gist-comments`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public reads where accessible; authenticated gist permission and author/moderation rights for writes. Comments are external communication; use only within authorized scope.

Example routes (5 documented in this family):

```text
GET /gists/{gist_id}/comments
POST /gists/{gist_id}/comments
PATCH /gists/{gist_id}/comments/{comment_id}
DELETE /gists/{gist_id}/comments/{comment_id}
```

[Official documentation](https://docs.github.com/rest/gists/comments).

### Star/unstar repositories and list stars/stargazers

Coverage ID: `admin-repository-stars`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public reads; authenticated Starring read/write permission for personal list/actions. Stars are personal social actions, distinct from watches and Projects.

Example routes (8 documented in this family):

```text
GET /repos/{owner}/{repo}/stargazers
GET /repos/{owner}/{repo}/stargazers/count
PUT /user/starred/{owner}/{repo}
DELETE /user/starred/{owner}/{repo}
```

[Official documentation](https://docs.github.com/rest/activity/starring).

### Repository subscribers and personal watch subscriptions

Coverage ID: `admin-repository-watches`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public subscriber reads where available; authenticated Watching read/write. Watch changes alter notifications for the authenticated user, not all collaborators.

Example routes (6 documented in this family):

```text
GET /repos/{owner}/{repo}/subscribers
GET /repos/{owner}/{repo}/subscription
PUT /repos/{owner}/{repo}/subscription
DELETE /repos/{owner}/{repo}/subscription
```

[Official documentation](https://docs.github.com/rest/activity/watching).

### Personal notification inbox, thread state and subscriptions

Coverage ID: `admin-notifications`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated user notifications permission or classic notifications scope as documented. Inbox is not an audit log; marking read/done changes personal state.

Example routes (10 documented in this family):

```text
GET /notifications
PUT /notifications
PATCH /notifications/threads/{thread_id}
DELETE /notifications/threads/{thread_id}
```

[Official documentation](https://docs.github.com/rest/activity/notifications).

### Public/private activity event feeds

Coverage ID: `admin-activity-events`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public reads or authenticated access for private events. Events have retention/latency limits and are not a reliable audit trail or complete webhook replacement.

Example routes (9 documented in this family):

```text
GET /events
GET /networks/{owner}/{repo}/events
```

[Official documentation](https://docs.github.com/rest/activity/events).

### Account feed links

Coverage ID: `admin-activity-feeds`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Public or authenticated user context according to feed. Private feed URLs may contain credentials; treat them as secrets.

Example routes (1 documented in this family):

```text
GET /feeds
```

[Official documentation](https://docs.github.com/rest/activity/feeds).

### Agent automation lifecycle, runs and scheduling

Coverage ID: `admin-agent-automations`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Authenticated account/repository authority and endpoint-specific agent-automation permissions; verify product entitlement. Scheduled agents can consume paid usage and perform repository writes. Inspect schedule, actor, permissions and run outputs; automation creation is not successful execution.

Example routes (12 documented in this family):

```text
GET /agents/automations
GET /agents/repos/{owner}/{repo}/automations
POST /agents/repos/{owner}/{repo}/automations
PATCH /agents/repos/{owner}/{repo}/automations/{automation_id}
```

[Official documentation](https://docs.github.com/rest/agent-automations/agent-automations).

### Agent task creation, status and task lifecycle

Coverage ID: `admin-agent-tasks`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Repository access, supported agent entitlement and endpoint-specific task permissions. Task execution can run code and produce changes. Verify actual task state, artifacts and resulting PRs; do not equate accepted with completed.

Example routes (5 documented in this family):

```text
GET /agents/repos/{owner}/{repo}/tasks
POST /agents/repos/{owner}/{repo}/tasks
```

[Official documentation](https://docs.github.com/rest/agent-tasks/agent-tasks).

### Agent organization/repository encrypted secrets and repository selection

Coverage ID: `admin-agent-secrets`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Endpoint-specific organization/repository agent secret read/write permissions and delegated admin authority. Agent secret stores are distinct from Actions/Codespaces/Dependabot. Values cannot be read back; use documented public-key encryption and verify metadata/scope only.

Example routes (15 documented in this family):

```text
GET /orgs/{org}/agents/secrets
GET /orgs/{org}/agents/secrets/public-key
PUT /orgs/{org}/agents/secrets/{secret_name}
DELETE /orgs/{org}/agents/secrets/{secret_name}
```

[Official documentation](https://docs.github.com/rest/agents/secrets).

### Agent organization/repository variables and repository selection

Coverage ID: `admin-agent-variables`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Endpoint-specific organization/repository agent variable read/write permissions. Variables are plaintext configuration, not a place for secrets; organization selection and repository overrides affect effective values.

Example routes (15 documented in this family):

```text
GET /orgs/{org}/agents/variables
POST /orgs/{org}/agents/variables
PATCH /orgs/{org}/agents/variables/{name}
DELETE /orgs/{org}/agents/variables/{name}
```

[Official documentation](https://docs.github.com/rest/agents/variables).

### Copilot Space lifecycle and discovery

Coverage ID: `admin-copilot-spaces`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Space owner/collaborator authority and applicable Copilot Spaces API permissions/entitlement. Space visibility can expose context. A GitHub Copilot Space is distinct from a ChatGPT Space and GitHub Project.

Example routes (10 documented in this family):

```text
GET /orgs/{org}/copilot-spaces
POST /orgs/{org}/copilot-spaces
PUT /orgs/{org}/copilot-spaces/{space_number}
DELETE /orgs/{org}/copilot-spaces/{space_number}
```

[Official documentation](https://docs.github.com/rest/copilot-spaces/copilot-spaces).

### Copilot Space user/team collaborators

Coverage ID: `admin-copilot-space-collaborators`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Space owner/admin and endpoint-specific collaborator permissions. Granting a Space role does not necessarily grant access to underlying private repositories/resources.

Example routes (8 documented in this family):

```text
GET /orgs/{org}/copilot-spaces/{space_number}/collaborators
POST /orgs/{org}/copilot-spaces/{space_number}/collaborators
PUT /orgs/{org}/copilot-spaces/{space_number}/collaborators/{actor_type}/{actor_identifier}
DELETE /orgs/{org}/copilot-spaces/{space_number}/collaborators/{actor_type}/{actor_identifier}
```

[Official documentation](https://docs.github.com/rest/copilot-spaces/collaborators).

### Copilot Space attached repository/file/text resources

Coverage ID: `admin-copilot-space-resources`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Space write authority plus source-resource access. Attachments may expose context; verify visibility and source access independently. Metadata attachment is not evidence the agent can read all source contents.

Example routes (10 documented in this family):

```text
GET /orgs/{org}/copilot-spaces/{space_number}/resources
POST /orgs/{org}/copilot-spaces/{space_number}/resources
PUT /orgs/{org}/copilot-spaces/{space_number}/resources/{space_resource_id}
DELETE /orgs/{org}/copilot-spaces/{space_number}/resources/{space_resource_id}
```

[Official documentation](https://docs.github.com/rest/copilot-spaces/resources).

### Organization private-registry authentication configurations

Coverage ID: `admin-private-registries`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Organization owner/delegated registry manager; Private registry configurations permissions by operation. Secret authentication material uses documented encryption; private registry reachability, supported ecosystem and consumer configuration must be verified separately.

Example routes (6 documented in this family):

```text
GET /orgs/{org}/private-registries
POST /orgs/{org}/private-registries
PATCH /orgs/{org}/private-registries/{secret_name}
DELETE /orgs/{org}/private-registries/{secret_name}
```

[Official documentation](https://docs.github.com/rest/private-registries/organization-configurations).

### Closed GitHub Classroom API (historical coverage)

Coverage ID: `admin-classroom`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** UNAVAILABLE since 2026-08-28 according to all six current official endpoint descriptions. The OpenAPI still retains routes for historical compatibility documentation. Do not claim Classroom reporting works or infer that missing permission is the cause of endpoint closure; student identifiers and grades remain sensitive.

Example routes (6 documented in this family):

```text
GET /assignments/{assignment_id}
GET /assignments/{assignment_id}/accepted_assignments
```

[Official documentation](https://docs.github.com/rest/classroom/classroom).

### Revocation of exposed supported GitHub credentials

Coverage ID: `admin-credential-revocation`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Endpoint supports documented credential-revocation flow; verify token type and credential format. Revocation invalidates credentials and can break integrations; never disclose submitted tokens in logs. This is not token issuance or account recovery.

Example routes (1 documented in this family):

```text
POST /credentials/revoke
```

[Official documentation](https://docs.github.com/rest/credentials/revoke).

### Organization/enterprise SAML SSO, 2FA, SSH CA, IP allow lists and domain verification

Coverage ID: `admin-identity-policies`. Surfaces: GitHub web UI, GraphQL API, DNS provider.

**Access and limits:** Owners/security administrators; Enterprise Cloud for SAML/IP/SSH CA features as documented. DNS changes need domain authority. Some authentication/IdP steps require interactive user action. IP policy changes can lock out the agent; IdP conditional-access mode can disable GitHub allow-list APIs.

Operations: inspect authentication settings; configure authorized SSO/2FA/IP policy; manage IP allow-list entries via supported GraphQL mutations; verify domain DNS challenge.

[Official documentation](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization).

### Organization/enterprise policy inheritance and defaults

Coverage ID: `admin-organization-policy-settings`. Surfaces: GitHub web UI, REST API, GraphQL API.

**Access and limits:** Organization/enterprise owners; exact APIs vary by policy. A field in the organization PATCH API does not imply every web setting is writable. Preserve inherited enterprise controls; mark UI-only settings explicitly.

Operations: inspect member privileges and default repository permissions; reconcile repository creation, deletion, transfer, forking and visibility policies; inspect OAuth/App/PAT access policies; inspect Actions, Packages, Pages and Codespaces restrictions.

[Official documentation](https://docs.github.com/en/organizations/managing-organization-settings).

### Account/organization shared community files and templates

Coverage ID: `admin-community-defaults`. Surfaces: Git, Contents REST API, GitHub web UI.

**Access and limits:** Contents write on shared .github repository. Normally public; managed-user organization defaults use internal repository. No inherited default LICENSE. Changes affect repositories lacking overrides; template files do not create referenced labels.

Operations: inspect .github defaults and local overrides; edit supported health files and issue/PR/discussion templates through PR; check inheritance and rendered create flow.

[Official documentation](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).

### Organization public/member profile and pinned repositories

Coverage ID: `admin-organization-profile-content`. Surfaces: Git, Contents REST API, GitHub web UI.

**Access and limits:** Contents write for profile files; organization owners pin repositories in UI. Member profile requires private .github-private, not internal. Public profile unavailable for EMU organizations; never leak member-only content into public README.

Operations: edit .github/profile/README.md; edit private .github-private/profile/README.md; inspect/reorder public or member pinned repositories.

[Official documentation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile).

### GitHub Enterprise Importer migrations

Coverage ID: `admin-enterprise-importer`. Surfaces: GitHub CLI GEI extension, GraphQL API, GitHub web UI.

**Access and limits:** Requires supported Enterprise Cloud destination, source/destination access and migrator/owner authority; check token scopes and IP policies. Not every feature migrates: verify source-specific limits, LFS, attachments, webhooks, secrets, audit logs, team references and Actions execution state separately.

Operations: inventory supported source and destination; grant/check migrator role; start and monitor repository or organization migration; inspect migration logs and map mannequins; verify repository and organization settings after migration.

[Official documentation](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-between-github-products/migrating-repositories-from-githubcom-to-github-enterprise-cloud).

### Repository transfer, archive/unarchive, deletion and restoration

Coverage ID: `admin-repository-lifecycle-admin`. Surfaces: REST API, gh repo, GitHub web UI.

**Access and limits:** Repository admin and permitted target organization creation/transfer authority; delete_repo for classic deletion where required. Transfers change ownership/access/billing; restoration is time- and fork-network-dependent and must not be promised. Git archive downloads are not archival policy.

Operations: inspect archive/ownership state; transfer repository with explicit target and teams; archive/unarchive via repository update; delete or restore with documented recovery constraints.

[Official documentation](https://docs.github.com/en/rest/repos/repos).

### Repository traffic, statistics and community health

Coverage ID: `admin-repository-insights`. Surfaces: REST API, gh api, GitHub web UI.

**Access and limits:** Traffic requires repository push access and Contents read under documented fine-grained endpoints; statistics availability varies by repository size and host. Traffic has a short reporting window; statistics can return 202 while computing. UI insights are not all writeable through API.

Operations: read clones/views/referrers/popular paths; read contributor/commit/code-frequency statistics; read community profile; inspect dependency, network and pulse views where available.

[Official documentation](https://docs.github.com/en/rest/metrics).

### Devcontainer configuration and Codespaces prebuild/policy settings

Coverage ID: `admin-devcontainers`. Surfaces: Git, Codespaces REST API, GitHub web UI, devcontainer CLI when installed.

**Access and limits:** Repository Contents write for config; Codespaces entitlement and admin for prebuild/policy settings. Do not execute untrusted lifecycle commands without considering secrets and privilege. Git config commits are not evidence of successful prebuild or live policy changes.

Operations: inspect/edit .devcontainer/devcontainer.json and related Dockerfiles; validate container build and feature configuration; inspect Codespaces prebuilds, retention, idle timeout, machine and region policies.

[Official documentation](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces).

### Copilot MCP controls, registries, custom agents and managed client settings

Coverage ID: `admin-mcp-and-custom-agent-policy`. Surfaces: GitHub web UI, Git, supported policy REST API, managed client configuration.

**Access and limits:** Enterprise owner/AI manager for enterprise settings; repository authority for repository agent config; product/client gates apply. Private MCP registries cover Copilot CLI/IDEs, not cloud agents. A registry setting is not a universal tool-access grant; secrets and external-tool permissions stay independent.

Operations: inspect enterprise MCP access and registry policies; configure authorized repository MCP settings; maintain .github/agents profiles and organization/enterprise agent definitions; inspect managed-settings.json deployment and client compatibility.

[Official documentation](https://docs.github.com/en/copilot/concepts/enterprise/agent-management).

### Git LFS tracking, migration, verification, archive and billing behavior

Coverage ID: `admin-git-lfs`. Surfaces: Git LFS CLI, Git, GitHub web UI, billing REST API.

**Access and limits:** Repository read/write; admin for archive settings; account billing role for budget. History migration rewrites commits and needs explicit authorization. Removing pointers/history does not purge remote LFS storage; request GitHub Support when purge is required. Do not delete/recreate a repository to save storage without explicit authorization.

Operations: inspect git lfs env/ls-files and .gitattributes; track or migrate authorized large files; fetch/push/verify objects; inspect LFS archive inclusion and billed usage.

[Official documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage).

### Personal account security, billing and recovery boundaries

Coverage ID: `admin-account-security-and-billing-ui`. Surfaces: GitHub web UI, documented REST API for narrow supported operations.

**Access and limits:** Account owner; MFA/passkey/password/payment/recovery steps can require interactive user input. Never claim ordinary API support for signup, password/2FA recovery, arbitrary PAT creation or full billing checkout.

Operations: inspect account sessions, authorized Apps and token settings; guide token/key rotation and session revocation; inspect subscriptions, invoices, payment method and account recovery.

[Official documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure).

### GitHub Enterprise Server appliance administration

Coverage ID: `admin-enterprise-server-admin`. Surfaces: GHES REST API, Management Console API, SSH administrative shell, GitHub web UI.

**Access and limits:** GHES site administrator and instance-specific credentials; exact version and deployment access required. This plugin has no appliance credentials by default. Cloud organization ownership does not grant site administration. Backup/restore and upgrades require the owning runbook and maintenance authorization.

Operations: identify deployed version and API base URL; inspect appliance health and admin stats; plan backups, upgrades, license and maintenance; use documented management console APIs and administrative SSH only when authorized.

[Official documentation](https://docs.github.com/en/enterprise-server@latest/admin).

## Cross-feature gaps to record explicitly

Coverage is complete only when every applicable family has observed evidence or a named blocker. A plan gate, required owner role, unsupported token, IdP/DNS prerequisite, unavailable UI automation or uninstalled optional CLI is a **gap**, not proof that a feature is configured. Do not enable paid products, create identities or publish public profile content just to make a checklist green.

The REST inventory is a documented surface map, not an independent implementation of every GitHub feature or an assurance that current credentials were tested. UI-specific settings, rollout previews, client-specific Copilot policies, Enterprise Server versions, external identity providers and billing providers require live inspection in the relevant environment. Shared workflow templates, Projects templates, security configuration and repository collaboration features also have their dedicated coverage elsewhere in this skill; organization-level ownership must be checked when those operations are selected.

## Additional platform and product surfaces

These capabilities require product-level handling beyond the api.github.com operation registry. Retired services are recorded as unavailable, not executable.

### Retired GitHub Models playground, catalog, inference and BYOK

Coverage ID: `admin-github-models-retired`. Surfaces: Historical product documentation, Git repository inspection.

Operations: identify former GitHub Models integrations, prompt/evaluation assets and models.github.ai dependencies; record service retirement and preserve existing repository prompt/evaluation files; plan an authorized replacement against its own current provider documentation.

**Access and limits:** UNAVAILABLE: GitHub Models was fully retired 2026-07-30, including playground, model catalog, inference API and BYOK. Do not present models.github.ai inference/catalog/evaluation as live GitHub capabilities. Existing prompt/evaluation files do not establish service availability. Copilot is a separate product, and an alternative provider needs its own permissions, costs and data policy.

**Verification:** Verify the official retirement notice and identify actual caller configuration without sending inference traffic to the retired service. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/github-models).

### GitHub Connect between Enterprise Server and Enterprise Cloud

Coverage ID: `admin-github-connect`. Surfaces: GHES enterprise/site administration UI, GitHub Enterprise Cloud UI, documented instance APIs.

Operations: inspect/enable authorized Connect association with GitHub.com or GHE.com; inspect automatic license synchronization and latest sync evidence; inspect connected Dependabot, server statistics, unified search and connected workflow capabilities; inspect per-user cloud-account connection for private unified search.

**Access and limits:** Supported GHES version, site/enterprise administrator authority and a corresponding Cloud enterprise/account are required. Connect association and each connected capability are separate settings. Unified search is a server web-search feature; REST/GraphQL searches do not automatically include Cloud results. Network/identity prerequisites and licensed features apply.

**Verification:** Read both sides of the association, actual synchronization state and each enabled capability; verify a representative authorized user experience. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/enterprise-server@3.22/admin/configuring-settings/configuring-github-connect).

### Enterprise support entitlements and access

Coverage ID: `admin-support-entitlements`. Surfaces: GitHub enterprise settings UI, GitHub Support portal.

Operations: inspect current support plan and entitled members; grant/revoke support entitlements for authorized enterprise members; verify Support portal access under the correct enterprise identity.

**Access and limits:** Enterprise owners manage entitlements; owners and billing managers have entitlement automatically. Eligible extra-member counts depend on support plan. Ordinary organization ticket access and enterprise support entitlements are different; refreshed portal sign-in may be needed.

**Verification:** Read the entitlement list and have the intended identity verify enterprise selection in the Support portal. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-support-entitlements-for-your-enterprise).

### GitHub Support tickets, attachments and ongoing case management

Coverage ID: `admin-support-tickets`. Surfaces: GitHub Support portal, authorized browser interaction.

Operations: inspect existing tickets and entitled account scope; prepare diagnostic evidence and reproduction details; create an explicitly authorized ticket or reply through the Support portal; track responses, status and requested evidence.

**Access and limits:** Correct account/product identity and support entitlement/plan apply; data-resident enterprise cases use the GHE.com identity. Ticket submission/replies contact another party and require explicit user authorization. Do not invent a public general-purpose Support REST API. Uploaded attachment URLs may be accessible without authentication; remove secrets and private data.

**Verification:** Read back the actual ticket ID, account, submitted content and status. Prepared diagnostics or a filled form are not proof of submission. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/enterprise-cloud@latest/support/contacting-github-support/creating-a-support-ticket).

### Enterprise organization creation, invitations and transfers

Coverage ID: `admin-enterprise-organization-lifecycle`. Surfaces: GitHub enterprise settings UI, documented GraphQL enterprise mutations.

Operations: inspect organizations linked to the enterprise and pending invitations; create an authorized organization within the enterprise; invite an existing eligible organization; transfer an eligible organization between enterprises and verify policies/billing/access.

**Access and limits:** Enterprise owners; enterprise type, ownership, billing and policy effects need authorization. Enterprise Managed Users cannot add existing ordinary organizations. GitHub.com organizations cannot be transferred directly to a GHE.com enterprise; use supported migration instead.

**Verification:** Read the owning enterprise, organization identity, effective policies, memberships and billing association after the operation. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/adding-organizations-to-your-enterprise).

### Enterprise Cloud data residency and host-specific feature/network compatibility

Coverage ID: `admin-enterprise-data-residency`. Surfaces: Enterprise settings UI, host-specific REST/GraphQL APIs, GitHub Enterprise Importer, IdP/network administration.

Operations: identify GitHub.com, GHE.com or GHES hosting and actual API hostname; inspect data region, enterprise type and feature availability; verify identity provisioning, trusted SSH fingerprints and required network domains through host-specific meta data; prepare authorized migration/onboarding and inspect billing connections.

**Access and limits:** Data-resident Enterprise Cloud uses managed users and a dedicated GHE.com subdomain. Product features, domains and network behavior can differ from GitHub.com; do not reuse github.com API paths/SSH identity blindly. Region guarantees have documented exceptions; account creation, migration, billing and network changes need the corresponding authority.

**Verification:** Check the enterprise host and current feature matrix, fetch its own /meta data and verify affected product access in the actual tenant. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/feature-overview-for-github-enterprise-cloud-with-data-residency).

### Personal account data export and expiring archive access

Coverage ID: `admin-personal-data-export`. Surfaces: GitHub account settings UI, User Migration REST API, authenticated download.

Operations: request authorized account-data export through account settings or supported migration API; inspect completion notification and retrieve the resulting archive; revoke an active export download link.

**Access and limits:** Account owner; UI may require password reauthentication/email interaction. The export is a point-in-time metadata archive, not a continuously updated backup of every service. Download links expire and exports contain private personal information.

**Verification:** Check completed export state, inspect downloaded archive structure without exposing private content, and verify link revocation when requested. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/requesting-an-archive-of-your-personal-accounts-data).

### Public repository participation in the GitHub Archive Program

Coverage ID: `admin-archive-program`. Surfaces: Repository settings UI.

Operations: inspect Preserve this repository setting; opt an authorized public repository into/out of future long-term preservation.

**Access and limits:** Public repository administrator. This is separate from repository read-only archival and downloading a ZIP/tarball. Opting out affects future program archives and does not retract content already archived elsewhere.

**Verification:** Read back the repository preservation setting in the owning settings page. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/opting-into-or-out-of-the-github-archive-program-for-your-public-repository).

### GitHub platform API discovery, host metadata and operational diagnostics

Coverage ID: `admin-platform-meta`. Surfaces: REST API, gh api, GitHub Status web UI.

Operations: GET /; GET /meta; GET /versions; GET /octocat; GET /zen; inspect host-specific endpoint URLs, SSH fingerprints, IP ranges and advertised domains.

**Access and limits:** Public metadata usually needs no account permission; use the actual host. Meta IP/domain lists are not permanent and can omit some services; do not automatically rewrite firewalls from a partial snapshot. Status information is operational evidence, not proof that a specific repository operation succeeded.

**Verification:** Fetch the intended host metadata and inspect response headers/host identity; preserve actual request failures and relevant status evidence. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/rest/meta).

### REST/GraphQL rate-limit budgets and respectful retry behavior

Coverage ID: `admin-platform-rate-limits`. Surfaces: REST API, GraphQL API, gh api response headers.

Operations: GET /rate_limit; inspect x-ratelimit-* and retry-after headers; query GraphQL rateLimit cost/remaining/reset fields; paginate and pace operations; obey primary/secondary limits and backoff.

**Access and limits:** Unauthenticated and authenticated budgets differ by token, resource and product. A positive core budget does not rule out search, GraphQL or secondary throttling. Avoid needless repeated /rate_limit polling and never broaden credentials merely to bypass limits.

**Verification:** Record returned quota/reset data and actual throttled response; resume only under documented retry rules and verify resulting operations. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/rest/rate-limit).

### License catalog and detected repository license metadata

Coverage ID: `admin-platform-license-catalog`. Surfaces: REST API, gh api.

Operations: GET /licenses; GET /licenses/{license}; GET /repos/{owner}/{repo}/license; inspect SPDX identifiers and license templates for an owner-selected license.

**Access and limits:** Public catalog reads usually need no permission; private repository license detection requires repository access. Detection can be incomplete for custom/multiple licenses. Template discovery does not select a license or grant authority to relicense existing content.

**Verification:** Read the detected file and owner-approved licensing choice; verify actual committed license text when a separate authorized change is made. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/rest/licenses).

### GitHub gitignore template catalog

Coverage ID: `admin-platform-gitignore-templates`. Surfaces: REST API, gh api, Git.

Operations: GET /gitignore/templates; GET /gitignore/templates/{name}; compare selected template with existing repository ignore rules.

**Access and limits:** Catalog is publicly readable; committing a selected template needs Contents write/normal PR authority. Preserve repository-specific rules. Ignoring a path does not remove already tracked content, purge history or secure leaked secrets.

**Verification:** Fetch the template and check effective local rules using git check-ignore; inspect tracked files separately. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/rest/gitignore).

### GitHub emoji catalog

Coverage ID: `admin-platform-emojis`. Surfaces: REST API, gh api.

Operations: GET /emojis; resolve supported shortcodes and image URLs for GitHub-authored content.

**Access and limits:** Public read; catalog/image references are presentation data, not an authorization or upload endpoint. No personal/team custom emoji administration is implied.

**Verification:** Read current shortcode mappings and verify rendering only when that matters for the requested content. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/rest/emojis).

### GitHub Markdown and GFM rendering utilities

Coverage ID: `admin-platform-markdown-rendering`. Surfaces: REST API, gh api, GitHub rendered UI.

Operations: POST /markdown; POST /markdown/raw; render content using repository context when supported to resolve issue/user references.

**Access and limits:** Rendering POSTs return HTML; they do not create a comment, file or Page. Repository context can require source access. Treat returned HTML with the destination renderer security model; rendered preview is not a substitute for accessibility or link checks.

**Verification:** Inspect the returned rendered HTML and relevant target UI; verify context-sensitive links resolve to the intended objects. Official documentation checked 2026-11-15; no live write test.

[Official documentation](https://docs.github.com/en/rest/markdown).


## Spark and Copilot client/runtime products

GitHub Models retirement is already covered by `admin-github-models-retired`; these current product surfaces are independent of that retired service. GitHub Mobile uses the existing issue/PR/notification/account capability families and does not need duplicate API coverage.

### GitHub Spark app creation, iteration, publishing and data-access controls

Coverage ID: `admin-github-spark`. Surfaces: GitHub Spark web UI, deployed Spark site, linked Git repository when available.

Operations: inspect an existing spark and its current publication/access state; create/iterate an authorized app through Spark prompts, preview and available editing tools; inspect repository/code linkage where available without assuming a generic Spark REST API; publish an approved version and select private, organization or all-GitHub-users visibility where eligible; set read-only versus write access for shared app data; verify the deployed site.

**Access and limits:** Requires eligible Spark entitlement, enabled account/organization policy and interactive authenticated UI. Publishing is deployment and data exposure, so authorization must cover both visibility and data-write access. All-GitHub-users access is unavailable for managed users. Read-only access differs from private visibility. Review and remove private app data before widening access; do not claim arbitrary Spark lifecycle REST endpoints from the repository API inventory.

**Verification:** Read deployed URL and publication/data-access settings, then verify intended authenticated audience can access the correct version and permitted data operations. Official documentation checked 2026-11-15; no live product mutation test.

[Official documentation](https://docs.github.com/en/copilot/tutorials/spark/your-first-spark).

### Copilot CLI local sessions, instructions, skills, plugins, hooks, LSP and permission settings

Coverage ID: `admin-copilot-cli-customization`. Surfaces: Copilot CLI, Git repository files, user-local CLI configuration, organization/enterprise policy UI.

Operations: inspect installed CLI version/authentication, enabled organization policy and discovered customizations; maintain repository/user instructions and path-specific instruction files without conflicts; configure authorized skills, custom agents, hooks, MCP/LSP servers, plugins and marketplaces; inspect CLI settings, model/provider selection, workspace paths and tool permissions; start/resume authorized sessions and verify loaded customizations and resulting outputs.

**Access and limits:** Copilot CLI entitlement, installed runtime and organization policy apply. Hooks/plugins/tools may execute arbitrary local commands or contact external services; config discovery is not execution authorization. Preserve host approval boundaries and secrets. Client-specific plugin components are not universally portable; consult installed CLI format support. Instructions may require a fresh/resumed session to reload; do not assume Codex skill installation installs a Copilot plugin.

**Verification:** Inspect current CLI help/settings and loaded instructions/plugins, then verify a bounded authorized session uses the intended configuration and retains tool permission controls. Official documentation checked 2026-11-15; no live product mutation test.

[Official documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview).

### Copilot SDK application integration, sessions, tools and lifecycle control

Coverage ID: `admin-copilot-sdk`. Surfaces: Official Copilot SDK, Copilot CLI JSON-RPC runtime, application source and tests.

Operations: inspect supported SDK/runtime and authenticated Copilot CLI connectivity; build authorized applications using session creation/resume, prompt submission, streaming events and cleanup; register custom tools, custom agents, MCP servers, plugin directories and lifecycle hooks; apply permission handlers, workspace scope and allowed tool/resource boundaries; verify errors, cancellation and integration behavior with a bounded test session.

**Access and limits:** Requires supported language runtime, compatible SDK/CLI and authorized Copilot entitlement/authentication. Bundled CLI availability depends on SDK language/version. This is a programmatic agent runtime, not GitHub Models inference or an undocumented REST endpoint. Tool callbacks run application code; permission handlers, provider costs and external data access remain the application owner's responsibility. Do not introduce a new SDK/dependency unless the requested integration needs it.

**Verification:** Verify installed package/runtime versions and authentication without printing credentials; exercise one authorized bounded session, tool result, streaming completion/error path and cleanup. Official documentation checked 2026-11-15; no live product mutation test.

[Official documentation](https://docs.github.com/en/copilot/get-started/sdk-quickstart).

