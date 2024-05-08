from flask import Flask
from config import Config
from .db import init_app
from .routes import routing


app = Flask(__name__)
app.config.from_object(Config)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_app(app)
    app.register_blueprint(routing)

    return app


