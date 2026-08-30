from src.curso.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class CursoNoEncontrado(NotFound):
    DETAIL = ErrorCode.CURSO_NO_ENCONTRADO


class CursoDuplicado(BadRequest):
    DETAIL = ErrorCode.CURSO_DUPLICADO


class CursoTieneInscriptos(BadRequest):
    DETAIL = ErrorCode.CURSO_TIENE_INSCRIPTOS