import logging
from typing import List
from sqlalchemy import delete, select, update, func
from sqlalchemy.orm import Session
from src.estudiante.models import Estudiante
from src.estudiante import schemas, exceptions
from src.inscripcion.models import Inscripcion

logger = logging.getLogger(__name__)

# operaciones CRUD para Estudiante


def crear_estudiante(db: Session, estudiante: schemas.EstudianteCreate) -> schemas.Estudiante:
    _estudiante = Estudiante(**estudiante.model_dump())
    db.add(_estudiante)
    db.commit()
    db.refresh(
        _estudiante
    )  # <- qué hace refresh()?: https://docs.sqlalchemy.org/en/21/orm/session_api.html#sqlalchemy.orm.Session.refresh
    return _estudiante


def listar_estudiantes(db: Session) -> List[schemas.Estudiante]:
    return db.scalars(select(Estudiante)).all()


def leer_estudiante(db: Session, estudiante_id: int) -> schemas.Estudiante:
    db_estudiante = db.scalar(select(Estudiante).where(Estudiante.id == estudiante_id))
    if db_estudiante is None:
        raise exceptions.EstudianteNoEncontrado() # <- usamos nuestras propias excepciones adaptadas al dominio de aplicación
    return db_estudiante


def modificar_estudiante(
    db: Session, estudiante_id: int, estudiante: schemas.EstudianteUpdate
) -> Estudiante:
    db_estudiante = leer_estudiante(db, estudiante_id)
    db.execute(update(Estudiante)
               .where(Estudiante.id == estudiante_id)
               .values(**estudiante.model_dump()))
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante


def eliminar_estudiante(db: Session, estudiante_id: int) -> schemas.EstudianteDelete:
    db_estudiante = leer_estudiante(db, estudiante_id)
    if len(db_estudiante.inscripciones) > 0:
        raise exceptions.EstudianteTieneInscripciones()
    db.execute(
        delete(Estudiante).where(Estudiante.id == estudiante_id)
    )
    db.commit()
    return db_estudiante

def obtener_promedio_calificaciones(db: Session, estudiante_id: int) -> dict:
    resultado = db.query(
        Estudiante.id,
        Estudiante.nombre,
        func.avg(Inscripcion.calificacion_final).label("promedio")
    ).join(Inscripcion, Estudiante.id == Inscripcion.estudiante_id)\
     .filter(Estudiante.id == estudiante_id)\
     .group_by(Estudiante.id, Estudiante.nombre).first()
     
    if not resultado:
        raise exceptions.EstudianteNoEncontrado()
        
    return {
        "estudiante_id": resultado[0],
        "nombre": resultado[1],
        "promedio": round(resultado[2], 2) if resultado[2] is not None else 0.0
    }