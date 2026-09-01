from src.exceptions import NotFound, BadRequest
from src.profesor.constants import ErrorCode


class ProfesorNoEncontrado(NotFound):
    DETAIL = ErrorCode.PROFESOR_NO_ENCONTRADO


class EmailDuplicado(BadRequest):
    DETAIL = ErrorCode.EMAIL_DUPLICADO