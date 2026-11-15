"""Check a full-profile coverage ledger; this validates claims, not live GitHub state."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

from execution_history import validate_reference


CAPABILITY_IDS = {row['id'] for row in json.loads(
    (Path(__file__).resolve().parents[1] / 'skills/full-github/data/capabilities.json').read_text())['capabilities']}
FINAL_STATES = {'configured': 'matched', 'unavailable': 'gate-confirmed',
                'not-applicable': 'context-confirmed'}
PLACEHOLDERS = {'unknown', 'todo', 'tbd', 'n/a', 'not-applicable', 'unavailable'}


def check(ledger):
    """Return complete/checked/gaps for repository and all catalog capability rows.

    Each row needs id, state, desired, observed, action, gate, evidence (HTTPS
    links), and verification. Unavailable/inapplicable rows also need a reason.
    Explicit verification distinguishes read-back from command success; observed
    objects may contain extra metadata, so values are not compared structurally.
    """
    gaps = []
    def gap(field, message):
        gaps.append({'field': field, 'message': message})

    if not isinstance(ledger, dict):
        return {'complete': False, 'checked': 0,
                'gaps': [{'field': 'ledger', 'message': 'Expected a JSON object'}]}
    repository = ledger.get('repository')
    if not isinstance(repository, str) or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) or any(
            part in ('.', '..') for part in repository.split('/')):
        gap('repository', 'Expected OWNER/REPO')
    rows = ledger.get('capabilities')
    if not isinstance(rows, list):
        gap('capabilities', 'Expected the full catalog as an array of rows')
        rows = []
    seen = set()
    for index, row in enumerate(rows):
        prefix = f'capabilities[{index}]'
        if not isinstance(row, dict):
            gap(prefix, 'Expected a capability object')
            continue
        capability_id = row.get('id')
        if not isinstance(capability_id, str) or capability_id not in CAPABILITY_IDS:
            gap(prefix + '.id', 'Unknown capability ID')
            continue
        if capability_id in seen:
            gap(prefix + '.id', 'Duplicate capability ID')
        seen.add(capability_id)
        state = row.get('state')
        if not isinstance(state, str) or state not in FINAL_STATES:
            gap(prefix + '.state', 'Unfinished or invalid state; reconcile before completion')
        elif row.get('verification') != FINAL_STATES[state]:
            gap(prefix + '.verification', f'Expected {FINAL_STATES[state]} after inspecting evidence')
        for field in ('desired', 'observed', 'action', 'gate'):
            value = row.get(field)
            if (field in ('action', 'gate') and not isinstance(value, str)) or value is None or value == '' or value == [] or value == {} or (
                    isinstance(value, str) and (not value.strip() or value.strip().lower() in PLACEHOLDERS)):
                gap(prefix + '.' + field, 'Provide the concrete configuration, action or access gate')
        if state in ('unavailable', 'not-applicable'):
            reason = row.get('reason')
            if not isinstance(reason, str) or not reason.strip() or reason.strip().lower() in PLACEHOLDERS:
                gap(prefix + '.reason', 'Provide a concrete target-specific reason')
        evidence = row.get('evidence')
        if not isinstance(evidence, list) or not evidence:
            gap(prefix + '.evidence', 'Provide at least one HTTPS evidence link')
        else:
            for link in evidence:
                try:
                    if not isinstance(link, str) or not link or any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in link):
                        raise ValueError('Invalid evidence link')
                    validate_reference(link)
                    urlsplit(link).port
                except ValueError:
                    gap(prefix + '.evidence', 'Evidence must be HTTPS without credentials, whitespace or query parameters')
    for capability_id in sorted(CAPABILITY_IDS - seen):
        gap('capabilities.' + capability_id, 'Missing catalog capability')
    return {'complete': not gaps, 'checked': len(seen), 'gaps': gaps}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ledger', type=Path, help='JSON object with repository and capabilities rows')
    args = parser.parse_args()
    try:
        result = check(json.loads(args.ledger.read_text()))
    except (OSError, UnicodeError, json.JSONDecodeError):
        result = {'complete': False, 'checked': 0,
                  'gaps': [{'field': 'ledger', 'message': 'Cannot read a valid UTF-8 JSON ledger'}]}
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['complete'] else 1)
