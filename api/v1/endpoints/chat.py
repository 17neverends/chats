from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from task_shared.models.chat.repository import ChatRepository
from task_shared.database_utils import get_collection
from task_shared.models.chat.schemas import ChatCreate


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/get_all")
async def get_all_chats():
    collection = await get_collection("chats")
    repo: ChatRepository = ChatRepository(collection)

    messages: List[dict] = await repo.get_all()
    return JSONResponse(content=messages, status_code=200)


@router.post("/create")
async def create_chat(chat_create: ChatCreate):
    collection = await get_collection("chats")
    repo: ChatRepository = ChatRepository(collection)
    chat = await repo.create(chat_create=chat_create)
    return JSONResponse(content=chat, status_code=200)
