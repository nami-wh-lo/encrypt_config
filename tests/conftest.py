import os
from pathlib import Path

import pytest

FIXTURE_PATH = Path(__file__).parent / 'fixtures'


@pytest.fixture(scope='session')
def unencrypted_files():
    matched_files = dict()
    for root, dirs, files in os.walk(FIXTURE_PATH, topdown=False):
        for name in files:
            if name.startswith('unencrypted_'):
                matched_files[name] = os.path.join(root, name)
    return matched_files


def test_unencrypted_fixtures(unencrypted_files):
    assert 'unencrypted_creds.json' in unencrypted_files.keys()


