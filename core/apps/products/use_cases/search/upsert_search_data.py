from dataclasses import dataclass

from core.apps.products.services.products import BaseProductService
from core.apps.products.services.search import BaseProductSearchService


@dataclass
class UpsertSearchDataUseCase:
    search_service: BaseProductSearchService
    product_service: BaseProductService

    def execute(self):
        products = self.product_service.get_all_products()

        for product in products:
            self.search_service.upsert_product(product)
