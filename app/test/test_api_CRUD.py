import pytest
from app.api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestApiCRUD:
    def test_create_account(self, client):
        response = client.post("/api/accounts", json={
            "name": "John",
            "surname": "Doe",
            "pesel": "01234567890",
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["message"] == "Account created"
        response = client.post("/api/accounts", json={
            "name": "John",
            "surname": "Doe",
            "pesel": "01234567890",
        })
        assert response.status_code == 409
        data = response.get_json()
        assert data["message"] == "Account with this PESEL already exists"

    def test_get_all_accounts(self, client):
        response = client.get("/api/accounts")
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert any(acc["pesel"] == "01234567890" for acc in data)

    def test_get_account_count(self, client):
        response = client.get("/api/accounts/count")
        assert response.status_code == 200
        data = response.get_json()
        assert data["count"] == 1

    def test_get_account_by_pesel(self, client):
        client.post("/api/accounts", json={
            "name": "John",
            "surname": "Doe",
            "pesel": "01234567891",
        })
        response = client.get("/api/accounts/01234567891")
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "John"
        assert data["surname"] == "Doe"
        assert data["balance"] == 0
        response = client.get("/api/accounts/11111111111")
        assert response.status_code == 404
        data = response.get_json()
        assert data["message"] == "Account not found"
    
    def test_update_account(self, client):
        response = client.patch("/api/accounts/01234567890", json={
        "first_name": "Jane",
        "last_name": "Xia"
        })
        assert response.status_code == 200
        data = response.get_json()
        assert data["message"] == "Account updated"
        response = client.patch("/api/accounts/00000000000", json={
        "first_name": "Jane",
        "last_name": "Xia"
        })
        assert response.status_code == 404
        data = response.get_json()
        assert data["message"] == "Account not found"
        
    def test_delete_account(self, client):
        response = client.delete("/api/accounts/01234567890")
        assert response.status_code == 200
        data = response.get_json()
        assert data["message"] == "Account deleted"
        response = client.delete("/api/accounts/00000000000")
        assert response.status_code == 404
        data = response.get_json()
        assert data["message"] == "Account not found"

