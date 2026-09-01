import logging
from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.profesor.models import Profesor
from src.profesor import schemas, exceptions


logger = logging.getLogger(__name__)


def crear_profesor(
    db: Session, profesor: schemas.ProfesorCreate
) -> Profesor:
    db_profesor = Profesor(**profesor.model_dump())

    db.add(db_profesor)
    db.commit()
    db.refresh(db_profesor)

    return db_profesor


def listar_profesores(db: Session) -> List[Profesor]:
    logger.info("Listando profesores desde services")

    return db.scalars(select(Profesor)).all()


def leer_profesor(db: Session, profesor_id: int) -> Profesor:
    db_profesor = db.scalar(
        select(Profesor).where(Profesor.id == profesor_id)
    )

    if db_profesor is None:
        raise exceptions.ProfesorNoEncontrado()

    return db_profesor


def modificar_profesor(
    db: Session,
    profesor_id: int,
    profesor: schemas.ProfesorUpdate
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


def eliminar_profesor(
    db: Session, profesor_id: int
) -> Profesor:

    db_profesor = leer_profesor(db, profesor_id)

    db.execute(
        delete(Profesor)
        .where(Profesor.id == profesor_id)
    )

    db.commit()

    return db_profesor