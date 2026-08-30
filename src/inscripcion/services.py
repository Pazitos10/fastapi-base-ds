import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from src.inscripcion.models import Inscripcion
from src.inscripcion import schemas, exceptions


logger = logging.getLogger(__name__)
# operaciones CRUD para Inscripcion


def crear_inscripcion(db: Session, inscripcion: schemas.InscripcionCreate) -> schemas.Inscripcion:
    _inscripcion = Inscripcion(**inscripcion.model_dump())
    db.add(_inscripcion)
    db.commit()
    db.refresh(
        _inscripcion
    )  # <- qué hace refresh()?: https://docs.sqlalchemy.org/en/21/orm/session_api.html#sqlalchemy.orm.Session.refresh
    return _inscripcion


def listar_inscripciones(db: Session) -> List[schemas.Inscripcion]:
    logger.info("Listando inscripciones desde servicios")
    return db.scalars(select(Inscripcion)).all()


def leer_inscripcion(db: Session, estudiante_id: int, curso_id: int) -> schemas.Inscripcion:
    db_inscripcion = db.scalar(
        select(Inscripcion).where(
            Inscripcion.estudiante_id == estudiante_id, 
            Inscripcion.curso_id == curso_id
        )
    )
    if db_inscripcion is None:
        raise exceptions.InscripcionNoEncontrada()
    return db_inscripcion


def modificar_inscripcion(
    db: Session, estudiante_id: int, curso_id: int, inscripcion: schemas.InscripcionUpdate
) -> Inscripcion:
    db_inscripcion = leer_inscripcion(db, estudiante_id, curso_id)
    db.execute(
        update(Inscripcion)
        .where(Inscripcion.estudiante_id == estudiante_id, Inscripcion.curso_id == curso_id)
        .values(**inscripcion.model_dump())
    )
    db.commit()
    db.refresh(db_inscripcion)
    return db_inscripcion


def eliminar_inscripcion(db: Session, estudiante_id: int, curso_id: int) -> schemas.InscripcionDelete:
    db_inscripcion = leer_inscripcion(db, estudiante_id, curso_id)
    db.execute(
        delete(Inscripcion).where(
            Inscripcion.estudiante_id == estudiante_id, 
            Inscripcion.curso_id == curso_id
        )
    )
    db.commit()
    return db_inscripcion

def matricular_estudiante(db: Session, inscripcion: schemas.InscripcionCreate) -> Inscripcion:
    try:
        existe = db.query(Inscripcion).filter(
            Inscripcion.estudiante_id == inscripcion.estudiante_id,
            Inscripcion.curso_id == inscripcion.curso_id
        ).first()
        
        if existe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="El alumno ya se encuentra matriculado en este curso."
            )
            
        _inscripcion = Inscripcion(**inscripcion.model_dump())
        db.add(_inscripcion)
        db.commit()
        db.refresh(_inscripcion)
        return _inscripcion
        
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {str(e)}"
        )