import os

import pytest

from encrypt_config.configuration import set_fernet_key
from encrypt_config import settings


@pytest.fixture
def fernet_key_filename():
    original_filename = settings.FERNET_KEY
    settings.FERNET_KEY = 'test_configurations.key'
    yield settings.FERNET_KEY
    settings.FERNET_KEY = original_filename


def tests_ini_file_data():
    assert '.encryptconfig' in settings.CONFIG_FOLDER
    assert not settings.ALLOW_OVERWRITE
    assert settings.FERNET_KEY == 'fernet.key'


def test_set_fernet_key(fernet_key_filename):
    key = 'BUGUSKEY7IIOI131131'
    filename = set_fernet_key(key)
    with open(filename, 'r') as txt:
        serialized_key = txt.read()
    print(f'Filename: {filename}')
    assert key == serialized_key
    assert settings.CONFIG_FOLDER in filename
    print(f'Fernet filename: {filename}')
