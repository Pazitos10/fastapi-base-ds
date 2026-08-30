import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.profesor.models import Profesor
from src.profesor import schemas, exceptions


logger = logging.getLogger(__name__)
# operaciones CRUD para Profesor


def crear_profesor(db: Session, profesor: schemas.ProfesorCreate) -> schemas.Profesor:
    _profesor = Profesor(**profesor.model_dump())
    db.add(_profesor)
    db.commit()
    db.refresh(
        _profesor
    )  # <- qué hace refresh()?: https://docs.sqlalchemy.org/en/21/orm/session_api.html#sqlalchemy.orm.Session.refresh
    return _profesor


def listar_profesores(db: Session) -> List[schemas.Profesor]:
    logger.info("Listando profesores desde servicios")
    return db.scalars(select(Profesor)).all()


def leer_profesor(db: Session, profesor_id: int) -> schemas.Profesor:
    db_profesor = db.scalar(select(Profesor).where(Profesor.id == profesor_id))
    if db_profesor is None:
        raise exceptions.ProfesorNoEncontrado() # <- usamos nuestras propias excepciones adaptadas al dominio de aplicación
    return db_profesor


def modificar_profesor(
    db: Session, profesor_id: int, profesor: schemas.ProfesorUpdate
) -> Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    db.execute(update(Profesor)
               .where(Profesor.id == profesor_id)
               .values(**profesor.model_dump()))
    db.commit()
    db.refresh(db_profesor)
    return db_profesor


def eliminar_profesor(db: Session, profesor_id: int) -> schemas.ProfesorDelete:
    db_profesor = leer_profesor(db, profesor_id)
    if len(db_profesor.cursos) > 0:
        raise exceptions.ProfesorTieneCursos()
    db.execute(
        delete(Profesor).where(Profesor.id == profesor_id)
    )
    db.commit()
    return db_profesor
