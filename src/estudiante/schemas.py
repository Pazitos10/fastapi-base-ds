
from pydantic import BaseModel, ConfigDict

class EstudianteBase(BaseModel):
    nombre: str
    legajo: int



class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(EstudianteBase):
    pass

class Estudiante(EstudianteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class EstudianteDelete(EstudianteBase):
    id: int
    nombre: str
    legajo: int