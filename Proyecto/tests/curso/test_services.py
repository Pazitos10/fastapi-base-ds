import pytest
from datetime import date
from sqlalchemy.orm import Session
from tests.database import session
from src.curso import exceptions
from src.curso.services import (
    listar_cursos,
    crear_curso,
    modificar_curso,
    leer_curso,
    eliminar_curso,
    agregar_clase_a_curso,
    matricular_estudiante,
)
from src.curso.schemas import CursoCreate, CursoUpdate
from src.clase.schemas import ClaseCreate


def test_crear_curso(session: Session) -> None:
    nombre = "Fisica I"
    descripcion = "Curso introductorio de fisica"
    curso_3 = crear_curso(
        session, 
        CursoCreate(nombre=nombre, descripcion=descripcion)
    )
    assert curso_3.nombre == nombre
    assert curso_3.descripcion == descripcion


def test_modificar_curso(session: Session) -> None:
    nuevo_nombre = "Fisica I Avanzada"
    curso_id = 1  # Asumiendo que el curso con ID 1 existe en tus fixtures de prueba
    curso_1 = leer_curso(session, curso_id)
    curso_1 = modificar_curso(
        session, 
        curso_id, 
        CursoUpdate(
            nombre=nuevo_nombre, 
            descripcion=curso_1.descripcion
        )
    )
    assert curso_1.nombre == nuevo_nombre


def test_eliminar_curso(session: Session) -> None:
    # Intentamos borrar un curso que tenga estudiantes inscriptos (según tus fixtures base).
    # Verificamos que se lanza la excepción esperada.
    with pytest.raises(exceptions.CursoTieneInscriptos):
        curso_id = 1
        eliminar_curso(session, curso_id)

    # Probamos crear un curso nuevo sin inscriptos y eliminarlo.
    nombre = "Curso Temporal"
    descripcion = "Temporal"
    curso_nuevo = crear_curso(
        session, 
        CursoCreate(nombre=nombre, descripcion=descripcion)
    )

    cursos_antes = listar_cursos(session)

    eliminar_curso(session, curso_nuevo.id)

    cursos_despues = listar_cursos(session)
    assert len(cursos_despues) == len(cursos_antes) - 1


def test_listar_cursos(session: Session) -> None:
    cursos = listar_cursos(session)
    assert isinstance(cursos, list)
    assert len(cursos) > 0


def test_agregar_clase_a_curso(session: Session) -> None:
    curso_id = 1
    titulo_clase = "Introduccion a la materia"
    
    curso_actualizado = agregar_clase_a_curso(
        session, 
        curso_id, 
        ClaseCreate(titulo=titulo_clase)
    )
    
    # Verificamos que la clase se haya añadido al curso
    titulos_clases = [clase.titulo for clase in curso_actualizado.clases]
    assert titulo_clase in titulos_clases


def test_matricular_estudiante(session: Session) -> None:
    # Asumiendo un curso con ID 2 y un estudiante con ID 2 que no estén ya matriculados entre sí
    curso_id = 2
    estudiante_id = 2
    calificacion = 9.0

    inscripcion = matricular_estudiante(
        session,
        curso_id=curso_id,
        estudiante_id=estudiante_id,
        calificacion_final=calificacion,
        fecha_inscripcion=date.today()
    )

    assert inscripcion.curso_id == curso_id
    assert inscripcion.estudiante_id == estudiante_id
    assert inscripcion.calificacion_final == calificacion