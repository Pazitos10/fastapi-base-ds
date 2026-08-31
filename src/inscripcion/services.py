from sqlalchemy.orm import Session
from src.inscripcion import models, schemas

def get_inscripciones(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Inscripcion).offset(skip).limit(limit).all()


def get_inscripcion(db: Session, estudiante_id: int, curso_id: int):
    return db.query(models.Inscripcion).filter(
        models.Inscripcion.estudiante_id == estudiante_id,
        models.Inscripcion.curso_id == curso_id
    ).first()

def create_inscripcion(db: Session, inscripcion: schemas.InscripcionCreate):
    db_inscripcion = models.Inscripcion(**inscripcion.model_dump())
    db.add(db_inscripcion)
    db.commit()
    db.refresh(db_inscripcion)
    return db_inscripcion