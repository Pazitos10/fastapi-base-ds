from src.departamentos.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class DepartamentoNoEncontrado(NotFound):
    DETAIL = ErrorCode.DEPTO_NO_ENCONTRADO


class DepartamentoConProfesores(BadRequest):
    DETAIL = ErrorCode.DEPTO_CON_PROFES


class NombreDuplicado(BadRequest):
    DETAIL = ErrorCode.NOMBRE_REPETIDO
