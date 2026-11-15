# Administration option decisions and human lifecycle

Source review: 2026-11-15. This supplements [administration.md](administration.md), which maps capability routes. It is a decision checklist, not evidence that any tenant is configured. **Documented default**, **observed value**, and **recommended choice** must be recorded separately. Where a setting has no verified universal default, read the actual tenant; API example values are not defaults. Exact current endpoint schemas and supported host/version win.

For each applicable option capture owner/host, effective inherited policy, object ID, observed value, chosen value/reason, approver when required, before/after evidence and recovery action. Preserve original audit exports and human-authored content. Verify with both a new object and an existing customized object. A failed read stays unknown. This reference adds no automatic external actions.

## Organization member privileges and effective access

Group: `organization-access-defaults`. Capability IDs: `admin-organization-profile`, `admin-organization-policy-settings`, `admin-organization-members`, `admin-outside-collaborators`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Base repository permission | none  /  read  /  write  /  admin; REST documented default read | Recommend none for private least-privilege organizations, then explicit teams; preserve existing grants. Internal repositories remain readable to enterprise members. | Read default_repository_permission and test effective access of a representative ordinary member. |
| Member repository creation | members_can_create_public_repositories/private_repositories/internal_repositories: boolean per visibility | Use separate visibility controls; enterprise may prohibit internal/public creation. Do not send closing-down members_allowed_repository_creation_type. | Read each flag and inherited enterprise constraint. |
| Member administrative powers | members_can_delete_repositories; members_can_change_repo_visibility; members_can_invite_outside_collaborators; members_can_create_teams; members_can_delete_issues: booleans | Choose each separately; broad repository admin authority does not authorize destructive actions in this session. | Read flags plus actual repository administrators; record inherited restrictions. |
| Public identity versus billing contact | name/company/blog/location/public email/description versus billing_email | Publish only owner-approved contact data; billing address stays private. | Inspect public profile signed out and billing contact through owner-only settings. |
| Invitation and membership | invitation pending/failed; organization role member/admin; member visibility private/public | Invite exact login/email and chosen role; wait for acceptance and required identity setup. Never infer full membership from public members. | Read invitations and authenticated membership; verify access after acceptance. |
| Outside collaborator conversion/removal | organization member versus outside collaborator; repository role per grant | Inventory team access and owned responsibilities first; explicit offboarding scope includes deploy keys/App access, not just user removal. | Read remaining direct/team/base grants and outstanding invitations after change. |

**Failure and preservation notes:** REST response examples are not tenant defaults. Base changes affect existing members too; private forks require separate inspection. A lower direct grant cannot subtract higher base/team/custom-role access.

