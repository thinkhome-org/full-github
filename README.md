# Full GitHub

[![Checks](https://github.com/thinkhome-org/full-github/actions/workflows/check.yml/badge.svg)](https://github.com/thinkhome-org/full-github/actions/workflows/check.yml)
[![Release](https://img.shields.io/github/v/release/thinkhome-org/full-github)](https://github.com/thinkhome-org/full-github/releases)

A native Codex plugin for using GitHub throughout repository setup, development and maintenance. Published by ThinkHome.

## Install

Requires Codex with plugin support, Python 3, Git and authenticated GitHub CLI.

```sh
codex plugin marketplace add thinkhome-org/full-github
codex plugin add full-github@thinkhome
```

Open a new Codex chat in your repository and select Full GitHub.

## Use

- “Audit this repository with Full GitHub.” performs a read-only review.
- “Set up this repository using the full profile.” reconciles settings and records repository-specific decisions.
- “Deliver this issue and update its Project and Wiki.” keeps planning and documentation connected to the implementation.

The full profile covers Issues, Projects, branches, pull requests, Actions, security, documentation, Wiki and releases. Packages, Pages and hooks are evaluated for applicability. The agent uses existing GitHub access and asks for unresolved material decisions.

This is a skills plugin. Codex executes the workflow through gh, Git and available UI tools. Repository rules become discoverable through GITHUB.md linked from AGENTS.md. Automatic invocation depends on the host and selected skills.

## Read-only snapshot

```sh
python3 scripts/audit.py thinkhome-org/full-github
python3 -m unittest discover -s tests -v
```

Failed reads appear as unknown. The snapshot supplies evidence for the wider skill audit and covers repository settings, labels, milestones, rulesets, workflows, releases and community files.

See the [Wiki](https://github.com/thinkhome-org/full-github/wiki), [coverage reference](skills/full-github/references/features.md), [contribution guide](CONTRIBUTING.md) and [repository workflow](GITHUB.md).

## Status

Version 0.1 is an initial public release. UI-only Projects configuration requires computer access. GitHub permissions and subscription features vary. See Wiki verification for tested capabilities and outstanding limitations.

## License

A license has not yet been selected by the owner. Contact ThinkHome before redistribution beyond rights granted by GitHub's terms.
