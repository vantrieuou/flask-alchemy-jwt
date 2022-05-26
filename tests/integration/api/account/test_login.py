from flask import json


def test_auth_login_with_correct_credentials_passed_returning_200_status_code(client):
    """
        GIVEN a Flask application
        WHEN the '/account/login' URL is requested (POST)
        THEN check the response is valid and the tokens creations
        """

    data = {'email': 'test@mail.com', 'password': 'test'}
    response = client.post('/account/login',
                           data=json.dumps(data),
                           content_type='application/json')

    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data']['token']
    assert response.json['data']['message'] == 'Login successfully'
