"""This module provides means to perform operations on the database
using the SQLAlchemy library."""


from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Base = None
engine = None
db_session = None


def init(app: Flask) -> None:
    """This function initialize the SQLAlchemy ORM, providing a session
    and command line to create the tables in the database.

    Parameters:    
        app (flask.app.Flask): The application instance.
    """

    global Base, engine, db_session
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))

    # The declarative extension in SQLAlchemy allows to define
    # tables and models in one go, that is in the same class
    Base = declarative_base()
    Base.query = db_session.query_property()

    # attach the shutdown_session function to be execute when a request ended.
    app.teardown_appcontext(shutdown_session)


def shutdown_session(exception=None) -> None:
    """Remove the db session if request is ended."""
    db_session.remove()
