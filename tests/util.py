import time
from werkzeug.security import generate_password_hash
from sqlalchemy import desc
from flaskr.model.user import User
from datetime import datetime, timedelta
import jwt
from flask import current_app

def get_unique_email():
    return f"email{get_unique_id()}@mail.com"


def get_unique_id():
    unique = hash(time.time())
    return unique


def create_user(session):
    """Creates new user.

    Parameters:
        session: a SLQAlchmey Session object.

    Returns:
        user: A user model object.
    """

    from flaskr.model.user import User

    user = User()
    user.username = get_unique_email()
    user.password = generate_password_hash("123")

    session.add(user)
    session.commit()

    return user

def get_users_count(session):
    """Counts the amount of user contained in the database.

    Parameters:
        session: a SLQAlchmey Session object.

    Returns:
        An int value corresponding to the amount of registered user.
    """

    from flaskr.model.user import User
    return session.query(User).order_by(desc(User.id)).count()


def get_jwt_token(user: User):
    token = jwt.encode(
        {
            'public_id': user.public_id,
            'created_date': str(user.created_date),
            'exp': datetime.utcnow() + timedelta(days=60)
        },
        current_app.config['SECRET_KEY'],
        "HS256"
    )
    return token