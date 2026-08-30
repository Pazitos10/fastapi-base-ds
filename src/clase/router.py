import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.clase import schemas, services

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/clases", tags=["clases"])

@router.post("/", response_model = schemas.Clase)
def create_clase(clase: schemas.ClaseCreate, db: Session = Depends(get_db)):
    return services.crearClase(db, clase)

@router.get("/{claseId}", response_model = schemas.Clase)
def read_clase(claseId: int, db: Session = Depends(get_db)):
    return services.leerClase(db, claseId)

@router.put("/{claseId}", response_model = schemas.Clase)
def update_clase(claseId: int, clase: schemas.ClaseUpdate, db: Session = Depends(get_db)):
    return services.modificarClase(db, claseId, clase)

@router.delete("/{claseId}", response_model = schemas.ClaseDelete)
def delete_clase(claseId: int, db: Session = Depends(get_db)):
    return services.eliminarClase(db, claseId)

