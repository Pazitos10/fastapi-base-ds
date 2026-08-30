from datetime import date
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Inscripcion(ModeloBase):
    __tablename__ = "inscripcion"

    curso_id: Mapped[int] = mapped_column(ForeignKey("curso.id"), primary_key=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiante.id"), primary_key=True)
    fecha_inscripcion: Mapped[date] = mapped_column(default=date.today)
    calificacion_final: Mapped[float]
    extra_data: Mapped[Optional[str]] = None

    estudiante: Mapped["src.estudiante.models.Estudiante"] = relationship(
        "src.estudiante.models.Estudiante", back_populates="cursos"
    )
    curso: Mapped["src.curso.models.Curso"] = relationship(
        "src.curso.models.Curso", back_populates="estudiantes"
    )