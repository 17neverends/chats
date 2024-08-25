from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field


class MessageSchema(BaseModel):
    id: Optional[str] = Field(alias="_id")
    chat_id: int
    from_user: int
    text: str
    type: str
    date: datetime
    is_read: bool

    class Config:
        json_encoders = {
            ObjectId: str
        }


class MessageCreate(BaseModel):
    chat_id: int
    from_user: int
    text: str
    type: str
    date: datetime
    is_read: bool


class MessageUpdate(BaseModel):
    chat_id: Optional[int] = None
    from_user: Optional[int] = None
    text: Optional[str] = None
    type: Optional[str] = None
    date: Optional[datetime] = None
    is_read: Optional[bool] = None
