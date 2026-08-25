from src.profesor.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class ProfesorNoEncontrado(NotFound):
    DETAIL = ErrorCode.PROFESOR_NO_ENCONTRADO

class EmailDuplicado(BadRequest):
    DETAIL = ErrorCode.EMAIL_DUPLICADO

class ProfesorTieneCursos(BadRequest):
    DETAIL = ErrorCode.PROFESOR_TIENE_CURSOS
