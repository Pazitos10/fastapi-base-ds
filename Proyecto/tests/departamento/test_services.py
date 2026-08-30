import pytest
from sqlalchemy.orm import Session
from tests.database import session
from src.departamento import exceptions
from src.departamento.services import (
    listar_departamentos,
    crear_departamento,
    modificar_departamento,
    leer_departamento,
    eliminar_departamento,
)
from src.departamento.schemas import DepartamentoCreate, DepartamentoUpdate


def test_crear_departamento(session: Session) -> None:
    nombre = "Departamento de Ciencias"
    departamento_3 = crear_departamento(
        session, 
        DepartamentoCreate(nombre=nombre)
    )
    assert departamento_3.nombre == nombre


def test_modificar_departamento(session: Session) -> None:
    nuevo_nombre = "Departamento de Ciencias Exactas"
    departamento_id = 1  # Asumiendo que el departamento con ID 1 existe en tus fixtures
    departamento_1 = leer_departamento(session, departamento_id)
    departamento_1 = modificar_departamento(
        session, 
        departamento_id, 
        DepartamentoUpdate(nombre=nuevo_nombre)
    )
    assert departamento_1.nombre == nuevo_nombre


def test_eliminar_departamento(session: Session) -> None:
    # Probamos crear un departamento nuevo y eliminarlo de forma segura.
    nombre = "Departamento Temporal"
    departamento_nuevo = crear_departamento(
        session, 
        DepartamentoCreate(nombre=nombre)
    )

    departamentos_antes = listar_departamentos(session)

    eliminar_departamento(session, departamento_nuevo.id)

    departamentos_despues = listar_departamentos(session)
    assert len(departamentos_despues) == len(departamentos_antes) - 1


def test_listar_departamentos(session: Session) -> None:
    departamentos = listar_departamentos(session)
    assert isinstance(departamentos, list)
    assert len(departamentos) > 0