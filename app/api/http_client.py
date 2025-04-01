from contextlib import asynccontextmanager

from httpx import AsyncClient


@asynccontextmanager
async def get_http_client() -> AsyncClient:
    async with AsyncClient() as client:
        try:
            yield client
        except Exception as error:
            print(f'[ERROR] {error}')
