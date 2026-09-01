from datetime import date

from pydantic import BaseModel, ConfigDict


class InscripcionBase(BaseModel):
    estudiante_id: int
    curso_id: int
    fecha_inscripcion: date
    calificacion_final: float | None = None


class InscripcionCreate(InscripcionBase):
    pass


class InscripcionUpdate(BaseModel):
    fecha_inscripcion: date
    calificacion_final: float | None = None


class Inscripcion(InscripcionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)