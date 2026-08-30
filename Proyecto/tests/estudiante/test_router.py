from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session


client = TestClient(app)


def test_read_estudiantes(session: Session) -> None:
    response = client.get("/estudiantes")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_create_estudiante(session: Session) -> None:
    nuevo_estudiante = {
        "nombre": "Lucia Gomez",
        "email": "lucia.gomez@gmail.com"
    }
    response = client.post("/estudiantes/", json=nuevo_estudiante)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["nombre"] == "Lucia Gomez"
    assert "id" in data