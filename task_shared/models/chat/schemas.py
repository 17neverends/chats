from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List, Optional


class ChatSchema(BaseModel):
    id: Optional[str] = Field(alias="_id")
    manager_id: int
    client_id: int
    messages: List[str] = Field(default_factory=list)

    class Config:
        json_encoders = {
            ObjectId: str
        }


class ChatCreate(BaseModel):
    manager_id: int
    client_id: int
    messages: List[str] = Field(default_factory=list)


class ChatUpdate(BaseModel):
    manager_id: Optional[int] = None
    client_id: Optional[int] = None
    messages: List[str] = Field(default_factory=list)
