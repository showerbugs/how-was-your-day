from flask import Blueprint
from flask import jsonify
from flask import request
from flask import g
from flask_login import current_user
from flask_login import login_required

from db.models import Project


app = Blueprint('projects', __name__)


@app.route('/', methods=['GET'])
@login_required
def list_projects():
    projects = current_user.projects
    projects = [project.to_dict() for project in projects]
    return jsonify(success=True, data={'projects': projects})


@app.route('/<int:project_id>', methods=['GET'])
@login_required
def get_project(id):
    project = current_user.projects.filter(Project.id == id).first()
    return jsonify(success=True, data={'project': project})


@app.route('/', methods=['POST'])
@login_required
def create_project():
    params = request.json
    name = params['name']
    new_project = Project(name=name)
    new_project.users.append(current_user)
    g.db.add(new_project)
    return jsonify(success=True)
