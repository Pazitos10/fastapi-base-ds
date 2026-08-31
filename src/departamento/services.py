from sqlalchemy.orm import Session
from src.departamento import models, schemas

def get_departamentos(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Departamento).offset(skip).limit(limit).all()

def get_departamento(db: Session, departamento_id: int):
    return db.query(models.Departamento).filter(models.Departamento.id == departamento_id).first()

def create_departamento(db: Session, departamento: schemas.DepartamentoCreate):
    db_departamento = models.Departamento(**departamento.model_dump())
    
    db.add(db_departamento)
    db.commit()
    db.refresh(db_departamento)
    
    return db_departamento