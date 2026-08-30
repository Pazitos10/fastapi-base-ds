from src.departamento.constants import ErrorCode
from src.exceptions import NotFound, BadRequest


class DepartamentoNoEncontrado(NotFound):
    DETAIL = ErrorCode.DEPARTAMENTO_NO_ENCONTRADO


class DepartamentoDuplicado(BadRequest):
    DETAIL = ErrorCode.DEPARTAMENTO_DUPLICADO


class DepartamentoTieneProfesores(BadRequest):
    DETAIL = ErrorCode.DEPARTAMENTO_TIENE_PROFESORES