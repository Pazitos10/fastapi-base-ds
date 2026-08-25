from typing import List
from src.cursos.constants import ErrorCode
from src.exceptions import NotFound, BadRequest

class CursoNoEncontrado(NotFound):
    DETAIL = ErrorCode.CURSO_NO_ENCONTRADO

class CursoTieneClases(BadRequest):
    DETAIL = ErrorCode.CURSO_CON_CLASES

class CursoTieneInscriptos(BadRequest):
    DETAIL = ErrorCode.CURSO_CON_INSCRIPCIONES