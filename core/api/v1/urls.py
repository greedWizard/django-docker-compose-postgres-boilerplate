from ninja import Router

from core.api.v1.customers.handlers import router as customer_router
from core.api.v1.products.handlers import router as product_router
from core.api.v1.reviews.handlers import router as review_router


router = Router(tags=['v1'])

product_router.add_router('', review_router)

router.add_router('customers/', customer_router)
router.add_router('products/', product_router)
router.add_router('customers/', customer_router)
