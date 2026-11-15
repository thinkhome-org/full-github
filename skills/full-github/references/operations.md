# Discover and execute operations

The bundled registries provide exact operation names and parameters without loading entire schema files into the model context. Use the existing authenticated GitHub CLI. Shell evaluation is never used by the executor.

## Capability lookup

```sh
python3 scripts/operations.py capabilities projects
python3 scripts/operations.py capability projects-views
python3 scripts/operations.py search issue-field
python3 scripts/operations.py describe issues/set-issue-field-values
```

Capability IDs are discoverable using the first command. Use the returned ID if an example name changes in a future catalog. Every capability includes operation-level routes and official documentation. Follow those docs for body schemas, token permission requirements and plan restrictions.

## REST execution

```sh
python3 scripts/operations.py describe repos/get
python3 scripts/operations.py call repos/get --params '{"owner":"OWNER","repo":"REPO"}'
python3 scripts/operations.py describe issues/create
python3 scripts/operations.py call issues/create --params '{"owner":"OWNER","repo":"REPO"}' --body-file issue.json --dry-run
python3 scripts/operations.py call issues/create --params '{"owner":"OWNER","repo":"REPO"}' --body-file issue.json
```

For the issue example, issue.json contains the desired JSON payload with a title and any body, labels or assignees supported by the endpoint.

The operation supplies the HTTP method. Path values are encoded, query parameters retain their types, required parameters are checked, and body files go to gh through stdin. JSON GET responses use pagination and preserve page boundaries. Binary/archive/log downloads preserve raw response bytes. Responses and errors are returned through gh's normal output and exit status.

Use --header to select media types or send API-version and conditional-request headers. Custom binary media types preserve raw output. The descriptor contains body field hints. GitHub validates the full payload schema. A body file may also contain binary data for operations such as repos/upload-release-asset. Its separate uploads.github.com server and media type are preserved.

call executes the named operation, including writes and destructive operations. Follow the user's authorization and host approval requirements before invocation. dry-run builds argv without making a network request. Do not put credentials into parameters or public reports. GET is an HTTP method rather than a guarantee that a service performs no work, as asynchronous SBOM generation demonstrates.

The catalog marks deprecated entries and blocks known retired operations with their official replacement guidance. A deprecated operation with no closure date remains discoverable, with its documented risk. Server-side entitlement checks remain authoritative.

## GraphQL discovery and execution

```sh
python3 scripts/operations.py search ProjectV2 --graphql
python3 scripts/operations.py describe updateProjectV2View --graphql
python3 scripts/operations.py type UpdateProjectV2ViewInput
gh api graphql --input request.json
```

request.json contains query and variables. Use GraphQL variables for all user-provided values. Resolve input and enum types through the type command. The bundled snapshot has the full type inventory, argument nullability, enums, interface implementations, union members, directives and deprecation metadata.

Paginate each connection independently. For gh pagination declare an endCursor variable, pass it to the selected connection's after argument, and select pageInfo with hasNextPage and endCursor. A project with 100 fields or items must not be mistaken for a complete project until pagination finishes. Preserve partial data and GraphQL errors separately.

Project view CRUD and status-update CRUD have current GraphQL mutations. Workflow read/delete also exist. Configuration of built-in workflows and custom Insights charts still requires checking the current schema and UI. Do not infer UI-only status from older documentation.

## Read-only audit

```sh
python3 scripts/audit.py OWNER/REPO
python3 scripts/audit.py OWNER/REPO --organization --project 5
```

The second command inspects repository configuration, organization settings and paginated Project fields/items/views. The default branch's classic protection is checked separately from repository rulesets. HTTP failures, invalid JSON, timeouts and GraphQL errors stay unknown while other probes continue. Successful empty responses are handled.

The snapshot supplies configuration evidence. Object-level inspection, account and enterprise contexts, chart/UI state and actual mutations require follow-up operations from the catalog. Keep private metadata local and review it before sharing.

