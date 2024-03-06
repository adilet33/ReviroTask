from sqlalchemy.orm import Session
from schemas.product_schemas import Product, UpdateProduct, CreateProduct
from db.models import ProductDB
import uuid
from typing import Union
from pydantic import TypeAdapter


class ProductsService:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, product: CreateProduct) -> Product:
        new_product = ProductDB(**product.model_dump(exclude={"id"}))
        self._session.add(new_product)
        self._session.commit()
        self._session.refresh(new_product)
        return Product.model_validate(new_product, from_attributes=True)

    def get(self, product_id: uuid.UUID) -> Union[Product, None]:
        product = (
            self._session.query(ProductDB).filter(ProductDB.id == product_id).first()
        )
        if product is not None:
            return Product.model_validate(product, from_attributes=True)

    def get_all(self, skip: int = 0, limit: int = 10) -> list[Product]:
        products = self._session.query(ProductDB).offset(skip).limit(limit).all()

        product_dicts = [
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity_in_stock": product.quantity_in_stock,
            }
            for product in products
        ]

        pydantic_products = [Product(**product_dict) for product_dict in product_dicts]

        return pydantic_products

    def update(
        self, product_id: uuid.UUID, product: UpdateProduct
    ) -> Union[Product, None]:
        product_updated = (
            self._session.query(ProductDB).filter(ProductDB.id == product_id).first()
        )
        if product_updated is not None:
            self._session.query(ProductDB).filter(ProductDB.id == product_id).update(
                product.model_dump(), synchronize_session=False
            )
            self._session.commit()
            return Product.model_validate(product_updated, from_attributes=True)

    def delete(self, deleted_id: uuid.UUID):
        self._session.query(ProductDB).filter(ProductDB.id == deleted_id).delete(
            synchronize_session=False
        )
        self._session.commit()
