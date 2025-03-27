"""Connection to database."""

import aioredis

from contextlib import asynccontextmanager
from app.core.settings import settings


@asynccontextmanager
async def get_redis_connection():
    client = await aioredis.from_url(f'redis://{settings.redis_host}:{settings.redis_port}', decode_responses=True)
    try:
        yield client
    finally:
        await client.close()
