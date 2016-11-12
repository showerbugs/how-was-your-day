import os

try:
    from config.local import LocalConfig
except ImportError:
    pass
from config.dev import DevConfig
from config.prod import ProdConfig


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
        'local': 'config.local.LocalConfig',
        'dev': 'config.dev.DevConfig',
        'prod': 'config.prod.ProdConfig',
    }[env]
    return config_object


config = get_config()
flask_config = get_flask_config()
