from src.exceptions import NotFound
from src.inscripcion.constants import ErrorCode


class InscripcionNoEncontrada(NotFound):
    DETAIL = ErrorCode.INSCRIPCION_NO_ENCONTRADA