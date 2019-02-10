from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

# Initialize Flask
app = Flask(__name__)

# Load Configuration from Config.py's class "Config"
app.config.from_object(Config)

# Initalize of SQLAlchemy
db = SQLAlchemy(app)

# The session is used for none type objekt transferring (add user, static Users)
# Also for other methods, where an modified session is usefull/ needed
engine = create_engine('sqlite:///app/static/database/VKS_main.sqlite',
 convert_unicode=True or os.path.join(basedir, "VKS_Fallback.sqlite"))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# Load routes
from app import models, routes
