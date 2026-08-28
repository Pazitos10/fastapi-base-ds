from src.clases.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class ClaseNoEncontrada(NotFound):
    DETAIL = ErrorCode.CLASE_NO_ENCONTRADA


class CursoInexistente(BadRequest):
    DETAIL = ErrorCode.CURSO_INVALIDO
