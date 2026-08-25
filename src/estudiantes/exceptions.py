from src.estudiantes.constants import ErrorCode
from src.exceptions import BadRequest, NotFound


class EstudianteNoEncontrado(NotFound):
    DETAIL = ErrorCode.ESTUDIANTE_NO_ENCONTRADO


class LegajoDuplicado(BadRequest):
    DETAIL = ErrorCode.LEGAJO_DUPLICADO


class EstudianteTieneInscripciones(BadRequest):
    DETAIL = ErrorCode.ESTUDIANTE_TIENE_INSCRIPCIONES