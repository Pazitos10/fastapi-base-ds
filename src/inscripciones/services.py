from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.inscripciones.models import Inscripcion
from src.inscripciones import schemas, exceptions
from src.estudiantes.models import Estudiante
from src.cursos.models import Curso


def crear_inscripcion(db: Session, datos: schemas.InscripcionCreate) -> schemas.Inscripcion:
    alumno = db.scalar(select(Estudiante).where(Estudiante.id == datos.estudiante_id))
    if alumno is None:
        raise exceptions.EstudianteInexistente()
    materia = db.scalar(select(Curso).where(Curso.id == datos.curso_id))
    if materia is None:
        raise exceptions.CursoInexistente()
    ya_esta = db.scalar(
        select(Inscripcion).where(
            Inscripcion.estudiante_id == datos.estudiante_id,
            Inscripcion.curso_id == datos.curso_id,
        )
    )
    if ya_esta is not None:
        raise exceptions.YaInscripto()
    fila = Inscripcion(**datos.model_dump())
    db.add(fila)
    db.commit()
    db.refresh(fila)
    return fila


def listar_inscripciones(db: Session) -> List[schemas.Inscripcion]:
    return db.scalars(select(Inscripcion)).all()


def leer_inscripcion(db: Session, insc_id: int) -> schemas.Inscripcion:
    fila = db.scalar(select(Inscripcion).where(Inscripcion.id == insc_id))
    if fila is None:
        raise exceptions.InscripcionNoEncontrada()
    return fila


def modificar_inscripcion(
    db: Session, insc_id: int, datos: schemas.InscripcionUpdate
) -> Inscripcion:
    fila = leer_inscripcion(db, insc_id)
    cambios = datos.model_dump(exclude_unset=True)
    alumno_id = cambios.get("estudiante_id", fila.estudiante_id)
    materia_id = cambios.get("curso_id", fila.curso_id)
    alumno = db.scalar(select(Estudiante).where(Estudiante.id == alumno_id))
    if alumno is None:
        raise exceptions.EstudianteInexistente()
    materia = db.scalar(select(Curso).where(Curso.id == materia_id))
    if materia is None:
        raise exceptions.CursoInexistente()
    choque = db.scalar(
        select(Inscripcion).where(
            Inscripcion.estudiante_id == alumno_id,
            Inscripcion.curso_id == materia_id,
            Inscripcion.id != insc_id,
        )
    )
    if choque is not None:
        raise exceptions.YaInscripto()
    db.execute(update(Inscripcion).where(Inscripcion.id == insc_id).values(**cambios))
    db.commit()
    db.refresh(fila)
    return fila


def eliminar_inscripcion(db: Session, insc_id: int) -> schemas.InscripcionDelete:
    fila = leer_inscripcion(db, insc_id)
    db.execute(delete(Inscripcion).where(Inscripcion.id == insc_id))
    db.commit()
    return fila
