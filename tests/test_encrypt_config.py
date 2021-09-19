#!/usr/bin/env python

"""Tests for `encrypt_config` package."""
import json
import os

import pytest

from encrypt_config.encrypt_config import FernetEncryptedConfig, JSONFernetFileConfig


@pytest.fixture
def fernet_key():
    # enc_config = FernetEncryptedConfig()
    # print(enc_config.key.decode())
    # return enc_config.key
    key = 'ZD1g-k09xoZ2h8v2QqgIAnyW-UZUBkSDKE93Ks1fBdI='
    return key


@pytest.fixture
def simple_dict():
    data = {'username': 'batman_4', 'password': 'MyP8998KK-;/', 'favorite_port': 3455}
    return data


@pytest.fixture
def fernet_dict():
    enc_data = {
        "username": "gAAAAABhR0R9ycCwJr_lDIKm1fh1mLoclhQsmoQRoCGJzgql9UtzBI7BpC21k6LaqdYG85BDUI0vmkvSiZxcYXEzjT3gOdOwxg==",
        "password": "gAAAAABhR0R9Vyba6g2N3NTvJpJVC28QUda8vbFz4desjfQLzRiJ8PLnv7Caj62UU5iz2iV3m3-0AZXlDZstuzPqv8jNxtx_9w==",
        "favorite_port": 3455
    }
    return enc_data


def test_fernet_encryption():
    enc_config = FernetEncryptedConfig()
    data = {'username': 'batman_4', 'password': 'MyP8998KK-;/', 'favorite_port': 3455}
    enc_data = enc_config.encrypt_config(data)
    dec_data = enc_config.decrypt_config(enc_data)
    assert len(data) == len(enc_data)
    assert len(data) == len(dec_data)
    for key in data.keys():
        assert dec_data[key] == data[key]
        if isinstance(data[key], str):
            assert enc_data[key] != data[key]


def test_fernet_decrypt(fernet_key):
    enc_config = FernetEncryptedConfig(fernet_key)
    data = {'username': 'batman_4', 'password': 'MyP8998KK-;/', 'favorite_port': 3455}
    enc_data = enc_config.encrypt_config(data)
    dec_data = enc_config.decrypt_config(enc_data)
    assert len(data) == len(enc_data)
    assert len(data) == len(dec_data)
    for key in data.keys():
        assert dec_data[key] == data[key]
        if isinstance(data[key], str):
            assert enc_data[key] != data[key]


def test_write_files(fernet_key, simple_dict, fernet_dict):
    manager = JSONFernetFileConfig(fernet_key)
    filename = '../output/simple_dict.json'
    if os.path.exists(filename):
        os.remove(filename)

    encrypted, key = manager.write(filename, simple_dict)
    assert fernet_key == key
    assert os.path.exists(filename)

    with open(filename, 'r') as json_file:
        encrypted_from_file = json.load(json_file)

    assert encrypted_from_file.keys() == simple_dict.keys()

    decrypted, dec_key = manager.read(filename)
    assert decrypted == simple_dict
