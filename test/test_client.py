import json
from fastapi.testclient import TestClient
import pytest
from app.main import app


client = TestClient(app)


def test_valid_id():
    # True=="true"
    response = client.get("/user/3")
    assert response.status_code == 200
    assert response.json() == [{"idper": 3, "name": "fa", "mail": "fa@example.com", "active": True}]


def test_create_userok():
    user = {"idper": 16, "name": "bo", "mail": "bo@example.com"}
    response = client.post("/registeruser_status", json.dumps(user))
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["mail"] == user["mail"]
    assert data["name"] == user["name"]
