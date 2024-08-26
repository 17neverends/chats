from typing import Optional
from task_shared.models.chat_info.schemas import (ChatInfoCreate,
                                                  ChatInfoUpdate)
from bson import ObjectId


class ChatInfoRepository:
    def __init__(self, collection):
        self.collection = collection

    async def create(self, chat_info_create: ChatInfoCreate):
        chat_info = chat_info_create.model_dump()
        result = await self.collection.insert_one(chat_info)
        chat_info["_id"] = result.inserted_id
        return chat_info

    async def delete(self, chat_info_id: ObjectId):
        await self.collection.delete_one({"_id": chat_info_id})

    async def update(self, chat_info_update: ChatInfoUpdate):
        chat_info = chat_info_update.model_dump()
        await self.collection.update_one({"_id": chat_info["id"]},
                                         {"$set": chat_info})
        return chat_info

    async def get_by_id(self, chat_info_id: ObjectId):
        chat_info = await self.collection.find_one({"_id": chat_info_id})
        return chat_info if chat_info else None

    async def get_all(self):
        cursor = self.collection.find({})
        chat_infos = []
        async for chat_info in cursor:
            chat_infos.append(chat_info)
        return chat_infos


    async def get_all_by_user_id(self, user_id: Optional[str] = None):
        query = {}
        
        if user_id:
            query['user_id'] = user_id

        cursor = self.collection.find(query)
        chat_infos = []
        async for chat_info in cursor:
            chat_infos.append(chat_info)
        return chat_infos