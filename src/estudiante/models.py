from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from src.models import ModeloBase


class Estudiante(ModeloBase):
    __tablename__ = "estudiantes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))
    legajo: Mapped[int] = mapped_column(unique=True)
    
    inscripciones: Mapped[List["src.inscripcion.models.Inscripcion"]] = relationship(back_populates="estudiante")

