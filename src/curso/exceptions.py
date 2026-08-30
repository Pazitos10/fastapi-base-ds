from src.curso.constants import ErrorCode
from src.exceptions import NotFound

class CursoNoEncontrado(NotFound):
    DETAIL = ErrorCode.CURSO_NO_ENCONTRADO