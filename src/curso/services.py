import logging
from typing import List
from sqlalchemy import delete, select, update, func
from sqlalchemy.orm import Session
from src.curso.models import Curso
from src.curso import schemas, exceptions
from src.inscripcion.models import Inscripcion


logger = logging.getLogger(__name__)
# operaciones CRUD para Curso


def crear_curso(db: Session, curso: schemas.CursoCreate) -> schemas.Curso:
    _curso = Curso(**curso.model_dump())
    db.add(_curso)
    db.commit()
    db.refresh(
        _curso
    )  # <- qué hace refresh()?: https://docs.sqlalchemy.org/en/21/orm/session_api.html#sqlalchemy.orm.Session.refresh
    return _curso


def listar_cursos(db: Session) -> List[schemas.Curso]:
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
    if len(db_curso.clases) > 0:
        raise exceptions.CursoTieneClases()
    if len(db_curso.inscripciones) > 0:
        raise exceptions.CursoTieneInscripciones()
    db.execute(
        delete(Curso).where(Curso.id == curso_id)
    )
    db.commit()
    return db_curso

def contar_estudiantes_por_curso(db: Session) -> List[dict]:
    resultados = db.query(
        Curso.id,
        Curso.titulo,
        func.count(Inscripcion.estudiante_id).label("total")
    ).outerjoin(Inscripcion, Curso.id == Inscripcion.curso_id)\
     .group_by(Curso.id, Curso.titulo).all()
     
    return [
        {"curso_id": r[0], "titulo": r[1], "total_estudiantes": r[2]}
        for r in resultados
    ]