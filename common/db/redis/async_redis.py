import aioredis

from common.db.redis.settings import (
    REDIS_DB,
    REDIS_HOST,
    REDIS_POOL_MAX_CONNECTIONS,
    REDIS_PORT,
)

pool = aioredis.ConnectionPool.from_url(
    f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
    max_connections=REDIS_POOL_MAX_CONNECTIONS,
)
redis = aioredis.Redis(connection_pool=pool)
