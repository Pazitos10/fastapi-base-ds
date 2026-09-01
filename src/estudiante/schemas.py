from pydantic import BaseModel, ConfigDict
from src.inscripcion.schemas import Inscripcion


class EstudianteBase(BaseModel):
    nombre: str
    legajo: int


class EstudianteCreate(EstudianteBase):
    pass


class EstudianteUpdate(EstudianteBase):
    pass


class Estudiante(EstudianteBase):
    id: int
    inscripciones: list[Inscripcion] = []

    model_config = ConfigDict(from_attributes=True)