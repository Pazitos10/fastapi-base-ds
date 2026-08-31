from sqlalchemy.orm import Session
from src.curso import models, schemas

def get_cursos(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Curso).offset(skip).limit(limit).all()

def get_curso(db: Session, curso_id: int):
    return db.query(models.Curso).filter(models.Curso.id == curso_id).first()

def create_curso(db: Session, curso: schemas.CursoCreate):
    db_curso = models.Curso(**curso.model_dump())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso