## Installation

For a new installation, register the public Git marketplace and add the plugin.

```sh
codex plugin marketplace add thinkhome-org/full-github
codex plugin add full-github@thinkhome
```

For an existing installation, refresh the marketplace before adding the current version.

```sh
codex plugin marketplace upgrade thinkhome
codex plugin add full-github@thinkhome
```

Open a fresh Codex chat and select Full GitHub.

## Validation evidence

The tagged Release workflow runs the regression suite and registry/documentation checks, binds the archive to the source commit and tag, verifies transferred checksums and produces GitHub build provenance. Publication verifies uploaded bytes before freezing the release.

Download the ZIP/checksum and inspect the workflow run linked from the repository's Actions page. Verify the artifact's provenance against thinkhome-org/full-github using gh attestation verify. Native immutable-release verification is available through gh release verify.

The Wiki records release-specific verification, with executable checks and provider/account boundaries.

## Limitations

The operation registry and option guidance are dated snapshots. Use current official endpoint documentation, schema errata and target-host verification before a consequential change. Administrative, paid and enterprise capabilities depend on the actual credential, organization policy and entitlement.

The private local journal records executor attempts and read-back references. GitHub's native actor/audit/review records and required human approvals retain their own authority. Original plugin content still awaits an owner-selected license; third-party OpenAPI licensing is preserved in NOTICE.md.
