import json
from aiokafka import AIOKafkaProducer


async def send_one(user_data: str):
    producer = AIOKafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    await producer.start()
    try:
        await producer.send("tracker_to_auth", value={"user_data": user_data})
    finally:
        await producer.stop()
