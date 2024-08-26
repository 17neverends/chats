from fastapi import APIRouter

from .endpoints import (
    chat,
    message,
    role,
    chat_info
)


router = APIRouter(
    prefix="/api",
)

router.include_router(chat.router)
router.include_router(message.router)
router.include_router(role.router)
router.include_router(chat_info.router)
