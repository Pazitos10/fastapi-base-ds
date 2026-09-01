from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ModeloBase


class Profesor(ModeloBase):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    cursos = relationship(
        "Curso",
        back_populates="profesor"
    )