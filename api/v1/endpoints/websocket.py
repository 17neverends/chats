from fastapi import WebSocket, APIRouter, WebSocketDisconnect
from task_shared.database_utils import get_collection
from task_shared.models.user.repository import UserRepository
router = APIRouter(
    prefix="/ws"
)


connections = []


@router.websocket("/ws/chat/{room_name}")
async def websocket_endpoint(websocket: WebSocket, id: int, room_name: str):
    await websocket.accept()
    connections.append(websocket)
    collection = await get_collection("users")
    repo: UserRepository = UserRepository(collection)
    try:
        while True:
            user_role = await repo.get_role_by_id(user_id=id)
            print(user_role)
            data = await websocket.receive_text()
            for connection in connections:
                if connection is not websocket:
                    await connection.send_text(f"Room {room_name}: {data}")
    except WebSocketDisconnect:
        connections.remove(websocket)
