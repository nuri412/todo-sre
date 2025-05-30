import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_get_concerts(client):
    response = client.get('/concerts')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_buy_ticket_success(client):
    response = client.post('/buy', json={'concert_id': 1, 'quantity': 1})
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Tickets purchased successfully'

def test_buy_ticket_not_found(client):
    response = client.post('/buy', json={'concert_id': 999, 'quantity': 1})
    assert response.status_code == 404
    assert 'error' in response.get_json()

def test_buy_ticket_not_enough(client):
    response = client.post('/buy', json={'concert_id': 1, 'quantity': 999})
    assert response.status_code == 400
    assert 'error' in response.get_json()
