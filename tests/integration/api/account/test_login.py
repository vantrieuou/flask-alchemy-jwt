import jwt
from flask import json
from tests.util import create_user, get_unique_email


def test_auth_login_with_correct_credentials_passed_returning_200_status_code(client):
    """
        GIVEN a Flask application
        WHEN the '/account/reset-password' URL is requested (POST)
        THEN check the response is valid and the tokens creations
        """

    data = {'email': 'test@mail.com', 'password': 'test'}
    response = client.post('/account/reset-password',
                           data=json.dumps(data),
                           content_type='application/json')

    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data']['token']
    assert response.json['data']['message'] == 'Login successfully'
