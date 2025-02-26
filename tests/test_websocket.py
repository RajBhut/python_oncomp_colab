import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_websocket_connection():
    response = client.websocket_connect("/ws/testroom")
    assert response is not None
    response.close()

def test_websocket_broadcast():
    client1 = client.websocket_connect("/ws/testroom")
    client2 = client.websocket_connect("/ws/testroom")

    client1.send_text('{"event": "code", "data": "Hello World"}')
    response = client2.receive_text()
    
    assert response == '{"event": "code", "room": "testroom", "data": "Hello World"}'

    client1.close()
    client2.close()