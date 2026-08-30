from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Clase(ModeloBase):
    __tablename__ = "clase"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tema: Mapped[str] = mapped_column(String(200))
    duracion_M: Mapped[int]

    curso_id: Mapped[int] = mapped_column(ForeignKey("curso.id"))

    curso: Mapped["src.curso.models.Curso"] = relationship(
        "src.curso.models.Curso", back_populates="clases"
    )