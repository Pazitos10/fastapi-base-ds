from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.profesores.models import Profesor
from src.profesores import schemas, exceptions
from src.departamentos.models import Departamento


def _chequear_depto(db: Session, depto_id: int | None):
    if depto_id is None:
        return
    depto = db.scalar(select(Departamento).where(Departamento.id == depto_id))
    if depto is None:
        raise exceptions.DepartamentoInexistente()


def crear_profesor(db: Session, datos: schemas.ProfesorCreate) -> schemas.Profesor:
    _chequear_depto(db, datos.departamento_id)
    repetido = db.scalar(select(Profesor).where(Profesor.email == datos.email))
    if repetido is not None:
        raise exceptions.EmailDuplicado()
    campos = datos.model_dump(exclude_unset=True)
    if campos.get("fecha_ingreso") is None:
        campos.pop("fecha_ingreso", None)
    profe = Profesor(**campos)
    db.add(profe)
    db.commit()
    db.refresh(profe)
    return profe


def listar_profesores(db: Session) -> List[schemas.Profesor]:
    return db.scalars(select(Profesor)).all()


def leer_profesor(db: Session, profe_id: int) -> schemas.Profesor:
    profe = db.scalar(select(Profesor).where(Profesor.id == profe_id))
    if profe is None:
        raise exceptions.ProfesorNoEncontrado()
    return profe


def modificar_profesor(
    db: Session, profe_id: int, datos: schemas.ProfesorUpdate
) -> Profesor:
    profe = leer_profesor(db, profe_id)
    cambios = datos.model_dump(exclude_unset=True)
    if "departamento_id" in cambios:
        _chequear_depto(db, cambios["departamento_id"])
    if "email" in cambios:
        otro = db.scalar(
            select(Profesor).where(
                Profesor.email == cambios["email"],
                Profesor.id != profe_id,
            )
        )
        if otro is not None:
            raise exceptions.EmailDuplicado()
    db.execute(update(Profesor).where(Profesor.id == profe_id).values(**cambios))
    db.commit()
    db.refresh(profe)
    return profe


def eliminar_profesor(db: Session, profe_id: int) -> schemas.ProfesorDelete:
    profe = leer_profesor(db, profe_id)
    if len(profe.cursos) > 0:
        raise exceptions.ProfesorDictaCursos()
    db.execute(delete(Profesor).where(Profesor.id == profe_id))
    db.commit()
    return profe
