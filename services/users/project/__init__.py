# services/users/project/__init__.py
import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db = SQLAlchemy(app)

def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # set up extensions
    db.init_app(app)
    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app