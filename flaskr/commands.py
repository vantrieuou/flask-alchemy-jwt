import click
from flask.cli import with_appcontext
from .database import Base, engine
import flaskr.model

def register_commands(app):
    """Add commands to the line command input.

    Parameters:
        app (flask.app.Flask): The application instance.
    """

    app.cli.add_command(init_db_command)

@click.command('init-db')
@with_appcontext
def init_db_command():
    Base.metadata.create_all(bind=engine)
    click.echo('Initialized the database.')
