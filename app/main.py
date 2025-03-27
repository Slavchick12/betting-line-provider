"""Main module."""

from fastapi import FastAPI
from app.core.settings import settings
from app.api.routers import router as api_v1_router

app = FastAPI(
    title=settings.app_title,
    docs_url='/api/openapi',
    redoc_url='/api/redoc',
)
app.include_router(api_v1_router, prefix='/api/v1')
