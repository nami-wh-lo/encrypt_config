import configparser
import os

from appdirs import user_config_dir

from encrypt_config.settings import APP_NAME, FERNET_KEY


def get_fernet_key():
    key = None
    config_folder = user_config_dir(APP_NAME)
    filename = os.path.join(config_folder, FERNET_KEY)
    if filename:
        with open(filename, 'r') as txt:
            key = txt.read()
    return key


def set_fernet_key(key):
    config_folder = user_config_dir(APP_NAME)
    if not os.path.exists(config_folder):
        os.mkdir(config_folder)

    filename = os.path.join(config_folder, FERNET_KEY)
    if filename:
        with open(filename, 'w') as txt:
            key = txt.write(key)
    return filename


def write_configuration(filename):
    config = configparser.ConfigParser()
    config['DEFAULT'] = dict()
    config['DEFAULT']['config_folder'] = '.encryptconfig'
    config['DEFAULT']['overwrite_keys'] = 'False'
    config['Fernet'] = dict()
    config['Fernet']['filename'] = 'fernet.key'

    with open(filename, 'w') as ini_file:
        config.write(ini_file)


if __name__ == '__main__':
    home_folder = os.environ['HOME']

    fn = '../output/encrypted-config.ini'
    write_configuration(fn, home_folder)
