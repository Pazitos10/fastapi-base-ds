from typing import Optional, List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Departamento(ModeloBase):
    __tablename__ = "departamento"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), index=True)
    
    profesor: Mapped[List["src.profesor.models.Profesor"]] = relationship(
        "src.profesor.models.Profesor", back_populates="departamento"
    )