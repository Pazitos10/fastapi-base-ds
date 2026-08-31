from pydantic import BaseModel, ConfigDict

class DepartamentoBase(BaseModel):
    nombre: str

class DepartamentoCreate(DepartamentoBase):
    pass

class Departamento(DepartamentoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)