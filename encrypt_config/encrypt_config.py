"""Main module."""
from abc import ABC

from cryptography.fernet import Fernet


class EncryptedConfig(ABC):

    def encrypt_config(self, config_data, keys_to_encrypt=None):
        pass

    def decrypt_config(self, config_data, keys_to_encrypt=None):
        pass


class FernetEncryptedConfig(EncryptedConfig):

    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], str):
            self.key = args[0].encode()
        elif len(args) > 0 and isinstance(args[0], bytes):
            self.key = args[0]
        else:
            self.key = Fernet.generate_key()
        # Instance the Fernet class with the key
        self.fernet = Fernet(self.key)  # noqa

    def encrypt_config(self, config_data, keys_to_encrypt=None):
        encrypted_data = config_data.copy()
        if keys_to_encrypt is None:
            keys_to_encrypt = config_data.keys()
        for key in config_data.keys():
            if key in keys_to_encrypt and isinstance(config_data[key], str):
                encrypted_data[key] = self.fernet.encrypt(config_data[key].encode()).decode()
        return encrypted_data

    def decrypt_config(self, config_data, keys_to_encrypt=None):
        decrypted_data = config_data.copy()
        if keys_to_encrypt is None:
            keys_to_encrypt = config_data.keys()
        for key in config_data.keys():
            if key in keys_to_encrypt and isinstance(config_data[key], str):
                decrypted_data[key] = self.fernet.decrypt(config_data[key].encode()).decode()
        return decrypted_data
