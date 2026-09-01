from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.estudiante import schemas, services


router = APIRouter(
    prefix="/estudiantes",
    tags=["estudiantes"]
)


@router.post("/", response_model=schemas.Estudiante)
def create_estudiante(
    estudiante: schemas.EstudianteCreate,
    db: Session = Depends(get_db)
):
    return services.crear_estudiante(
        db,
        estudiante
    )


@router.get("/", response_model=list[schemas.Estudiante])
def read_estudiantes(
    db: Session = Depends(get_db)
):
    return services.listar_estudiantes(db)


@router.get("/{estudiante_id}", response_model=schemas.Estudiante)
def read_estudiante(
    estudiante_id: int,
    db: Session = Depends(get_db)
):
    return services.leer_estudiante(
        db,
        estudiante_id
    )


@router.put("/{estudiante_id}", response_model=schemas.Estudiante)
def update_estudiante(
    estudiante_id: int,
    estudiante: schemas.EstudianteUpdate,
    db: Session = Depends(get_db)
):
    return services.modificar_estudiante(
        db,
        estudiante_id,
        estudiante
    )


@router.delete("/{estudiante_id}", response_model=schemas.Estudiante)
def delete_estudiante(
    estudiante_id: int,
    db: Session = Depends(get_db)
):
    return services.eliminar_estudiante(
        db,
        estudiante_id
    )