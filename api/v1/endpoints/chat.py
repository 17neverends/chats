from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.v1.models.chat_props import ChatProps
from task_shared.models.chat.repository import ChatRepository
from task_shared.database_utils import get_collection
from task_shared.models.chat.schemas import ChatCreate


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/get_all")
async def get_all_chats(chat_props: ChatProps):
    collection = await get_collection("chats")
    repo: ChatRepository = ChatRepository(collection)

    messages: List[dict] = await repo.get_all_by_user_id(limit=chat_props.limit,
                                                         offset=chat_props.offset,
                                                         client_id=chat_props.client_id,
                                                         manager_id=chat_props.manager_id)
    return JSONResponse(content=messages, status_code=200)


@router.post("/create")
async def create_chat(chat_create: ChatCreate):
    collection = await get_collection("chats")
    repo: ChatRepository = ChatRepository(collection)
    chat = await repo.create(chat_create=chat_create)
    return JSONResponse(content=chat, status_code=200)
