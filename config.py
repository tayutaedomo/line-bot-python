import os

APP_SECRET_KEY = os.getenv('APP_SECRET_KEY', 'this-really-needs-to-be-changed')


class Config(object):
    # ENV = 'production'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = APP_SECRET_KEY


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    ENV = 'staging'
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True

