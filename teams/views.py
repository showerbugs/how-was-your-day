from flask import Blueprint
from flask import jsonify
from flask import request
from flask import g
from flask_login import current_user
from flask_login import login_required

from db.models import User
from db.models import Team


app = Blueprint('teams', __name__)


@app.route('/', methods=['GET'])
@login_required
def get_team_list():
    teams = current_user.teams
    teams = [team.to_json() for team in teams]
    return jsonify(success=True, data={'teams': teams})


@app.route('/<int:team_id>', methods=['GET'])
@login_required
def get_team(team_id):
    team = current_user.teams.filter(Team.id == team_id).first()
    if not team:
        error = {
            'code': 111,
            'message': 'No team with id {}'.format(team_id),
        }
        return jsonify(success=False, error=error), 404

    user_ids = [user.id for user in team.users]
    stories = team.stories

    team = team.to_json()
    team['userIds'] = user_ids

    def load_story_user(story):
        user = story.user
        story = story.to_json()
        story['user'] = user.to_json()
        return story
    team['stories'] = [load_story_user(story) for story in stories]

    return jsonify(success=True, data={'team': team})


@app.route('/', methods=['POST'])
@login_required
def create_team():
    params = request.json
    name = params['name']
    description = params['description']
    owner = current_user.unwrap_localproxy()
    new_team = Team(name=name, description=description, owner_id=owner.id)

    user_emails = params.get('userEmails')
    if user_emails:
        users = g.db.query(User)\
            .filter(User.email.in_(params['userEmails']))
        for user in users:
            new_team.users.append(user)

    g.db.add(new_team)
    return jsonify(success=True, data={})


@app.route('/<int:team_id>', methods=['PUT'])
@login_required
def update_team(team_id):
    params = request.json
    update_name = params['name']
    update_description = params['description']

    origin_team = g.db.query(Team)\
        .filter(Team.id == team_id).first()
    if not origin_team:
        error = {
            'code': 111,
            'message': 'No team with id {}'.format(team_id),
        }
        return jsonify(success=False, error=error), 404

    origin_team.name = update_name
    origin_team.description = update_description
    return jsonify(success=True, data={})
