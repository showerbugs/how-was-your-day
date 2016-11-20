from flask import Flask
from flask import send_from_directory

from config import flask_config
from users.views import app as users_app


def create_app():
    app = Flask(__name__)
    app.config.from_object(flask_config)
    app.register_blueprint(users_app, url_prefix='/users')
    return app


app = create_app()


@app.route('/', methods=['GET'])
def hello_world():
    return send_from_directory('client', 'index.html')

if __name__ == '__main__':
    app.run()
