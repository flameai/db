from common.fastapi.base import AppEventProvidedComponent, ComponentProvidedApp
from common.db.redis.async_redis import redis


class Redis(AppEventProvidedComponent):
    async def startup(self, app: ComponentProvidedApp) -> None:
        app.redis = redis

    async def shutdown(self, app: ComponentProvidedApp) -> None:
        await app.redis.close()
