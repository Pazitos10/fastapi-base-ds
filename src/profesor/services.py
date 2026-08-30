from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.profesor.models import Profesor
from src.profesor import schemas, exceptions

def crearProfesor(db: Session, profesor: schemas.ProfesorCreate) -> schemas.Profesor: 
    _profesor = Profesor(**profesor.model_dump())
    db.add(_profesor)
    db.commit()
    db.refresh(_profesor)
    return _profesor

def leerProfesor(db: Session, profesorId: int) -> schemas.Profesor:
    db_profesor = db.scalar(select(Profesor).where(Profesor.id == profesorId))
    if db_profesor is None:
        raise exceptions.ProfesorNoEncontrado()
    return db_profesor

def modificarProfesor(db: Session, profesorId: int, profesor: schemas.ProfesorUpdate) -> schemas.ProfesorUpdate:
    db_profesor = leerProfesor(db, profesorId)
    db.execute(update(Profesor).where(Profesor.id == profesorId).values(**profesor.model_dump()))
    db.commit()
    db.refresh(db_profesor)
    return db_profesor

def eliminarProfesor(db: Session, profesorId: int) -> schemas.ProfesorDelete:
    db_profesor = leerProfesor(db, profesorId)
    db.execute(delete(Profesor).where(Profesor.id == profesorId))
    db.commit()
    return db_profesor

