from src.profesores.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class ProfesorNoEncontrado(NotFound):
    DETAIL = ErrorCode.PROFESOR_NO_ENCONTRADO


class EmailDuplicado(BadRequest):
    DETAIL = ErrorCode.MAIL_REPETIDO


class ProfesorDictaCursos(BadRequest):
    DETAIL = ErrorCode.PROFESOR_CON_CURSOS


class DepartamentoInexistente(BadRequest):
    DETAIL = ErrorCode.DEPTO_INVALIDO
