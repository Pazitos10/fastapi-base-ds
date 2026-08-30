from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session


client = TestClient(app)


def test_read_profesores(session: Session) -> None:
    response = client.get("/profesores")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_create_profesor(session: Session) -> None:
    nuevo_profesor = {
        "nombre": "Carlos Perez",
        "email": "carlos.perez@gmail.com",
        "departemento_id": 1
    }
    response = client.post("/profesores/", json=nuevo_profesor)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["nombre"] == "Carlos Perez"
    assert "id" in data
