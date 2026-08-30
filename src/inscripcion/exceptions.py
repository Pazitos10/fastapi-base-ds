from typing import List
from src.inscripcion.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class InscripcionNoEncontrada(NotFound):
    DETAIL = ErrorCode.INSCRIPCION_NO_ENCONTRADA