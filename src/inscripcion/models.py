from datetime import date

from sqlalchemy import Date, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ModeloBase


class Inscripcion(ModeloBase):
    __tablename__ = "inscripciones"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    estudiante_id: Mapped[int] = mapped_column(
        ForeignKey("estudiantes.id"),
        nullable=False
    )

    curso_id: Mapped[int] = mapped_column(
        ForeignKey("cursos.id"),
        nullable=False
    )

    fecha_inscripcion: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    calificacion_final: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    estudiante = relationship(
        "Estudiante",
        back_populates="inscripciones"
    )

    curso = relationship(
        "Curso",
        back_populates="inscripciones"
    )

    __table_args__ = (
        UniqueConstraint(
            "estudiante_id",
            "curso_id",
            name="uq_estudiante_curso"
        ),
    )