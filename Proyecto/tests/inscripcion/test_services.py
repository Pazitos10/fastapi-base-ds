import pytest
from sqlalchemy.orm import Session
from tests.database import session
from src.inscripcion import exceptions
from src.inscripcion.services import (
    listar_inscripciones,
    crear_inscripcion,
    modificar_inscripcion,
    leer_inscripcion,
    eliminar_inscripcion,
)
from src.inscripcion.schemas import InscripcionCreate, InscripcionUpdate


def test_crear_inscripcion(session: Session) -> None:
    # Asumiendo que existen un curso_id=2 y un estudiante_id=2 que no estén ya inscriptos
    curso_id = 2
    estudiante_id = 2
    calificacion = 8.5

    inscripcion_nueva = crear_inscripcion(
        session, 
        InscripcionCreate(
            curso_id=curso_id, 
            estudiante_id=estudiante_id, 
            calificacion_final=calificacion
        )
    )
    assert inscripcion_nueva.curso_id == curso_id
    assert inscripcion_nueva.estudiante_id == estudiante_id
    assert inscripcion_nueva.calificacion_final == calificacion


def test_crear_inscripcion_duplicada(session: Session) -> None:
    # Intentamos crear una inscripción que ya exista en las fixtures base (por ejemplo, curso_id=1, estudiante_id=1)
    with pytest.raises(exceptions.EstudianteYaInscripto):
        crear_inscripcion(
            session, 
            InscripcionCreate(
                curso_id=1, 
                estudiante_id=1, 
                calificacion_final=10.0
            )
        )


def test_modificar_inscripcion(session: Session) -> None:
    curso_id = 1
    estudiante_id = 1
    nueva_calificacion = 10.0

    inscripcion_1 = leer_inscripcion(session, curso_id, estudiante_id)
    inscripcion_modificada = modificar_inscripcion(
        session, 
        curso_id, 
        estudiante_id, 
        InscripcionUpdate(
            curso_id=curso_id,
            estudiante_id=estudiante_id,
            calificacion_final=nueva_calificacion,
            extra_data=inscripcion_1.extra_data
        )
    )
    assert inscripcion_modificada.calificacion_final == nueva_calificacion


def test_eliminar_inscripcion(session: Session) -> None:
    # Creamos una inscripción temporal para eliminarla de forma segura
    curso_id = 2
    estudiante_id = 1
    inscripcion_temporal = crear_inscripcion(
        session,
        InscripcionCreate(
            curso_id=curso_id,
            estudiante_id=estudiante_id,
            calificacion_final=7.0
        )
    )

    inscripciones_antes = listar_inscripciones(session)

    eliminar_inscripcion(session, curso_id, estudiante_id)

    inscripciones_despues = listar_inscripciones(session)
    assert len(inscripciones_despues) == len(inscripciones_antes) - 1


def test_listar_inscripciones(session: Session) -> None:
    inscripciones = listar_inscripciones(session)
    assert isinstance(inscripciones, list)
    assert len(inscripciones) > 0