def test_access_index_url_returning_200_status_code(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'The server is running!'

def test_acces_an_inexistent_url_returning_404_status_code(client):

    response = client.get('/invalid-request')
    assert response.status_code == 404
    assert response.json['status'] == 'error'
    assert response.json['message'] == 'not Found'


def test_to_access_a_protected_url_with_a_invalid_token_returning_422_status_code(client):
    """
    GIVEN a Flask application
    WHEN an protected URL is requested (GET) with an invalid authentication
    THEN check the response HTTP 200 response
    """

    endpoint = '/books'
    response = client.get(endpoint, headers={'x-access-tokens': ' xxxxxxxxxxxxxxxxxxx'})
    assert response.status_code == 422
    assert response.json['message'] == 'JWT token is invalid'


def test_to_access_a_protected_url_returning_401_status_code(client):
    """
    GIVEN a Flask application
    WHEN an protected URL is requested (GET) missing an valid authentication
    THEN check the response HTTP 200 response
    """

    endpoint = '/books'
    response = client.get(endpoint)
    assert response.status_code == 401
    assert response.json['message'] == 'JWT token is required'