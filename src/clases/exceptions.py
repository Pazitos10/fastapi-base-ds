from src.clases.constants import ErrorCode
from src.exceptions import NotFound

class ClaseNoEncontrada(NotFound):
    DETAIL = ErrorCode.CLASE_NO_ENCONTRADA

