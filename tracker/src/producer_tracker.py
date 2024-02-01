import json
from aiokafka import AIOKafkaProducer
import asyncio


async def send_expense_info(expense_info):
    producer = AIOKafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    await producer.start()
    try:
        await producer.send_and_wait("tracker_to_auth", value=expense_info)
    finally:
        await producer.stop()


# Вызывайте эту функцию при создании объекта expense


#0x7fc9ffe74790