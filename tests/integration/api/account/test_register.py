from flask import json
from tests.util import create_user, get_unique_email


def test_auth_register_with_data_well_formatted_returning_200_status_code(client):
    """
    GIVEN a Flask application
    WHEN the '/account/register' URL is requested (POST)
    THEN check the response is valid
    """

    data = {'email': get_unique_email(), 'password': "123"}
    response = client.post('/account/register',
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data']['email'] == data['email']


def test_auth_register_with_data_empty_email_returning_400_status_code(client):
    data = {'email': '', 'password': "123"}
    response = client.post('/account/register',
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 400
    assert response.json['status'] == 'error'
    assert response.json['message'] == 'Email is required'

def test_auth_register_with_data_empty_password_returning_400_status_code(client):
    data = {'email': 'a@email.com', 'password': ""}
    response = client.post('/account/register',
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 400
    assert response.json['status'] == 'error'
    assert response.json['message'] == 'Password is required'
