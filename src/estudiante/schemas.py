from pydantic import BaseModel, ConfigDict

class EstudianteBase(BaseModel):
    legajo: int
    nombre: str

class EstudianteCreate(EstudianteBase):
    pass

class Estudiante(EstudianteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)