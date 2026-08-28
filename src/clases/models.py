from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.cursos.models import Curso


class Clase(ModeloBase):
    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(200))
    duracion_minutos: Mapped[int] = mapped_column(Integer)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))

    curso: Mapped["Curso"] = relationship(back_populates="clases")
