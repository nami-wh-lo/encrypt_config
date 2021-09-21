import configparser
import os
from pathlib import Path
APP_DIR = Path(__file__).parent
APP_NAME = 'encrypted_config'

config = configparser.ConfigParser()
config.read(f'{APP_DIR}/encrypted-config.ini')

CONFIG_FOLDER = config['DEFAULT']['config_folder']

ALLOW_OVERWRITE = config['DEFAULT']['overwrite_keys']
FERNET_KEY = config['Fernet']['filename']
