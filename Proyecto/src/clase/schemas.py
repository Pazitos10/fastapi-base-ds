from pydantic import BaseModel, ConfigDict
from typing import Optional

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class ClaseBase(BaseModel):
    tema: str
    duracion_M: int
    curso_id: int


class ClaseCreate(ClaseBase):
    pass


class ClaseUpdate(ClaseBase):
    pass


class Clase(ClaseBase):
    id: int
    curso_id: Optional[int] = None

    # from_attributes=True permite que Pydantic trabaje con modelos SQLAlchemy
    # más info.: https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.from_attributes
    model_config = ConfigDict(from_attributes=True)