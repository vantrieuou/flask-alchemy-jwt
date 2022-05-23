"""Blueprint to organize and group, views related
to the '/auth' endpoint of HTTP REST API.
"""

from flask import (
    current_app, abort, Blueprint, request, Response, make_response, jsonify
)
from flaskr.exceptions import TokenNotFound


bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/register', methods=('GET',))
def register() -> Response:
    return make_response(jsonify({
        'status': 'success',
        'data': {
            'account': 'trieubui'
        }
    }))
