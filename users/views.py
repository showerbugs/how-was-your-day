from flask import Blueprint
from flask import g
from flask import jsonify
from flask import request
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from db.models import User

app = Blueprint('users', __name__)


@app.route('/signin', methods=['POST'])
def signin():
    params = request.json
    email = params['email']
    password = params['password']

    user = g.db.query(User) \
        .filter(User.email == email,
                User.password == password) \
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


@app.route('', methods=['POST'])
def create_user():
    params = request.json
    email = params['email']
    name = params['name']
    password = params['password']
    password_repeat = params['passwordRepeat']
    if password != password_repeat:
        return jsonify(
            success=False,
            error={'code': 123, 'message':'Repeat same password'}
        )

    new_user = User(email=email, name=name, password=password)
    g.db.add(new_user)
    g.db.flush()
    g.db.refresh(new_user)
    return jsonify(success=True, data={'user_id': new_user.id})
