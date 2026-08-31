from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

class ProfesorBase(BaseModel):
    nombre:str 
    email:EmailStr
    id_departamento:int

class ProfesorCreate(ProfesorBase):
    fecha_ingeso: datetime

class Profesor(ProfesorBase):
    id:int

    model_config = ConfigDict(from_attributes=True)