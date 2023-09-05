from common.fastapi.base import AppEventProvidedComponent, ComponentProvidedApp
from common.fastapi.config import AppConfig, ComponentCategoryGetterEnum
from common.db.redis.async_redis import redis
from common.db.redis.fabric import RedisMethodsFabric


class Redis(AppEventProvidedComponent):
    async def startup(self, app: ComponentProvidedApp) -> None:
        AppConfig[ComponentCategoryGetterEnum.NoSQLDB] = RedisMethodsFabric(redis)

    async def shutdown(self, app: ComponentProvidedApp) -> None:
        await app.redis.close()
