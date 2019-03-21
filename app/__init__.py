from flask import Flask
from flask_misaka import Misaka
from config import Config

# Initialize Flask
app = Flask(__name__)

# Load Configuration from Config.py's class "Config"
app.config.from_object(Config)

# Initalize of Flask misaka
md = Misaka(app)

# Load routes
from app import routes
