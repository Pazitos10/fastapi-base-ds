from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.profesores import schemas, services

router = APIRouter(prefix="/profesores", tags=["profesores"])


@router.post("/", response_model=schemas.Profesor)
def create_profesor(datos: schemas.ProfesorCreate, db: Session = Depends(get_db)):
    return services.crear_profesor(db, datos)


@router.get("/", response_model=list[schemas.Profesor])
def read_profesores(db: Session = Depends(get_db)):
    return services.listar_profesores(db)


@router.get("/{profe_id}", response_model=schemas.Profesor)
def read_profesor(profe_id: int, db: Session = Depends(get_db)):
    return services.leer_profesor(db, profe_id)


@router.put("/{profe_id}", response_model=schemas.Profesor)
def update_profesor(
    profe_id: int, datos: schemas.ProfesorUpdate, db: Session = Depends(get_db)
):
    return services.modificar_profesor(db, profe_id, datos)


@router.delete("/{profe_id}", response_model=schemas.ProfesorDelete)
def delete_profesor(profe_id: int, db: Session = Depends(get_db)):
    return services.eliminar_profesor(db, profe_id)
