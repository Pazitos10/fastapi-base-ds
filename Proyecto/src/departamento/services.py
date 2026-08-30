import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.departamento.models import Departamento
from src.departamento import schemas, exceptions

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

# operaciones CRUD para Departamentos

def crear_departamento(db: Session, departamento: schemas.DepartamentoCreate) -> schemas.Departamento:
    _departamento = Departamento(**departamento.model_dump())
    db.add(_departamento)
    db.commit()
    db.refresh(_departamento)
    return _departamento


def listar_departamentos(db: Session) -> List[schemas.Departamento]:
    logger.info("Listando departamentos desde services")  # <- este mensaje se verá por la terminal
    return db.scalars(select(Departamento)).all()


def leer_departamento(db: Session, departamento_id: int) -> schemas.Departamento:
    db_departamento = db.scalar(select(Departamento).where(Departamento.id == departamento_id))
    if db_departamento is None:
        raise exceptions.DepartamentoNoEncontrado()
    return db_departamento


def modificar_departamento(
    db: Session, departamento_id: int, departamento: schemas.DepartamentoUpdate
) -> Departamento:
    db_departamento = leer_departamento(db, departamento_id)
    db.execute(
        update(Departamento).where(Departamento.id == departamento_id).values(**departamento.model_dump())
    )
    db.commit()
    db.refresh(db_departamento)
    return db_departamento


def eliminar_departamento(db: Session, departamento_id: int) -> schemas.Departamento:
    db_departamento = leer_departamento(db, departamento_id)
    if len(db_departamento.profesor) > 0:
        raise exceptions.DepartamentoTieneProfesores()
    db.execute(delete(Departamento).where(Departamento.id == departamento_id))
    db.commit()
    return db_departamento