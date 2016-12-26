import os
import sys

from flask import Flask
from flask import g
from flask_login.login_manager import LoginManager

from config import flask_config
from db.session import Session
from db.models import User
from users.views import app as users_app
from teams.views import app as projects_app


def create_app():
    app = Flask(__name__)
    app.config.from_object(flask_config)
    app.secret_key = os.urandom(24)

    app.register_blueprint(users_app, url_prefix='/users')
    app.register_blueprint(projects_app, url_prefix='/teams')

    login_manager = LoginManager()
    login_manager.init_app(app)

    def flask_login_user_loader(user_id):
        return g.db.query(User).filter(User.id == user_id).first()
    login_manager.user_loader(flask_login_user_loader)

    return app


app = create_app()


@app.before_request
def before_request():
    g.db = Session()


@app.teardown_request
def teardown_request(e):
    db = getattr(g, 'db', None)
    if db is not None:
        if not e or not hasattr(sys, '_called_from_test'):
            # there's no exception, or not executed by pytest
            db.commit()
        else:
            db.rollback()
        db.close()


if __name__ == '__main__':
    app.run()
