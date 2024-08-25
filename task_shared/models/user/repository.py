from task_shared.models.user.schemas import (UserCreate,
                                             UserUpdate)
from bson import ObjectId


class UserRepository:
    def __init__(self, collection):
        self.collection = collection

    async def create(self, user_create: UserCreate):
        user = user_create.model_dump()
        result = await self.collection.insert_one(user)
        user["_id"] = result.inserted_id
        return user

    async def delete(self, user_id: ObjectId):
        await self.collection.delete_one({"_id": user_id})

    async def update(self, user_update: UserUpdate):
        user = user_update.model_dump()
        await self.collection.update_one({"_id": user["id"]}, {"$set": user})
        return user

    async def get_by_id(self, user_id: ObjectId):
        user = await self.collection.find_one({"_id": user_id})
        return user if user else None

    async def get_all(self):
        cursor = self.collection.find({})
        users = []
        async for user in cursor:
            users.append(user)
        return users

    async def get_role_by_id(self, user_id: ObjectId):
        user = await self.collection.find_one({"_id": user_id})
        return user.role if user else None
