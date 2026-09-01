from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.estudiante.models import Estudiante
from src.estudiante import schemas, exceptions


def crear_estudiante(
    db: Session,
    estudiante: schemas.EstudianteCreate
) -> Estudiante:

    db_estudiante = Estudiante(**estudiante.model_dump())

    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)

    return db_estudiante


def listar_estudiantes(
    db: Session
) -> List[Estudiante]:

    return db.scalars(
        select(Estudiante)
    ).all()


def leer_estudiante(
    db: Session,
    estudiante_id: int
) -> Estudiante:

    db_estudiante = db.scalar(
        select(Estudiante).where(
            Estudiante.id == estudiante_id
        )
    )

    if db_estudiante is None:
        raise exceptions.EstudianteNoEncontrado()

    return db_estudiante


def modificar_estudiante(
    db: Session,
    estudiante_id: int,
    estudiante: schemas.EstudianteUpdate
) -> Estudiante:

    db_estudiante = leer_estudiante(
        db,
        estudiante_id
    )

    db.execute(
        update(Estudiante)
        .where(Estudiante.id == estudiante_id)
        .values(**estudiante.model_dump())
    )

    db.commit()
    db.refresh(db_estudiante)

    return db_estudiante


def eliminar_estudiante(
    db: Session,
    estudiante_id: int
) -> Estudiante:

    db_estudiante = leer_estudiante(
        db,
        estudiante_id
    )

    db.execute(
        delete(Estudiante)
        .where(Estudiante.id == estudiante_id)
    )

    db.commit()

    return db_estudiante