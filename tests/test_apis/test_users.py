import json


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
