from pydantic import BaseModel, ConfigDict
from typing import Optional


class CursoBase(BaseModel):
    titulo: str
    creditos: int

class CursoCreate(CursoBase):
    profesorId: Optional[int] = None


class CursoUpdate(CursoBase):
    pass

class Curso(CursoBase):
    id: int
    profesorId: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class CursoDelete(CursoBase):
    id: int
    titulo: str
