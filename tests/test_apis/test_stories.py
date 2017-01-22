import json

from db.models import Story


class TestStory:
    def test_create_story(self, flask_client, session, team_hou,
                          logined_user_hou):
        # Given story 내용을가지고
        content = "김소여니는 귀엽당, 왜냐면 귀엽기 때문이다."
        data = json.dumps({'content': content})

        # When POST /teams/1
        resp = flask_client.post('/teams/{}/stories'.format(team_hou.id),
                                 data=data,
                                 content_type='application/json')
        # Then 잘들어가있다
        assert resp.status_code == 200
        created_story = session.query(Story) \
            .filter(Story.content == content).first()
        assert created_story

    def test_get_stories(self, flask_client, session, team_hou, team_guni,
                         logined_user_hou):
        # Given Story를 hou팀에 2개, guni팀에 1개 만들고
        session.add(Story(user_id=logined_user_hou.id, team_id=team_hou.id,
                          content="story_hou_1"))
        session.add(Story(user_id=logined_user_hou.id, team_id=team_hou.id,
                          content="story_hou_2"))
        session.add(Story(user_id=logined_user_hou.id, team_id=team_guni.id,
                          content="story_guni_1"))

        # When GET /teams/1/stories 를 각각 날리면
        resp_hou = flask_client.get('/teams/{}'.format(team_hou.id),
                                content_type='application/json',
                                follow_redirects=True)
        resp_guni = flask_client.get('/teams/{}'.format(team_guni.id),
                                    content_type='application/json',
                                    follow_redirects=True)

        # Then 잘들어와잇다.
        result_hou = json.loads(resp_hou.data.decode())
        assert resp_hou.status_code == 200
        assert result_hou['success']
        assert result_hou['data']
        assert result_hou['data']['team']['stories']
        assert len(result_hou['data']['team']['stories']) == 2

        result_guni= json.loads(resp_guni.data.decode())
        assert resp_guni.status_code == 200
        assert result_guni['success']
        assert result_guni['data']
        assert result_guni['data']['team']['stories']
        assert len(result_guni['data']['team']['stories']) == 1