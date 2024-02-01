import json
from aiokafka import AIOKafkaConsumer
from fastapi import Depends, Request
import asyncio


async def process_expense_messages(user_id: int):
    consumer = AIOKafkaConsumer(
        "tracker_to_auth",
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )

    await consumer.start()
    try:
        async for msg in consumer:
            expense_info = msg.value
            print(f"Received expense info: {expense_info} for user: {user_id}")
            await consumer.send_and_wait("tracker_to_auth", value={"user_id": user_id})
    finally:
        await consumer.stop()


# Запустите этот код в фоне, чтобы он мог непрерывно слушать сообщения
if __name__ == "__main__":
    asyncio.run(process_expense_messages())
