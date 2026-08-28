from src.estudiantes.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class EstudianteNoEncontrado(NotFound):
    DETAIL = ErrorCode.ALUMNO_NO_ENCONTRADO


class LegajoDuplicado(BadRequest):
    DETAIL = ErrorCode.LEGAJO_REPETIDO


class EstudianteConInscripciones(BadRequest):
    DETAIL = ErrorCode.ALUMNO_CON_INSC
