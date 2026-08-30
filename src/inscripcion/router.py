import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.inscripcion import schemas, services

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/inscripciones", tags=["inscripciones"])

@router.post("/", response_model = schemas.Inscripcion)
def create_inscripcion(inscripcion: schemas.InscripcionCreate, db: Session = Depends(get_db)):
    return services.crearInscripcion(db, inscripcion)

@router.get("/{estudianteId}/{cursoId}", response_model = schemas.Inscripcion)
def read_inscripcion(estudianteId: int, cursoId: int, db: Session = Depends(get_db)):
    return services.leerInscripcion(db, estudianteId, cursoId)

@router.put("/{estudianteId}/{cursoId}", response_model = schemas.Inscripcion)
def update_inscripcion(estudianteId: int, cursoId: int, inscripcion: schemas.InscripcionUpdate, db: Session = Depends(get_db)):
    return services.modificarInscripcion(db, estudianteId, cursoId, inscripcion)

@router.delete("/{estudianteId}/{cursoId}", response_model = schemas.InscripcionDelete)
def delete_inscripcion(estudianteId: int, cursoId: int, db: Session = Depends(get_db)):
    return services.eliminarInscripcion(db, estudianteId, cursoId)

