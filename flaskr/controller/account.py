"""Blueprint to organize and group, views related
to the '/auth' endpoint of HTTP REST API.
"""

from flask import (
    current_app, abort, Blueprint, request, Response, make_response, jsonify
)
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from flaskr.model.user import User
from flaskr.database import db_session
from flaskr.exceptions import InvalidFormInput, JwtTokenInvalid
import jwt
from datetime import datetime, timedelta

bp = Blueprint('account', __name__, url_prefix='/account')

@bp.route('/register', methods=['POST'])
def register() -> Response:
    data = request.get_json()
    if not data.get('email'):
        raise InvalidFormInput('Email is required')
    if not data.get('password'):
        raise InvalidFormInput('Password is required')

    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), email=data['email'], password=hashed_password)
    db_session.add(new_user)
    db_session.commit()

    return make_response(jsonify({
        'status': 'success',
        'data': {
            'message': 'Registered successfully',
            'email': data['email']
        }
    }))

@bp.route('/login', methods=['POST'])
def login_user():
    auth = request.get_json()
    if not auth.get('email'):
        raise InvalidFormInput('Email is required')
    if not auth.get('password'):
        raise InvalidFormInput('Password is required')

    curr_user = db_session.query(User).filter_by(email=auth.get('email')).first()

    if not check_password_hash(curr_user.password, auth['password']):
        raise JwtTokenInvalid

    token = jwt.encode(
        {
            'public_id': curr_user.public_id,
            'created_date': str(curr_user.created_date),
            'exp': datetime.utcnow() + timedelta(days=60)
        },
        current_app.config['SECRET_KEY'],
        "HS256"
    )
    return make_response(jsonify({
        'status': 'success',
        'data': {
            'message': 'Login successfully',
            'token': token.decode("utf-8")
        }
    }))

@bp.route('/reset-password', methods=['POST'])
def reset_password():
    auth = request.get_json()
    if not auth.get('email'):
        raise InvalidFormInput('Email is required')
    if not auth.get('password'):
        raise InvalidFormInput('Password is required')

    curr_user = db_session.query(User).filter_by(email=auth.get('email')).first()

    if not check_password_hash(curr_user.password, auth['password']):
        raise JwtTokenInvalid

    token = jwt.encode(
        {
            'public_id': curr_user.public_id,
            'created_date': str(curr_user.created_date),
            'exp': datetime.utcnow() + timedelta(days=60)
        },
        current_app.config['SECRET_KEY'],
        "HS256"
    )
    return make_response(jsonify({
        'status': 'success',
        'data': {
            'message': 'Login successfully',
            'token': token.decode("utf-8")
        }
    }))