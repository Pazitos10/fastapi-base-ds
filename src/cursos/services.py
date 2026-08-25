from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.cursos.models import Curso
from src.cursos import schemas, exceptions


# operaciones CRUD para Cursos


def crear_curso(db: Session, curso: schemas.CursoCreate) -> schemas.Curso:
    _curso = Curso(**curso.model_dump())
    db.add(_curso)
    db.commit()
    db.refresh(
        _curso
    )  # <- qué hace refresh()?: https://docs.sqlalchemy.org/en/21/orm/session_api.html#sqlalchemy.orm.Session.refresh
    return _curso


def listar_curso(db: Session) -> List[schemas.Curso]:
    return db.scalars(select(Curso)).all()


def leer_curso(db: Session, curso_id: int) -> schemas.Curso:
    db_curso = db.scalar(select(Curso).where(Curso.id == curso_id))
    if db_curso is None:
        raise exceptions.CursoNoEncontrado() # <- usamos nuestras propias excepciones adaptadas al dominio de aplicación
    return db_curso


def modificar_curso(
    db: Session, curso_id: int, curso: schemas.CursoUpdate
) -> Curso:
    db_curso = leer_curso(db, curso_id)
    db.execute(update(Curso)
               .where(Curso.id == curso_id)
               .values(**curso.model_dump()))
    db.commit()
    db.refresh(db_curso)
    return db_curso


def eliminar_curso(db: Session, curso_id: int) -> schemas.CursoDelete:
    db_curso = leer_curso(db, curso_id)

    if len(db_curso.inscripciones) > 0:
        raise exceptions.CursoTieneInscriptos()
    if len(db_curso.clases) > 0:
        raise exceptions.CursoTieneClases()
    
    db.execute(
        delete(Curso).where(Curso.id == curso_id)
    )
    db.commit()
    return db_curso
