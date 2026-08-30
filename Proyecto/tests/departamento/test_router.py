from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session


client = TestClient(app)


def test_read_departamentos(session: Session) -> None:
    response = client.get("/departamentos")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_create_departamento(session: Session) -> None:
    nuevo_departamento = {
        "nombre": "Departamento de Informatica"
    }
    response = client.post("/departamentos/", json=nuevo_departamento)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["nombre"] == "Departamento de Informatica"
    assert "id" in data