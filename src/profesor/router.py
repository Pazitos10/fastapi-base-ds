import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.profesor import schemas, services

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/profesores", tags=["profesores"])

@router.post("/", response_model = schemas.Profesor)
def create_profesor(profesor: schemas.ProfesorCreate, db: Session = Depends(get_db)):
    return services.crearProfesor(db, profesor)

@router.get("/{profesorId}", response_model = schemas.Profesor)
def read_profesor(profesorId: int, db: Session = Depends(get_db)):
    return services.leerProfesor(db, profesorId)

@router.put("/{profesorId}", response_model = schemas.Profesor)
def update_profesor(profesorId: int, profesor: schemas.ProfesorUpdate, db: Session = Depends(get_db)):
    return services.modificarProfesor(db, profesorId, profesor)

@router.delete("/{profesorId}", response_model = schemas.ProfesorDelete)
def delete_profesor(profesorId: int, db: Session = Depends(get_db)):
    return services.eliminarProfesor(db, profesorId)

