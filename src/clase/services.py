from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.clase.models import Clase
from src.clase import schemas, exceptions

def crearClase(db: Session, clase: schemas.ClaseCreate) -> schemas.Clase: 
    _clase = Clase(**clase.model_dump())
    db.add(_clase)
    db.commit()
    db.refresh(_clase)
    return _clase

def leerClase(db: Session, claseId: int) -> schemas.Clase:
    db_clase = db.scalar(select(Clase).where(Clase.id == claseId))
    if db_clase is None:
        raise exceptions.ClaseNoEncontrada()
    return db_clase

def modificarClase(db: Session, claseId: int, clase: schemas.ClaseUpdate) -> schemas.ClaseUpdate:
    db_clase = leerClase(db, claseId)
    db.execute(update(Clase).where(Clase.id == claseId).values(**clase.model_dump()))
    db.commit()
    db.refresh(db_clase)
    return db_clase

def eliminarClase(db: Session, claseId: int) -> schemas.ClaseDelete:
    db_clase = leerClase(db, claseId)
    db.execute(delete(Clase).where(Clase.id == claseId))
    db.commit()
    return db_clase

