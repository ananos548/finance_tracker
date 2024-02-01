import json
from fastapi import Depends
from aiokafka import AIOKafkaProducer
import asyncio

# from src.models.models import User
from src.utils.base_config import current_user


# async def send_one(user_id: int):
#     producer = AIOKafkaProducer(
#         bootstrap_servers="localhost:9092",
#         value_serializer=lambda v: json.dumps(v).encode("utf-8")
#     )
#     await producer.start()
#     try:
#         await producer.send_and_wait("tracker_to_auth", value={"user_id": user_id})
#     finally:
#         await producer.stop()


# if __name__ == "__main__":
#     asyncio.run(send_one(123))
