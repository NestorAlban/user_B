from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_valid_id():
    # True=="true"
    response = client.get("/user/3")
    assert response.status_code == 200
    assert response.json() == [{"idper": 3, "name": "fa", "mail": "fa@example.com", "active": True}]
