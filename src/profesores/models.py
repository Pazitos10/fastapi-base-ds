from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Profesor(ModeloBase):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), index=True)
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)

    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    departamento: Mapped["src.departamentos.models.Departamento"] = relationship(
        "src.departamentos.models.Departamento", back_populates="profesores"
    )