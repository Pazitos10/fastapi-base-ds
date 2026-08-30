from typing import List
from src.estudiante.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class EstudianteNoEncontrado(NotFound):
    DETAIL = ErrorCode.ESTUDIANTE_NO_ENCONTRADO


class EstudianteTieneInscripciones(BadRequest):
    DETAIL = ErrorCode.ESTUDIANTE_TIENE_INSCRIPCIONES
