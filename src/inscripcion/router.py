from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.inscripcion import schemas, services
from src.database import get_db

router = APIRouter(
    prefix="/inscripciones",
    tags=["inscripciones"]
)

@router.post("/", response_model=schemas.Inscripcion)
def create_inscripcion(inscripcion: schemas.InscripcionCreate, db: Session = Depends(get_db)):
    return services.create_inscripcion(db=db, inscripcion=inscripcion)

@router.get("/", response_model=list[schemas.Inscripcion])
def read_inscripciones(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return services.get_inscripciones(db, skip=skip, limit=limit)

@router.get("/{estudiante_id}/{curso_id}", response_model=schemas.Inscripcion)
def read_inscripcion(estudiante_id: int, curso_id: int, db: Session = Depends(get_db)):
    db_inscripcion = services.get_inscripcion(db, estudiante_id=estudiante_id, curso_id=curso_id)
    if db_inscripcion is None:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return db_inscripcion