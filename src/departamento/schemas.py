from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional, List
from datetime import datetime

class DepartamentoBase(BaseModel):
    nombre: str

class DepartamentoCreate(DepartamentoBase):
    pass

class DepartamentoUpdate(DepartamentoBase):
    pass

class Departamento(DepartamentoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class DepartamentoDelete(DepartamentoBase):
    id: int
    nombre: str
