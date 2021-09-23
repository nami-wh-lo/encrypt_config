import os

import pytest

from encrypt_config.settings import CONFIG_FOLDER, ALLOW_OVERWRITE, FERNET_KEY


def tests_ini_file_data():
    assert '.encryptconfig' in CONFIG_FOLDER
    assert ALLOW_OVERWRITE == 'False'
    assert FERNET_KEY == 'fernet.key'
