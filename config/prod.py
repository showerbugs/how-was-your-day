from config.base import BaseConfig


class ProdConfig(BaseConfig):
    DEBUG = False

    DB_NAME = 'howwasyourday'
    TEST_DB_NAME = 'howwasyourday_test'
