from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ModeloBase


class Curso(ModeloBase):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    titulo: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    creditos: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    profesor_id: Mapped[int] = mapped_column(
        ForeignKey("profesores.id"),
        nullable=False
    )

    profesor = relationship(
        "Profesor",
        back_populates="cursos"
    )

    inscripciones = relationship(
        "Inscripcion",
        back_populates="curso"
    )