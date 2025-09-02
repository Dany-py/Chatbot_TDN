from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_socket():
    with client.websocket_connect("/api/ws/chat") as websocket:
        # Envoie un message JSON comme attendu par le serveur
        websocket.send_json({"message": "salut"})
        # Reçoit la réponse
        data = websocket.receive_json()
        assert "text" in data
        print(data["text"])