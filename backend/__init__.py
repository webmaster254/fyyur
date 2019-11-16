import os
import jinja2
from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_fyyur_app():

    current_file_path = Path(__file__)

    templates_dir = current_file_path.parent.parent/'templates'
    static_dir = current_file_path.parent.parent/'static'

    fyyur_app = Flask(__name__, template_folder=templates_dir,
                static_folder=static_dir)

    fyyur_app.config.from_pyfile('config.py')

    return fyyur_app
