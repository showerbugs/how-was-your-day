import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig

from wsgi import create_app
from config import config


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
    Session = sessionmaker(bind=engine)
    _db = {
        'engine': engine,
        'session': Session,
    }
    alembic_config = AlembicConfig(config['ALEMBIC_INI'])
    alembic_config.set_main_option('sqlalchemy.url', config['TEST_DB_URL'])
    alembic_upgrade(alembic_config, 'head')
    print('################### migration complete')
    yield _db
    engine.dispose()


@pytest.fixture(scope='function')
def session(db):
    session = db['session']()
    yield session
    session.rollback()
    session.close()
