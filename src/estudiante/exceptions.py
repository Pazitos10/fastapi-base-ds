from src.exceptions import NotFound
from src.estudiante.constants import ErrorCode


class EstudianteNoEncontrado(NotFound):
    DETAIL = ErrorCode.ESTUDIANTE_NO_ENCONTRADO