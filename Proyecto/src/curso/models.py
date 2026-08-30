from typing import Optional, List
from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase



class Curso(ModeloBase):
    __tablename__ = "curso"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))
    creditos: Mapped[float] = mapped_column(Float)

    profesor: Mapped["src.profesor.models.Profesor"] = relationship(
        "src.profesor.models.Profesor", back_populates="cursos"
    )
    clases: Mapped[List["src.clase.models.Clase"]] = relationship(
        "src.clase.models.Clase", back_populates="curso", cascade="all, delete-orphan"
    )
    estudiantes: Mapped[List["src.inscripcion.models.Inscripcion"]] = relationship(
        "src.inscripcion.models.Inscripcion", back_populates="curso"
    )