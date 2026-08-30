from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from src.models import ModeloBase


class Curso(ModeloBase):
    __tablename__ = "cursos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column()
    
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped["src.profesor.models.Profesor"] = relationship(back_populates="cursos")
    clases: Mapped[List["src.clase.models.Clase"]] = relationship(back_populates="curso")
    inscripciones: Mapped[List["src.inscripcion.models.Inscripcion"]] = relationship(back_populates="curso")
    
    @property
    def nombre_profesor(self) -> str:
        return self.profesor.nombre if self.profesor else ""