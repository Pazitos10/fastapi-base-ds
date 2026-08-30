import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.inscripcion.models import Inscripcion
from src.inscripcion import schemas, exceptions
from src.estudiante.models import Estudiante
from src.curso.models import Curso

# Creamos un logger para este módulo específico
logger = logging.getLogger(__name__)

# Operaciones CRUD para Inscripciones

def crear_inscripcion(db: Session, inscripcion: schemas.InscripcionCreate) -> schemas.Inscripcion:
    # Verificamos que el estudiante exista
    db_estudiante = db.scalar(select(Estudiante).where(Estudiante.id == inscripcion.estudiante_id))
    if db_estudiante is None:
        raise exceptions.EstudianteNoEncontrado()

    # Verificamos que el curso exista
    db_curso = db.scalar(select(Curso).where(Curso.id == inscripcion.curso_id))
    if db_curso is None:
        raise exceptions.CursoNoEncontrado()

    # Verificamos si ya existe la inscripción para evitar duplicados
    db_inscripcion_existente = db.scalar(
        select(Inscripcion).where(
            Inscripcion.curso_id == inscripcion.curso_id,
            Inscripcion.estudiante_id == inscripcion.estudiante_id
        )
    )
    if db_inscripcion_existente is not None:
        raise exceptions.EstudianteYaInscripto()

    _inscripcion = Inscripcion(**inscripcion.model_dump())
    db.add(_inscripcion)
    db.commit()
    db.refresh(_inscripcion)
    return _inscripcion


def listar_inscripciones(db: Session) -> List[schemas.Inscripcion]:
    logger.info("Listando inscripciones desde services")
    return db.scalars(select(Inscripcion)).all()


def leer_inscripcion(db: Session, curso_id: int, estudiante_id: int) -> schemas.Inscripcion:
    db_inscripcion = db.scalar(
        select(Inscripcion).where(
            Inscripcion.curso_id == curso_id,
            Inscripcion.estudiante_id == estudiante_id
        )
    )
    if db_inscripcion is None:
        raise exceptions.InscripcionNoEncontrada()
    return db_inscripcion


def modificar_inscripcion(
    db: Session, curso_id: int, estudiante_id: int, inscripcion: schemas.InscripcionUpdate
) -> Inscripcion:
    db_inscripcion = leer_inscripcion(db, curso_id, estudiante_id)
    db.execute(
        update(Inscripcion)
        .where(Inscripcion.curso_id == curso_id, Inscripcion.estudiante_id == estudiante_id)
        .values(**inscripcion.model_dump())
    )
    db.commit()
    db.refresh(db_inscripcion)
    return db_inscripcion


def eliminar_inscripcion(db: Session, curso_id: int, estudiante_id: int) -> schemas.Inscripcion:
    db_inscripcion = leer_inscripcion(db, curso_id, estudiante_id)
    db.execute(
        delete(Inscripcion).where(
            Inscripcion.curso_id == curso_id,
            Inscripcion.estudiante_id == estudiante_id
        )
    )
    db.commit()
    return db_inscripcion