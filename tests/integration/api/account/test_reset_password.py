from flask import json
from tests.util import create_user, get_unique_email


def test_auth_correct_reset_password_returning_200_status_code(client):
    """
        GIVEN a Flask application
        WHEN the '/account/reset-password' URL is requested (POST)
        THEN check the response is valid and the tokens creations
        """

    data = {
        'email': 'resetting_user@mail.com',
        'current_password': 'test',
        'new_password': '123',
        'confirm_password': '123'
    }
    response = client.post('/account/reset-password',
                           data=json.dumps(data),
                           content_type='application/json')

    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data']['message'] == 'Reset password successfully.'


