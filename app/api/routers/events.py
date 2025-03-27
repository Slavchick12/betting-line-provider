"""Api urls for events."""

from fastapi import APIRouter

from app.api.views.events import router as events

router = APIRouter(tags=['events'])

router.include_router(events)
