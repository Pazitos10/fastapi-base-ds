from src.inscripciones.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class InscripcionNoEncontrada(NotFound):
    DETAIL = ErrorCode.INSC_NO_ENCONTRADA


class YaInscripto(BadRequest):
    DETAIL = ErrorCode.YA_INSCRIPTO


class EstudianteInexistente(BadRequest):
    DETAIL = ErrorCode.ALUMNO_INVALIDO


class CursoInexistente(BadRequest):
    DETAIL = ErrorCode.CURSO_INVALIDO
