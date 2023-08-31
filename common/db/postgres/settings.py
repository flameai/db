from dotenv import load_dotenv
from pydantic import PositiveInteger


from common.environ import EnvironBase


load_dotenv()


class PostgresSettings(EnvironBase):
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "secret"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: PositiveInteger = 5432
    POSTGRES_DB: str = "postgres"


postgres_settings = PostgresSettings()

POSTGRES_USER = postgres_settings.POSTGRES_USER
POSTGRES_PASSWORD = postgres_settings.POSTGRES_PASSWORD
POSTGRES_SERVER = postgres_settings.POSTGRES_SERVER
POSTGRES_PORT = postgres_settings.POSTGRES_PORT
POSTGRES_DB = postgres_settings.POSTGRES_DB

POSTGRES_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
