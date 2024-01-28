from enum import Enum
from typing import Any

from ninja import Schema


class PaginationOut(Schema):
    offset: int
    limit: int
    total: int


class PaginationIn(Schema):
    offset: int = 0
    limit: int = 20


class DefaultFilter(Enum):
    NOT_SET: Any
