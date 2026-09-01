from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.curso.models import Curso
from src.curso import schemas, exceptions


def crear_curso(
    db: Session,
    curso: schemas.CursoCreate
) -> Curso:

    db_curso = Curso(**curso.model_dump())

    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)

    return db_curso


def listar_cursos(
    db: Session
) -> List[Curso]:

    return db.scalars(
        select(Curso)
    ).all()


def leer_curso(
    db: Session,
    curso_id: int
) -> Curso:

    db_curso = db.scalar(
        select(Curso).where(Curso.id == curso_id)
    )

    if db_curso is None:
        raise exceptions.CursoNoEncontrado()

    return db_curso


def modificar_curso(
    db: Session,
    curso_id: int,
    curso: schemas.CursoUpdate
) -> Curso:

    db_curso = leer_curso(db, curso_id)

    db.execute(
        update(Curso)
        .where(Curso.id == curso_id)
        .values(**curso.model_dump())
    )

    db.commit()
    db.refresh(db_curso)

    return db_curso


def eliminar_curso(
    db: Session,
    curso_id: int
) -> Curso:

    db_curso = leer_curso(db, curso_id)

    db.execute(
        delete(Curso)
        .where(Curso.id == curso_id)
    )

    db.commit()

    return db_curso