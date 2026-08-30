from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session


client = TestClient(app)


def test_read_inscripciones(session: Session) -> None:
    response = client.get("/inscripciones/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_create_inscripcion(session: Session) -> None:
    nueva_inscripcion = {
        "curso_id": 1,
        "estudiante_id": 1,
        "calificacion_final": 9.5
    }
    response = client.post("/inscripciones/", json=nueva_inscripcion)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["curso_id"] == 1
    assert data["estudiante_id"] == 1
    assert data["calificacion_final"] == 9.5