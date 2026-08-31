from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class InscripcionBase(BaseModel):
    estudiante_id: int
    curso_id: int
    fecha_inscripcion: datetime
    calificacion_final: Optional[float] = None

class InscripcionCreate(InscripcionBase):
    pass

class Inscripcion(InscripcionBase):
    model_config = ConfigDict(from_attributes=True)