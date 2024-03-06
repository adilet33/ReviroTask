from fastapi import APIRouter

from .products.routes import router as product
from .establishment.router import router as establishment

router = APIRouter()


router.include_router(product, prefix="/products", tags=["prodcuts"])
router.include_router(establishment, prefix="/establishments", tags=["establishment"])
