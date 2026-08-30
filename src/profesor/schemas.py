from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime

class ProfesorBase(BaseModel):
    nombre: str
    email: EmailStr
    fechaIngreso: datetime

class ProfesorCreate(ProfesorBase):
    departamentoId:  Optional[int] = None

    

class ProfesorUpdate(ProfesorBase):
    pass

class Profesor(ProfesorBase):
    id: int
    departamentoId: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class ProfesorDelete(ProfesorBase):
    id: int
    nombre: str
