import os
import random
import tempfile

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


def test_set_fernet_key(fernet_key_filename, monkeypatch):
    with monkeypatch.context() as m:
        mock_key_filename = '{}_fernet.key'.format(random.randint(1, 1000))
        m.setattr('encrypt_config.settings.FERNET_KEY', mock_key_filename, raising=True)

        key = 'BUGUSKEY7IIOI131131'
        filename = set_fernet_key(key)
        with open(filename, 'r') as txt:
            serialized_key = txt.read()

        assert key == serialized_key
        assert settings.CONFIG_FOLDER in filename
        os.remove(filename)
