from pydantic import BaseModel, ConfigDict
from typing import List
from src.inscripcion.schemas import Inscripcion

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class EstudianteBase(BaseModel):
    nombre: str
    legajo: int


class EstudianteCreate(EstudianteBase):
    pass


class EstudianteUpdate(EstudianteBase):
    pass


class Estudiante(EstudianteBase):
    id: int
    cursos: List[Inscripcion] = []

    # from_attributes=True permite que Pydantic trabaje con modelos SQLAlchemy
    # más info.: https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.from_attributes
    model_config = ConfigDict(from_attributes=True)