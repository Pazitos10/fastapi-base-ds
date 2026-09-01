from typing import List

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ModeloBase


class Estudiante(ModeloBase):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    legajo: Mapped[int] = mapped_column(Integer, nullable=False)

    inscripciones = relationship(
        "Inscripcion",
        back_populates="estudiante"
    )