import json

from aiokafka import AIOKafkaConsumer
import asyncio


async def consume():
    consumer = AIOKafkaConsumer(
        "tracker_to_auth",
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )
    await consumer.start()
    try:
        async for msg in consumer:
            user_id = msg.value['user_id']
            print(f"Received user_id: {user_id}")
    finally:
        await consumer.stop()


asyncio.run(consume())
