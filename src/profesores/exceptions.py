from src.profesores.constants import ErrorCode
from src.exceptions import NotFound


class ProfesorNoEncontrado(NotFound):
    DETAIL = ErrorCode.PROFESOR_NO_ENCONTRADO