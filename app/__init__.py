from flask import Flask

from .config import Config
from .routes import route_blueprint
from .extensions import db, migrate


def create_app(config_cls=Config):
    app = Flask(__name__)
    app.config.from_object(config_cls)

    configure_blueprints(app)
    configure_extensions(app)

    return app


def configure_blueprints(app):
    app.register_blueprint(route_blueprint)


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
