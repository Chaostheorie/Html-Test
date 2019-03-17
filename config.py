import os

# Config for basedir
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Run setting
    DEBUG = True
    PORT = 5000

    # Secret key for sessions of flask users
    # change it before using in anything that could be attacked
    SECRET_KEY = "not_secrEt53454325_SecrT_kEy_chaNGe_8t_bef4re_us8ng_in_pr0duc"

    # File-based SQLite3 database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app/static/database/VKS_main.sqlite") or \
        "sqlite:///" + os.path.join(basedir, "VKS_Fallback.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-User settings
    USER_APP_NAME = "Communicatio"
    USER_ENABLE_EMAIL = False
    USER_ENABLE_USERNAME = True
    USER_ENABLE_CHANGE_USERNAME = True
    USER_ENABLE_CHANGE_PASSWORD = True
    USER_ENABLE_REGISTER = True

    # Options for functions like login tracing etc.
    # Is Set with Bol Values (True/ False)
    TRACE_LOGIN = True

    # If you disable it the user with the name guest will deleted if it exists
    # If you enable before the first run nothing will happen
    GUEST_USER = False
