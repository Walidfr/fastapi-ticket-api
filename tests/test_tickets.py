"""
Unit tests for FastAPI Ticket API endpoints.
Each test uses TestClient to simulate HTTP requests.
"""

import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_ticket():
    """
    Test ticket creation endpoint.
    Asserts status 201 and correct response fields.
    """
    response = client.post("/tickets/", json={"title": "Test", "description": "Desc"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test"
    assert data["status"] == "open"


def test_list_tickets():
    """
    Test listing all tickets endpoint.
    Asserts status 200 and response is a list.
    """
    client.post("/tickets/", json={"title": "A", "description": "B"})
    response = client.get("/tickets/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_ticket():
    """
    Test retrieving a ticket by UUID.
    Asserts status 200 and correct id in response.
    """
    post = client.post("/tickets/", json={"title": "X", "description": "Y"})
    tid = post.json()["id"]
    response = client.get(f"/tickets/{tid}")
    assert response.status_code == 200
    assert response.json()["id"] == tid


def test_update_ticket():
    """
    Test updating a ticket by UUID.
    Asserts status 200 and updated title in response.
    """
    post = client.post("/tickets/", json={"title": "Old", "description": "Old"})
    tid = post.json()["id"]
    response = client.put(f"/tickets/{tid}", json={"title": "New"})
    assert response.status_code == 200
    assert response.json()["title"] == "New"


def test_close_ticket():
    """
    Test closing a ticket by UUID.
    Asserts status 200 and status is 'closed'.
    """
    post = client.post("/tickets/", json={"title": "ToClose", "description": "D"})
    tid = post.json()["id"]
    response = client.patch(f"/tickets/{tid}/close")
    assert response.status_code == 200
    assert response.json()["status"] == "closed"


def test_ticket_not_found():
    """
    Test not found cases for get, put, patch endpoints.
    Asserts status 404 for all.
    """
    fake_id = str(uuid.uuid4())
    response = client.get(f"/tickets/{fake_id}")
    assert response.status_code == 404
    response = client.put(f"/tickets/{fake_id}", json={"title": "X"})
    assert response.status_code == 404
    response = client.patch(f"/tickets/{fake_id}/close")
    assert response.status_code == 404
