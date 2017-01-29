import os

from config.local import LocalConfig
from config.dev import DevConfig
from config.prod import ProdConfig
from config.travis import TravisConfig

print('confing.__init__')


def get_config():
    env = os.environ.get('HOW_WAS_YOUR_DAY_ENV')
    print('get_config {}'.format(env))

    config_object = {
        'local': LocalConfig,
        'dev': DevConfig,
        'prod': ProdConfig,
        'travis': TravisConfig
    }[env]

    config = {}
    for name in dir(config_object):
        if name.startswith('__'):
            continue
        config[name] = getattr(config_object, name)

    print('get_config {}'.format(config))
    return config


def get_flask_config():
    env = os.environ.get('HOW_WAS_YOUR_DAY_ENV')
    print('get_flask_config {}'.format(env))

    config_object = {
        'local': 'config.local.LocalConfig',
        'dev': 'config.dev.DevConfig',
        'prod': 'config.prod.ProdConfig',
        'travis': 'config.travis.TravisConfig',
    }[env]
    return config_object


config = get_config()
flask_config = get_flask_config()
