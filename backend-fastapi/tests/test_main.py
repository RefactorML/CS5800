from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root_success():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Welcome to JobQuest FastAPI Backend!"}

def test_divide_normal_case():
    r = client.get("/api/divide", params={"a": 10, "b": 2})
    assert r.status_code == 200
    assert r.json() == {"result": 5.0}

def test_divide_by_zero_returns_400():
    r = client.get("/api/divide", params={"a": 10, "b": 0})
    assert r.status_code == 400
    assert r.json()["detail"] == "Division by zero is undefined."
