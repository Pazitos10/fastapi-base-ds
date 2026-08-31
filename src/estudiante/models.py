from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase

class Estudiante(ModeloBase):
    __tablename__ = "estudiante"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    legajo: Mapped[int] 
    nombre: Mapped[str] = mapped_column(String(20))

    # Relación escrita como texto
    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="estudiante")