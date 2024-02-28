import pytest
from client import RequestClient

def test_client_succes():
    client = RequestClient()
    response = client.chuck()
    assert response.status_code == 200

def test_client_raises_correctly():
    client = RequestClient()
    with pytest.raises(AttributeError):
        client._request(method='Monkey', path='https://google.com')