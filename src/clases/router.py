from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.clases import schemas, services

router = APIRouter(prefix="/clases", tags=["clases"])


@router.post("/", response_model=schemas.Clase)
def create_clase(datos: schemas.ClaseCreate, db: Session = Depends(get_db)):
    return services.crear_clase(db, datos)


@router.get("/", response_model=list[schemas.Clase])
def read_clases(db: Session = Depends(get_db)):
    return services.listar_clases(db)


@router.get("/{clase_id}", response_model=schemas.Clase)
def read_clase(clase_id: int, db: Session = Depends(get_db)):
    return services.leer_clase(db, clase_id)


@router.put("/{clase_id}", response_model=schemas.Clase)
def update_clase(clase_id: int, datos: schemas.ClaseUpdate, db: Session = Depends(get_db)):
    return services.modificar_clase(db, clase_id, datos)


@router.delete("/{clase_id}", response_model=schemas.ClaseDelete)
def delete_clase(clase_id: int, db: Session = Depends(get_db)):
    return services.eliminar_clase(db, clase_id)
