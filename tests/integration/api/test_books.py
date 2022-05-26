import jwt
from flask import json
from tests.util import create_user, get_unique_email, get_jwt_token


def test_ebook_list_with_correct_credentials_passed_returning_200_status_code(client, db_session):
    """
        GIVEN a Flask application
        WHEN the '/books' URL is requested (GET)
        THEN check the response is giving books
        """
    from flaskr.model.user import User
    endpoint = '/books'
    user = db_session.query(User).filter_by(id=1).first()
    response = client.get(endpoint, headers={'x-access-tokens': get_jwt_token(user)})
    assert response.json['data']['list_of_books'][0]['name'] == 'Book1'
