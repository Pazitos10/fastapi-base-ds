from pydantic import BaseModel, ConfigDict


class CursoBase(BaseModel):
    titulo: str
    creditos: int
    profesor_id: int


class CursoCreate(CursoBase):
    pass


class CursoUpdate(CursoBase):
    pass


class Curso(CursoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)