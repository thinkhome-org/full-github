# Installation

Requires Codex with plugin support, Python 3.10+, Git and authenticated gh.

```sh
codex plugin marketplace add thinkhome-org/full-github
codex plugin add full-github@thinkhome
```

For an existing installation, refresh the source and install the current version.

```sh
codex plugin marketplace upgrade thinkhome
codex plugin add full-github@thinkhome
```

Open a fresh Codex chat in the target repository and select Full GitHub. Ask for an audit, setup or delivery workflow. See [[Usage]] and [[API]].
