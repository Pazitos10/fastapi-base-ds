from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.profesores.models import Profesor
from src.profesores import schemas, exceptions


def crear_profesor(db: Session, profesor: schemas.ProfesorCreate) -> schemas.Profesor:
    _profesor = Profesor(**profesor.model_dump())
    db.add(_profesor)
    db.commit()
    db.refresh(_profesor)
    return _profesor


def listar_profesores(db: Session) -> List[schemas.Profesor]:
    return db.scalars(select(Profesor)).all()


def leer_profesor(db: Session, profesor_id: int) -> schemas.Profesor:
    db_profesor = db.scalar(select(Profesor).where(Profesor.id == profesor_id))
    if db_profesor is None:
        raise exceptions.ProfesorNoEncontrado()
    return db_profesor


def modificar_profesor(
    db: Session, profesor_id: int, profesor: schemas.ProfesorUpdate
) -> Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    db.execute(
        update(Profesor)
        .where(Profesor.id == profesor_id)
        .values(**profesor.model_dump())
    )
    db.commit()
    db.refresh(db_profesor)
    return db_profesor


def eliminar_profesor(db: Session, profesor_id: int) -> schemas.ProfesorDelete:
    db_profesor = leer_profesor(db, profesor_id)
    db.execute(delete(Profesor).where(Profesor.id == profesor_id))
    db.commit()
    return db_profesor