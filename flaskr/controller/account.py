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
from flaskr.exceptions import InvalidFormInput

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
