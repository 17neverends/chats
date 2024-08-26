from typing import Optional
from pydantic import BaseModel


class MessageProps(BaseModel):
    limit: Optional[int] = None
    offset: Optional[int] = 0
    user_id: str
