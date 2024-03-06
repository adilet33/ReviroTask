import uuid
from typing import Optional
from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


###Schemas for Products###


class Product(TunedModel):
    id: uuid.UUID | None = None
    name: str | None
    description: str | None
    price: float | None
    quantity_in_stock: int | None


class CreateProduct(BaseModel):
    name: str
    description: str
    price: float
    quantity_in_stock: int


class UpdateProduct(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity_in_stock: Optional[int] = None
