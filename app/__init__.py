from flask import Flask

from .routes import route_blueprint


def create_app():
    app = Flask(__name__)

    configure_blueprints(app)

    return app


def configure_blueprints(app):
    app.register_blueprint(route_blueprint)
