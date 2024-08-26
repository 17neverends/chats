from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.v1.models.message_props import MessageProps
from task_shared.models.message.repository import MessageRepository
from task_shared.database_utils import get_collection

router = APIRouter(prefix="/message", tags=["chat"])


@router.post("/get_all")
async def get_chat_history(message_props: MessageProps):
    collection = await get_collection("messages")
    repo: MessageRepository = MessageRepository(collection)

    messages: List[dict] = await repo.get_all_by_chat_id(limit=message_props.limit,
                                                         offset=message_props.offset,
                                                         user_id=message_props.user_id)
    return JSONResponse(content=messages, status_code=200)
