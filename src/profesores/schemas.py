from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class ProfesorBase(BaseModel):
    nombre: str
    email: EmailStr
    fecha_ingreso: datetime


class ProfesorCreate(ProfesorBase):
    departamento_id: int


class ProfesorUpdate(ProfesorBase):
    departamento_id: int


class Profesor(ProfesorBase):
    id: int
    departamento_id: int

    model_config = ConfigDict(from_attributes=True)


class ProfesorDelete(ProfesorBase):
    id: int