import os

# Config for basedir
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # setup of basedir
    BASEDIR  = basedir

    # Run setting
    DEBUG = True
    PORT = 5000
