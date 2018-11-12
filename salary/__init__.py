#! ../env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'daisutao'
__email__ = 'daisutao@163.com'
__version__ = '1.3'

from flask import Flask
from salary.controllers.main import main
from salary.models import db

from salary.extensions import (
    debug_toolbar,
    login_manager
)


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. salary.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # register our blueprints
    app.register_blueprint(main)

    return app
