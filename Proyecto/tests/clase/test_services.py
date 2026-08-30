import pytest
from sqlalchemy.orm import Session
from tests.database import session
from src.clase import exceptions
from src.clase.services import (
    listar_clases,
    crear_clase,
    modificar_clase,
    leer_clase,
    eliminar_clase,
)
from src.clase.schemas import ClaseCreate, ClaseUpdate


def test_crear_clase(session: Session) -> None:
    titulo = "Introduccion a la Programacion"
    curso_id = 1
    clase_3 = crear_clase(
        session, 
        ClaseCreate(titulo=titulo, curso_id=curso_id)
    )
    assert clase_3.titulo == titulo
    assert clase_3.curso_id == curso_id


def test_modificar_clase(session: Session) -> None:
    nuevo_titulo = "Programacion Avanzada"
    clase_id = 1  # Asumiendo que la clase con ID 1 existe en tus fixtures de prueba
    clase_1 = leer_clase(session, clase_id)
    clase_1 = modificar_clase(
        session, 
        clase_id, 
        ClaseUpdate(
            titulo=nuevo_titulo, 
            curso_id=clase_1.curso_id
        )
    )
    assert clase_1.titulo == nuevo_titulo


def test_eliminar_clase(session: Session) -> None:
    # Probamos crear una clase nueva y eliminarla de forma segura.
    titulo = "Clase Temporal"
    curso_id = 1
    clase_nueva = crear_clase(
        session, 
        ClaseCreate(titulo=titulo, curso_id=curso_id)
    )

    clases_antes = listar_clases(session)

    eliminar_clase(session, clase_nueva.id)

    clases_despues = listar_clases(session)
    assert len(clases_despues) == len(clases_antes) - 1


def test_listar_clases(session: Session) -> None:
    clases = listar_clases(session)
    assert isinstance(clases, list)
    assert len(clases) > 0