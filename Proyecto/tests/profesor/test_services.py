import pytest
from sqlalchemy.orm import Session
from tests.database import session
from src.profesor import exceptions
from src.profesor.services import (
    listar_profesores,
    crear_profesor,
    modificar_profesor,
    leer_profesor,
    eliminar_profesor,
    asignar_curso_a_profesor,
    asignar_departamento_a_profesor,
)
from src.profesor.schemas import ProfesorCreate, ProfesorUpdate


def test_crear_profesor(session: Session) -> None:
    nombre = "Carlos Perez"
    email = "carlos@gmail.com"
    departemento_id = 1
    profesor_3 = crear_profesor(
        session, 
        ProfesorCreate(nombre=nombre, email=email, departemento_id=departemento_id)
    )
    assert profesor_3.nombre == nombre
    assert profesor_3.email == email
    assert profesor_3.departemento_id == departemento_id


def test_modificar_profesor(session: Session) -> None:
    nuevo_nombre = "Carlos Modificado"
    profesor_id = 1  # Asumiendo que el profesor con ID 1 existe en tus fixtures de prueba
    profesor_1 = leer_profesor(session, profesor_id)
    profesor_1 = modificar_profesor(
        session, 
        profesor_id, 
        ProfesorUpdate(
            nombre=nuevo_nombre, 
            email=profesor_1.email, 
            departemento_id=profesor_1.departemento_id
        )
    )
    assert profesor_1.nombre == nuevo_nombre


def test_eliminar_profesor(session: Session) -> None:
    # Intentamos borrar a un profesor que tiene cursos asociados.
    # Verificamos que se lanza la excepción esperada.
    with pytest.raises(exceptions.ProfesorTieneCursos):
        profesor_id = 1
        eliminar_profesor(session, profesor_id)

    # Probamos crear un profesor nuevo sin cursos y eliminarlo.
    nombre = "Profesor Temporal"
    email = "temporal@gmail.com"
    departemento_id = 1
    profesor_nuevo = crear_profesor(
        session, 
        ProfesorCreate(nombre=nombre, email=email, departemento_id=departemento_id)
    )

    profesores_antes = listar_profesores(session)

    eliminar_profesor(session, profesor_nuevo.id)

    profesores_despues = listar_profesores(session)
    assert len(profesores_despues) == len(profesores_antes) - 1


def test_listar_profesores(session: Session) -> None:
    profesores = listar_profesores(session)
    assert isinstance(profesores, list)
    assert len(profesores) > 0

def test_asignar_departamento_a_profesor(session: Session) -> None:
    profesor_id = 1
    nuevo_departamento_id = 2  # Asumiendo que existe un departamento con ID 2
    profesor_actualizado = asignar_departamento_a_profesor(
        session, profesor_id, nuevo_departamento_id
    )
    assert profesor_actualizado.departemento_id == nuevo_departamento_id


def test_asignar_curso_a_profesor(session: Session) -> None:
    profesor_id = 1
    curso_id = 1  # Asumiendo que existe un curso con ID 1
    profesor_actualizado = asignar_curso_a_profesor(session, profesor_id, curso_id)
    
    # Verificamos que el curso ahora esté en la lista de cursos del profesor
    ids_cursos = [curso.id for curso in profesor_actualizado.cursos]
    assert curso_id in ids_cursos