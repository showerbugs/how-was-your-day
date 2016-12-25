from flask import Blueprint
from flask import request
from flask import jsonify
from flask import g
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from db.models import User

app = Blueprint('users', __name__)


@app.route('/signin', methods=['POST'])
def signin():
    params = request.json
    email = params['email']
    password = params['password']

    user = g.db.query(User)\
        .filter(User.email == email,
                User.password == password)\
        .first()
    if not user:
        return jsonify(success=False, msg='No such user')

    login_user(user)
    return jsonify(success=True)


@app.route('/signout', methods=['DELETE'])
@login_required
def signout():
    logout_user()
    return jsonify(success=True)


@app.route('/', methods=['POST'])
def create_user():
    params = request.json
    email = params['email']
    name = params['name']
    password = params['password']
    password_repeat = params['password_repeat']
    if password != password_repeat:
        return jsonify(success=False, msg='Repeat same password')

    new_user = User(email=email, name=name, password=password)
    g.db.add(new_user)
    return jsonify(success=True)
