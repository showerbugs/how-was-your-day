from flask import Blueprint
from flask import request
from flask import jsonify
from flask import g
from db.models import User

app = Blueprint('users', __name__)


@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    g.db.add(User(email, password, name))
    return jsonify(result={'success': True})
