from pydantic import BaseModel, ConfigDict, field_validator

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class ClaseBase(BaseModel):
    tema: str
    duracion_minutos: int
    curso_id: int
    
    @field_validator("duracion_minutos")
    @classmethod
    def validar_duracion(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("La duración debe ser mayor a 0 minutos.")
        return v


class ClaseCreate(ClaseBase):
    pass


class ClaseUpdate(ClaseBase):
    pass


class Clase(ClaseBase):
    id: int
    titulo_curso: str

    # La siguiente opción nos permite instanciar schemas pydantic pasando modelos SQLAlchemy por parámetros.
    # De otro modo solo podríamos usar diccionarios.
    # Más info. sobre ConfigDict -> https://pydantic.dev/docs/validation/dev/api/pydantic/config
    model_config = ConfigDict(from_attributes = True)


class ClaseDelete(ClaseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
