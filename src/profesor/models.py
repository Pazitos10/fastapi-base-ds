from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List, Optional
from src.models import ModeloBase
import src

class Profesor(ModeloBase):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(String(60))
    fechaIngreso: Mapped[datetime] = mapped_column(DateTime)

    departamentoId: Mapped[Optional[int]] = mapped_column(ForeignKey("departamentos.id"))
    departamento: Mapped[Optional["src.departamento.models.Departamento"]] = relationship(back_populates="profesores")

    cursos: Mapped[List["src.curso.models.Curso"]] = relationship(back_populates="profesor")

