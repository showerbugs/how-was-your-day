import sys
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config

if hasattr(sys, '_called_from_test'):
    db_url = config['TEST_DB_URL']
else:
    db_url = config['DB_URL']

engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)


@contextmanager
def db():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
