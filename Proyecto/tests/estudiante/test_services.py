import pytest
from sqlalchemy.orm import Session
from tests.database import session
from src.estudiante import exceptions
from src.estudiante.services import (
    listar_estudiantes,
    crear_estudiante,
    modificar_estudiante,
    leer_estudiante,
    eliminar_estudiante,
)
from src.estudiante.schemas import EstudianteCreate, EstudianteUpdate


def test_crear_estudiante(session: Session) -> None:
    nombre = "Lucia Gomez"
    email = "lucia@gmail.com"
    estudiante_3 = crear_estudiante(
        session, 
        EstudianteCreate(nombre=nombre, email=email)
    )
    assert estudiante_3.nombre == nombre
    assert estudiante_3.email == email


def test_modificar_estudiante(session: Session) -> None:
    nuevo_nombre = "Lucia Modificada"
    estudiante_id = 1  # Asumiendo que el estudiante con ID 1 existe en tus fixtures de prueba
    estudiante_1 = leer_estudiante(session, estudiante_id)
    estudiante_1 = modificar_estudiante(
        session, 
        estudiante_id, 
        EstudianteUpdate(
            nombre=nuevo_nombre, 
            email=estudiante_1.email
        )
    )
    assert estudiante_1.nombre == nuevo_nombre


def test_eliminar_estudiante(session: Session) -> None:
    # Intentamos borrar a un estudiante que tiene cursos asociados (según tus fixtures base).
    # Verificamos que se lanza la excepción esperada.
    with pytest.raises(exceptions.EstudianteTieneCursos):
        estudiante_id = 1
        eliminar_estudiante(session, estudiante_id)

    # Probamos crear un estudiante nuevo sin cursos y eliminarlo.
    nombre = "Estudiante Temporal"
    email = "temporal.estudiante@gmail.com"
    estudiante_nuevo = crear_estudiante(
        session, 
        EstudianteCreate(nombre=nombre, email=email)
    )

    estudiantes_antes = listar_estudiantes(session)

    eliminar_estudiante(session, estudiante_nuevo.id)

    estudiantes_despues = listar_estudiantes(session)
    assert len(estudiantes_despues) == len(estudiantes_antes) - 1


def test_listar_estudiantes(session: Session) -> None:
    estudiantes = listar_estudiantes(session)
    assert isinstance(estudiantes, list)
    assert len(estudiantes) > 0