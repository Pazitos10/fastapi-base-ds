from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from src.models import ModeloBase


class Inscripcion(ModeloBase):
    __tablename__ = "inscripciones"
        
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)
    
    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime)
    calificacion_final: Mapped[float] = mapped_column()
    
    
    estudiante: Mapped["src.estudiante.models.Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["src.curso.models.Curso"] = relationship(back_populates="inscripciones")
    