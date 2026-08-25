
from sqlalchemy import ForeignKey,Float,String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.profesor.models import Profesor
    from src.clases.models import Clase
    from src.inscripciones.models import Inscripcion
    from src.estudiantes.models import Estudiante

class Curso(ModeloBase):

    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)    
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[float] = mapped_column(Float)

    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped["Profesor"] = relationship (back_populates="cursos")

    clases: Mapped[list["Clase"]] = relationship(back_populates="curso")

    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="curso")
    
    estudiantes: Mapped[list["Estudiante"]] = relationship(secondary="inscripciones", back_populates="cursos", viewonly=True) 
