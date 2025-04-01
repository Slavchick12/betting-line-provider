"""Schemas for events."""

from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

from app.utils.enums import EventStatusEnum


class Event(BaseModel):
    uuid: UUID
    name: str
    odds: Annotated[float, Field(gt=0)]
    deadline: Annotated[int, Field(gte=0)]
    status: EventStatusEnum

    @field_validator('odds')
    @classmethod
    def odds_validate(cls, value: float) -> float:
        return round(value, 2)


class EventCreate(BaseModel):
    name: str
    deadline: Annotated[int, Field(gte=0)]
    status: EventStatusEnum


class EventUpdate(BaseModel):
    deadline: Annotated[int, Field(gte=0)]
    status: EventStatusEnum
