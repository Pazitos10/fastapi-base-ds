from src.profesor.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class ProfesorNoEncontrado(NotFound):
    DETAIL = ErrorCode.PROFESOR_NO_ENCONTRADO


class EmailDuplicado(BadRequest):
    DETAIL = ErrorCode.EMAIL_DUPLICADO


class NombreDuplicado(BadRequest):
    DETAIL = ErrorCode.NOMBRE_DUPLICADO

class CursoDuplicado(BadRequest):
    DETAIL = ErrorCode.CURSO_REPETIDO

class ProfesorTieneCursos(BadRequest):
    DETAIL = ErrorCode.PROFESOR_TIENE_CURSOS

class CursoNoEncontrado(NotFound):
    DETAIL = ErrorCode.CURSO_NO_ENCONTRADO