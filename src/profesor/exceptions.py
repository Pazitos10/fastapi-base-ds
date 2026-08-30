from typing import List
from src.profesor.constants import ErrorCode
from src.exceptions import NotFound

class ProfesorNoEncontrado(NotFound):
    DETAIL = ErrorCode.PROFESOR_NO_ENCONTRADO