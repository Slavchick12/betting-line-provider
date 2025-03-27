"""Views for events routers."""

from fastapi import APIRouter, status, HTTPException
from app.schemas.events import EventCreate, Event, EventUpdate
from app.api.services.events import EventCRUD
from uuid import UUID

router = APIRouter()


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
    return event_obj


@router.delete('/{uuid}', status_code=status.HTTP_200_OK)
async def delete_event(uuid: UUID) -> dict:
    if not await EventCRUD.delete(uuid):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return {'detail': f'Event {uuid} was deleted'}
