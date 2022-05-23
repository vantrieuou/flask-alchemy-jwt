"""This package is Flask HTTP REST API template that already has the database bootstrap
implemented all feature.

This module contains the factory function 'create_app' that is
responsible for initializing the application according
to given configuration.
"""


import os
from flask import Flask

def create_app(test_config: dict = {}) -> Flask:
    """This function is responsible to create a Flask instance according
    a previous setting passed from environment. In that process, it also
    initialise the database source.

    Parameters:
        test_config (dict): settings coming from test environment

    Returns:
        flask.app.Flask: The application instance
    """

    app = Flask(__name__, instance_relative_config=True)

    load_config(app, test_config)

    init_instance_folder(app)
    init_database(app)
    init_controllers(app)
    init_commands(app)
    return app


def load_config(app: Flask, test_config) -> None:
    """Load the application's config

    Parameters:
        app (flask.app.Flask): The application instance Flask that'll be running
        test_config (dict):
    """

    if os.environ.get('FLASK_ENV') == 'development' or test_config.get("FLASK_ENV") == 'development':
        app.config.from_object('flaskr.config.Development')

    elif test_config.get('TESTING'):
        app.config.from_mapping(test_config)

    else:
        app.config.from_object('flaskr.config.Production')


def init_instance_folder(app: Flask) -> None:
    """Ensure the instance folder exists.

    """

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def init_database(app: Flask) -> None:
    from .database import init
    init(app)


def init_controllers(app: Flask) -> None:
    """Registers the error handler and controllers of the application.

    Parameters:
        app (flask.app.Flask): The application instance Flask that'll be running
    """

    # error handlers
    from .errorhandler import register_handler
    register_handler(app)

    # register controller
    from .controller import account
    from .controller import index
    app.register_blueprint(account.bp)
    app.register_blueprint(index.bp)

def init_commands(app: Flask) -> None:
    from flaskr.commands import register_commands
    register_commands(app)
