from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.cursos.models import Curso
from src.estudiantes.models import Estudiante
from src.inscripciones import exceptions, schemas
from src.inscripciones.models import Inscripcion


def crear_inscripcion(
    db: Session, inscripcion: schemas.InscripcionCreate
) -> schemas.Inscripcion:
    
    estudiante = db.scalar(
        select(Estudiante).where(Estudiante.id == inscripcion.estudiante_id)
    )
    if estudiante is None:
        raise exceptions.EstudianteNoExiste()

    curso = db.scalar(select(Curso).where(Curso.id == inscripcion.curso_id))
    if curso is None:
        raise exceptions.CursoNoExiste()
    
    existe = db.scalar(
        select(Inscripcion).where(
            Inscripcion.estudiante_id == inscripcion.estudiante_id,
            Inscripcion.curso_id == inscripcion.curso_id,
        )
    )
    if existe is not None:
        raise exceptions.InscripcionDuplicada()

    _inscripcion = Inscripcion(**inscripcion.model_dump())
    db.add(_inscripcion)
    db.commit()
    db.refresh(_inscripcion)
    return _inscripcion


def listar_inscripciones(db: Session) -> List[schemas.Inscripcion]:
    return db.scalars(select(Inscripcion)).all()


def leer_inscripcion(
    db: Session, inscripcion_id: int
) -> schemas.Inscripcion:
    db_inscripcion = db.scalar(
        select(Inscripcion).where(Inscripcion.id == inscripcion_id)
    )
    if db_inscripcion is None:
        raise exceptions.InscripcionNoEncontrada()
    return db_inscripcion


def modificar_inscripcion(
    db: Session,
    inscripcion_id: int,
    inscripcion: schemas.InscripcionUpdate,
) -> schemas.Inscripcion:
    db_inscripcion = leer_inscripcion(db, inscripcion_id)

    db.execute(
        update(Inscripcion)
        .where(Inscripcion.id == inscripcion_id)
        .values(**inscripcion.model_dump(exclude_unset=True))
    )
    db.commit()
    db.refresh(db_inscripcion)
    return db_inscripcion


def eliminar_inscripcion(
    db: Session, inscripcion_id: int
) -> schemas.InscripcionDelete:
    db_inscripcion = leer_inscripcion(db, inscripcion_id)

    db.execute(
        delete(Inscripcion).where(Inscripcion.id == inscripcion_id)
    )
    db.commit()
    return db_inscripcion