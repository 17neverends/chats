from fastapi import APIRouter
from fastapi.responses import JSONResponse
from task_shared.database_utils import get_collection
from task_shared.models.user.repository import UserRepository


router = APIRouter(prefix="/role", tags=["role"])


@router.post("/get_by_id", response_class=JSONResponse)
async def get_all_chats(user_id: int) -> JSONResponse:
    collection = await get_collection("users")
    repo: UserRepository = UserRepository(collection)
    role  = await repo.get_role_by_id(user_id=user_id)
    return JSONResponse(content=role, status_code=200)
