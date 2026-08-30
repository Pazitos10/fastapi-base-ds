from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.inscripcion.models import Inscripcion
from src.inscripcion import schemas, exceptions

def crearInscripcion(db: Session, inscripcion: schemas.InscripcionCreate) -> schemas.Inscripcion: 
    _inscripcion = Inscripcion(**inscripcion.model_dump())
    db.add(_inscripcion)
    db.commit()
    db.refresh(_inscripcion)
    return _inscripcion

def leerInscripcion(db: Session, estudianteId: int, cursoId: int) -> schemas.Inscripcion:
    db_inscripcion = db.scalar(select(Inscripcion).where(Inscripcion.estudianteId == estudianteId, Inscripcion.cursoId == cursoId))
    if db_inscripcion is None:
        raise exceptions.InscripcionNoEncontrada()
    return db_inscripcion

def modificarInscripcion(db: Session, estudianteId: int, cursoId: int, inscripcion: schemas.InscripcionUpdate) -> schemas.InscripcionUpdate:
    db_inscripcion = leerInscripcion(db, estudianteId, cursoId)
    db.execute(update(Inscripcion).where(Inscripcion.estudianteId == estudianteId, Inscripcion.cursoId == cursoId).values(**inscripcion.model_dump()))
    db.commit()
    db.refresh(db_inscripcion)
    return db_inscripcion

def eliminarInscripcion(db: Session, estudianteId: int, cursoId: int) -> schemas.InscripcionDelete:
    db_inscripcion = leerInscripcion(db, estudianteId, cursoId)
    db.execute(delete(Inscripcion).where(Inscripcion.estudianteId == estudianteId, Inscripcion.cursoId == cursoId))
    db.commit()
    return db_inscripcion

