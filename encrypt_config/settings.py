import configparser
import os
from pathlib import Path

APP_DIR = Path(__file__).parent
APP_NAME = 'encrypted_config'

config = configparser.ConfigParser()
config.read(f'{APP_DIR}/encrypted-config.ini')

home_folder = os.path.expanduser('~')
CONFIG_FOLDER = os.path.join(home_folder, config['DEFAULT']['config_folder'])

ALLOW_OVERWRITE = config['DEFAULT']['overwrite_keys']
FERNET_KEY = config['Fernet']['filename']
