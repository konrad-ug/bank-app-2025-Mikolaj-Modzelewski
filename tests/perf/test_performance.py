import requests
import time

def test_perf_create_delete_account():
    base_url = "http://127.0.0.1:5000/api/accounts"
    
    for i in range(100):
        pesel = f"99999999{i:03d}"
        payload = {
            "name": "John",
            "surname": "Doe",
            "pesel": pesel
        }

        start = time.time()
        response_create = requests.post(base_url, json=payload, timeout=0.5)
        end = time.time()
        
        assert response_create.status_code == 201
        assert end - start < 0.5

        start = time.time()
        response_delete = requests.delete(f"{base_url}/{pesel}", timeout=0.5)
        end = time.time()
        
        assert response_delete.status_code == 200
        assert end - start < 0.5

def test_perf_incoming_transfers():
    base_url = "http://127.0.0.1:5000/api/accounts"
    pesel = "88888888888"
    
    payload = {
        "name": "John",
        "surname": "Doe",
        "pesel": pesel
    }
    requests.post(base_url, json=payload)

    transfer_url = f"{base_url}/{pesel}/transfer"
    transfer_payload = {"type": "incoming", "amount": 10}

    for _ in range(100):
        start = time.time()
        response = requests.patch(transfer_url, json=transfer_payload, timeout=0.5)
        end = time.time()

        assert response.status_code == 200
        assert end - start < 0.5

    response_get = requests.get(f"{base_url}/{pesel}")
    assert response_get.status_code == 200
    assert response_get.json()["balance"] == 1000

    requests.delete(f"{base_url}/{pesel}")