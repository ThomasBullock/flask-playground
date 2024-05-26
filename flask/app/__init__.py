from flask import Flask
from logging.config import dictConfig
from config import Config
from .mysql import DB
from .controllers.employee_controller import routing as employee_controller
# from .routes import routing

#current_app['DB_PASSWORD']
db = DB('root',
        'root',
        'db',
        'sql_hr'
        )

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



def create_app():
    """ Flask app factory function """
    app = Flask(__name__)
    app.config.from_object(Config)
    app.db = db  # Attach the db instance to the Flask app
    # init_app(app)
    app.register_blueprint(employee_controller)

    return app


