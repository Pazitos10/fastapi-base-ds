from pydantic import BaseModel, ConfigDict, field_validator, EmailStr
from datetime import datetime
from typing import List
from src.profesor import exceptions

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class ProfesorBase(BaseModel):
    nombre: str
    email: EmailStr
    fecha_ingreso: datetime
    departamento_id: int
    
    @field_validator("fecha_ingreso")
    @classmethod
    def validar_fecha_pasada(cls, v: datetime) -> datetime:
        if v > datetime.now():
            raise ValueError("La fecha de ingreso no puede ser en el futuro.")
        return v


class ProfesorCreate(ProfesorBase):
    pass


class ProfesorUpdate(ProfesorBase):
    pass


class Profesor(ProfesorBase):
    id: int
    nombre_departamento: str
    cursos: List["Curso"]

    # La siguiente opción nos permite instanciar schemas pydantic pasando modelos SQLAlchemy por parámetros.
    # De otro modo solo podríamos usar diccionarios.
    # Más info. sobre ConfigDict -> https://pydantic.dev/docs/validation/dev/api/pydantic/config
    model_config = ConfigDict(from_attributes = True)


class ProfesorDelete(ProfesorBase):
    id: int
    model_config = ConfigDict(from_attributes = True)
    

from src.curso.schemas import Curso
