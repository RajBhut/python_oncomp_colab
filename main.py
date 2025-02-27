from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_websockets=True
)
@app.middleware("http")
async def add_proxy_headers(request, call_next):
    response = await call_next(request)
    if "upgrade" in request.headers.get("connection", "").lower():
        response.headers["Connection"] = "upgrade"
        response.headers["Upgrade"] = "websocket"
    return response
rooms = {}
codes = {}
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.websocket("/ws/{room_name}")
async def websocket_endpoint(websocket: WebSocket, room_name: str):
    await websocket.accept()
    
    print(f"Connected to {room_name}")
    
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

async def broadcast(room_name: str, message: str):
    if room_name in rooms:
        for connection in rooms[room_name].copy():
            try:
                await connection.send_text(message)
            except:
                rooms[room_name].remove(connection)