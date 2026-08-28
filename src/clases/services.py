from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.clases.models import Clase
from src.clases import schemas, exceptions
from src.cursos.models import Curso


def crear_clase(db: Session, datos: schemas.ClaseCreate) -> schemas.Clase:
    materia = db.scalar(select(Curso).where(Curso.id == datos.curso_id))
    if materia is None:
        raise exceptions.CursoInexistente()
    sesion = Clase(**datos.model_dump())
    db.add(sesion)
    db.commit()
    db.refresh(sesion)
    return sesion


def listar_clases(db: Session) -> List[schemas.Clase]:
    return db.scalars(select(Clase)).all()


def leer_clase(db: Session, clase_id: int) -> schemas.Clase:
    sesion = db.scalar(select(Clase).where(Clase.id == clase_id))
    if sesion is None:
        raise exceptions.ClaseNoEncontrada()
    return sesion


def modificar_clase(db: Session, clase_id: int, datos: schemas.ClaseUpdate) -> Clase:
    sesion = leer_clase(db, clase_id)
    cambios = datos.model_dump(exclude_unset=True)
    if "curso_id" in cambios:
        materia = db.scalar(select(Curso).where(Curso.id == cambios["curso_id"]))
        if materia is None:
            raise exceptions.CursoInexistente()
    db.execute(update(Clase).where(Clase.id == clase_id).values(**cambios))
    db.commit()
    db.refresh(sesion)
    return sesion


def eliminar_clase(db: Session, clase_id: int) -> schemas.ClaseDelete:
    sesion = leer_clase(db, clase_id)
    db.execute(delete(Clase).where(Clase.id == clase_id))
    db.commit()
    return sesion


def clases_de_un_curso(db: Session, curso_id: int) -> List[schemas.Clase]:
    return db.scalars(
        select(Clase)
        .join(Curso)
        .where(Curso.id == curso_id)
        .order_by(Clase.id)
    ).all()
