from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from common.db.postgres.settings import POSTGRES_DSN

engine = create_async_engine(POSTGRES_DSN)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
