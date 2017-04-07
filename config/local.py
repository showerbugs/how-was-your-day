import os

from config.base import BaseConfig


class LocalConfig(BaseConfig):
    DEBUG = True

    DB_USER = 'showerbugs'
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_NAME = 'howwasyourday'
    DB_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    TEST_DB_NAME = 'howwasyourday_test'
    TEST_DB_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, TEST_DB_NAME)

    ALEMBIC_INI = os.path.join(os.getcwd(), 'alembic.ini')
    SESSION_COOKIE_HTTPONLY = False
