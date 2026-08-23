from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Departamento(ModeloBase):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), index=True)

    profesores: Mapped[List["src.profesores.models.Profesor"]] = relationship(
        "src.profesores.models.Profesor", back_populates="departamento"
    )