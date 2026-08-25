from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class InscripcionBase(BaseModel):
    estudiante_id: int = Field(gt=0, description="ID del estudiante")
    curso_id: int = Field(gt=0, description="ID del curso")
    calificacion_final: Optional[float] = Field(default=None, ge=0.0, le=10.0,
        description="Calificación entre 0 y 10",
    )

class InscripcionCreate(InscripcionBase):
    pass

class InscripcionUpdate(BaseModel):
    calificacion_final: Optional[float] = Field(
        default=None, ge=0.0, le=10.0
    )

class Inscripcion(InscripcionBase):
    id: int
    fecha_inscripcion: datetime

    model_config = ConfigDict(from_attributes=True)

class InscripcionDelete(Inscripcion):
    pass