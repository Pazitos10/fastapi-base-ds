from pydantic import BaseModel, ConfigDict, field_validator
from src.curso import exceptions
from typing import List

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class CursoBase(BaseModel):
    titulo: str
    creditos: int
    profesor_id: int
    
    @field_validator("creditos")
    @classmethod
    def validar_creditos(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Los créditos del curso deben ser mayor a 0.")
        return v


class CursoCreate(CursoBase):
    pass


class CursoUpdate(CursoBase):
    pass


class Curso(CursoBase):
    id: int
    nombre_profesor: str
    clases: List["Clase"]
    inscripciones: List["Inscripcion"]

    # La siguiente opción nos permite instanciar schemas pydantic pasando modelos SQLAlchemy por parámetros.
    # De otro modo solo podríamos usar diccionarios.
    # Más info. sobre ConfigDict -> https://pydantic.dev/docs/validation/dev/api/pydantic/config
    model_config = ConfigDict(from_attributes = True)


class CursoDelete(CursoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ContadorInscritos(BaseModel):
    curso_id: int
    titulo: str
    total_estudiantes: int

    model_config = ConfigDict(from_attributes=True)

from src.clase.schemas import Clase
from src.inscripcion.schemas import Inscripcion
