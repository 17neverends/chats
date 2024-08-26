from typing import Optional
from task_shared.models.message.schemas import (MessageCreate,
                                                MessageUpdate)
from bson import ObjectId


class MessageRepository:
    def __init__(self, collection):
        self.collection = collection

    async def create(self, message_create: MessageCreate):
        message = message_create.model_dump()
        result = await self.collection.insert_one(message)
        message["_id"] = result.inserted_id
        return message

    async def delete(self, message_id: ObjectId):
        await self.collection.delete_one({"_id": message_id})

    async def update(self, message_update: MessageUpdate):
        message = message_update.model_dump()
        await self.collection.update_one({"_id": message["id"]},
                                         {"$set": message})
        return message

    async def get_by_id(self, message_id: ObjectId):
        message = await self.collection.find_one({"_id": message_id})
        return message if message else None

    async def get_all(self,
                      limit: Optional[int] = None,
                      offset: Optional[int] = 0):
        cursor = self.collection.find({}).skip(offset)

        if limit:
            cursor = cursor.limit(limit)

        messages = []
        async for message in cursor:
            messages.append(message)
        return messages


    async def get_all_by_chat_id(self,
                                 chat_id: Optional[str] = None,
                                 limit: Optional[int] = None,
                                 offset: Optional[int] = 0):
        query = {}
        
        if chat_id:
            query['chat_id'] = chat_id

        cursor = self.collection.find(query).skip(offset)

        if limit:
            cursor = cursor.limit(limit)

        messages = []
        async for message in cursor:
            messages.append(message)
        return messages
