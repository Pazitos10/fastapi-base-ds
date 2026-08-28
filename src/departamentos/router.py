from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.departamentos import schemas, services

router = APIRouter(prefix="/departamentos", tags=["departamentos"])


@router.post("/", response_model=schemas.Departamento)
def create_departamento(datos: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    return services.crear_departamento(db, datos)


@router.get("/", response_model=list[schemas.Departamento])
def read_departamentos(db: Session = Depends(get_db)):
    return services.listar_departamentos(db)


@router.get("/{depto_id}", response_model=schemas.Departamento)
def read_departamento(depto_id: int, db: Session = Depends(get_db)):
    return services.leer_departamento(db, depto_id)


@router.put("/{depto_id}", response_model=schemas.Departamento)
def update_departamento(
    depto_id: int, datos: schemas.DepartamentoUpdate, db: Session = Depends(get_db)
):
    return services.modificar_departamento(db, depto_id, datos)


@router.delete("/{depto_id}", response_model=schemas.DepartamentoDelete)
def delete_departamento(depto_id: int, db: Session = Depends(get_db)):
    return services.eliminar_departamento(db, depto_id)
