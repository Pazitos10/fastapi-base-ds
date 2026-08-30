from pydantic import BaseModel, ConfigDict
from typing import Optional


class ClaseBase(BaseModel):
    tema: str
    duracionMinutos: int

class ClaseCreate(ClaseBase):
    cursoId: Optional[int] = None


class ClaseUpdate(ClaseBase):
    pass

class Clase(ClaseBase):
    id: int
    cursoId: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class ClaseDelete(ClaseBase):
    id: int
    tema: str
    duracionMinutos: int
