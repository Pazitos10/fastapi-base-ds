import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.clase.models import Clase
from src.clase import schemas, exceptions

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

# Operaciones CRUD para Clases

def crear_clase(db: Session, clase: schemas.ClaseCreate) -> schemas.Clase:
    _clase = Clase(**clase.model_dump())
    db.add(_clase)
    db.commit()
    db.refresh(_clase)
    return _clase


def listar_clases(db: Session) -> List[schemas.Clase]:
    logger.info("Listando clases desde services")  # <- este mensaje se verá por la terminal
    return db.scalars(select(Clase)).all()


def leer_clase(db: Session, clase_id: int) -> schemas.Clase:
    db_clase = db.scalar(select(Clase).where(Clase.id == clase_id))
    if db_clase is None:
        raise exceptions.ClaseNoEncontrada()
    return db_clase


def modificar_clase(
    db: Session, clase_id: int, clase: schemas.ClaseUpdate
) -> Clase:
    db_clase = leer_clase(db, clase_id)
    db.execute(
        update(Clase).where(Clase.id == clase_id).values(**clase.model_dump())
    )
    db.commit()
    db.refresh(db_clase)
    return db_clase


def eliminar_clase(db: Session, clase_id: int) -> schemas.Clase:
    db_clase = leer_clase(db, clase_id)
    db.execute(delete(Clase).where(Clase.id == clase_id))
    db.commit()
    return db_clase