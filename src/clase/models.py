from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from src.models import ModeloBase
import src

class Clase(ModeloBase):
    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(60))
    duracionMinutos: Mapped[int] = mapped_column(Integer)

    cursoId: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped["src.curso.models.Curso"] = relationship(back_populates="clases")