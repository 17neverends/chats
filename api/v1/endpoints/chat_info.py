from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from task_shared.models.chat_info.repository import ChatInfoRepository
from task_shared.database_utils import get_collection


router = APIRouter(prefix="/chat_info", tags=["chat_info"])


@router.post("/get")
async def get_all_chats(user_id: str):
    collection = await get_collection("chats")
    repo: ChatInfoRepository = ChatInfoRepository(collection)
    data: List[dict] = await repo.get_all_by_user_id(user_id=user_id)
    return JSONResponse(content=data, status_code=200)
