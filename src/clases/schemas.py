from typing import Optional
from pydantic import BaseModel, ConfigDict


class ClaseBase(BaseModel):
    tema: str
    duracion_minutos: int
    curso_id: int


class ClaseCreate(ClaseBase):
    pass


class ClaseUpdate(BaseModel):
    tema: Optional[str] = None
    duracion_minutos: Optional[int] = None
    curso_id: Optional[int] = None


class Clase(ClaseBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ClaseDelete(Clase):
    pass
