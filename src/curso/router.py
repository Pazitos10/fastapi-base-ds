import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.curso import schemas, services

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/cursos", tags=["cursos"])

@router.post("/", response_model = schemas.Curso)
def create_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    return services.crearCurso(db, curso)

@router.get("/{cursoId}", response_model = schemas.Curso)
def read_curso(cursoId: int, db: Session = Depends(get_db)):
    return services.leerCurso(db, cursoId)

@router.put("/{cursoId}", response_model = schemas.Curso)
def update_curso(cursoId: int, curso: schemas.CursoUpdate, db: Session = Depends(get_db)):
    return services.modificarCurso(db, cursoId, curso)

@router.delete("/{cursoId}", response_model = schemas.CursoDelete)
def delete_curso(cursoId: int, db: Session = Depends(get_db)):
    return services.eliminarCurso(db, cursoId)

