import logging
from typing import List
from datetime import datetime
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.profesor.models import Profesor
from src.profesor import schemas, exceptions

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

# operaciones CRUD para Personas

def crear_profesor(db: Session, profesor: schemas.ProfesorCreate) -> schemas.Profesor:

    existe_email = db.scalar(select(Profesor).where(Profesor.email == profesor.email))
    if existe_email is not None:
        raise exceptions.EmailDuplicado

    datos = profesor.model_dump()

    if datos.get("fecha_ingreso") is None:
        datos["fecha_ingreso"] = datetime.now()
    
    _profesor = Profesor(**profesor.model_dump())
    db.add(_profesor)
    db.commit()
    db.refresh(_profesor)
    return _profesor


def listar_profesores(db: Session) -> List[schemas.Profesor]:
    logger.info("Listando profesores desde services")  # <- este mensaje se verá por la terminal
    return db.scalars(select(Profesor)).all()


def leer_profesor(db: Session, profesor_id: int) -> schemas.Profesor:
    db_profesor = db.scalar(select(Profesor).where(Profesor.id == profesor_id))
    if db_profesor is None:
        raise exceptions.ProfesorNoEncontrado()
    return db_profesor


def modificar_profesor(
    db: Session, profesor_id: int, profesor: schemas.ProfesorUpdate
) -> Profesor:
    db_profesor = leer_profesor(db, profesor_id)

    if profesor.email is not None:
        email_en_uso = db.scalar(select(Profesor).where(Profesor.email == profesor.email,Profesor.id != profesor_id))
        if email_en_uso is not None:
            raise exceptions.EmailDuplicado()

    db.execute(
        update(Profesor).where(Profesor.id == profesor_id).values(**profesor.model_dump())
    )
    db.commit()
    db.refresh(db_profesor)
    return db_profesor

def eliminar_profesor(db: Session, profesor_id: int) -> schemas.Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    if len(db_profesor.cursos) > 0:
        raise exceptions.ProfesorTieneCursos()
    db.execute(delete(Profesor).where(Profesor.id == profesor_id))
    db.commit()
    return db_profesor
