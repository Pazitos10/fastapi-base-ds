from sqlalchemy.orm import Session
from src.estudiante import models, schemas

def get_estudiantes(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Estudiante).offset(skip).limit(limit).all()

def get_estudiante(db: Session, estudiante_id: int):
    return db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()

def create_estudiante(db: Session, estudiante: schemas.EstudianteCreate):
    db_estudiante = models.Estudiante(**estudiante.model_dump())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante