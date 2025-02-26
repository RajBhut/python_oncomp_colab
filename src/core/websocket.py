# filepath: /fastapi-websocket-server/src/core/websocket.py
from fastapi import WebSocket, WebSocketDisconnect
import json

rooms = {}
codes = {}

async def broadcast(room_name: str, message: str):
    if room_name in rooms:
        for connection in rooms[room_name].copy():
            try:
                await connection.send_text(message)
            except:
                rooms[room_name].remove(connection)

async def websocket_endpoint(websocket: WebSocket, room_name: str):
    await websocket.accept()
    
    if room_name not in rooms:
        rooms[room_name] = set()
    
    rooms[room_name].add(websocket)
    
    if room_name not in codes:
        codes[room_name] = {"code": "",}
    else: 
        response = {"event": "join", "room": room_name, "data": codes[room_name]["code"]}
        await websocket.send_text(json.dumps(response))

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            event_type = message.get("event")
            payload = message.get("data")
            response = {"event": event_type, "room": room_name, "data": payload}
            
            if event_type == "code":
                codes[room_name]["code"] = payload

            await broadcast(room_name, json.dumps(response))

    except WebSocketDisconnect:
        rooms[room_name].remove(websocket)
        if not rooms[room_name]:  
            del rooms[room_name]