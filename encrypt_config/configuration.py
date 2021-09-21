import configparser
import os


from encrypt_config.settings import APP_NAME, FERNET_KEY, CONFIG_FOLDER


def get_fernet_key():
    key = None
    filename = os.path.join(CONFIG_FOLDER, FERNET_KEY)
    if filename:
        with open(filename, 'r') as txt:
            key = txt.read()
    return key


def set_fernet_key(key):
    if not os.path.exists(CONFIG_FOLDER):
        os.mkdir(CONFIG_FOLDER)

    filename = os.path.join(CONFIG_FOLDER, FERNET_KEY)
    if filename:
        with open(filename, 'w') as txt:
            txt.write(key)
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