**Official sources:** [orgs](https://docs.github.com/en/rest/orgs/orgs), [setting-base-permissions-for-an-organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/setting-base-permissions-for-an-organization), [members](https://docs.github.com/en/rest/orgs/members), [outside-collaborators](https://docs.github.com/en/rest/orgs/outside-collaborators).

## Nested teams and delegated roles

Group: `teams-roles`. Capability IDs: `admin-teams`, `admin-team-members`, `admin-team-idp-sync`, `admin-team-external-groups`, `admin-organization-role-assignments`, `admin-organization-custom-roles`, `admin-organization-custom-role-definitions`, `admin-enterprise-role-assignments`, `admin-organization-security-managers`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Team privacy | secret  /  closed; new non-nested REST default secret, child default closed | Set explicitly: closed for discoverable normal teams; secret cannot have parent/children. | Read privacy and parent for every team, including secret teams through owner identity. |
| Hierarchy and identity | parent_team_id or parent_team_slug; ID takes precedence | Keep existing team IDs; resolve current slug after rename; verify inherited repository grants. | Read parent/children and effective repository access for child member. |
| Mention notifications | notifications_enabled  /  notifications_disabled; default enabled | Disable only intentionally; CODEOWNERS/team mentions must reach responsible humans. | Read notification_setting; ask intended maintainers to verify receipt during authorized collaboration. |
| Team member authority | member  /  maintainer; pending invitation versus active membership | Maintainer is team administration, not organization owner. Team creator becomes maintainer automatically. IdP-synced membership is changed at IdP. | Read team membership role/state and synchronization mapping. |
| Repository roles | read/triage/write/maintain/admin in UI; pull/push map to read/write in team REST; custom role name/ID | Assign the least role needed; check combined base/direct/team/custom permissions. | Read permission sources and a representative allowed/denied operation. |
| Custom role definition | base repository role plus additional permission identifiers; organization role permissions from fine-grained-permission discovery | Discover currently allowed identifiers, dependencies and plan; do not hard-code an old permission list. Separate definition from user/team assignment. | Read role definitions, assigned users/teams and inherited permissions before deleting or replacing a role. |
| Security manager migration | organization roles assignment; legacy security-managers routes retiring | Use current organization role discovery; preserve historical role-change evidence and existing assignments. | Read replacement role and exact affected users/teams; record unsupported legacy endpoint response. |

**Failure and preservation notes:** Secret-team names can appear in mention text. A successful visible-team list does not prove no secret team exists. Do not remove a role as a shortcut to reconciling assignments; recover original role and grants first.

**Official sources:** [teams](https://docs.github.com/en/rest/teams/teams), [about-teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams), [about-custom-repository-roles](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles), [organization-roles](https://docs.github.com/en/rest/orgs/organization-roles), [security-managers](https://docs.github.com/en/rest/orgs/security-managers).

## SSO, provisioning, 2FA and account recovery

Group: `identity-recovery`. Capability IDs: `admin-identity-policies`, `admin-organization-audit-and-sso`, `admin-organization-scim`, `admin-enterprise-scim`, `admin-enterprise-credentials`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Organization SAML connection | Sign on URL; Issuer; public certificate; enabled versus required | Configure/test first, authenticate owner at least once, preserve offline recovery codes; only then enforce. | Test IdP login and inspect list of members GitHub proposes removing before confirmation. |
| Enterprise SAML inheritance | enterprise enforced versus organization configuration | Enterprise enforcement overrides organization SAML; assess every organization and service credential before rollout. | Verify effective connection and representative member login across affected organizations. |
| Provisioning model | ordinary account invitations; organization SCIM; Enterprise Managed Users SCIM | Identify model before changing users. IdP governs managed-user lifecycle; ordinary local invitation is not an EMU substitute. | Read external identity, active state and group/team mapping with correct host API. |
| Authentication assurance | 2FA required yes/no; allowed 2FA methods per actual host policy; passkeys/security keys/recovery methods | Inventory impacted users and service accounts, notify humans, retain independent recovery methods; enforcement requires access-impact authorization. | Read requirement and member compliance; verify owners retain a tested recovery route. |
| Verified/approved domains | DNS verification record; verified domain; notification-domain restriction where available | Verify DNS ownership before restricting notifications; record DNS lifecycle owner. | Read verification and send destinations; do not confuse verified domain with automatic SSO provisioning. |
| Offboarding and recovery | suspend/deprovision; remove membership; revoke SSO credential; revoke token; delete account are distinct | Record actor/subject IDs, teams, grants and recovery constraints; choose reversible suspension when it meets request. | Check effective denial and preserved records; use documented recovery rather than recreating identity blindly. |

**Failure and preservation notes:** Enforcing organization SAML can remove members who have not authenticated with IdP. Downloading recovery codes into logs exposes recovery access. SCIM deprovisioning, IdP group deletion and GitHub membership removal are different effects; verify all required layers.

**Official sources:** [enabling-and-testing-saml-single-sign-on-for-your-organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/enabling-and-testing-saml-single-sign-on-for-your-organization), [enforcing-saml-single-sign-on-for-your-organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/enforcing-saml-single-sign-on-for-your-organization), [configuring-saml-single-sign-on-for-your-enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise), [scim](https://docs.github.com/en/rest/scim).

## PAT and OAuth lifecycle

Group: `tokens-oauth`. Capability IDs: `admin-organization-token-governance`, `admin-enterprise-token-inventory`, `admin-oauth-app-authorizations`, `admin-credential-revocation`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| PAT family and resource owner | fine-grained  /  classic; one resource owner for fine-grained; all versus selected repositories | Prefer fine-grained when endpoint supports it, or installation App for long-lived automation. Check unsupported workflows before choosing token. | Inspect token family, owner, selected repositories and endpoint-specific permission without showing token. |
| Fine-grained approval | Require administrator approval (documented default)  /  Do not require administrator approval | Keep approval unless owner explicitly chooses otherwise; owners own requests auto-approve. Pending tokens only read public resources. | Read pending requests, requested access/expiry and final request state; requester confirms operation after approval. |
| Classic access policy | allow versus restrict classic PAT access, separate from fine-grained approval | An approval rule does not control classic PATs; choose both policies and inherited enterprise restrictions. | Read both token-family policies and existing token inventory. |
| Maximum token lifetime | organization/enterprise configured maximum per token family; token expiration date | Use finite lifetime appropriate to workflow and rotation owner; read actual allowed range from current host rather than inventing universal default. | Check expiry and rotation reminder; verify replacement works before revoking old token. |
| Request decision API | action approve  /  deny; optional reason max1024; GitHub App user/installation tokens only | Human reviews requested repositories and permissions; organization App token needs Personal access token requests write. PAT cannot approve itself through this API. | Read request ID/state; preserve reason and actor; requester gets notification. |
| OAuth app governance | authorized user grant; organization OAuth restrictions; approved/requested App access | Separate user authorization from organization approval and SSO authorization. Never assume OAuth install is GitHub App install. | Read app owner/client identity, scopes, organization authorization and last-use evidence. |
| Revocation | revoke organization access; revoke authorization; delete secret; emergency credential revocation | Record consequence and affected automation; revoke exposed credential and rotate consumers. Revocation cannot recover original secret. | Verify old credential fails and new scoped credential succeeds without logging either. |

**Failure and preservation notes:** 403/404 may be SSO/resource-selection/approval restrictions, not absent repository. Changing token scope cannot add rights the token owner lacks. Do not paste credentials into issue reports, approval reasons, URLs or diagnostic artifacts.

**Official sources:** [managing-your-personal-access-tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), [setting-a-personal-access-token-policy-for-your-organization](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization), [managing-requests-for-personal-access-tokens-in-your-organization](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/managing-requests-for-personal-access-tokens-in-your-organization), [personal-access-tokens](https://docs.github.com/en/rest/orgs/personal-access-tokens), [oauth-applications](https://docs.github.com/en/rest/apps/oauth-applications).

## App registration versus installation

Group: `app-registration`. Capability IDs: `admin-github-apps`, `admin-github-app-installations`, `admin-enterprise-app-installations`, `admin-marketplace`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Registration owner/distribution | personal or organization owner; Only on this account  /  Any account | Keep internal app private unless broader distribution requested. | Read App ID/slug/owner and installation availability. |
| User authorization flow | up to10 callback URLs; expiring user tokens selected by default; request OAuth during installation; device flow optional | Enable only needed flow; keep expiry. Setup URL cannot coexist with requesting user OAuth during installation. | Test exact redirect and expiration/refresh path without exposing secrets. |
| Post-install configuration | Setup URL; Redirect on update boolean | Use for required onboarding; installation repository selection changes can re-trigger setup. | Verify existing installation update preserves completed human configuration. |
| Permission/event selection | No access  /  Read-only  /  Read & write as offered; repository/organization/account permissions; events constrained by permissions | Choose endpoint minimum; expanded permissions require installation approval. | Compare requested registration permissions to currently approved installation permissions. |
| Installation repository scope | All repositories  /  Only select repositories; installation ID; suspended state | Select only necessary repositories; registration, user consent and installation are separate. | Read installation repository list and mint a scoped token only for authorized operation. |
| Private keys and token lifecycle | App JWT; installation token; user token; private-key rotation | Store keys securely; install token may narrow approved permissions/repos. Rotate by adding replacement, verifying, then removing old key. | Verify App identity and token expiry/permissions; do not print PEM/JWT/token. |

**Failure and preservation notes:** Uninstalling an external-property App removes its external custom properties; preserve values first. App permission change is not proof all existing installations accepted the expansion.

**Official sources:** [registering-a-github-app](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app), [installing-a-github-app-from-a-third-party](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party), [authenticating-as-a-github-app-installation](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation).

## Webhook security and delivery recovery

Group: `webhook-delivery`. Capability IDs: `admin-organization-webhooks`, `admin-github-app-webhooks`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Delivery configuration | active true/false; config.url HTTPS; content_type json/form; insecure_ssl 0/1; secret stored separately | Use HTTPS, verification enabled (0) and high-entropy secret; subscribe only needed events. | Read redacted configuration and selected events; validate signature on receiver. |
| Receiver behavior | X-GitHub-Event plus action; X-GitHub-Delivery; 2XX within10seconds | Durably enqueue, acknowledge quickly, process idempotently; unknown action is not assumed safe. | Inspect receipt, signature failure, queue processing and resulting business object. |
| Delivery recovery | ping; deliveries; delivery detail; redeliver attempt | Inspect failures before replay; replay same GUID must not duplicate side effects. | Read redelivery result and downstream state; POST acceptance alone is incomplete. |
| Retry credentials/runtime | organization/App/repository webhook permissions; installed runtime/module support | Use scope-correct credentials; GITHUB_TOKEN cannot redeliver repository webhooks. Validate sample runtime imports before deployment. | Run bounded redelivery test; check response status and error paths. |
| History and secret rotation | original delivery GUID plus attempt IDs/statuses; old/new verifier secret transition | Retain payload metadata only under approved data policy; coordinate producer/receiver rotation. | Verify latest signature and queue state, preserve original failed delivery and retry evidence. |

**Failure and preservation notes:** OAuth-created hooks can be inaccessible to another credential type. Secret plaintext is not recoverable from readback. Community #126156 reports a stale CommonJS Octokit sample failing ERR_REQUIRE_ESM; current App guide uses .mjs. Verify installed package/runtime, do not cargo-cult old snippet.

**Official sources:** [best-practices-for-using-webhooks](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks), [automatically-redelivering-failed-deliveries-for-a-repository-webhook](https://docs.github.com/en/webhooks/using-webhooks/automatically-redelivering-failed-deliveries-for-a-repository-webhook), [automatically-redelivering-failed-deliveries-for-a-github-app-webhook](https://docs.github.com/en/webhooks/using-webhooks/automatically-redelivering-failed-deliveries-for-a-github-app-webhook), [webhooks](https://docs.github.com/en/rest/orgs/webhooks).

**Community research (reports, not product guarantees):** [Discussion #126156](https://github.com/orgs/community/discussions/126156). Current documentation and a bounded target-host reproduction govern remediation.

## Audit history and incident evidence preservation

Group: `audit-history`. Capability IDs: `admin-organization-audit-and-sso`, `admin-enterprise-audit`, `admin-organization-api-insights`, `admin-activity-events`, `admin-personal-data-export`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Read channel/time window | UI; JSON/CSV export; REST; stream; explicit created/date filters | UI default shows3months; enterprise web events180days and Git events7days. Export early; event channel determines completeness. | Record earliest/latest timestamps, filters, pages and counts for each channel. |
| Git versus API event evidence | Git clone/fetch/push; API requests; web-origin operations; SSO responses | Git REST events exclude some web/API initiated effects; do not equate Git event inventory with all mutations. | Correlate request IDs, actor/subject IDs, repository IDs and object timelines. |
| Streaming configuration | destination; active/paused; API request events opt-in; source IP disclosure; available Copilot agent events preview | Use enterprise stream for future retention; decide sensitive IP/log access and destination permissions with owner. | Verify receiver ingestion, last event time, health notifications and queryable retained sample. |
| Continuity and deduplication | at-least-once delivery;7day pause buffer; destination-specific acceptance window | Keep event IDs and deduplicate; repair misconfiguration within6days. Datadog can reject events older than18hours. | Monitor gaps and resume cursor; do not claim backfill predating stream enablement. |
| Preservation artifact | raw read-only export; capture timestamp/host/API version/filter; checksum; restricted storage; separate analysis | Preserve original evidence and write an additive change ledger; record renamed/deleted actor IDs. Export before destructive account/policy changes. | Verify archive readability and checksums; test incident-responder access without publishing private logs. |
| Account export | requested/in-progress/completed; expiring download link; revoke download link | Treat point-in-time personal metadata export separately from repository backup and audit stream. | Inspect completed archive structure privately and verify requested revocation. |

**Failure and preservation notes:** An empty event slice can be retention, filter, permission or channel loss. GitHub Support does not preserve incident logs for you. API usage statistics, public Events and repository traffic are not substitutes for retained security audit evidence.

**Official sources:** [accessing-the-audit-log-for-your-enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/accessing-the-audit-log-for-your-enterprise), [reviewing-the-audit-log-for-your-organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization), [streaming-the-audit-log-for-your-enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise), [requesting-an-archive-of-your-personal-accounts-data](https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/requesting-an-archive-of-your-personal-accounts-data).

## Billing budgets, attribution and hard stops

Group: `billing-budget-options`. Capability IDs: `admin-billing-budgets`, `admin-billing-usage`, `admin-billing-cost-centers`, `admin-billing-usage-reports`, `admin-enterprise-licensing`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Budget subject | budget_scope organization/repository/multi_user_customer/user; enterprise/cost_center on their supported scope endpoints | Match payer and subject; do not create a duplicate budget before reading existing overlapping controls. | Read budget IDs, scopes, product/SKU and payer; reconcile pages against total_count/has_next_page. |
| Pricing selector | BundlePricing + ai_credits; ProductPricing + product; SkuPricing + SKU | Use live supported billing schema, not retired product assumptions. | Read chosen selector and resulting budget; export actual SKU usage. |
| Amount/enforcement | budget_amount integer; prevent_further_usage boolean; user/universal must true | Set authorized cap; ordinary budget UI hard stop is off by default, alerts alone do not cap spend. | Read enforcement and applicable remaining capacity; never disable cap merely to clear an error. |
| User budget payload | user login required for user scope; budget_entity_name empty allowed; optional future expires_at YYYY-MM-DD | Explicit user field is required even where generated schema omits it. User budgets always stop usage. | Read subject/expiry and test affected user policy without incurring unauthorized charges. |
| Alerting | budget_alerting.will_alert; alert_recipients logins; user-scope alerting unavailable | Route supported alerts to responsible humans; distinguish budget notice from product-access or seat request. | Read alert recipients and supported scope; verify delivery through authorized process. |
| Cost center inclusion | usage counts toward enterprise by default; exclusion optional | Exclude only with approved independent spending authority; keep a cost-center cap. | Reconcile organization/user membership and exported attribution against invoice/usage. |
| Recovery from blocked usage | reset cycle; paid usage policy; user limit; organizational/cost-center/enterprise limit; account entitlement | Identify limiting layer first; request budget increase from budget owner or wait for reset. | Read all applicable controls and report exact failed endpoint/policy; use UI when API is unhealthy. |

**Failure and preservation notes:** Community #166810 suggests disabling stop usage; this can permit uncapped charges and is not a safe default. Current official budget order/AI credits supersede old premium-only advice. Community #206489 reports organization budgets 400 with user-scoped budgets; unconfirmed globally. Preserve error and use UI, do not report zero budgets or delete seats as a workaround.

**Official sources:** [budgets](https://docs.github.com/en/rest/billing/budgets), [budgets](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/budgets), [manage-company-spending](https://docs.github.com/en/copilot/how-tos/manage-and-track-spending/manage-company-spending).

**Community research (reports, not product guarantees):** [Discussion #166810](https://github.com/orgs/community/discussions/166810), [Discussion #206489](https://github.com/orgs/community/discussions/206489), [Discussion #173899](https://github.com/orgs/community/discussions/173899). Current documentation and a bounded target-host reproduction govern remediation.

## Copilot seats, nested policy and client governance

Group: `copilot-governance`. Capability IDs: `admin-copilot-seats`, `admin-copilot-usage-metrics`, `admin-copilot-agent-policy`, `admin-enterprise-ai-controls`, `admin-mcp-and-custom-agent-policy`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Access assignment | selected users/teams versus broader membership; organization seat versus enterprise-assigned access | Start with authorized pilot; identify payer and approval owner. A seat is not a feature policy or budget. | Read assigned seats/access and active entitlement for target human. |
| Enterprise enforcement | Enabled; Disabled; Let organizations decide/No policy; selected organizations where offered | Read inherited policy first; organization cannot override enterprise enforcement. | Inspect effective policy for each target organization and user. |
| Unconfigured defaults | separate default availability policies for GA features and GA models; enterprise-assigned user fallback policy | Choose future-feature/model defaults explicitly; do not invent one universal default for every product. | Read both defaults and explicit per-feature/model overrides. |
| Multiple license conflicts | same-enterprise usually least restrictive; cross-enterprise usually most restrictive; feature-specific exceptions | Evaluate paying org and exact conflict matrix: metrics/public-code privacy/non-GitHub semantic indexing differ. | Test target identity effective feature access, not only one organization settings page. |
| Separate feature/client switches | GitHub.com; CLI; Copilot app; cloud agent; review; model availability; preview; feedback; MCP in Copilot | Configure each applicable switch; Copilot MCP policy does not govern GitHub MCP in third-party hosts. | Read policy supported-surface matrix and verify actual client behavior. |
| Cloud-agent organization targeting | enabled everywhere/disabled/organization-delegated/selected organizations; selected IDs or organization properties | Property-based selection is evaluated at configuration time, not continuously on later property edits. | Re-read enabled org list after property changes; reconcile intentionally. |
| Human lifecycle and cost | access request; owner approval; onboarding; usage review; inactivity/offboarding | Give users instructions, responsible support contact and budget limit; usage metrics are not a productivity ranking. | Verify activation and failed access, record approved removal and effective date without deleting review history. |

**Failure and preservation notes:** A toggle read is not a seat, model entitlement, client setting or billing verification. Do not assume organization policy applies to personal users merely accessing an organization repository; policy descriptions define audience.

**Official sources:** [policies](https://docs.github.com/en/copilot/concepts/enterprise/policies), [policy-conflicts](https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/enterprise-administrators/policy-conflicts), [manage-policies](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies), [agent-management](https://docs.github.com/en/copilot/concepts/enterprise/agent-management), [copilot-user-management](https://docs.github.com/en/rest/copilot/copilot-user-management).

## Content exclusion, review and local agent controls

Group: `copilot-exclusions`. Capability IDs: `admin-copilot-content-exclusions`, `admin-copilot-code-review`, `admin-copilot-cli-customization`, `admin-copilot-sdk`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Repository exclusion syntax | YAML list of path patterns; /scripts/** versus /scripts/*; case-insensitive fnmatch | Use patterns scoped to actual sensitive files; preserve inherited exclusions. | Test excluded file and nonexcluded control file for inline/chat/review behavior. |
| Organization/enterprise patterns | repository URL/name mapping to path list; wildcard repository key for filesystem-wide paths | Match intended clone URL and seat audience; enterprise and org scopes differ. | Inspect merged effective policies and actual resolved repository. |
| Propagation and supported clients | up to30minutes IDE propagation; reload client to refresh; current canonical support matrix | Recheck current canonical docs and installed client: older enterprise docs may still say CLI/agents unsupported. | Reload VS Code or restart supported IDE then test actual target client. |
| Exclusion boundary | guardrail; indirect access, symlinks, remote filesystems, third-party MCP exceptions | Use OS/tool permissions for hard boundaries; content exclusion cannot guarantee every access path. | Inspect tool permissions and avoid sensitive-file access in verification. |
| CLI/SDK execution | instructions/agents/skills/plugins/hooks/MCP/LSP; allowed tools/paths; permission handler; model/provider | Read installed runtime schema; installation of config does not authorize arbitrary hooks or tools. | Bounded session verifies loaded customizations, cancellation, error handling, cleanup and permission prompt. |

**Failure and preservation notes:** Content exclusion is not a secret store or filesystem sandbox. Changing model/provider may change data handling and costs.

**Official sources:** [exclude-content-from-copilot](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot), [content-exclusion](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion), [overview](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview), [sdk-quickstart](https://docs.github.com/en/copilot/get-started/sdk-quickstart).

## Codespaces policies and secrets

Group: `codespaces-options`. Capability IDs: `admin-codespaces-lifecycle`, `admin-codespaces-machines`, `admin-codespaces-organization-access`, `admin-codespaces-organization-secrets`, `admin-codespaces-repository-secrets`, `admin-codespaces-user-secrets`, `admin-devcontainers`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Idle timeout | default30minutes; personal timeout plus org maximum; shortest applicable wins | Set maximum acceptable inactivity for organization-paid codespaces; terminal output can keep one active. | Read policy scope and inspect effective timeout after start/restart. |
| Policy targeting | All repositories  /  Selected repositories; organization-paid codespaces only | Do not claim policy restricts personally paid codespaces. Maximum codespaces per user constraint is organization-wide. | Verify payer, targeted IDs and existing codespace next-start behavior. |
| Retention and lifecycle | default30days retention; stop/start/rebuild/delete; machine selection from available list | Save uncommitted work before destructive deletion/rebuild; stopping compute does not remove storage charges. | Read state, machine and storage; verify committed backup before deletion. |
| Additional constraints | allowed machine types; base-image restrictions; forwarded-port visibility; max codespaces per user | Configure individual constraints from real eligible plan UI; preserve intended developer functionality. | Create only an authorized bounded sample; verify restrictions and failure message. |
| Secret scope | organization all/private/selected repositories; repository; user selected repositories; encrypted value | Use narrowest scope and current public key; never log plaintext; explicitly grant needed additional repository access. | List names/scope and test authorized consumer; readback cannot reveal encrypted secret. |

**Failure and preservation notes:** Deletion does not erase storage already accrued in the current billing cycle. Shared forwarded ports and terminal traffic can defeat expected idle savings.

**Official sources:** [restricting-the-idle-timeout-period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period), [troubleshooting-included-usage](https://docs.github.com/en/enterprise-cloud@latest/codespaces/troubleshooting/troubleshooting-included-usage), [organization-secrets](https://docs.github.com/en/rest/codespaces/organization-secrets), [codespaces](https://docs.github.com/en/rest/codespaces/codespaces).

## Custom properties, issue types and shared fields

Group: `classification-schema`. Capability IDs: `admin-organization-properties`, `admin-enterprise-properties`, `admin-enterprise-organization-properties`, `admin-organization-issue-types`, `admin-organization-issue-fields`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Repository property schema | string/single_select/multi_select/true_false; required/default/allowed_values/values_editable_by as offered | Read existing schema and consumers first; preserve property names and values. | Read schema and values for new and existing customized repositories. |
| External property registration | installation_id; display_name1..15alphanumeric immutable; App-only namespace | Confirm installation permission and lifecycle owner; unregister/uninstall can destroy App-owned values. | Read registration as owner (installation token only sees itself); export values before uninstall. |
| Issue type | name; is_enabled boolean; description; gray/blue/green/yellow/orange/red/pink/purple/null color | Reuse type ID; disable obsolete type before deleting when preservation matters. | Read definitions and representative issue assignments. |
| Shared issue field datatype | text/date/single_select/multi_select/number | Choose native semantics; select types require options; not the same object as Project-only field. | Read field ID/type and issue values; test visibility with intended collaborator. |
| Shared field visibility/options | restricted  /  all; organization_members_only deprecated; select option name/description/color/priority | Explicit restricted recommended for private metadata; all exposes to anyone able to see issue. Preserve option IDs during update. | Read effective visibility and existing values; check host visibility-feature support. |

**Failure and preservation notes:** API docs currently default visibility to deprecated organization_members_only; explicitly use restricted on supported versions. Schema deletion/recreation can break ruleset targeting, reporting and historical issue field values.

**Official sources:** [custom-properties](https://docs.github.com/en/rest/orgs/custom-properties), [issue-types](https://docs.github.com/en/rest/orgs/issue-types), [issue-fields](https://docs.github.com/en/rest/orgs/issue-fields), [managing-custom-properties-for-repositories-in-your-organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization).

## Personal identity, notifications and human action

Group: `personal-human-workflow`. Capability IDs: `admin-account-profile`, `admin-account-emails`, `admin-account-keys`, `admin-account-gpg-keys`, `admin-account-ssh-signing-keys`, `admin-account-security-and-billing-ui`, `admin-notifications`, `admin-repository-watches`, `admin-account-blocking`, `admin-organization-blocking`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Email/privacy | primary/verified/public email; keep email private; block pushes exposing private email | Preserve verified recovery address; choose noreply Git identity when privacy requested. | Inspect public commit/profile and private verification state; never publish recovery address. |
| Key purpose | SSH authentication key versus SSH signing key versus GPG key; read-only/write deploy key separate | Keep purpose explicit; public key fingerprint identifies key, not private credential. | Read purpose/fingerprint and verify bounded auth or signature; inspect deploy-key grants on offboarding. |
| Recovery | passkeys/security keys/TOTP/recovery codes; active sessions; password reauthentication | Require human control of second factors and backup recovery; never save recovery material in shared docs. | Owner verifies independent recovery route; revoke only explicitly targeted session/credential. |
| Repository watch | Participating/@mentions; All activity; Ignore; Custom event types | Use releases/security/review signals needed by actual maintainer; automatically participating subscription can add noise. | Read subscription and intended event categories; intended human verifies notifications. |
| Delivery channels | On GitHub; email; Mobile; participating/watching categories; default/per-org verified email; working hours | Keep actionable maintainer notices; personal settings require account owner context. | Check inbox/email settings and representative received notification; a sent mention is not proof of delivery. |
| Moderation | block/unblock; organization block differs from personal block; interaction limits | Preserve abuse evidence privately; specify affected relationships and access before blocking. | Read current block/limit and verify intended scope; avoid unnecessary duplicate contact. |

**Failure and preservation notes:** Email replies can create public comments. Notification privacy and contributor consent still matter. Removing a user does not revoke a deploy key whose private key they retained.

**Official sources:** [configuring-notifications](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications), [connecting-to-github-with-ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh), [managing-commit-signature-verification](https://docs.github.com/en/authentication/managing-commit-signature-verification), [securing-your-account-with-two-factor-authentication-2fa](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa), [blocking](https://docs.github.com/en/rest/users/blocking).

## Host-specific enterprise lifecycle and support

Group: `enterprise-host-lifecycle`. Capability IDs: `admin-enterprise-accounts`, `admin-enterprise-organization-lifecycle`, `admin-enterprise-data-residency`, `admin-enterprise-server-admin`, `admin-github-connect`, `admin-organization-migrations`, `admin-user-migrations`, `admin-enterprise-importer`, `admin-support-entitlements`, `admin-support-tickets`, `admin-source-imports`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Hosting and identity | github.com  /  tenant.ghe.com  /  GHES version; ordinary identities versus managed users | Choose actual API/SSH host and product/version docs before credentials or network policy. | Read host /meta, enterprise identity and version; do not apply github.com IP/fingerprint snapshot blindly. |
| Organization lifecycle | create; invite existing; transfer; migration importer; pending acceptance | EMU cannot import an ordinary organization via simple enterprise invite; cross-host moves need supported migration. | Read destination ownership, inherited policy, billing and member access after completion. |
| Migration plan | source/export; destination; locks; import status; warnings; user attribution; redirect behavior | Preserve source and export; map humans and permissions; rehearse recovery before destructive cutover. | Inspect final migration log, counts, links and sampled historical issues/PR authors/files. |
| GHES administration | backup/restore; maintenance; upgrade; replica/HA; license; support bundle; GitHub Connect | Use instance version runbook and verified backups; repo admin is not appliance administrator. | Verify backup restore readiness, instance health/version and product connectivity after approved change. |
| Support interaction | entitlement; intended enterprise account; new/existing ticket; attachment; reply; status | Prepare redacted reproduction and preserve case history; submission/reply contacts another party and needs explicit instruction. | Read actual ticket ID/submitted content/status; form preparation alone is not submission. |

**Failure and preservation notes:** Migration/API success does not prove review history, actor attribution or every product artifact migrated. Support attachments can have unauthenticated URLs; redact before upload.

**Official sources:** [feature-overview-for-github-enterprise-cloud-with-data-residency](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/feature-overview-for-github-enterprise-cloud-with-data-residency), [adding-organizations-to-your-enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/adding-organizations-to-your-enterprise), [using-github-enterprise-importer](https://docs.github.com/en/migrations/using-github-enterprise-importer), [admin](https://docs.github.com/en/enterprise-server@latest/admin), [creating-a-support-ticket](https://docs.github.com/en/enterprise-cloud@latest/support/contacting-github-support/creating-a-support-ticket).

## Organization rules and hosted networking

Group: `rules-network`. Capability IDs: `admin-organization-rulesets`, `admin-organization-rule-suites`, `admin-enterprise-rulesets`, `admin-organization-network-configurations`, `admin-enterprise-network-configurations`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Ruleset nested scope | target branch/tag/push where supported; enforcement disabled/active/evaluate; repository/ref include/exclude conditions; bypass actors/modes | Preserve target conditions and bypass IDs; evaluate mode measures without enforcement. Detail rule parameters in delivery-security reference. | Read each ruleset, inherited sources and rule suites for sample pushes; list alone proves little. |
| Network configuration | name1..100 letters/numbers/._-; compute_service none/actions; exactly one network_settings_ids entry | Use provisioned network resource and proper compute attachment; a configuration alone attaches no runner. | Read network setting and attached runner group plus actual connectivity. |
| Failover network | failover_network_settings_ids exactly one when configured; failover_network_enabled boolean | Choose failover only with independently tested connectivity and owner-approved network policy. | Read failover configuration; bounded connectivity/failover test and rollback route. |

**Failure and preservation notes:** Push, branch and tag rules have different plan gates. Network API response examples showing multiple IDs conflict with current exactly-one request rule; current parameter constraint wins.

**Official sources:** [rules](https://docs.github.com/en/rest/orgs/rules), [rule-suites](https://docs.github.com/en/rest/orgs/rule-suites), [network-configurations](https://docs.github.com/en/rest/orgs/network-configurations), [network-configurations](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/network-configurations).

## Agent automation, task execution and human handoff

Group: `agent-automation-options`. Capability IDs: `admin-agent-automations`, `admin-agent-tasks`, `admin-agent-secrets`, `admin-agent-variables`, `admin-copilot-cloud-agent-sessions`, `admin-copilot-team-customizations`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Automation ownership | type personal/shared; enabled; require_actor_write_permission; continuous_history | Personal belongs to creator; shared is repository-readable and writer-manageable. Read repository allow-automations policy. | Read repository scope, creator and permitted actors; user-global list omits others shared automations. |
| Schedule and event triggers | cadence hourly/daily/weekly; hour_utc0..23; day_of_week0..6; minute_utc0/15/30/45 (omit with hourly); query/labels/workflow filters | Default daily/weekly midnight UTC, weekly Monday; choose explicitly with timezone conversion. | Read trigger fields and next/actual run time; preserve prior run history. |
| Trigger authority | write_scope trigger/repository; allow_copilot_triggers false default | Scheduled write_scope has no effect: scheduled runs can change entire repo. Keep Copilot-trigger loops disabled unless explicitly reviewed. | Read effective scope/policy; test trigger actor and targeted object. |
| Task request | prompt; model from current plan list; custom_agent filename stem; create_pull_request false default; base_ref/head_ref | Prompt must describe authorized work. Existing head_ref can receive commits; inspect branch/PR before start. | Read task/session/artifact and resulting diff; starting task is not completion. |
| Task states/history | queued/in_progress/completed/failed/idle/waiting_for_user/timed_out/cancelled; is_archived false default | Include archived records in history inventory; waiting_for_user needs actual human answer. | Read final state/output/errors and linked PR; retain original failed attempt before retry. |
| Secrets/variables/team customization | secret encryption key/value and repository visibility; plain variables; prompt/tool configuration | Never put secret in variable or prompt; preserve custom agents/tools and follow actual endpoint scope. | Read names/selection and bounded consumer output; no plaintext secret readback. |

**Failure and preservation notes:** Public-preview surfaces change. App installation tokens support shared automations but not ordinary agent-task start/list; choose endpoint-specific authentication. No retry may silently create another billable task or duplicate PR; reread task/artifacts first.

**Official sources:** [agent-automations](https://docs.github.com/en/rest/agent-automations/agent-automations), [agent-tasks](https://docs.github.com/en/rest/agent-tasks/agent-tasks), [secrets](https://docs.github.com/en/rest/agents/secrets), [variables](https://docs.github.com/en/rest/agents/variables), [copilot-cloud-agent-management](https://docs.github.com/en/rest/copilot/copilot-cloud-agent-management), [copilot-team-customizations](https://docs.github.com/en/rest/copilot/copilot-team-customizations).

## Copilot Spaces and private registry access

Group: `spaces-registry`. Capability IDs: `admin-copilot-spaces`, `admin-copilot-space-collaborators`, `admin-copilot-space-resources`, `admin-private-registries`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Space default access | base_role no_access(default)/reader/writer/admin; name/description/general_instructions | Keep no_access until audience approved; discover direct collaborators separately. | Read default/direct roles and test intended audience. |
| Space resource types | repository/github_file/free_text/github_issue/github_pull_request/media_content/uploaded_text_file; type-specific metadata | Preserve resource IDs and private context; fine-grained/user tokens need every referenced repository. | Read resource details; list can omit whole Spaces with inaccessible resources, so incomplete list remains unknown. |
| Registry access | visibility all/private/selected; selected_repository_ids only with selected; replaces_base false default | Select repositories and decide whether public-registry fallback is acceptable. | Read visibility, selected IDs and successful bounded dependency resolution. |
| Registry authentication | token(default)/username_password/oidc_azure/oidc_aws/oidc_jfrog/oidc_cloudsmith/oidc_gcp/anonymous | Token/password require encrypted_value/key_id; OIDC omit them; anonymous also omits username. Use provider-specific fields from current schema. | Read redacted auth config and external trust mapping; verify authorized resolution, not secret plaintext. |
| Provider-specific identity | Azure tenant_id/client_id; AWS region/account/role/domain/domain_owner; JFrog provider/audience; Cloudsmith namespace/service_slug/audience; GCP workload_identity_provider/service_account | Grant narrow external trust; GCP service_account optional for direct WIF. Cloudsmith api_host defaults api.cloudsmith.io. | Verify actual issuer/audience/subject and repository binding with external administrator. |

**Failure and preservation notes:** Space sharing and source repository access are distinct; do not widen source access to make inventory look complete. Credential rotation and trust-provider setup require both GitHub and registry-side verification.

**Official sources:** [copilot-spaces](https://docs.github.com/en/rest/copilot-spaces/copilot-spaces), [collaborators](https://docs.github.com/en/rest/copilot-spaces/collaborators), [resources](https://docs.github.com/en/rest/copilot-spaces/resources), [organization-configurations](https://docs.github.com/en/rest/private-registries/organization-configurations).

## Organization defaults, repository history and storage

Group: `repository-community-lifecycle`. Capability IDs: `admin-community-defaults`, `admin-organization-profile-content`, `admin-repository-lifecycle-admin`, `admin-repository-insights`, `admin-git-lfs`, `admin-archive-program`, `admin-github-models-retired`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Community defaults/profile | public .github defaults; repository-specific overrides; .github/profile/README.md and member profile where supported | Reuse organization defaults without overwriting repository custom documents; distinguish public/member audience. | Inspect rendered repository community profile and org profile with correct identity. |
| Repository lifecycle | visibility public/private/internal; archived; owner/name/default branch; delete versus archive | Check fork network, billing, actions/pages and collaborator consequences. Preserve history and transferable objects before move/delete. | Read metadata and history/redirect/access after change; archive is read-only, not backup. |
| LFS configuration | .gitattributes tracked patterns; LFS object store; pointers; quota/billing; migration rewritten history | Track only required files; git clone/mirror without LFS object fetch is insufficient backup. History rewrite requires coordinated human cutover. | Fetch/check LFS objects; verify fresh checkout and collaborators migration instructions. |
| Insights/preservation | traffic/clones/views; contributors/stats async response; Preserve this repository on/off | Capture ephemeral metric window before expiry. Archive Program opt-out only affects future preservation. | Read completed statistics and preservation setting; never equate UI archival, source export and long-term program. |
| Retired Models workflow | historical GitHub Models integration/configuration; retired endpoints | Preserve source/cost history, discover supported replacement only when requested; no new deployment against retired service. | Check endpoint retirement notice and installed integration; mark unavailable with dated evidence. |

**Failure and preservation notes:** No repository deletion or history rewrite is implied by full setup. A metadata snapshot cannot restore repository/LFS/product history.

**Official sources:** [creating-a-default-community-health-file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file), [customizing-your-organizations-profile](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile), [repos](https://docs.github.com/en/rest/repos/repos), [metrics](https://docs.github.com/en/rest/metrics), [about-git-large-file-storage](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage), [opting-into-or-out-of-the-github-archive-program-for-your-public-repository](https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/opting-into-or-out-of-the-github-archive-program-for-your-public-repository), [github-models](https://docs.github.com/en/github-models).

## Human-facing sharing, Classroom and Spark

Group: `human-social-education`. Capability IDs: `admin-account-following`, `admin-account-social-links`, `admin-gists`, `admin-gist-comments`, `admin-repository-stars`, `admin-activity-feeds`, `admin-classroom`, `admin-github-spark`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Social profile and subscriptions | follow/unfollow; social account URLs; star/unstar; public/private authenticated feeds | Only change owner-requested preferences; feed URLs can embed sensitive tokens. | Read actual relationship/profile/feed scope without logging private feed URLs. |
| Gist publication/history | public true/false on creation; description/files; file rename/delete; revisions/forks/comments | Secret gist is unlisted, not access-controlled private storage; never put secrets there. Preserve revision before edits. | Read visibility/files/history and comment IDs; inspect audience before publishing. |
| Classroom assignment | classroom/assignment ID; individual/group; accepted assignment repositories; students/teams; grades | Use teacher authority and preserve student privacy; acceptance and grading are separate human actions. | Read actual assignment, accepted repositories and grades with correct classroom scope. |
| Spark publishing/data | private/organization/all-GitHub-users where eligible; shared app data read-only/write; preview versus published version | Publication and data-write audience need explicit scope; managed users cannot publish to all GitHub users. | Read publication URL/version/audience and verify authorized viewer/data operation. |

**Failure and preservation notes:** Commenting, following and invitations affect other humans. Read-only discovery is not permission to contact or publish.

**Official sources:** [followers](https://docs.github.com/en/rest/users/followers), [social-accounts](https://docs.github.com/en/rest/users/social-accounts), [gists](https://docs.github.com/en/rest/gists/gists), [comments](https://docs.github.com/en/rest/gists/comments), [starring](https://docs.github.com/en/rest/activity/starring), [feeds](https://docs.github.com/en/rest/activity/feeds), [classroom](https://docs.github.com/en/rest/classroom/classroom), [your-first-spark](https://docs.github.com/en/copilot/tutorials/spark/your-first-spark).

## Platform diagnostics and templates

Group: `platform-diagnostics`. Capability IDs: `admin-platform-meta`, `admin-platform-rate-limits`, `admin-platform-license-catalog`, `admin-platform-gitignore-templates`, `admin-platform-emojis`, `admin-platform-markdown-rendering`.

| Option | Values and documented defaults | Decision rule | Verification |
| --- | --- | --- | --- |
| Host metadata | GET /meta; API versions; SSH fingerprints; IP/domain lists | Use real host metadata and documented exceptions; avoid rewriting firewall from partial snapshot. | Verify host identity and freshness before applying any external network change. |
| Quota and retry | core/search/GraphQL resource budgets; x-ratelimit-*; retry-after; GraphQL cost/reset | Obey primary and secondary throttles; positive core remaining does not rule out secondary limit. | Record failed request/status/headers; retry under documented delay and verify object state first. |
| Catalog templates | SPDX license ID; detected license file; gitignore template name; emoji shortcode | Owner chooses license; preserve custom ignore rules; catalog discovery does not authorize relicensing. | Read actual committed license; git check-ignore plus tracked-file inspection; verify chosen shortcode. |
| Markdown rendering | mode markdown/gfm; repository context; raw rendering endpoint | Context changes issue/user link resolution; rendering POST does not publish comment or file. | Inspect returned HTML and context-sensitive links in intended renderer. |

**Failure and preservation notes:** A successful render or catalog lookup proves only that lookup. It is not evidence of repository configuration or publication.

**Official sources:** [meta](https://docs.github.com/en/rest/meta), [rate-limit](https://docs.github.com/en/rest/rate-limit), [licenses](https://docs.github.com/en/rest/licenses), [gitignore](https://docs.github.com/en/rest/gitignore), [emojis](https://docs.github.com/en/rest/emojis), [markdown](https://docs.github.com/en/rest/markdown).

## Completeness and remaining implementation gaps

This option review deepens high-risk administration paths; it does not assert every present or future UI control has been enumerated. Every administration capability family is mapped below; this is a family coverage check, not a claim every host-specific nested field is frozen here. Expand the exact current operation schema and product UI for each applicable setting before configuration. Do not silently treat an available route as configured.

- `scripts/audit.py` reads organization summary lists, not effective user grants, member lifecycle, token approvals, webhook deliveries, audit retention/stream health, nested billing controls or effective Copilot policies. It cannot certify those configurations.
- `scripts/operations.py` submits a supplied REST body unchanged. The billing budget documentation explicitly supplies a required `user` field omitted by generated schemas; use the current documented override and readback. Schema discovery alone is insufficient.
- Generic `gh api --paginate` follows server pagination headers. Budget responses also expose `has_next_page` and `total_count`; reconcile these with fetched counts and explicitly request remaining pages when needed rather than assuming a complete inventory. This is a required verification guard, not a demonstrated current server-header defect.
- Neither script preserves an append-only administrative change history or captures human approvals, notification receipt and recovery tests. Maintain these evidence records alongside the coverage ledger before claiming full setup.
