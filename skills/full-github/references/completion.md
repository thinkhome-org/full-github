# Full-profile completion gate

A full setup/audit must evaluate every catalog capability, actively configure eligible useful features and preserve reasons for unavailable or inapplicable ones. Defaulting every feature off or listing supported endpoints is insufficient. Ordinary delivery tasks follow the relevant controls in [issue-lifecycle.md](issue-lifecycle.md).

Run `python3 <plugin-root>/scripts/check_completion.py LEDGER.json`. Exit zero means the submitted ledger is structurally complete and claims verified final decisions for every catalog ID. It does not fetch evidence or establish its truth. Inspect live read-back, permission and project-context evidence separately. The host must load and follow this skill; a plugin cannot globally force an unrelated agent's tool calls.

The JSON object has repository `OWNER/REPO` and a `capabilities` array containing each catalog ID exactly once. Each row uses this shape.

```json
{
  "id": "repository-lifecycle",
  "state": "configured",
  "desired": {"visibility": "public"},
  "observed": {"visibility": "public", "id": 123},
  "action": "Retained the approved public repository configuration",
  "gate": "Existing repository administration authorization",
  "evidence": ["https://github.com/OWNER/REPO/issues/NUMBER#issuecomment-ID"],
  "verification": "matched"
}
```

This is one example row, not a complete ledger or observed evidence. Use the actual desired configuration and read-back facts, including false/zero values where valid. Fields `action` and `gate` must be concrete text. Evidence must be nonempty HTTPS links without embedded credentials, query parameters, whitespace or control characters. Keep sensitive owner evidence in an appropriately restricted record.

Final states are `configured` with `verification: matched`, `unavailable` with `verification: gate-confirmed` and a target-specific `reason`, or `not-applicable` with `verification: context-confirmed` and a project-specific `reason`. Every state retains desired/observed/action/gate/evidence. An unavailable operation needs actual gate evidence; a feature that does not serve the project needs a contextual decision. Never invent absence, rights, entitlement or author approval to obtain a passing result.

`unknown`, `available-unconfigured`, duplicates, missing or unknown IDs and missing evidence fail. Preserve unfinished rows and continue meaningful work. A genuinely blocked feature remains an explicit limitation; do not call a failed gate a completed full setup.

Keep the ledger current after configuration changes and link it from the owning issue. Review representative customized and newly created objects after reconciliation. Preserve content, IDs, historical discussion and authorized access. Finishing the relevant code change is distinct from claiming every possible tenant operation was executed.
