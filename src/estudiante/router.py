from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.estudiante import schemas, services
from src.database import get_db

router = APIRouter(
    prefix="/estudiantes",
    tags=["estudiantes"]
)

@router.post("/", response_model=schemas.Estudiante)
def create_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    return services.create_estudiante(db=db, estudiante=estudiante)

@router.get("/", response_model=list[schemas.Estudiante])
def read_estudiantes(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return services.get_estudiantes(db, skip=skip, limit=limit)

@router.get("/{estudiante_id}", response_model=schemas.Estudiante)
def read_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    db_estudiante = services.get_estudiante(db, estudiante_id=estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante