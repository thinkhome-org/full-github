# Contributing

Open an issue describing the workflow and expected GitHub result. Link changes through a branch and PR. Run python3 -m unittest discover -s tests -v and python3 scripts/validate.py and python3 scripts/render_catalog.py --check before submitting.

Preserve existing repository content and distinguish unavailable API reads from missing configuration. Changes to setup behavior need evidence for repeat execution, partial failures and custom existing content. Never put credentials in fixtures or reports.


## Configuration changes

Identify the capability and option group. Read the complete nested schema and current official source. Add or update decision rules, defaults, applicability, verification and relevant community incident context. Every capability needs option coverage, and CI checks this mapping.

## History and interaction

Use Q&A for questions and Ideas for proposals. Keep source discussion links in accepted Issues/PRs. Preserve review comments and explain superseding choices. Follow CODE_OF_CONDUCT.md and keep private data out of public reports.

Changes to execution, pagination, history or publication need regression coverage for the specific failure. Verify failed/retried operations and preservation of prior evidence. Release changes must keep committed hidden manifests, checksums, prerelease status and existing asset bytes intact.
