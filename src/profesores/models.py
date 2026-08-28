from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase

if TYPE_CHECKING:
    from src.departamentos.models import Departamento
    from src.cursos.models import Curso


class Profesor(ModeloBase):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    departamento_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("departamentos.id"), nullable=True
    )

    departamento: Mapped[Optional["Departamento"]] = relationship(
        back_populates="profesores"
    )
    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")
