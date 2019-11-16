import os
import jinja2
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate

from flask import Flask

db = SQLAlchemy()
moment = Moment()
migrate = Migrate()


def create_fyyur_app():
    """Sets up the application configuations and 
    returns an instance of the fyyur app
    """

    current_file_path = Path(__file__)

    templates_dir = current_file_path.parent.parent/'templates'
    static_dir = current_file_path.parent.parent/'static'

    fyyur_app = Flask(__name__, template_folder=templates_dir,
                      static_folder=static_dir)

    fyyur_app.config.from_pyfile('config.py')


    migrate.init_app(fyyur_app, db)

    db.init_app(fyyur_app)

    moment.init_app(fyyur_app)

    return fyyur_app
