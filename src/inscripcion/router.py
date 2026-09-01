from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.inscripcion import schemas, services


router = APIRouter(
    prefix="/inscripciones",
    tags=["inscripciones"]
)


@router.post("/", response_model=schemas.Inscripcion)
def create_inscripcion(
    inscripcion: schemas.InscripcionCreate,
    db: Session = Depends(get_db)
):
    return services.crear_inscripcion(
        db,
        inscripcion
    )


@router.get("/", response_model=list[schemas.Inscripcion])
def read_inscripciones(
    db: Session = Depends(get_db)
):
    return services.listar_inscripciones(db)


@router.get(
    "/{inscripcion_id}",
    response_model=schemas.Inscripcion
)
def read_inscripcion(
    inscripcion_id: int,
    db: Session = Depends(get_db)
):
    return services.leer_inscripcion(
        db,
        inscripcion_id
    )


@router.put(
    "/{inscripcion_id}",
    response_model=schemas.Inscripcion
)
def update_inscripcion(
    inscripcion_id: int,
    inscripcion: schemas.InscripcionUpdate,
    db: Session = Depends(get_db)
):
    return services.modificar_inscripcion(
        db,
        inscripcion_id,
        inscripcion
    )


@router.delete(
    "/{inscripcion_id}",
    response_model=schemas.Inscripcion
)
def delete_inscripcion(
    inscripcion_id: int,
    db: Session = Depends(get_db)
):
    return services.eliminar_inscripcion(
        db,
        inscripcion_id
    )