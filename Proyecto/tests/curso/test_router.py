from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session


client = TestClient(app)


def test_read_cursos(session: Session) -> None:
    response = client.get("/cursos")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_create_curso(session: Session) -> None:
    nuevo_curso = {
        "nombre": "Matematica I",
        "descripcion": "Curso introductorio de matematica"
    }
    response = client.post("/cursos/", json=nuevo_curso)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["nombre"] == "Matematica I"
    assert "id" in data