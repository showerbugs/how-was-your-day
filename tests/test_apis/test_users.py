class TestUser:
    def test_signin(self, flask_client):
        resp = flask_client.post('users/signin')
        assert resp.status_code == 200
