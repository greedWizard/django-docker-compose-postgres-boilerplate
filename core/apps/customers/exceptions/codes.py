from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CodeException(ServiceException):
    @property
    def message(self):
        return 'Auth code exception occurred'


@dataclass(eq=False)
class CodeNotFoundException(CodeException):
    code: str

    @property
    def message(self):
        return 'Code not found'


@dataclass(eq=False)
class CodesNotEqualException(CodeException):
    code: str
    cached_code: str
    customer_phone: str

    @property
    def message(self):
        return 'Codes are not equal'
