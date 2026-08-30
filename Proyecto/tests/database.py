import pytest
from typing import Generator
from sqlalchemy import StaticPool, create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from src.main import app
from src.database import get_db
from src.config import settings
from src.models import ModeloBase
from src.departamento.services import crear_departamento
from src.departamento.schemas import DepartamentoCreate
from src.profesor.services import crear_profesor
from src.profesor.schemas import ProfesorCreate
from src.estudiante.services import crear_estudiante
from src.estudiante.schemas import EstudianteCreate
from src.curso.services import crear_curso
from src.curso.schemas import CursoCreate
from src.clase.services import crear_clase
from src.clase.schemas import ClaseCreate
from src.inscripcion.services import crear_inscripcion
from src.inscripcion.schemas import InscripcionCreate


# creamos una db para testing
engine = create_engine(
    settings.DB_URL_TEST,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    # utilizaremos esta funcion para "pisar" la que definimos en src/database.py.
    db = TestingSessionLocal()
    # Para usar restricciones de FK en SQLite, debemos habilitar la siguiente opción:
    db.execute(text("PRAGMA foreign_keys = ON"))
    try:
        print("Using test DB!")
        yield db
    finally:
        db.close()


# forzamos a fastapi para que utilice la db para testing.
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def session() -> Generator[Session, None, None]:
    # Creamos las tablas en la db de pruebas
    ModeloBase.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    # Para usar restricciones de FK en SQLite, debemos habilitar la siguiente opción:
    db.execute(text("PRAGMA foreign_keys = ON"))

    # Creamos datos iniciales (fixtures) respetando las dependencias (Foreign Keys)
    departamento_1 = crear_departamento(db, DepartamentoCreate(nombre="Informatica"))
    departamento_2 = crear_departamento(db, DepartamentoCreate(nombre="Matematica"))

    profesor_1 = crear_profesor(
        db, 
        ProfesorCreate(nombre="Carlos Perez", email="carlos@gmail.com", departemento_id=departamento_1.id)
    )

    estudiante_1 = crear_estudiante(
        db, 
        EstudianteCreate(nombre="Lucia Gomez", email="lucia@gmail.com")
    )
    estudiante_2 = crear_estudiante(
        db, 
        EstudianteCreate(nombre="Juan Lopez", email="juan@gmail.com")
    )

    curso_1 = crear_curso(
        db, 
        CursoCreate(nombre="Programacion I", descripcion="Introduccion a Python")
    )
    curso_2 = crear_curso(
        db, 
        CursoCreate(nombre="Base de Datos", descripcion="SQL y SQLAlchemy")
    )

    clase_1 = crear_clase(
        db, 
        ClaseCreate(titulo="Clase 1: Variables", curso_id=curso_1.id)
    )

    inscripcion_1 = crear_inscripcion(
        db, 
        InscripcionCreate(curso_id=curso_1.id, estudiante_id=estudiante_1.id, calificacion_final=8.0)
    )

    db.commit()

    yield db

    db.close()
    ModeloBase.metadata.drop_all(bind=engine)