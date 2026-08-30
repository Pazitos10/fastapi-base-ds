from typing import List
from src.curso.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class CursoNoEncontrado(NotFound):
    DETAIL = ErrorCode.CURSO_NO_ENCONTRADO


class CursoTieneClases(BadRequest):
    DETAIL = ErrorCode.CURSO_TIENE_CLASES


class CursoTieneInscripciones(BadRequest):
    DETAIL = ErrorCode.CURSO_TIENE_INSCRIPCIONES
