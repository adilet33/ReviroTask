import uuid

from .base_model import Base

from sqlalchemy import Text, Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID


class ProductDB(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)


class EstablishmentDB(Base):
    __tablename__ = "establishments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    locations = Column(String, nullable=False)
    opening_hours = Column(String)
