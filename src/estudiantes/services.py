from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.estudiantes.models import Estudiante
from src.estudiantes import schemas, exceptions


def crear_estudiante(db: Session, datos: schemas.EstudianteCreate) -> schemas.Estudiante:
    repetido = db.scalar(select(Estudiante).where(Estudiante.legajo == datos.legajo))
    if repetido is not None:
        raise exceptions.LegajoDuplicado()
    alumno = Estudiante(**datos.model_dump())
    db.add(alumno)
    db.commit()
    db.refresh(alumno)
    return alumno


def listar_estudiantes(db: Session) -> List[schemas.Estudiante]:
    return db.scalars(select(Estudiante)).all()


def leer_estudiante(db: Session, alumno_id: int) -> schemas.Estudiante:
    alumno = db.scalar(select(Estudiante).where(Estudiante.id == alumno_id))
    if alumno is None:
        raise exceptions.EstudianteNoEncontrado()
    return alumno


def modificar_estudiante(
    db: Session, alumno_id: int, datos: schemas.EstudianteUpdate
) -> Estudiante:
    alumno = leer_estudiante(db, alumno_id)
    cambios = datos.model_dump(exclude_unset=True)
    if "legajo" in cambios:
        otro = db.scalar(
            select(Estudiante).where(
                Estudiante.legajo == cambios["legajo"],
                Estudiante.id != alumno_id,
            )
        )
        if otro is not None:
            raise exceptions.LegajoDuplicado()
    db.execute(update(Estudiante).where(Estudiante.id == alumno_id).values(**cambios))
    db.commit()
    db.refresh(alumno)
    return alumno


def eliminar_estudiante(db: Session, alumno_id: int) -> schemas.EstudianteDelete:
    alumno = leer_estudiante(db, alumno_id)
    if len(alumno.inscripciones) > 0:
        raise exceptions.EstudianteConInscripciones()
    db.execute(delete(Estudiante).where(Estudiante.id == alumno_id))
    db.commit()
    return alumno
