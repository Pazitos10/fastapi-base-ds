import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.inscripcion import schemas, services

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/inscripciones", tags=["inscripciones"])

# Rutas para Inscripcions


@router.post("/", response_model=schemas.Inscripcion)
def create_inscripcion(inscripcion: schemas.InscripcionCreate, db: Session = Depends(get_db)):
    return services.crear_inscripcion(db, inscripcion)


@router.get("/", response_model=list[schemas.Inscripcion])
def read_inscripcions(db: Session = Depends(get_db)):
    logger.info("Listando inscripcions desde router") # <- este mensaje se verá por la terminal
    return services.listar_inscripciones(db)


@router.get("/{estudiante_id}/{curso_id}", response_model=schemas.Inscripcion)
def read_inscripcion(estudiante_id: int, curso_id: int, db: Session = Depends(get_db)):
    return services.leer_inscripcion(db, estudiante_id, curso_id)

@router.put("/{estudiante_id}/{curso_id}", response_model=schemas.Inscripcion)
def update_inscripcion(
    estudiante_id: int, curso_id: int, inscripcion: schemas.InscripcionUpdate, db: Session = Depends(get_db)
):
    return services.modificar_inscripcion(db, estudiante_id, curso_id, inscripcion)


@router.delete("/{estudiante_id}/{curso_id}", response_model=schemas.InscripcionDelete)
def delete_inscripcion(estudiante_id: int, curso_id: int, db: Session = Depends(get_db)):
    return services.eliminar_inscripcion(db, estudiante_id, curso_id)

@router.post("/inscribir", response_model=schemas.Inscripcion, tags=["Inscribir"])
def create_matricula_estudiante(inscripcion: schemas.InscripcionCreate, db: Session = Depends(get_db)):
    return services.matricular_estudiante(db, inscripcion)