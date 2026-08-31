from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase

class Curso(ModeloBase):
    __tablename__ = "curso"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(20))
    creditos: Mapped[int]
    id_profesor: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    
    profesor: Mapped["Profesor"] = relationship(back_populates="cursos")
    clases: Mapped[list["Clase"]] = relationship(back_populates="curso")
    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="curso")