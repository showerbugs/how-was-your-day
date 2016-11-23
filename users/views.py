from flask import Blueprint
from flask import request
from flask import jsonify
from db.session import Session
from db.models import User

app = Blueprint('users', __name__)
session = Session()

@app.route('', methods=['POST'])
def signin():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    
    session.add(User(email, password, name))
    session.commit()
    return jsonify(result={'success': True})
