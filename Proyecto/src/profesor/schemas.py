from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List, Optional

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class ProfesorBase(BaseModel):
    nombre: str
    email: EmailStr
    fecha_ingreso: date | None = None
    departemento_id: int


class ProfesorCreate(ProfesorBase):
    pass


class ProfesorUpdate(ProfesorBase):
    pass


class Profesor(ProfesorBase):
    id: int
    cursos_ids: List[int]
    departamento_id: Optional[int] = None

    # from_atributes=True permite que Pydantic trabaje con modelos SQLAlchemy
    # más info.: https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.from_attributes
    model_config = ConfigDict(from_attributes= True)
