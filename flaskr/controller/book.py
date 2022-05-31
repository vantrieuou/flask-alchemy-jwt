"""Blueprint to organize and group, views related
to the '/books' endpoint of HTTP REST API.
"""

from flask import (
    Blueprint, Response, make_response, jsonify
)
from flaskr.authentication import token_required
from flaskr.database import db_session
from flaskr.model.user import User
from sqlalchemy.orm import joinedload
bp = Blueprint('book', __name__, url_prefix='/books')

@bp.route('', methods=['GET'])
@token_required
def ebook_list(current_user) -> Response:
    # Use Joined Eager Loading to save number of query statements
    users = db_session.query(User).options(joinedload(User.books, innerjoin=True)).all()
    output = []
    for user in users:
        for book in user.books:
            output.append({
                'id': book.id,
                'name': book.name,
                'author': book.author,
                'publisher': book.publisher,
                'user_email': user.email
            })

    return make_response(jsonify({
        'status': 'success',
        'data': {
            'list_of_books': output
        }
    }))
