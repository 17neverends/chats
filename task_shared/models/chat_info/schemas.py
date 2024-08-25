from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field


class ChatInfoSchema(BaseModel):
    id: Optional[str] = Field(alias="_id")
    user_id: int
    chat_id: int
    last_message: datetime = None
    unread_count: int

    class Config:
        json_encoders = {
            ObjectId: str
        }


class ChatInfoCreate(BaseModel):
    user_id: int
    chat_id: int
    last_message: datetime = None
    unread_count: int


class ChatInfoUpdate(BaseModel):
    user_id: Optional[int] = None
    chat_id: Optional[int] = None
    last_message: Optional[datetime] = None
    unread_count: Optional[int] = None
