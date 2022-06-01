import os
import pytest
import dotenv

from flaskr import create_app
import uuid

def init_db() -> None:
    """Import all modules here that might define models so that
    they will be registered properly on the metadata.
    """

    import flaskr.model # Don't remove this line, it is used implicitly
    from flaskr.database import Base, engine
    Base.metadata.create_all(bind=engine)


def drop_db() -> None:
    """Remove all table from database."""

    from flaskr.database import Base, engine
    Base.metadata.drop_all(bind=engine)


def create_test_user() -> None:
    """Creates test user."""

    from flaskr.model import User, Book, Employee, Engineer, Manager
    from werkzeug.security import generate_password_hash
    from flaskr.database import db_session

    user = db_session.query(User).filter_by(email='test@mail.com').first()

    if not user:
        user = User(public_id=str(uuid.uuid4()), email='test@mail.com', password=generate_password_hash('test'))
        resetting_user = User(public_id=str(uuid.uuid4()), email='resetting_user@mail.com', password=generate_password_hash('test'))
        db_session.add(user)
        db_session.add(resetting_user)
        book = Book(user_id=1, name="Book1", author='author1', publisher='publisher', book_prize=1000)
        db_session.add(book)
        db_session.add(Manager(manager_name="Manager .1 Jonh", apartment="Manager", salary=4000))
        db_session.add(Manager(manager_name="Manager .1 Jonh", apartment="Manager", salary=3000))
        db_session.add(Engineer(engineer_name="Engineer .1 Comic", apartment="Engineer", salary=3000))

        db_session.commit()

@pytest.fixture
def app(request):
    """ Create an application instance from given settings.

    Parameters:
        request (FixtureRequest): A request for a fixture from a test or fixture function

    Returns:
        flask.app.Flask: The application instance
    """

    # loading the .env to environment
    dotenv.load_dotenv()

    # app instance
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL'),
        'SECRET_KEY': 'testing',
        'JWT_SECRET_KEY': 'testing',
        'DATABASE_LOGGING': bool(os.environ.get('DATABASE_LOGGING', True)),
    })

    # add to the scope
    ctx = app.app_context()
    ctx.push()

    def teardown():
        drop_db()
        init_db()
        ctx.pop()

    init_db()
    create_test_user()

    request.addfinalizer(teardown)
    return app

@pytest.fixture(scope='function')
def client(app):
    """Create a client with app.test_client() using app fixture.
    Tests will use the client to make requests to the application

    Parameters:
        app (flask.app.Flask): The application instance.

    Returns:
        FlaskClient: A client to allow make requests to the application.
    """

    return app.test_client()

@pytest.fixture(scope='function')
def db_session(app, request):
    """Creates a new database session for a test.

    Parameters:
        app (flask.app.Flask): The application instance.
        request (FixtureRequest): A request for a fixture from a test or fixture function

    Returns:
        db_session: a SLQAlchmey Session object.
    """

    from flaskr.database import db_session

    def teardown():
        db_session.remove()

    request.addfinalizer(teardown)
    return db_session