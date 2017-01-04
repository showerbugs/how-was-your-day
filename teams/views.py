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
def list_teams():
    teams = current_user.teams
    teams = [team.to_dict() for team in teams]
    return jsonify(success=True, data={'teams': teams})


@app.route('/<int:team_id>', methods=['GET'])
@login_required
def get_team(team_id):
    team = current_user.teams.filter(Team.id == team_id).first()
    team = team.to_dict()
    return jsonify(success=True, data={'team': team})


@app.route('/', methods=['POST'])
@login_required
def create_team():
    params = request.json
    name = params['name']
    description = params['description']
    users = g.db.query(User)\
        .filter(User.email.in_(params['userEmails']))
    owner = current_user.unwrap

    new_team = Team(name=name, description=description, owner_id=owner.id)
    for user in users:
        new_team.users.append(user)
    g.db.add(new_team)

    return jsonify(success=True, data={})
