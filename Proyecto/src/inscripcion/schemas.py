from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class InscripcionBase(BaseModel):
    curso_id: int
    estudiante_id: int
    fecha_inscripcion: date | None = None
    calificacion_final: float
    extra_data: Optional[str] = None


class InscripcionCreate(InscripcionBase):
    pass


class InscripcionUpdate(InscripcionBase):
    pass


class Inscripcion(InscripcionBase):
    # from_attributes=True permite que Pydantic trabaje con modelos SQLAlchemy
    # más info.: https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.from_attributes
    model_config = ConfigDict(from_attributes=True)