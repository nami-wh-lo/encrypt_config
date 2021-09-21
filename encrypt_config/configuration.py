import configparser
import os


def write_configuration(filename, home_folder):
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

    filename = '../output/encrypted-config.ini'
    write_configuration(filename, home_folder)
