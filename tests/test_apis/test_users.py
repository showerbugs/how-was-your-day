from db.models import User

class TestUser:
    def test_signin(self, flask_client, session):
        # Given
        # 중복되지 않는 아이디와 비밀번호

        # When
        # POST /users/로 중복되지 않는 아이디와 비밀번호를 담아 요청한다.
        data = dict(name='Hou', email='hou@gmail.com', password='1111')
        response = flask_client.post('/users/signin', data=data)

        # Then
        # 200 OK가 리턴된다.
        assert 200 == response.status_code

        # User Table에 저장된다.
        assigned_user = session.query(User).filter_by(name='Hou',email='hou@gmail.com',\
            password='1111').first()
        assert assigned_user != None

