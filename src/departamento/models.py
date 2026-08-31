from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase

class Departamento(ModeloBase):
    __tablename__ = "departamento"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))

    profesores: Mapped[list["Profesor"]] = relationship(back_populates="departamento")