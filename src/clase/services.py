from sqlalchemy.orm import Session
from src.clase import models, schemas

def get_clases(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Clase).offset(skip).limit(limit).all()

def get_clase(db: Session, clase_id: int):
    return db.query(models.Clase).filter(models.Clase.id == clase_id).first()

def create_clase(db: Session, clase: schemas.ClaseCreate):
    db_clase = models.Clase(**clase.model_dump())
    db.add(db_clase)
    db.commit()
    db.refresh(db_clase)
    return db_clase