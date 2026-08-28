from typing import TYPE_CHECKING, List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase

if TYPE_CHECKING:
    from src.cursos.models import Curso
    from src.inscripciones.models import Inscripcion


class Estudiante(ModeloBase):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80))
    legajo: Mapped[str] = mapped_column(String(20), unique=True)

    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante")
    materias: Mapped[List["Curso"]] = relationship(
        secondary="inscripciones", back_populates="alumnos", viewonly=True
    )
