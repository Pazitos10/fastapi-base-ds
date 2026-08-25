from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer,String
from src.models import ModeloBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.inscripciones.models import Inscripcion
    from src.cursos.models import Curso

class Estudiante(ModeloBase):

    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    legajo: Mapped[int] = mapped_column(Integer,unique=True, index=True)

    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="estudiante")

    cursos: Mapped[list["Curso"]] = relationship(secondary="inscripciones", back_populates="estudiantes", viewonly=True)