from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.cursos.models import Curso
from src.cursos import schemas, exceptions
from src.profesores.models import Profesor


def crear_curso(db: Session, datos: schemas.CursoCreate) -> schemas.Curso:
    profe = db.scalar(select(Profesor).where(Profesor.id == datos.profesor_id))
    if profe is None:
        raise exceptions.ProfesorInexistente()
    materia = Curso(**datos.model_dump())
    db.add(materia)
    db.commit()
    db.refresh(materia)
    return materia


def listar_cursos(db: Session) -> List[schemas.Curso]:
    return db.scalars(select(Curso)).all()


def leer_curso(db: Session, curso_id: int) -> schemas.Curso:
    materia = db.scalar(select(Curso).where(Curso.id == curso_id))
    if materia is None:
        raise exceptions.CursoNoEncontrado()
    return materia


def modificar_curso(db: Session, curso_id: int, datos: schemas.CursoUpdate) -> Curso:
    materia = leer_curso(db, curso_id)
    cambios = datos.model_dump(exclude_unset=True)
    if "profesor_id" in cambios:
        profe = db.scalar(select(Profesor).where(Profesor.id == cambios["profesor_id"]))
        if profe is None:
            raise exceptions.ProfesorInexistente()
    db.execute(update(Curso).where(Curso.id == curso_id).values(**cambios))
    db.commit()
    db.refresh(materia)
    return materia


def eliminar_curso(db: Session, curso_id: int) -> schemas.CursoDelete:
    materia = leer_curso(db, curso_id)
    if len(materia.inscripciones) > 0:
        raise exceptions.CursoTieneInscriptos()
    if len(materia.clases) > 0:
        raise exceptions.CursoTieneClases()
    db.execute(delete(Curso).where(Curso.id == curso_id))
    db.commit()
    return materia
