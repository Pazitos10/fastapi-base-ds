from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from src.models import ModeloBase


class Departamento(ModeloBase):
    __tablename__ = "departamentos"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(30), index=True, unique=True)
    profesores: Mapped[List["src.profesor.models.Profesor"]] = relationship(back_populates="departamento")

