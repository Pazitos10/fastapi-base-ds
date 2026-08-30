import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.departamento import schemas, services

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/departamentos", tags=["departamentos"])

@router.post("/", response_model = schemas.Departamento)
def create_departamento(departamento: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    return services.crearDepartamento(db, departamento)

@router.get("/{departamentoId}", response_model = schemas.Departamento)
def read_departamento(departamentoId: int, db: Session = Depends(get_db)):
    return services.leerDepartamento(db, departamentoId)

@router.put("/{departamentoId}", response_model = schemas.Departamento)
def update_departamento(departamentoId: int, departamento: schemas.DepartamentoUpdate, db: Session = Depends(get_db)):
    return services.modificarDepartamento(db, departamentoId, departamento)

@router.delete("/{departamentoId}", response_model = schemas.DepartamentoDelete)
def delete_departamento(departamentoId: int, db: Session = Depends(get_db)):
    return services.eliminarDepartamento(db, departamentoId)

