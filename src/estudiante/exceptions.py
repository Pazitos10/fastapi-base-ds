from src.estudiante.constants import ErrorCode
from src.exceptions import NotFound

class EstudianteNoEncontrado(NotFound):
    DETAIL = ErrorCode.ESTUDIANTE_NO_ENCONTRADO