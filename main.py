from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_socketio import SocketManager
from datetime import datetime
from typing import List, Dict
from task_shared.models.message.repository import MessageRepository
from task_shared.models.message.schemas import MessageCreate
from api.v1.routes import router
from contextlib import asynccontextmanager
from task_shared.database_utils import get_collection

message_repo = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    collection = await get_collection("messages")
    message_repo: MessageRepository = MessageRepository(collection)
    yield


app = FastAPI(lifespan=lifespan)


socket_manager = SocketManager(app=app, cors_allowed_origins=["*"])

rooms: Dict[str, List[str]] = {}

@socket_manager.on('connect')
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@socket_manager.on('disconnect')
async def disconnect(sid):
    print(f"Client disconnected: {sid}")
    for room_name, clients in rooms.items():
        if sid in clients:
            clients.remove(sid)
            break

@socket_manager.on('join')
async def join(sid, data):
    room_name = data['room']
    if room_name not in rooms:
        rooms[room_name] = []

    if sid not in rooms[room_name]:
        rooms[room_name].append(sid)

    messages = await message_repo.get_all(limit=50, offset=0)
    messages = [msg for msg in messages if msg['room'] == room_name]

    await socket_manager.emit('history', messages, room=sid)
    await socket_manager.emit('message', {'text': f"User {sid} joined the room {room_name}"}, room=room_name)

@socket_manager.on('leave')
async def leave(sid, data):
    room_name = data['room']
    if room_name in rooms:
        if sid in rooms[room_name]:
            rooms[room_name].remove(sid)
            await socket_manager.emit('message', {'text': f"User {sid} left the room {room_name}"}, room=room_name)

@socket_manager.on('message')
async def message(sid, data):
    room_name = data['room']
    message_text = data['message']
    message_type = data.get('message_type', 'text')
    timestamp = datetime.now()

    message_create = MessageCreate(
        user_id=sid,
        message=message_text,
        message_type=message_type,
        timestamp=timestamp,
        room=room_name
    )
    saved_message = await message_repo.create(message_create)

    await socket_manager.emit('message', saved_message, room=room_name)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
