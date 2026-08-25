from sqlalchemy import ForeignKey,UniqueConstraint, DateTime, Float, CheckConstraint
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.estudiantes.models import Estudiante
    from src.cursos.models import Curso

class Inscripcion(ModeloBase):

    __tablename__ = "inscripciones"
    __table_args__ = (UniqueConstraint("estudiante_id", "curso_id", name="uq_estudiante_curso"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    calificacion_final: Mapped[Optional[float]] = mapped_column(Float, CheckConstraint("calificacion_final >= 0 AND calificacion_final <= 10"), nullable=True) 

    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"))
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))

    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")