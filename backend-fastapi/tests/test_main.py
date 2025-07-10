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
def test_user_crud_flow():
    r = client.post("/api/users", json={"name": "Alice", "email": "a@b.com"})
    assert r.status_code == 201
    user_id = r.json()["id"]

    r = client.post(f"/api/users/{user_id}/award", json={"points": 50, "badge": True})
    assert r.status_code == 200
    data = r.json()
    assert data["points"] == 50
    assert data["badges"] == 1
