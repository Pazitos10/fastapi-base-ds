from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.departamentos.models import Departamento
from src.departamentos import schemas, exceptions


# operaciones CRUD para Departamento


def crear_departamento(db: Session, departamento: schemas.DepartamentoCreate) -> schemas.Departamento:

    existe = db.scalar(select(Departamento).where(Departamento.nombre == departamento.nombre))
    
    if existe is not None:
        raise exceptions.NombreDuplicado()

    _departamento = Departamento(**departamento.model_dump())
    db.add(_departamento)
    db.commit()
    db.refresh(_departamento)  # <- qué hace refresh()?: https://docs.sqlalchemy.org/en/21/orm/session_api.html#sqlalchemy.orm.Session.refresh
    return _departamento


def listar_departamentos(db: Session) -> List[schemas.Departamento]:
    return db.scalars(select(Departamento)).all()


def leer_departamento(db: Session, departamento_id: int) -> schemas.Departamento:
    db_departamento = db.scalar(select(Departamento).where(Departamento.id == departamento_id))
    if db_departamento is None:
        raise exceptions.DepartamentoNoEncontrado() # <- usamos nuestras propias excepciones adaptadas al dominio de aplicación
    return db_departamento


def modificar_departamento(
    db: Session, departamento_id: int, departamento: schemas.DepartamentoUpdate
) -> Departamento:
    db_departamento = leer_departamento(db, departamento_id)

    if departamento.nombre is not None:
        existe = db.scalar(
            select(Departamento).where(
                Departamento.nombre == departamento.nombre,
                Departamento.id != departamento_id,
            )
        )    
    if existe is not None:
        raise exceptions.NombreDuplicado()

    db.execute(update(Departamento)
               .where(Departamento.id == departamento_id)
               .values(**departamento.model_dump(exclude_unset = True)))
    db.commit()
    db.refresh(db_departamento)
    return db_departamento


def eliminar_departamento(db: Session, departamento_id: int) -> schemas.DepartamentoDelete:
    db_departamento = leer_departamento(db, departamento_id)

    if len(db_departamento.profesores) > 0:
        raise exceptions.DepartamentoTieneProfesores()

    db.execute(
        delete(Departamento).where(Departamento.id == departamento_id)
    )
    db.commit()
    return db_departamento
