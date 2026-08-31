from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase

class Clase(ModeloBase):
    __tablename__ = "clase"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("curso.id"))
    tema: Mapped[str] = mapped_column(String(20))
    duracion_minutos: Mapped[int]

    curso: Mapped["Curso"] = relationship(back_populates="clases")