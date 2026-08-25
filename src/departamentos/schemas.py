from pydantic import BaseModel, ConfigDict
from typing import Optional

class DepartamentoBase(BaseModel):
    nombre: str
    
class DepartamentoCreate(DepartamentoBase):
    pass

class DepartamentoUpdate(DepartamentoBase):
    nombre: Optional[str] = None

class Departamento(DepartamentoBase):
    id: int

    model_config = ConfigDict(from_attributes= True)

class DepartamentoDelete(Departamento):
    pass