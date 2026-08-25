from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.clases.models import Clase
from src.clases import schemas, exceptions


# operaciones CRUD para Mascota


def crear_clase(db: Session, clase: schemas.ClaseCreate) -> schemas.Clase:
    _clase = Clase(**clase.model_dump())
    db.add(_clase)
    db.commit()
    db.refresh(
        _clase
    )  # <- qué hace refresh()?: https://docs.sqlalchemy.org/en/21/orm/session_api.html#sqlalchemy.orm.Session.refresh
    return _clase


def listar_clases(db: Session) -> List[schemas.Clase]:
    return db.scalars(select(Clase)).all()

def leer_clase(db: Session, clase_id: int) -> schemas.Clase:
    db_clase = db.scalar(select(Clase).where(Clase.id == clase_id))
    if db_clase is None:
        raise exceptions.ClaseNoEncontrada() # <- usamos nuestras propias excepciones adaptadas al dominio de aplicación
    return db_clase


def modificar_clase(
    db: Session, clase_id: int, clase: schemas.ClaseUpdate
) -> Clase:
    db_clase = leer_clase(db, clase_id)
    db.execute(update(Clase)
               .where(Clase.id == clase_id)
               .values(**clase.model_dump(exclude_unset=True)))
    db.commit()
    db.refresh(db_clase)
    return db_clase


def eliminar_clase(db: Session, clase_id: int) -> schemas.ClaseDelete:
    db_clase = leer_clase(db, clase_id)
    db.execute(
        delete(Clase).where(Clase.id == clase_id)
    )
    db.commit()
    return db_clase

def listar_clases_por_curso(db:Session, curso_id: int) -> List[schemas.Clase]:
    return db.scalars(select(Clase).where(Clase.curso_id == curso_id)).all()
