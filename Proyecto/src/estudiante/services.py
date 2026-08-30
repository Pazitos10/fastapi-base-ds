import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.estudiante.models import Estudiante
from src.estudiante import schemas, exceptions

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

# Operaciones CRUD para Estudiantes

def crear_estudiante(db: Session, estudiante: schemas.EstudianteCreate) -> schemas.Estudiante:
    _estudiante = Estudiante(**estudiante.model_dump())
    db.add(_estudiante)
    db.commit()
    db.refresh(_estudiante)
    return _estudiante


def listar_estudiantes(db: Session) -> List[schemas.Estudiante]:
    logger.info("Listando estudiantes desde services")  # <- este mensaje se verá por la terminal
    return db.scalars(select(Estudiante)).all()


def leer_estudiante(db: Session, estudiante_id: int) -> schemas.Estudiante:
    db_estudiante = db.scalar(select(Estudiante).where(Estudiante.id == estudiante_id))
    if db_estudiante is None:
        raise exceptions.EstudianteNoEncontrado()
    return db_estudiante


def modificar_estudiante(
    db: Session, estudiante_id: int, estudiante: schemas.EstudianteUpdate
) -> Estudiante:
    db_estudiante = leer_estudiante(db, estudiante_id)
    db.execute(
        update(Estudiante).where(Estudiante.id == estudiante_id).values(**estudiante.model_dump())
    )
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante


def eliminar_estudiante(db: Session, estudiante_id: int) -> schemas.Estudiante:
    db_estudiante = leer_estudiante(db, estudiante_id)
    
    # Validamos que no tenga inscripciones a cursos antes de borrarlo
    if len(db_estudiante.cursos) > 0:
        raise exceptions.EstudianteTieneCursos()
        
    db.execute(delete(Estudiante).where(Estudiante.id == estudiante_id))
    db.commit()
    return db_estudiante