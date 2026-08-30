from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.database import engine
from src.models import ModeloBase

# Importamos la configuración validada por Pydantic
from src.config import settings

# Importamos configuracion de logger
from src.logger import setup_logging

# Importamos los routers desde nuestros modulos
from src.departamento.router import router as departamento_router
from src.curso.router import router as curso_router
from src.profesor.router import router as profesor_router
from src.clase.router import router as clase_router
from src.estudiante.router import router as estudiante_router
from src.inscripcion.router import router as inscripcion_router
from fastapi.middleware.cors import CORSMiddleware

# Rebuild schemas to resolve forward references after all imports
from src.profesor.schemas import Profesor, Curso
from src.departamento.schemas import Departamento
from src.estudiante.schemas import Estudiante
from src.inscripcion.schemas import Inscripcion
from src.clase.schemas import Clase

Profesor.model_rebuild()
Departamento.model_rebuild()
Curso.model_rebuild()
Estudiante.model_rebuild()
Inscripcion.model_rebuild()
Clase.model_rebuild()

ENV = settings.ENV.upper()
ROOT_PATH = getattr(settings, f"ROOT_PATH_{ENV}", "")

setup_logging()

@asynccontextmanager
async def db_creation_lifespan(app: FastAPI):
    ModeloBase.metadata.create_all(bind=engine)
    yield


app = FastAPI(root_path=ROOT_PATH, lifespan=db_creation_lifespan)

origins = [
    "http://localhost:5173", # para recibir requests desde app React (puerto: 5173)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# asociamos los routers a nuestra app
app.include_router(departamento_router)
app.include_router(curso_router)
app.include_router(profesor_router)
app.include_router(clase_router)
app.include_router(estudiante_router)
app.include_router(inscripcion_router)
