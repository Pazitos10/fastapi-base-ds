from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.inscripciones import schemas, services

router = APIRouter(prefix="/inscripciones", tags=["inscripciones"])


@router.post("/", response_model=schemas.Inscripcion)
def create_inscripcion(datos: schemas.InscripcionCreate, db: Session = Depends(get_db)):
    return services.crear_inscripcion(db, datos)


@router.get("/", response_model=list[schemas.Inscripcion])
def read_inscripciones(db: Session = Depends(get_db)):
    return services.listar_inscripciones(db)


@router.get("/{insc_id}", response_model=schemas.Inscripcion)
def read_inscripcion(insc_id: int, db: Session = Depends(get_db)):
    return services.leer_inscripcion(db, insc_id)


@router.put("/{insc_id}", response_model=schemas.Inscripcion)
def update_inscripcion(
    insc_id: int, datos: schemas.InscripcionUpdate, db: Session = Depends(get_db)
):
    return services.modificar_inscripcion(db, insc_id, datos)


@router.delete("/{insc_id}", response_model=schemas.InscripcionDelete)
def delete_inscripcion(insc_id: int, db: Session = Depends(get_db)):
    return services.eliminar_inscripcion(db, insc_id)
