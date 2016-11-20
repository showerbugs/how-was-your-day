from flask import Blueprint
from flask import jsonify

app = Blueprint('users', __name__)


@app.route('/signin', methods=['POST'])
def signin():
    return jsonify(result={'success': True})
