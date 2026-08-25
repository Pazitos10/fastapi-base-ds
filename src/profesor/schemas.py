from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import datetime
from typing import Optional,List
from src.cursos.schemas import Curso 

class ProfesorBase(BaseModel):
    nombre: str
    email: EmailStr
    departamento_id: int

class ProfesorCreate(ProfesorBase):
    fecha_ingreso: Optional[datetime] = None

class ProfesorUpdate(ProfesorBase):
    pass

class Profesor(ProfesorBase):
    id: int
    fecha_ingreso: datetime
    cursos: List[Curso] = []

class ProfesorDelete(ProfesorBase):
    id: int
    departamento_id: int

    model_config = ConfigDict(from_attributes=True)
