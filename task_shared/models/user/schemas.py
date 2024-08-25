from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId


class UserSchema(BaseModel):
    id: Optional[str] = Field(alias="_id")
    first_name: str
    last_name: str
    tg_id: Optional[str] = None
    role: str
    chats: List[str] = Field(default_factory=list)

    class Config:
        json_encoders = {
            ObjectId: str
        }


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    tg_id: Optional[str] = None
    role: str


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    tg_id: Optional[str] = None
    role: Optional[str] = None
    chats: List[str] = Field(default_factory=list)
