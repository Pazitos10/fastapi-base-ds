from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import datetime
from src.models import ModeloBase


class Profesor(ModeloBase):
    __tablename__ = "profesores"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(20))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)
    
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    
    departamento: Mapped["src.departamento.models.Departamento"] = relationship(back_populates="profesores")
    cursos: Mapped[List["src.curso.models.Curso"]] = relationship(back_populates="profesor")
    
    @property
    def nombre_departamento(self) -> str:
        return self.departamento.nombre if self.departamento else ""