## Authentication and compatibility

Check gh auth status and the endpoint's current supported credential types. Classic PAT scopes, fine-grained PAT permissions, GitHub App permissions, SSO authorization, organization roles and enterprise policies differ. Some enterprise endpoints require specific credential types. Refreshing authentication or changing account permissions follows the user's authorization and host policies.

The registry snapshot targets GitHub.com. For GHES use the host's matching versioned docs and gh api --hostname HOST. The executor's bundled route/media metadata targets GitHub.com, including its release upload host. Execute GHES operations directly through host-aware gh after checking compatibility.

## Refresh the registry

Obtain api.github.com.json from github/rest-api-description and live GraphQL full-type introspection JSON from the intended GitHub host. Preserve the official OpenAPI license in NOTICE.md. Review deprecation descriptions and update data/retired-operations.json with confirmed closures and official sources.

```sh
python3 scripts/update_registry.py openapi.json graphql-types.json --date YYYY-MM-DD
python3 scripts/render_catalog.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The OpenAPI input is the official document containing paths, components and operationId fields. The GraphQL input contains data.__schema.types with fields, args, inputFields, enumValues and nested type references. Use includeDeprecated on field and enum introspection. The generator derives the full query/mutation index from Query and Mutation types, including deprecated entries. Source digest and retrieval date are recorded for drift verification.

Review new products, endpoints and schema changes against domain references and the capability catalog. Updating the operation registry alone cannot establish that new functionality has been tested.


## Inspect nested choices

```sh
python3 scripts/operations.py options review
python3 scripts/operations.py option project-event-workflows
python3 scripts/operations.py schema repos/update --section requestBody --pointer /content/application~1json/schema/properties/allow_squash_merge
python3 scripts/operations.py schema billing/get-all-budgets-org --section responses --pointer /200/content/application~1json/schema
```

The full official OpenAPI snapshot is preserved in rest-schema.json.gz. The inspector traverses internal references at each pointer step. Use the document section to inspect components or global metadata. The original digest is validated independently of the compact index. describe also reports known documentation/schema errata.

Configuration groups include concrete values, defaults versus recommendations, decision rules, sources, community incident qualifications and proof. Follow the actual host and current documentation where behavior changed.

## Complete page-based reads

```sh
python3 scripts/operations.py collect issues/list-labels-for-repo --params '{"owner":"thinkhome-org","repo":"full-github","per_page":5}' --context https://github.com/thinkhome-org/full-github/issues/9
```

collect reads page/per_page collections from page 1, including APIs with missing Link headers. It follows explicit has_next_page metadata or probes continuation independently of the requested page size. Totals must remain consistent. incomplete_results, repeated pages, count mismatches, parsing and transport failures keep complete false and preserve received pages. Use --items-pointer when a response contains multiple arrays. A failed collection returns nonzero.

Cursor and nested GraphQL connections use their documented pagination protocol. Narrow search scopes to respect provider result limits and historical windows. complete describes exhausted pagination for the observed query; concurrent provider changes still require a stable time scope and reconciliation.

## Execution records

call and collect record local attempts and outcomes by default, with host and selected target metadata. Add --context with an issue, PR or discussion URL. Request/response bodies and header values are excluded. Dry-run redacts authentication headers. Read history and add verify-event only after actual read-back. --no-history supports explicitly ephemeral inspection. See [history and interaction](history-interaction.md).

## Release lifecycle

The repository's tagged release workflow validates source, packages committed hidden manifests, uploads a build artifact, produces a GitHub provenance attestation, resumes a draft release and verifies downloaded asset bytes before publication. Existing differing assets are preserved and block publication. An already-published release is verified without silent repair. RC tags retain prerelease classification.

Use gh attestation verify against this repository after downloading an artifact. Wiki history, issue/PR history, CHANGELOG and recorded decisions preserve the reasons and outcomes around releases.
