from pydantic import BaseModel, ConfigDict, field_validator
from typing import List
from src.departamento import exceptions

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class DepartamentoBase(BaseModel):
    nombre: str
    
    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("El nombre del departamento no puede estar vacío.")
        return v.strip()



class DepartamentoCreate(DepartamentoBase):
    pass


class DepartamentoUpdate(DepartamentoBase):
    pass


class Departamento(DepartamentoBase):
    id: int
    profesores: List["Profesor"]

    # La siguiente opción nos permite instanciar schemas pydantic pasando modelos SQLAlchemy por parámetros.
    # De otro modo solo podríamos usar diccionarios.
    # Más info. sobre ConfigDict -> https://pydantic.dev/docs/validation/dev/api/pydantic/config
    model_config = ConfigDict(from_attributes = True)


class DepartamentoDelete(DepartamentoBase):
    id: int
    model_config = ConfigDict(from_attributes = True)

from src.profesor.schemas import Profesor
