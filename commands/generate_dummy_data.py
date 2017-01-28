import json

import requests
from click import command
from click import prompt

session = requests.Session()

server_url = 'http://127.0.0.1:5000'

users = ['emma', 'olivia', 'sophia', 'isabella', 'ava', 'mia', 'emily',
         'madison', 'charlotte']
user_ids = []
teams = ['team1', 'team2', 'team3']
team_ids = []
# psql -U amazingguni -W {PASSWORD} DROP DATABASE howwasyourday
@command()
def generate_dummy_data():
    server_url = prompt('Enter the server address where you want to add the ' \
                        'dummy data.', type=str,
                        default='http://127.0.0.1:5000')
    for user in users:
        user_ids.append(create_user(user))
    for index, team_name in enumerate(teams):
        user_selected = users[0:index * 5 + 1]
        user_emails = ['{}@email.com'.format(user) for user in user_selected]
        team_ids.append(create_team(team_name, users[index], user_emails))


def create_team(new_team_name, owner_user_name, user_emails):
    try:
        print('try signup {}'.format(owner_user_name))
        response = session.post('{}/users/signin'.format(server_url),
                                json={'email': '{}@email.com'.format(
                                    owner_user_name),
                                    'password': '123123'})
        if response.status_code is not 200:
            raise Exception('The status code is not 200 OK. but {}'.format(
                response.status_code))
        print('successfully signed up..')
        new_team_description = '{}_description'.format(new_team_name)
        print('try create team "{}"'.format(new_team_name))
        response = session.post('{}/teams/'.format(server_url),
                                json={'name': new_team_name,
                                      'description': new_team_description,
                                      'userEmails': user_emails})
        if response.status_code is not 200:
            raise Exception('The status code is not 200 OK. but {}'.format(
                response.status_code))
        response_text = json.loads(response.text)
        if response_text['success'] is not True:
            raise Exception(response_text['msg'])
        print('team "{}"(owner:{}) is created...'.format(new_team_name,
                                                         owner_user_name))
        return response_text['data']['team_id']
    except Exception as e:
        print(e)


def create_user(username):
    try:
        print('try create user "{}"'.format(username))
        response = session.post('{}/users/'.format(server_url),
                                json={'email': '{}@email.com'.format(username),
                                      'name': username,
                                      'password': '123123',
                                      'password_repeat': '123123'})
        if response.status_code is not 200:
            raise Exception('The status code is not 200 OK. but {}'.format(
                response.status_code))
        response_text = json.loads(response.text)
        if response_text['success'] is not True:
            raise Exception(response_text['msg'])
        print('user "{}" is created...'.format(username))
        return response_text['data']['user_id']
    except Exception as e:
        print(e)


def create_post():
    print('try create user "{}"'.format())
    print('user "{}" is created...'.format())

