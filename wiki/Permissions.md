# Permissions and troubleshooting

Use gh auth status to inspect the active identity and granted scopes. Read the exact operation's documentation for supported credential types. Classic PAT scopes, fine-grained permissions, GitHub App installation/user tokens, SSO and organization/enterprise roles differ by endpoint.

The verification account could read 48 of 55 initial probes. Several organization reads require admin:org. Permissions were preserved and failures recorded. Public repository administration does not grant organization administration.

## Availability

GitHub.com, GHES versions, subscription plans, previews and organization policy expose different surfaces. Inspect the target host's schema and current documentation. A 403 or 404 remains unknown until access, product availability and object existence are distinguished.

Retired endpoints carry unavailable metadata and cannot be executed through the helper. Deprecated endpoints remain marked even when still callable. Inspect the replacement before use.

## Handling writes

The REST executor uses current gh authentication. call executes its selected operation, including writes. Follow host action approval requirements and user authorization. Use --dry-run to inspect argv. Keep credential values out of payload examples and public reports.

After timeout, re-read before retrying. Preserve custom content and IDs. Verify actual settings after a successful response. The Wiki uses a separate Git remote, and Project workflow/chart UI configuration requires live inspection when no suitable API exists.
