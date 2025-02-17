from flask import Flask

from .config import Config
from .routes import route_blueprint


def create_app(config_cls=Config):
    app = Flask(__name__)
    app.config.from_object(config_cls)

    configure_blueprints(app)

    return app


def configure_blueprints(app):
    app.register_blueprint(route_blueprint)
