"""App settings."""

from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    app_title: str = 'Line Provider'
    redis_host: str = 'redis'
    redis_port: int = 6379

    class Config:
        env_file = '.env'


settings = BaseConfig()
