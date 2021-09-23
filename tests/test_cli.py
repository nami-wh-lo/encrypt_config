import json
import tempfile

from encrypt_config.cli import fernet_encrypt


def test_fernet_encrypt(unencrypted_files):
    filename = unencrypted_files['unencrypted_creds.json']
    with open(filename, 'r') as json_file:
        unencrypted_data = json.load(json_file)
    new_file, output_filename = tempfile.mkstemp()
    encrypted_dict, key = fernet_encrypt(filename, output_filename)
    assert encrypted_dict.keys() == unencrypted_data.keys()
    assert len(key) > 0
