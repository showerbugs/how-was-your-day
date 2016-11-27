from flask import Flask
from flask import g
from flask import send_from_directory

from config import flask_config
from db.session import Session
from users.views import app as users_app


def create_app():
    app = Flask(__name__)
    app.config.from_object(flask_config)
    app.register_blueprint(users_app, url_prefix='/users')
    return app


app = create_app()


@app.before_request
def before_request():
    g.db = Session()


@app.teardown_request
def teardown_request(e):
    db = getattr(g, 'db', None)
    if db is not None:
        if not e:
            db.commit()
        else:
            db.rollback()
        db.close()


@app.route('/', methods=['GET'])
def hello_world():
    return send_from_directory('client', 'index.html')

if __name__ == '__main__':
    app.run()
