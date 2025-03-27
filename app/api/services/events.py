"""Service for event model."""

from random import uniform
from uuid import UUID, uuid4
from app.db.connection import get_redis_connection
from app.schemas.events import Event, EventCreate, EventUpdate


class EventCRUD:
    @classmethod
    async def get(cls, uuid: UUID) -> Event | None:
        async with get_redis_connection() as client:
            event = await client.get(str(uuid))

        if not event:
            return None

        return Event.model_validate_json(event)

    @classmethod
    async def list(cls) -> list[Event]:
        async with get_redis_connection() as client:
            cursor, keys = '0', []

            while cursor != 0:
                cursor, current_keys = await client.scan(cursor=cursor, match='*')
                keys.extend(current_keys)

            return [Event.model_validate_json(await client.get(key))for key in keys]

    @classmethod
    async def create(cls, event_input: EventCreate) -> Event:
        async with get_redis_connection() as client:
            event_obj = Event(
                uuid=uuid4(),
                odds=round(uniform(0, 10), 2),  # random because there has to be logic here
                **event_input.model_dump(),
            )
            await client.set(str(event_obj.uuid), event_obj.model_dump_json())
        return event_obj

    @classmethod
    async def update(cls, uuid: UUID, event_input: EventUpdate) -> Event | None:
        async with get_redis_connection() as client:
            event = await client.get(str(uuid))

        if not event:
            return None

        event_obj = Event.model_validate_json(event)
        updated_event_obj = Event(
            uuid=event_obj.uuid,
            odds=event_obj.odds,
            **event_input.model_dump(),
        )
        await client.set(str(updated_event_obj.uuid), updated_event_obj.model_dump_json())

        return updated_event_obj

    @classmethod
    async def delete(cls, uuid: UUID) -> int:
        async with get_redis_connection() as client:
            return await client.delete(str(uuid))
