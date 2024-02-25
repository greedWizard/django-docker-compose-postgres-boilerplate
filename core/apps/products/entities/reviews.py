from dataclasses import (
    dataclass,
    field,
)

from core.apps.common.enums import EntityStatus
from core.apps.customers.entities import Customer
from core.apps.products.entities.products import Product


@dataclass
class Review:
    customer: Customer | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: Product | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default='')
    rating: int = field(default=1)
