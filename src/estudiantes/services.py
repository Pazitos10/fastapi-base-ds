from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.estudiantes.models import Estudiante
from src.estudiantes import schemas, exceptions


# operaciones CRUD para Estudiante


def crear_estudiante(db: Session, estudiante: schemas.EstudianteCreate) -> schemas.Estudiante:

    existe_legajo = db.scalar(
        select(Estudiante).where(Estudiante.legajo == estudiante.legajo)
    )
    if existe_legajo is not None:
        raise exceptions.LegajoDuplicado()

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
) -> schemas.Estudiante:
    db_estudiante = leer_estudiante(db, estudiante_id)

    if estudiante.legajo is not None:
        existe_legajo = db.scalar(
            select(Estudiante).where(
                Estudiante.legajo == estudiante.legajo,
                Estudiante.id != estudiante_id,
            )
        )
        if existe_legajo is not None:
            raise exceptions.LegajoDuplicado()

    db.execute(update(Estudiante)
               .where(Estudiante.id == estudiante_id)
               .values(**estudiante.model_dump(exclude_unset=True)))
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante


def eliminar_estudiante(db: Session, estudiante_id: int) -> schemas.EstudianteDelete:
    db_estudiante = leer_estudiante(db, estudiante_id)

    if len(db_estudiante.inscripciones) > 0:
        raise exceptions.EstudianteTieneInscripciones
      
    db.execute(
        delete(Estudiante).where(Estudiante.id == estudiante_id)
    )
    db.commit()
    return db_estudiante
