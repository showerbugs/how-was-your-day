import unittest
import wsgi

from db.models import User
from users.views import session



class TestUser:
    def setup(self):
        self.app = wsgi.app.test_client()

    def test_signin(self):
        # Given
        # 중복되지 않는 아이디와 비밀번호
        
        # When
        # POST /users/로 중복되지 않는 아이디와 비밀번호를 담아 요청한다.
        response = self.app.post('/users', data=dict(name="Hou", email="hou@gmail.com", \
            password="1111"), follow_redirects=True)
        
        # Then
        # 200 OK가 리턴된다.
        assert 200 == response.status_code

        # User Dable에 저장된다.
        assigned_user = session.query(User).filter_by(name='Hou',email='hou@gmail.com',\
            password='1111').first()
        assert assigned_user != None
    

