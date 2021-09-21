"""Top-level package for Encrypt Config."""

__author__ = """Luis C. Berrocal"""
__email__ = 'luis.berrocal.1942@gmail.com'
__version__ = '0.1.5'

import configparser
import os
from pathlib import Path
APP_DIR = Path(__file__).parent

config = configparser.ConfigParser()
config.read(f'{APP_DIR}/encrypted-config.ini')

CONFIG_FOLDER = config['DEFAULT']['config_folder']

ALLOW_OVERWRITE = config['DEFAULT']['overwrite_keys']
FERNET_KEY = config['Fernet']['filename']
