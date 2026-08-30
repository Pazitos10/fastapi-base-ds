from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase



class Clase(ModeloBase):
    __tablename__ = "clases"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(150))
    duracion_minutos: Mapped[int] = mapped_column()
    
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped["src.curso.models.Curso"] = relationship(back_populates="clases")
    @property
    def titulo_curso(self) -> str:
        return self.curso.titulo if self.curso else ""