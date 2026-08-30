from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from src.models import ModeloBase
import src

class Curso(ModeloBase):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(40))
    creditos: Mapped[int] = mapped_column(Integer)

    profesorId: Mapped[Optional[int]] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped[Optional["src.profesor.models.Profesor"]] = relationship(back_populates="cursos")

    clases: Mapped[List["src.clase.models.Clase"]] = relationship(back_populates="curso")

    inscripciones: Mapped[List["src.inscripcion.models.Inscripcion"]] = relationship(back_populates="curso")
    estudiantes: Mapped[List["src.estudiante.models.Estudiante"]] = relationship(secondary="inscripciones", back_populates="cursos", viewonly=True)