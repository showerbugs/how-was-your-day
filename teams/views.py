from flask import Blueprint
from flask import jsonify
from flask import request
from flask import g
from flask_login import current_user
from flask_login import login_required

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
    return jsonify(success=True, data={'team': team.to_dict()})


@app.route('/', methods=['POST'])
@login_required
def create_team():
    params = request.json
    name = params['name']
    new_team = Team(name=name)
    new_team.users.append(current_user.unwrap)
    g.db.add(new_team)
    return jsonify(success=True)
