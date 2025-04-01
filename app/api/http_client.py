from contextlib import asynccontextmanager
from typing import AsyncGenerator

from httpx import AsyncClient


@asynccontextmanager
async def get_http_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient() as client:
        try:
            yield client
        except Exception as error:
            print(f'[ERROR] {error}')
