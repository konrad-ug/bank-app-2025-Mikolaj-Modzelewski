import pytest
from app.api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestApiDB:
    def test_save_and_load_accounts(self, client):
        client.delete("/api/accounts/99999999999")

        client.post("/api/accounts", json={
            "name": "Test",
            "surname": "Persistance",
            "pesel": "99999999999"
        })

        response = client.post("/api/accounts/save")
        assert response.status_code == 200

        client.delete("/api/accounts/99999999999")

        response = client.post("/api/accounts/load")
        assert response.status_code == 200

        response = client.get("/api/accounts/99999999999")
        assert response.status_code == 200

        data = response.get_json()
        assert data["name"] == "Test"
        assert data["surname"] == "Persistance"
        assert float(data["balance"]) == 0.0

        client.delete("/api/accounts/99999999999")