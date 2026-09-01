from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.inscripcion.models import Inscripcion
from src.inscripcion import schemas, exceptions


def crear_inscripcion(
    db: Session,
    inscripcion: schemas.InscripcionCreate
) -> Inscripcion:

    db_inscripcion = Inscripcion(**inscripcion.model_dump())

    db.add(db_inscripcion)
    db.commit()
    db.refresh(db_inscripcion)

    return db_inscripcion


def listar_inscripciones(
    db: Session
) -> List[Inscripcion]:

    return db.scalars(
        select(Inscripcion)
    ).all()


def leer_inscripcion(
    db: Session,
    inscripcion_id: int
) -> Inscripcion:

    db_inscripcion = db.scalar(
        select(Inscripcion).where(
            Inscripcion.id == inscripcion_id
        )
    )

    if db_inscripcion is None:
        raise exceptions.InscripcionNoEncontrada()

    return db_inscripcion


def modificar_inscripcion(
    db: Session,
    inscripcion_id: int,
    inscripcion: schemas.InscripcionUpdate
) -> Inscripcion:

    db_inscripcion = leer_inscripcion(
        db,
        inscripcion_id
    )

    db.execute(
        update(Inscripcion)
        .where(Inscripcion.id == inscripcion_id)
        .values(**inscripcion.model_dump())
    )

    db.commit()
    db.refresh(db_inscripcion)

    return db_inscripcion


def eliminar_inscripcion(
    db: Session,
    inscripcion_id: int
) -> Inscripcion:

    db_inscripcion = leer_inscripcion(
        db,
        inscripcion_id
    )

    db.execute(
        delete(Inscripcion)
        .where(Inscripcion.id == inscripcion_id)
    )

    db.commit()

    return db_inscripcion