from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class ProfesorBase(BaseModel):
    nombre: str
    email: EmailStr
    fecha_ingreso: datetime


class ProfesorCreate(ProfesorBase):
    pass


class ProfesorUpdate(ProfesorBase):
    pass


class Profesor(ProfesorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ProfesorDelete(ProfesorBase):
    id: int