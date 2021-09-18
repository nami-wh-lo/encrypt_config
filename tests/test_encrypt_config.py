#!/usr/bin/env python

"""Tests for `encrypt_config` package."""

import pytest


from encrypt_config import encrypt_config
from encrypt_config.encrypt_config import FernetEncryptedConfig


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

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

