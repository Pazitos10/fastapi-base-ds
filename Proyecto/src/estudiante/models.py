from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Estudiante(ModeloBase):
    __tablename__ = "estudiante"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(200))
    legajo: Mapped[int]

    cursos: Mapped[List["src.inscripcion.models.Inscripcion"]] = relationship(
        "src.inscripcion.models.Inscripcion", back_populates="estudiante"
    )