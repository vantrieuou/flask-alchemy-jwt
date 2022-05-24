import jwt
from functools import wraps
from flask import Flask, request, jsonify, make_response, current_app
from flaskr.model.user import User
from flaskr.database import db_session
from flaskr.exceptions import JwtTokenNotFound, JwtTokenInvalid

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            raise JwtTokenNotFound

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = db_session.query(User).filter_by(public_id=data['public_id']).first()
        except:
            raise JwtTokenInvalid

        return f(current_user, *args, **kwargs)

    return decorator