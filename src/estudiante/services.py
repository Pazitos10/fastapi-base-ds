from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.estudiante.models import Estudiante
from src.estudiante import schemas, exceptions

def crearEstudiante(db: Session, estudiante: schemas.EstudianteCreate) -> schemas.Estudiante: 
    _estudiante = Estudiante(**estudiante.model_dump())
    db.add(_estudiante)
    db.commit()
    db.refresh(_estudiante)
    return _estudiante

def leerEstudiante(db: Session, estudianteId: int) -> schemas.Estudiante:
    db_estudiante = db.scalar(select(Estudiante).where(Estudiante.id == estudianteId))
    if db_estudiante is None:
        raise exceptions.EstudianteNoEncontrado()
    return db_estudiante

def modificarEstudiante(db: Session, estudianteId: int, estudiante: schemas.EstudianteUpdate) -> schemas.EstudianteUpdate:
    db_estudiante = leerEstudiante(db, estudianteId)
    db.execute(update(Estudiante).where(Estudiante.id == estudianteId).values(**estudiante.model_dump()))
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

def eliminarEstudiante(db: Session, estudianteId: int) -> schemas.EstudianteDelete:
    db_estudiante = leerEstudiante(db, estudianteId)
    db.execute(delete(Estudiante).where(Estudiante.id == estudianteId))
    db.commit()
    return db_estudiante

