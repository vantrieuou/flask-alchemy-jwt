"""Blueprint to organize and group, views related
to the '/books' endpoint of HTTP REST API.
"""

from flask import (
    Blueprint, Response, make_response, jsonify
)
from flaskr.authentication import token_required
from flaskr.database import db_session
from flaskr.model import Employee, Engineer
from sqlalchemy.orm import joinedload
bp = Blueprint('employee', __name__, url_prefix='/employees')


@bp.route('', methods=['GET'])
@token_required
def employee_list(current_user) -> Response:
    # Use Joined Eager Loading to save number of query statements
    users = db_session.query(Engineer).filter_by(salary=3000).all()
    output = []
    for user in users:
        output.append({
            'salary': user.salary
        })

    return make_response(jsonify({
        'status': 'success',
        'data': {
            'list_of_books': output
        }
    }))
