import os

from click import command

from config import config


@command()
def drop_local_db():
    if not 'DB_NAME' in config:
        print('Please set database name first in configuration.')
        exit(1)
    drop_command = 'psql -d postgres -c "DROP DATABASE {}"'.format(
        config['DB_NAME'])
    if 'DB_USER' in config:
        drop_command = '{} -U {}'.format(drop_command, config['DB_USER'])
    if 'DB_PASSWORD' in config and config['DB_PASSWORD'] is not '':
        drop_command = '{} -W {}'.format(drop_command, config['DB_PASSWORD'])
    print(drop_command)
    os.system(drop_command)
