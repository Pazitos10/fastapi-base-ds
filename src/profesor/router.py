from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Importamos nuestros esquemas y servicios
from src.profesor import schemas, services
from src.database import get_db

router = APIRouter(
    prefix="/profesor",
    tags=["profesor"]
)

@router.post("/", response_model=schemas.Profesor)
def create_profesor(profesor: schemas.ProfesorCreate, db: Session = Depends(get_db)):
    return services.create_profesor(db=db, profesor=profesor)

@router.get("/", response_model=list[schemas.Profesor])
def read_profesores(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return services.get_profesores(db, skip=skip, limit=limit)

@router.get("/{profesor_id}", response_model=schemas.Profesor)
def read_profesor(profesor_id: int, db: Session = Depends(get_db)):
    db_profesor = services.get_profesor(db, profesor_id=profesor_id)
    if db_profesor is None:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return db_profesor