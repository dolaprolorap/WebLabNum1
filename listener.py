import socket
import globals

from src.ui.ImageViewerPage import setImage
from config import PORT, STATIC_PATH


def start_listener():
    
    globals.SERVER_RUNNING = True
        
    sock = socket.socket()
    sock.bind(('', int(PORT)))

    while True:
        sock.listen(1)
        conn, addr = sock.accept()

        data = conn.recv(2**4)

        print(data.decode())
        
        if globals.CURRENT_IMAGE == "show.jpg":
            globals.CURRENT_IMAGE = "show2.jpg"
        else:
            globals.CURRENT_IMAGE = "show.jpg"

        setImage(f"{STATIC_PATH}/{globals.CURRENT_IMAGE}")
        
        
# import asyncio
# import websockets

# async def handler(websocket):
#     print("Client connected")
#     message = await websocket.recv()

#     if globals.CURRENT_IMAGE == "show.jpg":
#         globals.CURRENT_IMAGE = "show2.jpg"
#     else:
#         globals.CURRENT_IMAGE = "show.jpg"

#     await websocket.send(f"Hello, {message}!")

# start_server = websockets.serve(handler, "localhost", PORT)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()