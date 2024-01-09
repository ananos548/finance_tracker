import json

from aiokafka import AIOKafkaProducer
import asyncio

producer = AIOKafkaProducer(
    bootstrap_servers=",",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


async def send_one():
    await producer.start()
