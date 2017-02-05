import os

from config.base import BaseConfig


class DevConfig(BaseConfig):
    DEBUG = True

    DB_USER = os.environ.get('HOWWASYOURDAY_DB_USER')
    DB_PASSWORD = os.environ.get('HOWWASYOURDAY_DB_PASSWORD')
    DB_HOST = os.environ.get('HOWWASYOURDAY_DB_HOST')
    DB_PORT = os.environ.get('HOWWASYOURDAY_DB_PORT')
    DB_NAME = 'howwasyourday'
    DB_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    TEST_DB_NAME = 'howwasyourday_test'
    TEST_DB_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, TEST_DB_NAME)

    ALEMBIC_INI = os.path.join(os.getcwd(), 'alembic.ini')
