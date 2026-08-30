from pydantic import BaseModel, ConfigDict
from typing import List, Optional
# Ajusta las siguientes importaciones según dónde tengas definidos estos schemas en tu proyecto

from src.inscripcion.schemas import Inscripcion

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class CursoBase(BaseModel):
    titulo: str
    creditos: float
    profesor_id: int


class CursoCreate(CursoBase):
    pass


class CursoUpdate(CursoBase):
    pass


class Curso(CursoBase):
    id: int
    profesor_id: int
    clases_ids: List[int] = []
    estudiantes: List[Inscripcion] = []

    # from_attributes=True permite que Pydantic trabaje con modelos SQLAlchemy
    # más info.: https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.from_attributes
    model_config = ConfigDict(from_attributes=True)