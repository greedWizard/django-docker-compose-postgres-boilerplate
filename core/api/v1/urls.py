from ninja import Router

from core.api.v1.customers.handlers import router as customer_router
from core.api.v1.products.handlers import router as product_router


router = Router(tags=['v1'])
router.add_router('products/', product_router)
router.add_router('customers/', customer_router)
