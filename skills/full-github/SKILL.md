---
name: full-github
description: Use GitHub throughout repository setup, audit, development, planning, automation, security, delivery and administration. Covers the complete indexed REST and GraphQL surfaces, Projects, Wiki, organizations and enterprise capabilities.
---

# Full GitHub

Use the full profile by default. Start with references/features.md and references/operations.md. The catalog enumerates individual capabilities, their actual operation routes, source documentation, permission gates and required verification.

## Discover the complete surface

1. Identify the GitHub host, authenticated identity, repository and owner from Git remotes, gh auth status and repository metadata. Read AGENTS.md, GITHUB.md, existing community files and workflows. Preserve repository-specific choices.
2. Search the capability catalog with python3 <plugin-root>/scripts/operations.py capabilities TERM. Read the relevant domain reference sections. Resolve plugin-root relative to this skill's ../../ directory. Keep the large JSON registries out of the conversation context.
3. Use operations.py search TERM, describe OPERATION and type INPUT_TYPE to discover exact current operations. Search with --graphql for GraphQL. Read official endpoint documentation and inspect request schemas before choosing payloads. The indexed API includes deprecated and retired operations, so check their status.
4. Run scripts/audit.py OWNER/REPO for repository probes. Add --organization for an organization owner and --project NUMBER for each relevant owner Project. Read failures remain unknown. Use operation discovery to inspect the remaining features, including object-level details, plan-specific and UI-only capabilities.
5. Maintain one coverage ledger row per applicable capability ID, with desired configuration, observed configuration, action, permission/plan gate, evidence URL/object ID and final state. Use configured, available-unconfigured, unavailable, not-applicable or unknown. Record a concrete reason for each unavailable or inapplicable row. A successful API read is evidence of observation, not configuration correctness.
6. With agent tools available, delegate independent collaboration, delivery/security and administration discovery to agents. Give each its exact catalog scope and require official sources and evidence. Consolidate their findings and inspect unresolved gaps before finishing.

## Full setup

Full setup considers the whole catalog. Enable and configure eligible capabilities serving this project, including advanced fields, views, automation, review rules, security controls and documentation. Evaluate newer API features and owner-level integrations rather than silently stopping at a baseline. Determine applicability from the actual project and document the reason.

Respect existing custom content, policies, collaborators, field and option IDs. Inventory live objects before creation. Resolve matching names and IDs, then compute the smallest desired change. Use native gh, Git and available connectors or UI tools. The REST executor runs exact operation IDs with structured parameters and an explicit payload file. It also supports binary release assets. See references/operations.md.

Continue authorized work autonomously. Infer reversible routine choices from the project. Ask only about unresolved material decisions and actions requiring approval under the host's rules, including access expansion, payment commitments and destructive changes. Never grant broader rights or bypass protection to complete setup.

After every mutation read back the object and check the intended configuration, not only HTTP success. Preserve confirmed partial progress. On timeout re-read before retrying. Reconcile again after setup and verify unchanged IDs/counts and preserved custom content. Include a newly-created object and an existing customized object in meaningful reconciliation acceptance tests.

## Repository instructions and documentation

Write the actual repository rules in GITHUB.md and link them from AGENTS.md. Include Project URLs, field/option mapping, issue types and shared issue fields, branch and review rules, CI commands, deployment and release policies, Wiki maintenance and documented capability gates. Respect existing casing and links.

Provide well-structured README and Wiki navigation, install/use/troubleshooting pages, ownership, contributing and security guidance, license and third-party notices where applicable. Badges must point to real checks and releases. Keep runtime requirements in the native ecosystem manifest. Clarify engines.md if the user means additional prose. See references/collaboration.md.

## Audit

Audit is read-only. Cover individual capabilities, including settings that require nested object reads. Check classic protection separately from rulesets. Read Project field types/options, saved views, workflows, updates and charts through supported interfaces. A 404 can mean absent, inaccessible or unavailable. Establish which before assigning a final state. Report ranked actionable gaps, access gates and proof.

## Delivery and maintenance

Track substantial work through an issue, existing issue type and shared fields, labels, assignee, milestone, Project item and status. Use sub-issues/dependencies where the work requires them. Branch, implement, verify and create a linked PR. Maintain reviews, checks, discussions and Project status throughout delivery. Observe review and merge-queue rules. Verify the resulting commit, closure and automation after merge.

Update affected Wiki/docs and publish a release when the project's policy calls for it. Validate artifact contents and downloaded bytes. Apply relevant deployment environments, approvals, attestations, registry and release immutability policies. Verify deployment/release results. Investigate and fix recoverable failures.

## Finish with evidence

Recheck all coverage rows. Source-backed support, executable operations, live read validation and live mutation validation are separate evidence levels. State the tested host/date and exact remaining gaps. Never claim all GitHub features were configured from a successful subset, a read-only repeated snapshot or a catalog entry. See references/workflows.md for recovery and authorization boundaries.
