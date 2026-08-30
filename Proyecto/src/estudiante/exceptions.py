from src.estudiante.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class EstudianteNoEncontrado(NotFound):
    DETAIL = ErrorCode.ESTUDIANTE_NO_ENCONTRADO


class LegajoDuplicado(BadRequest):
    DETAIL = ErrorCode.LEGAJO_DUPLICADO


class EstudianteTieneCursos(BadRequest):
    DETAIL = ErrorCode.ESTUDIANTE_TIENE_CURSOS