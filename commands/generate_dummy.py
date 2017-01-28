import json

import requests
from click import command
from click import prompt

session = requests.Session()

server_url = 'http://127.0.0.1:5000'

users = ['emma', 'olivia', 'sophia', 'isabella', 'ava', 'mia', 'emily',
         'madison', 'charlotte']
user_ids = []
teams = [{'name': 'team1',
          'emails': ['{}@email.com' for user in users[0:11]]},
         {'name': 'team2',
          'emails': ['{}@email.com' for user in users[0:6]]},
         {'name': 'team3',
          'emails': ['{}@email.com' for user in users[0:1]]}]
team_ids = []
stories = [
    '1) I am trying to understand. 이해하려고 노력 중입니다.',
    '2) I am ready to go out. 전 나갈 준비가 됐어요.',
    '3) I am just about to go to bed. 막 잠자리에 들려는 중이었어요.',
    '4) I am calling to make a reservation. 예약하려고 전화한 건데요.',
    '5) Are you going to study for your test? 너 시험공부할 거니? ',
    '6) Are you done with the report? 리포트 다 썼어요? ',
    '7) Can I have your phone number? 전화번호 좀 알려주시겠어요?',
    '8) Can I get you a drink? 마실 것 갖다드릴까요?',
    '9) Can I help you with your coat? 코트 받아드릴까요?',
    '10) Can you tell me where the bathroom is? 화장실이 어디 있는지 알려주실래요?',
    '11) Can you bring me a blanket? 담요 좀 갖다주실래요?',
    '12) Can you give me a chance? 제게 한번만 더 기회를 주세요.',
    '13) Can you show me the specials? 특별한 것들을 제게 보여주실 수 있나요?',
    '14) I can´t believe you did that. 네가 그렇게 했다는 것을 믿을 수가 없어.',
    '15) I can´t think of a solution. 해결방안이 안 떠오르네.',
    '16) I can´t wait for my birthday. 내 생일이 빨리 왔으면.',
    '17) I can´t stand it when you lie to me. 네가 거짓말을 할 때면 난 돌아버리겠어~',
    '18) Is it okay if I spend the night? 밤새우고 와도 괜찮아요?',
    '19) Is it possible that you´re wrong? 네가 틀렸다는 게 가능해? ',
    '20) Is that okay with you? 너 괜찮아?',
    '21) Would it be possible if I tried harder? 내가 좀더 노력하면 가능할까요?',
    '22) Is it done well? 잘 끝났어?',
    '23) Why don´t you look for a job? 직장을 찾아보는 게 어때요?',
    '24) Why are you here? 여기는 왜 왔어?',
    '25) Why are you always putting me down? 넌 왜 항상 나를 무시하니?',
    '26) That is how I do it. 그게 제가 그것을 하는 방법이에요.',
    '27) That is what I heard. 그게 바로 내가 들은 거야.',
    '28) That is why I´m so tired. 바로 그래서 내가 피곤 한거야.',
    '29) Would you please be quiet? 조용히 좀 해줄래요?',
    '30) Would you like to watch television? TV를 보실래요?',
    '31) Would you like me to drive? 제가 운전할까요?',
    '32) How would you like your steak done? 스테이크는 어떻게 요리해드릴까요?',
    '33) What would you like to drink? 뭐 마실래요?',
    '34) I think I like this place. 난 이곳이 맘에 들어.',
    '35) Do you need to go shopping? 너 쇼핑가야 돼?',
    '36) You´ll need to listen carefully. 너 잘 들어야 돼.',
    '37) All I need is some rest. 내게 필요한 건 휴식뿐이야.',
    '38) I think you should get some fresh air. 바깥 공기를 좀 쐬는 게 좋을 것 같은데.',
    '39) I think we need to get some professional help. 우린 전문가의 도움을 받아야 할 것 같아요.',
    '40) I think I might have the answer. 나한테 답이 있을 거야.',
    '41) What do you think of our new teacher? 새로 오신 우리 선생님 어때?',
    '42) How do you think I feel? 내가 어떻게 느낄 것 같아?',
    '43) I want you to listen to me 내 말 잘 들어봐.',
    '44) Do you want me to talk to him? 내가 그 사람하고 얘기해볼까?',
    '45) What do you want to do today? 오늘 뭐하고 싶어?',
    '46) Where can I park my car? 제 차를 어디에 주차할 수 있나요?',
    '47) Could you please tell me where the bathroom is? 화장실이 어딘지 알려주실래요?',
    '48) When do you expect to leave work? 퇴근은 언제 할 것 같아?',
    '49) When was the last time you saw a movie? 영화를 마지막으로 본 게 언제죠?',
    '50) Which one do you want? 넌 어떤 걸 원해?']


@command()
def generate_dummy():
    server_url = prompt('Enter the server address where you want to add the ' \
                        'dummy data.', type=str,
                        default='http://127.0.0.1:5000')
    for user in users:
        user_ids.append(create_user(user))
    for index, team in enumerate(teams):
        team_ids.append(create_team(team, users[index]))

    for index, team in enumerate(teams):
        team_emails = team['emails']
        team_id = team_ids[index]
        for index, story in enumerate(stories):
            create_story(team_emails[index % len(team_emails)], team_id, story)



def create_team(new_team, owner_user_name):
    try:
        print('Create team "{}"'.format(new_team['name']))
        print(' - try signup {}'.format(owner_user_name))
        response = session.post('{}/users/signin'.format(server_url),
                                json={'email': '{}@email.com'.format(
                                    owner_user_name),
                                    'password': '123123'})
        if response.status_code is not 200:
            raise Exception('The status code is not 200 OK. but {}'.format(
                response.status_code))
        print(' - successfully signed up..')
        new_team_description = '{}_description'.format(new_team['name'])
        print(' - try create team "{}"'.format(new_team['name']))
        response = session.post('{}/teams/'.format(server_url),
                                json={'name': new_team['name'],
                                      'description': new_team_description,
                                      'userEmails': new_team['emails']})
        if response.status_code is not 200:
            raise Exception('The status code is not 200 OK. but {}'.format(
                response.status_code))
        response_text = json.loads(response.text)
        if response_text['success'] is not True:
            raise Exception(response_text['msg'])
        print(' Team "{}"(owner:{}) is created...'.format(new_team['name'],
                                                          owner_user_name))
        return response_text['data']['team_id']
    except Exception as e:
        print(' - ' + str(e))


def create_user(username):
    try:
        print('Create user "{}"'.format(username))
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
        print(' User "{}" is created...'.format(username))
        return response_text['data']['user_id']
    except Exception as e:
        print(' - ' + str(e))

def create_story(user_email, team_id, content):
    print('Create story "{}"'.format(content))
    print(' Story "{}" is created...'.format(content))
