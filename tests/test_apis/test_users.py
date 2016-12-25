import json

from db.models import User


class TestUser:
    def test_signin(self, flask_client, user_hou):
        # Given

        # When
        data = json.dumps({'email': 'hou@email.com', 'password': '1111'})
        resp = flask_client.post('/users/signin', data=data,
                                 content_type='application/json')
        result = json.loads(resp.data.decode())

        # Then
        # 응답의 status code가 200이다.
        assert resp.status_code == 200
        # 로그인에 성공한다.
        assert result['success']

    def test_create_user(self, flask_client, session):
        data = json.dumps({'email': 'new@email.com', 'name': 'new',
                           'password': '123123', 'password_repeat': '123123'})
        resp = flask_client.post('/users/', data=data,
                                 content_type='application/json')
        result = json.loads(resp.data.decode())

        assert resp.status_code == 200
        assert result['success']

        new_user = session.query(User)\
            .filter(User.email == 'new@email.com').first()
        assert new_user
