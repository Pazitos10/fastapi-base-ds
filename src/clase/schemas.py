from pydantic import BaseModel, ConfigDict

class ClaseBase(BaseModel):
    curso_id: int
    tema: str
    duracion_minutos: int

class ClaseCreate(ClaseBase):
    pass

class Clase(ClaseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)