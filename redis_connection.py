import json

import aioredis


async def get_redis_connection():
    return await aioredis.create_redis('redis://localhost')


async def get_user_data_from_redis() -> dict:
    redis = await get_redis_connection()
    try:
        user_data = await redis.get('user_data')
        return json.loads(user_data) if user_data else None
    finally:
        redis.close()
        await redis.wait_closed()
