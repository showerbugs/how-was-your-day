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

    def test_signin(self, flask_client, user_hou):
        # Given signin을하고
        data = json.dumps({'email': 'hou@email.com', 'password': '1111'})
        flask_client.post('/users/signin', data=data,
                                 content_type='application/json')
        # When signout을하면
        resp = flask_client.delete('/users/signout')
        result = json.loads(resp.data.decode())

        # Then
        # 응답의 status code가 200이고 signout에 성공한다.
        assert resp.status_code == 200
        assert result['success']

    def test_signin_user_notexists(self, flask_client):
        # Given 서버에 없는 유저로
        not_exist_user_data = json.dumps({'email': 'notexist@email.com', 'password': '1111'})

        # When 로그인 요청을 하면
        resp = flask_client.post('/users/signin', data=not_exist_user_data,
                                 content_type='application/json')
        result = json.loads(resp.data.decode())

        # Then
        # 응답의 status code가 200이다.
        assert resp.status_code == 200
        # 로그인에 실패한다.
        assert result['success'] == False

    def test_create_user(self, flask_client, session):
        data = json.dumps({'email': 'new@email.com', 'name': 'new',
                           'password': '123123', 'password_repeat': '123123'})
        resp = flask_client.post('/users/', data=data,
                                 content_type='application/json')
        result = json.loads(resp.data.decode())

        assert resp.status_code == 200
        assert result['success']

        new_user = session.query(User) \
            .filter(User.email == 'new@email.com').first()
        assert new_user

    def test_create_user_repeated_password_different(self, flask_client, session):
        # Given password와 password_repeat가 다르게 주어지고
        data = json.dumps({'email': 'new@email.com', 'name': 'new',
                           'password': '123123', 'password_repeat': 'different'})

        # When users로 post method를 호출하면
        resp = flask_client.post('/users/', data=data,
                                 content_type='application/json')

        # Then 회원가입이 실패한다 응답이 돌아오고 DB에 저장되지 않는다.
        result = json.loads(resp.data.decode())
        assert resp.status_code == 200
        assert result['success'] == False

        user_list = session.query(User) \
            .filter(User.email == 'new@email.com').all()
        assert len(user_list) == 0