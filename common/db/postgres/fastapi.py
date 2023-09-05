from common.fastapi.base import AppEventProvidedComponent, ComponentProvidedApp
from common.fastapi.config import AppConfig, ComponentCategoryGetterEnum
from common.db.postgres.async_session import Session, engine


class Postgres(AppEventProvidedComponent):
    """
    Итак, леди и джентльмены! Кто не видел, как работает принцип DIP (Dependency Inversion Principle)
    он перед вами в полной красе: вместо того, чтобы поставить в зависимость либу FastAPI от
    либы DB, мы просто объявили интерфейс в либе FastAPI и реализуем его во всех остальных компонентах.
    """

    async def startup(self, app: ComponentProvidedApp) -> None:
        AppConfig[ComponentCategoryGetterEnum.RelationalDB] = Session

    async def shutdown(self, app: ComponentProvidedApp) -> None:
        await engine.dispose()
