import json

import requests
from click import command
from click import prompt

session = requests.Session()

server_url = 'http://127.0.0.1:5000'


@command()
def generate_dummy_data():
    server_url = prompt('Enter the server address where you want to add the ' \
                        'dummy data.', type=str,
                        default='http://127.0.0.1:5000')
    create_user('test12')

def create_user(username):
    try:
        response = session.post('{}/users/'.format(server_url),
                                json={'email': '{}@email.com'.format(username),
                                      'name': username,
                                      'password': '123123',
                                      'password_repeat': '123123'})
        if response.status_code is not 200:
            raise Exception('The status code is not 200 OK. but {}'.format(response.status_code))
        response_text = json.loads(response.text)
        if response_text['success'] is not True:
            raise Exception(response_text['msg'])
        print('user "{}" is created...'.format(username))
        return response_text
    except Exception as e:
        print(e)
