# src/inscripciones/exceptions.py
from src.exceptions import BadRequest, NotFound
from src.inscripciones.constants import ErrorCode

class InscripcionNoEncontrada(NotFound):
    DETAIL = ErrorCode.INSCRIPCION_NO_ENCONTRADA


class InscripcionDuplicada(BadRequest):
    DETAIL = ErrorCode.INSCRIPCION_DUPLICADA


class EstudianteNoExiste(NotFound):
    DETAIL = ErrorCode.ESTUDIANTE_NO_EXISTE


class CursoNoExiste(NotFound):
    DETAIL = ErrorCode.CURSO_NO_EXISTE