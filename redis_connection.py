import json

import aioredis
from fastapi import Cookie
from auth.src.utils.users import UserService


async def get_redis_connection():
    return await aioredis.create_redis('redis://localhost')


async def get_user_data_from_redis(cookie_jwt: str):
    redis = await get_redis_connection()
    current_user_id = UserService.get_current_user(cookie_jwt)
    print(current_user_id)
    try:
        user_data = await redis.get(f'user_data:{current_user_id["user_id"]}')
        return json.loads(user_data) if user_data else None
    finally:
        redis.close()
        await redis.wait_closed()
