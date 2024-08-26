from typing import Optional
from task_shared.models.chat.schemas import (ChatCreate,
                                             ChatUpdate)
from bson import ObjectId


class ChatRepository:
    def __init__(self, collection):
        self.collection = collection

    async def create(self, chat_create: ChatCreate):
        chat = chat_create.model_dump()
        result = await self.collection.insert_one(chat)
        chat["_id"] = result.inserted_id
        return chat

    async def delete(self, chat_id: ObjectId):
        await self.collection.delete_one({"_id": chat_id})

    async def update(self, chat_update: ChatUpdate):
        chat = chat_update.model_dump()
        await self.collection.update_one({"_id": chat["id"]}, {"$set": chat})
        return chat

    async def get_by_id(self, chat_id: ObjectId):
        chat = await self.collection.find_one({"_id": chat_id})
        return chat if chat else None

    async def get_all(self,
                      limit: Optional[int] = None,
                      offset: Optional[int] = 0):
        cursor = self.collection.find({}).skip(offset)

        if limit:
            cursor = cursor.limit(limit)

        chats = []
        async for chat in cursor:
            chats.append(chat)
        return chats

    async def get_all_by_user_id(self,
                                 limit: Optional[int] = None,
                                 offset: Optional[int] = 0,
                                 client_id: Optional[str] = None,
                                 manager_id: Optional[str] = None):
        query = {}
        
        if client_id:
            query['client_id'] = client_id
        
        if manager_id:
            query['manager_id'] = manager_id

        cursor = self.collection.find(query).skip(offset)

        if limit:
            cursor = cursor.limit(limit)

        chats = []
        async for chat in cursor:
            chats.append(chat)
        return chats
