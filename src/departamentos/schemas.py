from typing import Optional
from pydantic import BaseModel, ConfigDict


class DepartamentoBase(BaseModel):
    nombre: str


class DepartamentoCreate(DepartamentoBase):
    pass


class DepartamentoUpdate(BaseModel):
    nombre: Optional[str] = None


class Departamento(DepartamentoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class DepartamentoDelete(Departamento):
    pass
