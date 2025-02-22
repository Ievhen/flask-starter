import os


class Config(object):
    TESTING = False
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProductionConfig(Config):
    ...


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
