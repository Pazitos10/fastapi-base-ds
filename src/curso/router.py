from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.curso import schemas, services


router = APIRouter(
    prefix="/cursos",
    tags=["cursos"]
)


@router.post("/", response_model=schemas.Curso)
def create_curso(
    curso: schemas.CursoCreate,
    db: Session = Depends(get_db)
):
    return services.crear_curso(db, curso)


@router.get("/", response_model=list[schemas.Curso])
def read_cursos(
    db: Session = Depends(get_db)
):
    return services.listar_cursos(db)


@router.get("/{curso_id}", response_model=schemas.Curso)
def read_curso(
    curso_id: int,
    db: Session = Depends(get_db)
):
    return services.leer_curso(db, curso_id)


@router.put("/{curso_id}", response_model=schemas.Curso)
def update_curso(
    curso_id: int,
    curso: schemas.CursoUpdate,
    db: Session = Depends(get_db)
):
    return services.modificar_curso(db, curso_id, curso)


@router.delete("/{curso_id}", response_model=schemas.Curso)
def delete_curso(
    curso_id: int,
    db: Session = Depends(get_db)
):
    return services.eliminar_curso(db, curso_id)