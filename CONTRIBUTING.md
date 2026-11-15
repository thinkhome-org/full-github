# Contributing

Open an issue describing the workflow and expected GitHub result. Link changes through a branch and PR. Run python3 -m unittest discover -s tests -v and python3 scripts/validate.py and python3 scripts/render_catalog.py --check before submitting.

Preserve existing repository content and distinguish unavailable API reads from missing configuration. Changes to setup behavior need evidence for repeat execution, partial failures and custom existing content. Never put credentials in fixtures or reports.
