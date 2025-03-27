"""Views for events routers."""

from fastapi import APIRouter, status, HTTPException
from app.schemas.events import EventCreate, Event
from app.api.services.events import EventCRUD
from uuid import UUID

router = APIRouter()


@router.get('/{uuid}', status_code=status.HTTP_200_OK, response_model=Event)
async def get_event(uuid: UUID):
    if not (event_obj := await EventCRUD.get(uuid)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return event_obj


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Event)
async def create_event(event: EventCreate):
    return await EventCRUD.create(event)
