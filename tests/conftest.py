import sys
import pytest
from flask import g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig

from wsgi import create_app
from config import config


def pytest_configure(config):
    sys._called_from_test = True


def pytest_unconfigure(config):
    del sys._called_from_test


@pytest.fixture(scope='session')
def flask_app():
    app = create_app()
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()


@pytest.fixture(scope='session')
def flask_client(flask_app):
    return flask_app.test_client()


@pytest.fixture(scope='session')
def db():
    engine = create_engine(config['TEST_DB_URL'], echo=True)
    session = sessionmaker(bind=engine)
    _db = {'engine': engine,
           'session': session}

    alembic_config = AlembicConfig(config['ALEMBIC_INI'])
    alembic_config.set_main_option('sqlalchemy.url', config['TEST_DB_URL'])
    alembic_upgrade(alembic_config, 'head')

    yield _db
    engine.dispose()


@pytest.fixture(scope='function')
def session(db):
    session = db['session']()
    g.db = session  # production APIs use session with g.db
    yield session
    session.rollback()
    session.close()
