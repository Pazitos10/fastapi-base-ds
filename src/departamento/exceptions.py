from typing import List
from src.departamento.constants import ErrorCode
from src.exceptions import NotFound

class DepartamentoNoEncontrado(NotFound):
    DETAIL = ErrorCode.DEPARTAMENTO_NO_ENCONTRADO