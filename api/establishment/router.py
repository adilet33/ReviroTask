from fastapi import APIRouter, Depends, HTTPException, status
from schemas.establishment_schemas import (
    Establishment,
    CreateEstablishment,
    UpdateEstablishment,
)
import uuid
from typing import List
from api.depends import get_db

from sqlalchemy.orm import Session
from services.establishment_service import EstablishmentsService


router = APIRouter()


@router.get("/", response_model=List[Establishment], status_code=status.HTTP_200_OK)
def get_establishments(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 20
) -> List[Establishment]:
    establishments = EstablishmentsService(db).get_all(skip, limit)

    return establishments


@router.get(
    "/{establishment_id}/", response_model=Establishment, status_code=status.HTTP_200_OK
)
def get_establishment_by_id(
    establishment_id: uuid.UUID, db: Session = Depends(get_db)
) -> Establishment:
    establishment = EstablishmentsService(db).get(establishment_id)

    if establishment is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The id: {establishment_id} you requested for does not exist",
        )

    return establishment


@router.post("/", response_model=Establishment, status_code=status.HTTP_201_CREATED)
def create_establishment(
    establishment: CreateEstablishment, db: Session = Depends(get_db)
) -> Establishment:
    new_establishment = Establishment(**establishment.model_dump())

    return EstablishmentsService(db).create(new_establishment)


@router.put(
    "/{establishment_id}/",
    response_model=Establishment,
    status_code=status.HTTP_202_ACCEPTED,
)
def update_establishment(
    establishment_id: uuid.UUID,
    establishment_update: UpdateEstablishment,
    db: Session = Depends(get_db),
) -> Establishment:
    updated_establishment = EstablishmentsService(db).update(
        establishment_id, establishment_update
    )
    if updated_establishment is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The id: {establishment_id} you requested for does not exist",
        )
    return updated_establishment


@router.delete("/{establishment_id}/", status_code=status.HTTP_200_OK)
def delete_establishment(establishment_id: uuid.UUID, db: Session = Depends(get_db)):
    deleted_product = EstablishmentsService(db).delete(establishment_id)
    return deleted_product
