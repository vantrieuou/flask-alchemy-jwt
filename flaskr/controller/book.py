"""Blueprint to organize and group, views related
to the '/auth' endpoint of HTTP REST API.
"""

from flask import (
    current_app, abort, Blueprint, request, Response, make_response, jsonify
)
import flaskr.exceptions
from flaskr.authentication import token_required
from flaskr.database import db_session
from flaskr.model.user import User
# from flaskr.model.book import Book
from sqlalchemy.orm import joinedload
bp = Blueprint('book', __name__, url_prefix='/books')

@bp.route('', methods=['GET'])
@token_required
def ebook_list(current_user) -> Response:
    # Use Joined Eager Loading to save query statement
    users = db_session.query(User).options(joinedload(User.books, innerjoin=True)).all()
    output = []
    for u in users:
        for book in u.books:
            book_data = {}
            book_data['id'] = book.id
            book_data['name'] = book.name
            book_data['author'] = book.puthor
            book_data['publisher'] = book.publisher
            book_data['user_name'] = book.user.name
            output.append(book_data)

    return make_response(jsonify({
        'status': 'success',
        'data': {
            'list_of_books': output
        }
    }))
