from typing import Optional
from pydantic import BaseModel, ConfigDict


class CursoBase(BaseModel):
    titulo: str
    creditos: int
    profesor_id: int


class CursoCreate(CursoBase):
    pass


class CursoUpdate(BaseModel):
    titulo: Optional[str] = None
    creditos: Optional[int] = None
    profesor_id: Optional[int] = None


class Curso(CursoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CursoDelete(Curso):
    pass
