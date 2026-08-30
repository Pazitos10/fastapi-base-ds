from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.departamento.models import Departamento
from src.departamento import schemas, exceptions

def crearDepartamento(db: Session, departamento: schemas.DepartamentoCreate) -> schemas.Departamento: 
    _departamento = Departamento(**departamento.model_dump())
    db.add(_departamento)
    db.commit()
    db.refresh(_departamento)
    return _departamento

def leerDepartamento(db: Session, departamentoId: int) -> schemas.Departamento:
    db_departamento = db.scalar(select(Departamento).where(Departamento.id == departamentoId))
    if db_departamento is None:
        raise exceptions.DepartamentoNoEncontrado()
    return db_departamento

def modificarDepartamento(db: Session, departamentoId: int, departamento: schemas.DepartamentoUpdate) -> schemas.DepartamentoUpdate:
    db_departamento = leerDepartamento(db, departamentoId)
    db.execute(update(Departamento).where(Departamento.id == departamentoId).values(**departamento.model_dump()))
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

def eliminarDepartamento(db: Session, departamentoId: int) -> schemas.DepartamentoDelete:
    db_departamento = leerDepartamento(db, departamentoId)
    db.execute(delete(Departamento).where(Departamento.id == departamentoId))
    db.commit()
    return db_departamento

