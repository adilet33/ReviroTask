from fastapi import APIRouter, Depends, HTTPException, status
from schemas.product_schemas import Product, CreateProduct, UpdateProduct
import uuid
from typing import List
from api.depends import get_db

from sqlalchemy.orm import Session
from services.product_service import ProductsService


router = APIRouter()


@router.get("/", response_model=List[Product], status_code=status.HTTP_200_OK)
def get_products(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 20
) -> List[Product]:
    products = ProductsService(db).get_all(skip, limit)

    return products


@router.get("/{product_id}/", response_model=Product, status_code=status.HTTP_200_OK)
def get_product_by_id(product_id: uuid.UUID, db: Session = Depends(get_db)) -> Product:
    product = ProductsService(db).get(product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The id: {product_id} you requested for does not exist",
        )

    return product


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product_in: CreateProduct, db: Session = Depends(get_db)) -> Product:
    product = Product(**product_in.model_dump())
    return ProductsService(db).create(product)


@router.put(
    "/{product_id}/", response_model=Product, status_code=status.HTTP_202_ACCEPTED
)
def update_product(
    product_id: uuid.UUID, product_update: UpdateProduct, db: Session = Depends(get_db)
) -> Product:
    updated_product = ProductsService(db).update(product_id, product_update)
    if updated_product is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The id: {product_id} you requested for does not exist",
        )
    return updated_product


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: uuid.UUID, db: Session = Depends(get_db)):
    ProductsService(db).delete(product_id)
