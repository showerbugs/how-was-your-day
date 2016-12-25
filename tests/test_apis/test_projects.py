import json

from db.models import User
from db.models import Project


class TestUser:
    def test_create_project(self, flask_client, session, logined_user_hou):
        # Given
        new_project_name = 'new_project'

        # When
        data = json.dumps({'name': new_project_name})
        resp = flask_client.post('/projects/', data=data, \
                                 content_type='application/json', follow_redirects=True)
        result = json.loads(resp.data.decode())

        # Then
        resp = flask_client.get('/projects/', content_type='application/json', follow_redirects=True)
        result = json.loads(resp.data.decode())
        print(result['data']['projects'])
        assert len(result['data']['projects']) == 1
        assert result['data']['projects'][0]['name'] == new_project_name

    def test_get_project_list(self, flask_client, session, logined_user_hou):
        # Given 프로젝트를 만들고
        project = Project(name='new_project')
        project.users.append(logined_user_hou)
        session.add(project)

        # When projects를 호출하면
        resp = flask_client.get('/projects/', content_type='application/json', follow_redirects=True)
        result = json.loads(resp.data.decode())

        # Then 잘들어가있다
        assert resp.status_code == 200
        assert result['success']
        assert len(result['data']['projects']) == 1
        assert result['data']['projects'][0]['name'] == project.name
