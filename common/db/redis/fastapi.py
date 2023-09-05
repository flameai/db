from common.fastapi.base import AppEventProvidedComponent, ComponentProvidedApp, ComponentCategoryGetterEnum
from common.db.redis.async_redis import redis
from common.db.redis.fabric import RedisMethodsFabric


class Redis(AppEventProvidedComponent):
    async def startup(self, app: ComponentProvidedApp) -> None:
        app.config[ComponentCategoryGetterEnum.NoSQLDB] = RedisMethodsFabric(redis)

    async def shutdown(self, app: ComponentProvidedApp) -> None:
        await app.redis.close()
