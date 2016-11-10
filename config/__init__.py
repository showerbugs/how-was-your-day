import os

from config.local import Config as LocalConfig
from config.dev import Config as DevConfig
from config.prod import Config as ProdConfig


def get_config():
    env = os.environ.get('HOW_WAS_YOUR_DAY_ENV')
    config_object = {
        'local': LocalConfig,
        'dev': DevConfig,
        'prod': ProdConfig,
    }[env]

    config = {}
    for name in dir(config_object):
        if name.startswith('__'):
            continue
        config[name] = getattr(config_object, name)
    return config


def get_flask_config():
    env = os.environ.get('HOW_WAS_YOUR_DAY_ENV')
    config_object = {
        'local': 'config.local.Config',
        'dev': 'config.dev.Config',
        'prod': 'config.prod.Config',
    }[env]
    return config_object


config = get_config()
