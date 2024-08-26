from motor.motor_asyncio import AsyncIOMotorClient
import os

HOST: str = os.getenv("MONGO_HOST", "localhost")
PORT: int = int(os.getenv("MONGO_PORT", 27017))
DB_NAME: str = os.getenv("DB_NAME", "chats")
uri = f"mongodb://{HOST}:{PORT}"

client = AsyncIOMotorClient(uri)

async def get_database(database_name: str = DB_NAME):
    return client[database_name]


async def get_collection(collection_name: str):
    db = await get_database()
    return db[collection_name]
