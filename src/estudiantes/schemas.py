from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class EstudianteBase(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    legajo: int = Field(gt=0, description="Legajo numérico positivo")

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(BaseModel):
    nombre: Optional[str] = Field(default=None, min_length=3, max_length=100)
    legajo: Optional[int] = Field(
        default=None, gt=0, description="Legajo numérico positivo"
    )


# 4. Schema de respuesta al consultar (GET)
class Estudiante(EstudianteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class EstudianteDelete(Estudiante):
    pass