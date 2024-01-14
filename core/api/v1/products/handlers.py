from django.http import HttpRequest
from ninja import Router

from core.api.v1.products.schemas import ProductListSchema


router = Router(tags=['Products'])


@router.get('', response=ProductListSchema)
def get_product_list_handler(request: HttpRequest) -> ProductListSchema:
    return []
