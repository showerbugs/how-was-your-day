from flask import Flask
from flask import send_from_directory

from config import flask_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(flask_config)
    return app


app = create_app()


@app.route('/', methods=['GET'])
def hello_world():
    return send_from_directory('client', 'index.html')

if __name__ == '__main__':
    app.run()
