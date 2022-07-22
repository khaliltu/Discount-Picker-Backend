import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MONGO_URI = os.environ['DATABASE_URL']
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = 2525
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
