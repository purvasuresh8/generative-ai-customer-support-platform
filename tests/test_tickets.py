from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_ticket():

    payload = {
        "id": 1,
        "customer_name": "John",
        "issue": "Login problem",
        "status": "open"
    }

    response = client.post(
        "/tickets",
        json=payload
    )

    assert response.status_code == 200
  
