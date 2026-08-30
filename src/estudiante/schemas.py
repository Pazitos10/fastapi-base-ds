from pydantic import BaseModel, ConfigDict, field_validator
from src.estudiante import exceptions
from typing import List

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class EstudianteBase(BaseModel):
    nombre: str
    legajo: int

    @field_validator("legajo")
    @classmethod
    def validar_legajo(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("El número de legajo debe ser un entero positivo.")
        return v

class EstudianteCreate(EstudianteBase):
    pass


class EstudianteUpdate(EstudianteBase):
    pass


class Estudiante(EstudianteBase):
    id: int
    inscripciones: List["Inscripcion"]

    # La siguiente opción nos permite instanciar schemas pydantic pasando modelos SQLAlchemy por parámetros.
    # De otro modo solo podríamos usar diccionarios.
    # Más info. sobre ConfigDict -> https://pydantic.dev/docs/validation/dev/api/pydantic/config
    model_config = ConfigDict(from_attributes = True)


class EstudianteDelete(EstudianteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

from src.inscripcion.schemas import Inscripcion

class PromedioEstudiante(BaseModel):
    estudiante_id: int
    nombre: str
    promedio: float | None

    model_config = ConfigDict(from_attributes=True)