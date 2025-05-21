import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
