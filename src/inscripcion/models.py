from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from src.models import ModeloBase
from datetime import datetime
import src

class Inscripcion(ModeloBase):
    __tablename__ = "inscripciones"

    estudianteId: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    cursoId: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)

    fechaInscripcion: Mapped[datetime] = mapped_column(DateTime)
    calificacionFinal: Mapped[Optional[int]] = mapped_column(Integer)

    estudiante: Mapped["src.estudiante.models.Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["src.curso.models.Curso"] = relationship(back_populates="inscripciones")