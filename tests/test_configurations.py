import os

import pytest

from encrypt_config.configuration import set_fernet_key
from encrypt_config.settings import CONFIG_FOLDER, ALLOW_OVERWRITE, FERNET_KEY


def tests_ini_file_data():
    assert '.encryptconfig' in CONFIG_FOLDER
    assert ALLOW_OVERWRITE == 'False'
    assert FERNET_KEY == 'fernet.key'


def test_set_fernet_key():
    key = 'BUGUSKEY7IIOI131131'
    filename = set_fernet_key(key)
    with open(filename, 'r') as txt:
        serialized_key = txt.read()
    print(f'Filename: {filename}')
    assert key == serialized_key
    assert CONFIG_FOLDER in filename
