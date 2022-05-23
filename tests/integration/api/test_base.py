def test_access_index_url_returning_200_status_code(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'The server is runing!'

def test_acces_an_inexistent_url_returning_404_status_code(client):

    response = client.get('/invalid-request')
    assert response.status_code == 404
    assert response.json['status'] == 'error'
    assert response.json['message'] == 'not Found'