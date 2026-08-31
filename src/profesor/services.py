from sqlalchemy.orm import Session
from src.profesor import models, schemas

def get_profesores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profesor).offset(skip).limit(limit).all()

def get_profesor(db: Session, profesor_id: int):
    return db.query(models.Profesor).filter(models.Profesor.id == profesor_id).first()

def create_profesor(db: Session, profesor: schemas.ProfesorCreate):
    db_profesor = models.Profesor(**profesor.model_dump())
    
    db.add(db_profesor)
    db.commit()
    db.refresh(db_profesor)
    
    return db_profesor