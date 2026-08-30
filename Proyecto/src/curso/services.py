from datetime import date
import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.curso.models import Curso
from src.curso import schemas, exceptions
from src.clase.models import Clase
from src.estudiante.models import Estudiante
from src.inscripcion.models import Inscripcion

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

# operaciones CRUD para Cursos

def crear_curso(db: Session, curso: schemas.CursoCreate) -> schemas.Curso:
    _curso = Curso(**curso.model_dump())
    db.add(_curso)
    db.commit()
    db.refresh(_curso)
    return _curso


def listar_cursos(db: Session) -> List[schemas.Curso]:
    logger.info("Listando cursos desde services")  # <- este mensaje se verá por la terminal
    return db.scalars(select(Curso)).all()


def leer_curso(db: Session, curso_id: int) -> schemas.Curso:
    db_curso = db.scalar(select(Curso).where(Curso.id == curso_id))
    if db_curso is None:
        raise exceptions.CursoNoEncontrado()
    return db_curso


def modificar_curso(
    db: Session, curso_id: int, curso: schemas.CursoUpdate
) -> Curso:
    db_curso = leer_curso(db, curso_id)
    db.execute(
        update(Curso).where(Curso.id == curso_id).values(**curso.model_dump())
    )
    db.commit()
    db.refresh(db_curso)
    return db_curso


def eliminar_curso(db: Session, curso_id: int) -> schemas.Curso:
    db_curso = leer_curso(db, curso_id)
    if len(db_curso.estudiantes) > 0:
        raise exceptions.CursoTieneInscriptos()
    db.execute(delete(Curso).where(Curso.id == curso_id))
    db.commit()
    return db_curso

def agregar_clase_a_curso(db: Session, curso_id: int, clase_data: schemas.ClaseCreate) -> Curso:
    db_curso = leer_curso(db, curso_id)
    
    # Creamos la clase usando el ID del curso asegurándonos de asociarla
    nueva_clase = Clase(**clase_data.model_dump(), curso_id=db_curso.id)
    
    db.add(nueva_clase)
    db.commit()
    db.refresh(db_curso)
    return db_curso

def matricular_estudiante(
    db: Session, 
    curso_id: int, 
    estudiante_id: int, 
    calificacion_final: float, 
    fecha_inscripcion: date = date.today()
) -> Inscripcion:
    #Buscamos el curso y el estudiante
    db_curso = leer_curso(db, curso_id)
    db_estudiante = db.scalar(select(Estudiante).where(Estudiante.id == estudiante_id))
    
    if db_estudiante is None:
        raise exceptions.EstudianteNoEncontrado()
        
    #Validar si ya está inscripto para evitar duplicados
    inscripcion_existente = db.scalar(
        select(Inscripcion).where(
            Inscripcion.curso_id == curso_id, 
            Inscripcion.estudiante_id == estudiante_id
        )
    )
    if inscripcion_existente:
        raise exceptions.EstudianteYaInscripto()

    #Creamos la inscripción con los datos extra
    nueva_inscripcion = Inscripcion(
        curso=db_curso,
        estudiante=db_estudiante,
        fecha_inscripcion=fecha_inscripcion,
        calificacion_final=calificacion_final
    )
    
    db.add(nueva_inscripcion)
    db.commit()
    db.refresh(nueva_inscripcion)
    return nueva_inscripcion