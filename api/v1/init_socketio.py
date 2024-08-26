from fastapi_socketio import SocketManager


def init_socketio(app):
    sio = SocketManager(app=app)
