import asyncio
import json

from aiokafka import AIOKafkaConsumer
from redis_connection import get_redis_connection


async def consume():
    consumer = AIOKafkaConsumer(
        "tracker_to_auth",
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )
    await consumer.start()
    try:
        async for msg in consumer:
            user_data = msg.value["user_data"]
            redis = await get_redis_connection()
            print(user_data)
            await redis.set(f"user_data:{user_data['user_id']}", json.dumps(user_data))
            await redis.expire(f"user_data:{user_data['user_id']}", 360000)
            redis.close()
            await redis.wait_closed()
    finally:
        await consumer.stop()


if __name__ == "__main__":
    print(asyncio.run(consume()))
