from pydantic import BaseModel, ConfigDict, field_validator
from src.inscripcion import exceptions
from datetime import datetime
# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class InscripcionBase(BaseModel):
    estudiante_id: int
    curso_id: int
    fecha_inscripcion: datetime
    calificacion_final: float
    
    @field_validator("calificacion_final")
    @classmethod
    def validar_nota(cls, v: float) -> float:
        if v < 0.0 or v > 10.0:
            raise ValueError("La calificación final debe encontrarse entre 0.0 y 10.0.")
        return v


class InscripcionCreate(InscripcionBase):
    pass


class InscripcionUpdate(InscripcionBase):
    fecha_inscripcion: datetime
    calificacion_final: float
    
    @field_validator("calificacion_final")
    @classmethod
    def validar_nota_update(cls, v: float) -> float:
        if v < 0.0 or v > 10.0:
            raise ValueError("La calificación final debe encontrarse entre 0.0 y 10.0.")
        return v


class Inscripcion(InscripcionBase):

    # La siguiente opción nos permite instanciar schemas pydantic pasando modelos SQLAlchemy por parámetros.
    # De otro modo solo podríamos usar diccionarios.
    # Más info. sobre ConfigDict -> https://pydantic.dev/docs/validation/dev/api/pydantic/config
    model_config = ConfigDict(from_attributes = True)


class InscripcionDelete(InscripcionBase):
    model_config = ConfigDict(from_attributes = True)
