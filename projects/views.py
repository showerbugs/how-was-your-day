from flask import Blueprint
from flask import jsonify
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
def get_project(project_id):
    project = current_user.projects.filter(Project.id == project_id).first()
    return jsonify(success=True, data={'project': project})
