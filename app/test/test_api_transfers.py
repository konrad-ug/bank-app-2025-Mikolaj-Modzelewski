import pytest
from app.api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def test_account(client):
    from app.api import registry
    registry.accounts = []
    response = client.post("/api/accounts", json={
            "name": "John",
            "surname": "Doe",
            "pesel": "01234567890",
        })
    assert response.status_code == 201
    registry.accounts[0].balance = 100
    return "01234567890"

@pytest.mark.parametrize(
    "transfer_type, amount, target, status, message",
    [
        # incoming
        ("incoming", -1, "valid", 400, "Bad request"),
        ("incoming", 1, "valid", 200, "Transfer succesfull"),
        ("incoming", 1, "invalid", 404, "Account not found"),

        # outgoing
        ("outgoing", -1, "valid", 400, "Bad request"),
        ("outgoing", 101, "valid", 422, "Insufficient funds"),
        ("outgoing", 1, "valid", 200, "Transfer succesfull"),
        ("outgoing", 1, "invalid", 404, "Account not found"),

        # express
        ("express", -1, "valid", 400, "Bad request"),
        ("express", 101, "valid", 422, "Insufficient funds"),
        ("express", 1, "valid", 200, "Transfer succesfull"),
        ("express", 1, "invalid", 404, "Account not found"),

        # bad type
        ("lorem", 1, "valid", 400, "Bad request")
    ]
)

class TestApiTransfers:
    def test_transfers(self, client, test_account, transfer_type, amount, target, status, message):
        target_pesel = test_account if target == "valid" else "00000000000"

        response = client.patch(f"/api/accounts/{target_pesel}/transfer", json={
            "amount": amount,
            "type": transfer_type,
        })

        assert response.status_code == status
        assert response.get_json()["message"] == message
