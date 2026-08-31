from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional
from src.models import ModeloBase

class Inscripcion(ModeloBase):
    __tablename__ = "inscripcion"
    
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiante.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("curso.id"), primary_key=True)
    fecha_inscripcion: Mapped[datetime]
    
    calificacion_final: Mapped[Optional[float]] = mapped_column(
        CheckConstraint('calificacion_final >= 1 AND calificacion_final <= 10')
    )
    
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")
    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")