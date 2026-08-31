from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.curso import schemas, services
from src.database import get_db

router = APIRouter(
    prefix="/cursos",
    tags=["cursos"]
)

@router.post("/", response_model=schemas.Curso)
def create_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    return services.create_curso(db=db, curso=curso)

@router.get("/", response_model=list[schemas.Curso])
def read_cursos(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return services.get_cursos(db, skip=skip, limit=limit)

@router.get("/{curso_id}", response_model=schemas.Curso)
def read_curso(curso_id: int, db: Session = Depends(get_db)):
    db_curso = services.get_curso(db, curso_id=curso_id)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return db_curso