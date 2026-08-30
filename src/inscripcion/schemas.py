from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class InscripcionBase(BaseModel):
    fechaInscripcion: datetime
    calificacionFinal: Optional[int] = None

class InscripcionCreate(InscripcionBase):
    estudianteId: int
    cursoId: int


class InscripcionUpdate(InscripcionBase):
    pass

class Inscripcion(InscripcionBase):
    estudianteId: int
    cursoId: int

    model_config = ConfigDict(from_attributes=True)

class InscripcionDelete(InscripcionBase):
    pass