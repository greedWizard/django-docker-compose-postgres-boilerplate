import pytest

from core.apps.products.services.products import (
    BaseProductService,
    ORMProductService,
)


@pytest.fixture
def product_service() -> BaseProductService:
    return ORMProductService()
