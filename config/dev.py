from config.base import BaseConfig


class DevConfig(BaseConfig):
    DEBUG = True

    DB_NAME = 'howwasyourday'
    TEST_DB_NAME = 'howwasyourday_test'
