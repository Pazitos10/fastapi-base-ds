from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.departamentos.models import Departamento
from src.departamentos import schemas, exceptions


def crear_departamento(db: Session, datos: schemas.DepartamentoCreate) -> schemas.Departamento:
    existe = db.scalar(select(Departamento).where(Departamento.nombre == datos.nombre))
    if existe is not None:
        raise exceptions.NombreDuplicado()
    depto = Departamento(**datos.model_dump())
    db.add(depto)
    db.commit()
    db.refresh(depto)
    return depto


def listar_departamentos(db: Session) -> List[schemas.Departamento]:
    return db.scalars(select(Departamento)).all()


def leer_departamento(db: Session, depto_id: int) -> schemas.Departamento:
    depto = db.scalar(select(Departamento).where(Departamento.id == depto_id))
    if depto is None:
        raise exceptions.DepartamentoNoEncontrado()
    return depto


def modificar_departamento(
    db: Session, depto_id: int, datos: schemas.DepartamentoUpdate
) -> Departamento:
    depto = leer_departamento(db, depto_id)
    cambios = datos.model_dump(exclude_unset=True)
    if "nombre" in cambios:
        otro = db.scalar(
            select(Departamento).where(
                Departamento.nombre == cambios["nombre"],
                Departamento.id != depto_id,
            )
        )
        if otro is not None:
            raise exceptions.NombreDuplicado()
    db.execute(update(Departamento).where(Departamento.id == depto_id).values(**cambios))
    db.commit()
    db.refresh(depto)
    return depto


def eliminar_departamento(db: Session, depto_id: int) -> schemas.DepartamentoDelete:
    depto = leer_departamento(db, depto_id)
    if len(depto.profesores) > 0:
        raise exceptions.DepartamentoConProfesores()
    db.execute(delete(Departamento).where(Departamento.id == depto_id))
    db.commit()
    return depto
