import pytest
import json

from db.models import User
from db.models import Team


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


@pytest.fixture(scope='function')
def team_hou(session, user_hou):
    team_hou = Team(owner_id=user_hou.id,
                    name='team_hou',
                    description='team_hou')
    session.add(team_hou)
    session.flush()
    return team_hou
