"""Service for event model."""

from uuid import UUID

from app.schemas.events import Event
from app.db.connection import get_redis_connection


class EventCRUD:
    @classmethod
    async def get(cls, uuid: UUID) -> Event | None:
        async with get_redis_connection() as client:
            event = await client.get(str(uuid))

        if not event:
            return None

        return Event.model_validate_json(event)
