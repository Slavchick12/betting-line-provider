"""Views for events routers."""

from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.api.http_client import get_http_client
from app.api.services.events import EventCRUD
from app.schemas.events import Event, EventCreate, EventUpdate
from app.utils.constants import BET_MARKER_URL

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[Event])
async def list_event() -> list[Event]:
    return await EventCRUD.list()


@router.get('/{uuid}', status_code=status.HTTP_200_OK, response_model=Event)
async def get_event(uuid: UUID) -> Event:
    if not (event_obj := await EventCRUD.get(uuid)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return event_obj


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Event)
async def create_event(event: EventCreate) -> Event:
    return await EventCRUD.create(event)


@router.put('/{uuid}', status_code=status.HTTP_200_OK, response_model=Event)
async def update_event(uuid: UUID, event: EventUpdate) -> Event:
    if not (event_obj := await EventCRUD.update(uuid, event)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')

    async with get_http_client() as client:
        await client.patch(
            BET_MARKER_URL + f'/api/v1/{event_obj.uuid}/status',
            json={'enet_status': event_obj.status},
        )

    return event_obj


@router.delete('/{uuid}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(uuid: UUID) -> None:
    if not await EventCRUD.delete(uuid):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
