import pytest
import json

from db.models import User


@pytest.fixture(scope='function')
def user_hou(session):
    hou = User(email='hou@email.com',
               name='hou',
               password='1111')
    session.add(hou)
    return hou


@pytest.fixture(scope='function')
def logined_user_hou(flask_client, user_hou):
    data = json.dumps({'email': user_hou.email, 'password': user_hou.password})
    flask_client.post('/users/signin', data=data,
                      content_type='application/json')
    return user_hou
