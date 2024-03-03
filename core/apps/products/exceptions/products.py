from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class ProductNotFound(ServiceException):
    product_id: int

    @property
    def message(self):
        return 'Product not found'
