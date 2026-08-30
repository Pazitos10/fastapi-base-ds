from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.curso.models import Curso
from src.curso import schemas, exceptions

def crearCurso(db: Session, curso: schemas.CursoCreate) -> schemas.Curso: 
    _curso = Curso(**curso.model_dump())
    db.add(_curso)
    db.commit()
    db.refresh(_curso)
    return _curso

def leerCurso(db: Session, cursoId: int) -> schemas.Curso:
    db_curso = db.scalar(select(Curso).where(Curso.id == cursoId))
    if db_curso is None:
        raise exceptions.CursoNoEncontrado()
    return db_curso

def modificarCurso(db: Session, cursoId: int, curso: schemas.CursoUpdate) -> schemas.CursoUpdate:
    db_curso = leerCurso(db, cursoId)
    db.execute(update(Curso).where(Curso.id == cursoId).values(**curso.model_dump()))
    db.commit()
    db.refresh(db_curso)
    return db_curso

def eliminarCurso(db: Session, cursoId: int) -> schemas.CursoDelete:
    db_curso = leerCurso(db, cursoId)
    db.execute(delete(Curso).where(Curso.id == cursoId))
    db.commit()
    return db_curso

