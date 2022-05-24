"""Blueprint to organize and group, views related
to the '/auth' endpoint of HTTP REST API.
"""

from flask import (
    current_app, abort, Blueprint, request, Response, make_response, jsonify
)
import flaskr.exceptions
from flaskr.authentication import token_required

bp = Blueprint('book', __name__, url_prefix='/books')

@bp.route('', methods=('GET',))
@token_required
def list(current_user) -> Response:
    return make_response(jsonify({
        'status': 'success',
        'data': {
            'account': 'trieubui'
        }
    }))
