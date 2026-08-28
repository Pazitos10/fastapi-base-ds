from typing import Optional
from pydantic import BaseModel, ConfigDict


class EstudianteBase(BaseModel):
    nombre: str
    legajo: str


class EstudianteCreate(EstudianteBase):
    pass


class EstudianteUpdate(BaseModel):
    nombre: Optional[str] = None
    legajo: Optional[str] = None


class Estudiante(EstudianteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class EstudianteDelete(Estudiante):
    pass
