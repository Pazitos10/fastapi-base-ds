from pydantic import BaseModel, ConfigDict

class CursoBase(BaseModel):
    titulo: str
    creditos: int
    id_profesor: int

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)