import json

from db.models import Team


class TestUser:
    def test_create_team(self, flask_client, session, logined_user_hou):
        # Given
        new_team_name = 'new_team'
        data = json.dumps({'name': new_team_name})
        # When
        flask_client.post('/teams/', data=data,
                          content_type='application/json',
                          follow_redirects=True)
        # Then 새로운 team이 정상적으로 db에 들어가 있다.
        created_team = session.query(Team) \
            .filter(Team.name == new_team_name).first()
        assert created_team.name == new_team_name

    def test_get_team_list(self, flask_client, session, logined_user_hou):
        # Given 팀을 만들고
        team = Team(name='new_team')
        team.users.append(logined_user_hou)
        session.add(team)

        # When teams를 호출하면
        resp = flask_client.get('/teams/', content_type='application/json',
                                follow_redirects=True)
        result = json.loads(resp.data.decode())

        # Then 잘들어가있다
        assert resp.status_code == 200
        assert result['success']
        assert len(result['data']['teams']) == 1
        assert result['data']['teams'][0]['name'] == team.name

    def test_get_team(self, flask_client, session, logined_user_hou):
        # Given 팀을 만들고 id를 준비한다.
        team_name = 'new_team'
        team = Team(name=team_name)
        team.users.append(logined_user_hou)
        session.add(team)
        new_team = session.query(Team) \
            .filter(Team.name == team_name).first()
        team_id = new_team.id

        # When 팀 id를 path에 추가하여 정보를 요청하면
        resp = flask_client.get('/teams/{}'.format(team_id),
                                content_type='application/json',
                                follow_redirects=True)

        # Then 잘돌려준다
        result = json.loads(resp.data.decode())
        assert resp.status_code == 200
        assert result['success']
        assert result['data']['team']['name'] == team_name
