import uuid
from typing import Optional
from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class Establishment(TunedModel):
    id: uuid.UUID | None = None
    name: str | None
    description: str | None
    locations: str | None
    opening_hours: str | None


class CreateEstablishment(BaseModel):
    name: str
    description: str
    locations: str
    opening_hours: str


class UpdateEstablishment(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    locations: Optional[str] = None
    opening_hours: Optional[str] = None
