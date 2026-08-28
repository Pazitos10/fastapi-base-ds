from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.cursos import schemas, services
from src.clases import schemas as esquemas_clase
from src.clases import services as servicios_clase

router = APIRouter(prefix="/cursos", tags=["cursos"])


@router.post("/", response_model=schemas.Curso)
def create_curso(datos: schemas.CursoCreate, db: Session = Depends(get_db)):
    return services.crear_curso(db, datos)


@router.get("/", response_model=list[schemas.Curso])
def read_cursos(db: Session = Depends(get_db)):
    return services.listar_cursos(db)


@router.get("/{curso_id}/clases", response_model=list[esquemas_clase.Clase])
def read_clases_del_curso(curso_id: int, db: Session = Depends(get_db)):
    services.leer_curso(db, curso_id)
    return servicios_clase.clases_de_un_curso(db, curso_id)


@router.get("/{curso_id}", response_model=schemas.Curso)
def read_curso(curso_id: int, db: Session = Depends(get_db)):
    return services.leer_curso(db, curso_id)


@router.put("/{curso_id}", response_model=schemas.Curso)
def update_curso(curso_id: int, datos: schemas.CursoUpdate, db: Session = Depends(get_db)):
    return services.modificar_curso(db, curso_id, datos)


@router.delete("/{curso_id}", response_model=schemas.CursoDelete)
def delete_curso(curso_id: int, db: Session = Depends(get_db)):
    return services.eliminar_curso(db, curso_id)
