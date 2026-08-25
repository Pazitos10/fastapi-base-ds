from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String
from src.models import ModeloBase
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.departamentos.models import Departamento
    from src.cursos.models import Curso

class Profesor(ModeloBase):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)

    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    departamento: Mapped["Departamento"] = relationship(back_populates="profesores")
    
    cursos: Mapped[list["Curso"]] = relationship(back_populates="profesor")