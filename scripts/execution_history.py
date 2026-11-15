"""Append-only local execution records without request bodies, headers or responses."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sqlite3
from urllib.parse import urlsplit
import uuid

STATE = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "full-github"
DATABASE = STATE / "history.sqlite3"
TARGET_KEYS = {"owner", "repo", "org", "enterprise", "issue_number", "pull_number", "project_number", "release_id", "asset_id", "run_id", "job_id"}


def validate_reference(reference):
    if not reference:
        return
    url = urlsplit(reference)
    if url.scheme != "https" or not url.hostname or url.username or url.password or url.query:
        raise ValueError("History context/evidence must be an HTTPS link without credentials or query parameters")


def append_event(run_id, kind, details):
    DATABASE.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with sqlite3.connect(DATABASE, timeout=30) as database:
        database.execute("CREATE TABLE IF NOT EXISTS events (sequence INTEGER PRIMARY KEY, run_id TEXT NOT NULL, time TEXT NOT NULL, kind TEXT NOT NULL, details TEXT NOT NULL)")
        database.execute("INSERT INTO events(run_id,time,kind,details) VALUES(?,?,?,?)",
                         (run_id, datetime.now(timezone.utc).isoformat(), kind, json.dumps(details, sort_keys=True)))
    os.chmod(DATABASE, 0o600)


def start(operation_id, operation, parameters, context=""):
    validate_reference(context)
    run_id = str(uuid.uuid4())
    targets = {key: value for key, value in parameters.items() if key in TARGET_KEYS}
    host = urlsplit(operation.get("server", "")).hostname or os.environ.get("GH_HOST", "github.com")
    append_event(run_id, "started", {"operation": operation_id, "method": operation["method"], "host": host, "target": targets, "context": context})
    return run_id


def finish(run_id, returncode):
    kind = "command_succeeded" if returncode == 0 else "outcome_unknown"
    append_event(run_id, kind, {"exit_code": returncode})


def read_events(limit=100):
    if limit < 0:
        raise ValueError("History limit must be nonnegative; 0 returns all events")
    if not DATABASE.exists():
        return []
    with sqlite3.connect(DATABASE.resolve().as_uri() + "?mode=ro", uri=True, timeout=30) as database:
        rows = database.execute("SELECT sequence,run_id,time,kind,details FROM events ORDER BY sequence DESC LIMIT ?", (limit or -1,)).fetchall()
    return [{"sequence": row[0], "run_id": row[1], "time": row[2], "kind": row[3], "details": json.loads(row[4])} for row in rows]


def verify(run_id, outcome, evidence):
    validate_reference(evidence)
    if not evidence:
        raise ValueError("Verification requires an evidence link")
    if not DATABASE.exists():
        raise ValueError("Execution run not found")
    with sqlite3.connect(DATABASE.resolve().as_uri() + "?mode=ro", uri=True, timeout=30) as database:
        exists = database.execute("SELECT 1 FROM events WHERE run_id=? AND kind='started'", (run_id,)).fetchone()
    if not exists:
        raise ValueError("Execution run not found")
    append_event(run_id, "verification_recorded", {"outcome": outcome, "evidence": evidence})
