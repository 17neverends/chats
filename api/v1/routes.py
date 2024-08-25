from fastapi import APIRouter

from .endpoints import (
    chat,
    message
)


router = APIRouter(
    prefix="/api",
)

router.include_router(chat.router)
router.include_router(message.router)
