import pytest

from db.models import User


@pytest.fixture(scope='function')
def user_hou(session):
    hou = User(email='hou@email.com',
               name='hou',
               password='1111')
    session.add(hou)
