from typing import List, Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from task_shared.models.message.repository import MessageRepository
from task_shared.database_utils import get_collection
router = APIRouter(prefix="/message", tags=["chat"])


@router.post("/get_all")
async def get_chat_history(limit: Optional[int] = None,
                           offset: Optional[int] = 0):
    collection = await get_collection("messages")
    repo: MessageRepository = MessageRepository(collection)

    messages: List[dict] = await repo.get_all(limit=limit,
                                              offset=offset)
    return JSONResponse(content=messages, status_code=200)
