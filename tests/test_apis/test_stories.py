import json

from db.models import Story

class TestStory:
    def test_register_story(self, flask_client, session, team_hou, logined_user_hou):
        # Given story 내용을가지고
        content = "김소여니는 귀엽당, 왜냐면 귀엽기 때문이다."
        data = json.dumps({'content': content})

        # When POST /teams/1
        resp = flask_client.post('/teams/{}/stories'.format(team_hou.id),
                                 data=data,
                                 content_type='application/json')
        # Then 잘들어가있다
        assert resp.status_code == 200
        updated_story = session.query(Story) \
            .filter(Story.content == content).first()
        assert updated_story
