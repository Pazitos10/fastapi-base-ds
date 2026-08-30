import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.estudiante import schemas, services

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/estudiantes", tags=["estudiantes"])

@router.post("/", response_model = schemas.Estudiante)
def create_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    return services.crearEstudiante(db, estudiante)

@router.get("/{estudianteId}", response_model = schemas.Estudiante)
def read_estudiante(estudianteId: int, db: Session = Depends(get_db)):
    return services.leerEstudiante(db, estudianteId)

@router.put("/{estudianteId}", response_model = schemas.Estudiante)
def update_estudiante(estudianteId: int, estudiante: schemas.EstudianteUpdate, db: Session = Depends(get_db)):
    return services.modificarEstudiante(db, estudianteId, estudiante)

@router.delete("/{estudianteId}", response_model = schemas.EstudianteDelete)
def delete_estudiante(estudianteId: int, db: Session = Depends(get_db)):
    return services.eliminarEstudiante(db, estudianteId)

