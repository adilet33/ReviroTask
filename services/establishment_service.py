from sqlalchemy.orm import Session
from schemas.establishment_schemas import (
    Establishment,
    CreateEstablishment,
    UpdateEstablishment,
)
from db.models import EstablishmentDB
import uuid
from typing import Union


class EstablishmentsService:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, establishment: CreateEstablishment) -> Establishment:
        new_establishment = EstablishmentDB(**establishment.model_dump(exclude={"id"}))
        self._session.add(new_establishment)
        self._session.commit()
        self._session.refresh(new_establishment)
        return Establishment.model_validate(new_establishment, from_attributes=True)

    def get(self, establishment_id: uuid.UUID) -> Union[Establishment, None]:
        establishment = (
            self._session.query(EstablishmentDB)
            .filter(EstablishmentDB.id == establishment_id)
            .first()
        )
        if establishment is not None:
            return Establishment.model_validate(establishment, from_attributes=True)

    def get_all(self, skip: int = 0, limit: int = 10) -> list[Establishment]:
        establishments = (
            self._session.query(EstablishmentDB).offset(skip).limit(limit).all()
        )
        establishment_dicts = [
            {
                "id": establishment.id,
                "name": establishment.name,
                "description": establishment.description,
                "locations": establishment.locations,
                "opening_hours": establishment.opening_hours,
            }
            for establishment in establishments
        ]

        pydantic_establishments = [
            Establishment(**establishment_dict)
            for establishment_dict in establishment_dicts
        ]

        return pydantic_establishments

    def update(
        self, establishment_id: uuid.UUID, establishment: UpdateEstablishment
    ) -> Union[Establishment, None]:
        establishment_updated = (
            self._session.query(EstablishmentDB)
            .filter(EstablishmentDB.id == establishment_id)
            .first()
        )
        if establishment_updated is not None:
            self._session.query(EstablishmentDB).filter(
                EstablishmentDB.id == establishment_id
            ).update(establishment.model_dump(), synchronize_session=False)
            self._session.commit()
            return Establishment.model_validate(
                establishment_updated, from_attributes=True
            )

    def delete(self, deleted_id: uuid.UUID):
        establishment_delete = (
            self._session.query(EstablishmentDB)
            .filter(EstablishmentDB.id == deleted_id)
            .first()
        )
        if establishment_delete is not None:
            self._session.query(EstablishmentDB).filter(
                EstablishmentDB.id == deleted_id
            ).delete(synchronize_session=False)
            self._session.commit()
