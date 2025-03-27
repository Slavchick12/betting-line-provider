"""Main module."""

from fastapi import FastAPI

from app.api.routers import router as api_v1_router
from app.core.settings import settings

app = FastAPI(
    title=settings.app_title,
    docs_url='/api/swagger',
    redoc_url='/api/redoc',
)
app.include_router(api_v1_router, prefix='/api/v1')
