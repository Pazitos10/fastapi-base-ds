from datetime import date
from typing import Optional, List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Profesor(ModeloBase):

    __tablename__= "profesor"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str]
    fecha_ingreso: Mapped[date] = mapped_column(default=date.today)

    departemento_id: Mapped[int] = mapped_column(ForeignKey("departamento.id"))

    departamento: Mapped["src.departamento.models.Departamento"] = relationship("src.departamento.models.Departamento",back_populates="profesor")

    cursos: Mapped[List["src.curso.models.Curso"]] = relationship("src.curso.models.Curso",back_populates="profesor")
