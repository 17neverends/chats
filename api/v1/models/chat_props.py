from typing import Optional
from pydantic import BaseModel


class ChatProps(BaseModel):
    limit: Optional[int] = None
    offset: Optional[int] = 0
    client_id: Optional[str] = None
    manager_id: Optional[str] = None