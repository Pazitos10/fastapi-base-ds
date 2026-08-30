from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session


client = TestClient(app)


def test_read_clases(session: Session) -> None:
    response = client.get("/clases/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_create_clase(session: Session) -> None:
    nueva_clase = {
        "titulo": "Introduccion a la Programacion",
        "curso_id": 1
    }
    response = client.post("/clases/", json=nueva_clase)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["titulo"] == "Introduccion a la Programacion"
    assert "id" in data