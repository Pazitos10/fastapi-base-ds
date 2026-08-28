from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr


class ProfesorBase(BaseModel):
    nombre: str
    email: EmailStr
    departamento_id: Optional[int] = None


class ProfesorCreate(ProfesorBase):
    fecha_ingreso: Optional[datetime] = None


class ProfesorUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    departamento_id: Optional[int] = None
    fecha_ingreso: Optional[datetime] = None


class Profesor(ProfesorBase):
    id: int
    fecha_ingreso: datetime

    model_config = ConfigDict(from_attributes=True)


class ProfesorDelete(Profesor):
    pass
