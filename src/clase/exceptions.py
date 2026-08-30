from typing import List
from src.clase.constants import ErrorCode
from src.exceptions import NotFound, BadRequest



class ClaseNoEncontrada(NotFound):
    DETAIL = ErrorCode.CLASE_NO_ENCONTRADA