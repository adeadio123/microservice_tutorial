from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

# Test for the FastAPI application
# This file tests the root endpoint of the FastAPI application
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "A simple FastAPI app with wiki function, "
        "call /search/{value} or /search/{name} to search Wikipedia"
    }
