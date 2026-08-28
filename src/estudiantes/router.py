from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.estudiantes import schemas, services

router = APIRouter(prefix="/estudiantes", tags=["estudiantes"])


@router.post("/", response_model=schemas.Estudiante)
def create_estudiante(datos: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    return services.crear_estudiante(db, datos)


@router.get("/", response_model=list[schemas.Estudiante])
def read_estudiantes(db: Session = Depends(get_db)):
    return services.listar_estudiantes(db)


@router.get("/{alumno_id}", response_model=schemas.Estudiante)
def read_estudiante(alumno_id: int, db: Session = Depends(get_db)):
    return services.leer_estudiante(db, alumno_id)


@router.put("/{alumno_id}", response_model=schemas.Estudiante)
def update_estudiante(
    alumno_id: int, datos: schemas.EstudianteUpdate, db: Session = Depends(get_db)
):
    return services.modificar_estudiante(db, alumno_id, datos)


@router.delete("/{alumno_id}", response_model=schemas.EstudianteDelete)
def delete_estudiante(alumno_id: int, db: Session = Depends(get_db)):
    return services.eliminar_estudiante(db, alumno_id)
