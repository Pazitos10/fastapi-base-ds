from src.inscripcion.constants import ErrorCode
from src.exceptions import NotFound

class InscripcionNoEncontrada(NotFound):
    DETAIL = ErrorCode.INSCRIPCION_NO_ENCONTRADA