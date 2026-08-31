from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column, relationship
from datetime import datetime
from src.models import ModeloBase


class Profesor(ModeloBase):
    __tablename__ = "profesores"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_departamento: Mapped[int] = mapped_column(ForeignKey("departamento.id"))
    nombre: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(20))
    fecha_ingreso: Mapped[datetime]

    departamento: Mapped["Departamento"] = relationship(back_populates="profesores")
    cursos: Mapped[list["Curso"]] = relationship(back_populates="profesor")