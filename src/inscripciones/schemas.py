from typing import Optional
from pydantic import BaseModel, ConfigDict


class InscripcionBase(BaseModel):
    estudiante_id: int
    curso_id: int


class InscripcionCreate(InscripcionBase):
    pass


class InscripcionUpdate(BaseModel):
    estudiante_id: Optional[int] = None
    curso_id: Optional[int] = None


class Inscripcion(InscripcionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class InscripcionDelete(Inscripcion):
    pass
