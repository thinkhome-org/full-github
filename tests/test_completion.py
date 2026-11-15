import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
spec = importlib.util.spec_from_file_location('check_completion', ROOT / 'scripts/check_completion.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CompletionTests(unittest.TestCase):
    def setUp(self):
        self.ledger = {'repository': 'example/repository', 'capabilities': [
            {'id': capability_id, 'state': 'configured', 'desired': {'enabled': False},
             'observed': {'enabled': False, 'id': 1}, 'action': 'Retained reviewed configuration',
             'gate': 'Existing repository write permission',
             'evidence': ['https://github.com/example/repository/issues/1#issuecomment-1'],
             'verification': 'matched'} for capability_id in sorted(module.CAPABILITY_IDS)]}

    def test_all_catalog_capabilities_with_verified_configuration_pass(self):
        result = module.check(self.ledger)
        self.assertTrue(result['complete'], result)
        self.assertEqual(result['checked'], len(module.CAPABILITY_IDS))
        self.assertFalse(result['gaps'])

    def test_missing_duplicate_and_unknown_ids_fail(self):
        cases = [self.ledger['capabilities'][:-1],
                 self.ledger['capabilities'] + [copy.deepcopy(self.ledger['capabilities'][0])],
                 self.ledger['capabilities'] + [dict(self.ledger['capabilities'][0], id='invented-feature')]]
        for rows in cases:
            with self.subTest(rows=len(rows)):
                self.assertFalse(module.check(dict(self.ledger, capabilities=rows))['complete'])

    def test_unfinished_and_invalid_states_fail(self):
        for state in ('unknown', 'available-unconfigured', 'done', None, []):
            with self.subTest(state=state):
                self.ledger['capabilities'][0]['state'] = state
                result = module.check(self.ledger)
                self.assertFalse(result['complete'])
                self.assertTrue(result['gaps'])

    def test_configured_requires_readback_claim_and_complete_values(self):
        for key in ('verification', 'desired', 'observed', 'action', 'gate', 'evidence'):
            with self.subTest(key=key):
                ledger = copy.deepcopy(self.ledger)
                del ledger['capabilities'][0][key]
                self.assertFalse(module.check(ledger)['complete'])
        for field in ('action', 'gate'):
            ledger = copy.deepcopy(self.ledger)
            ledger['capabilities'][0][field] = True
            self.assertFalse(module.check(ledger)['complete'])
        self.ledger['capabilities'][0]['verification'] = 'command_succeeded'
        self.assertFalse(module.check(self.ledger)['complete'])

    def test_permission_and_inapplicability_need_specific_reason_and_evidence(self):
        for state, verification in (('unavailable', 'gate-confirmed'), ('not-applicable', 'context-confirmed')):
            with self.subTest(state=state):
                row = self.ledger['capabilities'][0]
                row.update(state=state, verification=verification,
                           reason='Target account has no enterprise entitlement')
                self.assertTrue(module.check(self.ledger)['complete'])
                for reason in ('', 'unknown', 'not-applicable', None):
                    row['reason'] = reason
                    self.assertFalse(module.check(self.ledger)['complete'])
                row['reason'] = 'Target account has no enterprise entitlement'
                row['evidence'] = []
                self.assertFalse(module.check(self.ledger)['complete'])
                row['evidence'] = ['https://github.com/example/repository/issues/1']
                row['verification'] = 'matched'
                self.assertFalse(module.check(self.ledger)['complete'])

    def test_evidence_cannot_contain_credentials_or_query_parameters(self):
        for evidence in (['http://github.com/example'], ['https://user:secret@github.com/example'],
                         ['https://github.com/example?token=secret'], ['https://github.com:bad/example'],
                         ['https://github.com/ex\x00ample'], ['https://gith\x01ub.com/example'],
                         [''], ['not a URL'],
                         [None], 'https://github.com/example'):
            with self.subTest(evidence=evidence):
                self.ledger['capabilities'][0]['evidence'] = evidence
                result = module.check(self.ledger)
                self.assertFalse(result['complete'])
                self.assertNotIn('secret', json.dumps(result))

    def test_invalid_document_shape_returns_gaps_instead_of_crashing(self):
        for ledger in ([], None, {}, {'repository': 'invalid', 'capabilities': []},
                       {'repository': 'owner/repo', 'capabilities': {}},
                       {'repository': 'owner/repo', 'capabilities': [None, {'id': []}]}):
            with self.subTest(ledger=ledger):
                self.assertFalse(module.check(ledger)['complete'])

    def test_cli_nonzero_on_incomplete_or_unreadable_ledger(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'ledger.json'
            path.write_text(json.dumps(self.ledger))
            command = [sys.executable, str(ROOT / 'scripts/check_completion.py'), str(path)]
            good = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(good.returncode, 0, good.stderr)
            self.assertTrue(json.loads(good.stdout)['complete'])
            path.write_text('{"repository":"example/repository","capabilities":[]}')
            bad = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(bad.returncode, 0)
            self.assertFalse(json.loads(bad.stdout)['complete'])
            path.write_text('{broken')
            malformed = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(malformed.returncode, 0)
            self.assertFalse(json.loads(malformed.stdout)['complete'])
            path.unlink()
            missing = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(missing.returncode, 0)
            self.assertFalse(json.loads(missing.stdout)['complete'])


if __name__ == '__main__':
    unittest.main()
