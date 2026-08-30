import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.inscripcion import schemas, services

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/inscripciones", tags=["inscripciones"])

# Rutas para Inscripciones


@router.post("/", response_model=schemas.Inscripcion)
def create_inscripcion(inscripcion: schemas.InscripcionCreate, db: Session = Depends(get_db)):
    return services.crear_inscripcion(db, inscripcion)


@router.get("/", response_model=list[schemas.Inscripcion])
def read_inscripciones(db: Session = Depends(get_db)):
    logger.info("Consultando la lista de inscripciones desde endpoint...")  # <- este mensaje se verá por la terminal
    return services.listar_inscripciones(db)


@router.get("/{curso_id}/{estudiante_id}", response_model=schemas.Inscripcion)
def read_inscripcion(curso_id: int, estudiante_id: int, db: Session = Depends(get_db)):
    return services.leer_inscripcion(db, curso_id, estudiante_id)


@router.put("/{curso_id}/{estudiante_id}", response_model=schemas.Inscripcion)
def update_inscripcion(
    curso_id: int, 
    estudiante_id: int, 
    inscripcion: schemas.InscripcionUpdate, 
    db: Session = Depends(get_db)
):
    return services.modificar_inscripcion(db, curso_id, estudiante_id, inscripcion)


@router.delete("/{curso_id}/{estudiante_id}", response_model=schemas.Inscripcion)
def delete_inscripcion(curso_id: int, estudiante_id: int, db: Session = Depends(get_db)):
    return services.eliminar_inscripcion(db, curso_id, estudiante_id)