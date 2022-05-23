import click
from flask.cli import with_appcontext
from flask import Flask
from .database import Base, engine
# Don't remove below line. Even models aren't included in any block code, the models still are called implicitly.
import flaskr.model

def register_commands(app: Flask):
    app.cli.add_command(init_db_command)

@click.command('init-db')
@with_appcontext
def init_db_command():
    Base.metadata.create_all(bind=engine)
    click.echo('Initialized the database.')
