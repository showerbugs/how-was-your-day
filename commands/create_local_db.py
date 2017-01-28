import os

from click import command

from config import config


@command()
def create_local_db():
    if not 'DB_NAME' in config:
        print('Please set database name first in configuration.')
        exit(1)
    create_command = 'psql -d postgres -c "CREATE DATABASE {}"'.format(
        config['DB_NAME'])
    if 'DB_USER' in config:
        create_command = '{} -U {}'.format(create_command, config['DB_USER'])
    if 'DB_PASSWORD' in config and config['DB_PASSWORD'] is not '':
        create_command = '{} -W {}'.format(create_command,
                                           config['DB_PASSWORD'])
    print(create_command)
    os.system(create_command)
