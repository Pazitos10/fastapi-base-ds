import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.profesor.models import Profesor
from src.profesor import schemas, exceptions
from src.curso.models import Curso
from src.departamento.models import Departamento
# Creamos un logger para este módulo específico
logger = logging.getLogger(__name__)

# Operaciones CRUD para Profesores

def crear_profesor(db: Session, profesor: schemas.ProfesorCreate) -> schemas.Profesor:
    _profesor = Profesor(**profesor.model_dump())
    db.add(_profesor)
    db.commit()
    db.refresh(_profesor)
    return _profesor


def listar_profesores(db: Session) -> List[schemas.Profesor]:
    logger.info("Listando profesores desde services")
    return db.scalars(select(Profesor)).all()


def leer_profesor(db: Session, profesor_id: int) -> schemas.Profesor:
    db_profesor = db.scalar(select(Profesor).where(Profesor.id == profesor_id))
    if db_profesor is None:
        raise exceptions.ProfesorNoEncontrado()  # Asegúrate de crear esta excepción en exceptions.py
    return db_profesor


def modificar_profesor(
    db: Session, profesor_id: int, profesor: schemas.ProfesorUpdate
) -> Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    db.execute(
        update(Profesor).where(Profesor.id == profesor_id).values(**profesor.model_dump())
    )
    db.commit()
    db.refresh(db_profesor)
    return db_profesor


def eliminar_profesor(db: Session, profesor_id: int) -> schemas.Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    # Como un profesor tiene cursos asociados, validamos que no tenga cursos antes de borrarlo (según tu regla de negocio)
    if len(db_profesor.cursos) > 0:
        raise exceptions.ProfesorTieneCursos()  # O la excepción que prefieras para evitar borrar profes con cursos
    db.execute(delete(Profesor).where(Profesor.id == profesor_id))
    db.commit()
    return db_profesor

def asignar_curso_a_profesor(db: Session, profesor_id: int, curso_id: int) -> Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    
    
    db_curso = db.scalar(select(Curso).where(Curso.id == curso_id))
    if db_curso is None:
        raise exceptions.CursoNoEncontrado()  

    
    if db_curso in db_profesor.cursos:
        raise exceptions.CursoDuplicado()


    db_profesor.cursos.append(db_curso)
    db.commit()
    db.refresh(db_profesor)
    return db_profesor

def asignar_departamento_a_profesor(db: Session, profesor_id: int, departamento_id: int) -> Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    
    db_departamento = db.scalar(select(Departamento).where(Departamento.id == departamento_id))
    if db_departamento is None:
        raise exceptions.DepartamentoNoEncontrado()

    db_profesor.departamento_id = db_departamento.id
    db.commit()
    db.refresh(db_profesor)
    return db_profesor