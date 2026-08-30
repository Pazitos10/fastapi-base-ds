from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from src.models import ModeloBase
import src

class Estudiante(ModeloBase):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(40))
    legajo: Mapped[int] = mapped_column(Integer)

    inscripciones: Mapped[List["src.inscripcion.models.Inscripcion"]] = relationship(back_populates="estudiante")
    cursos: Mapped[List["src.curso.models.Curso"]] = relationship(secondary="inscripciones", back_populates="estudiantes", viewonly = True)