import socket
import globals

from config import PORT


def start_listener():
    
    globals.SERVER_RUNNING = True
        
    sock = socket.socket()
    sock.bind(('', int(PORT)))

    while True:
        sock.listen(1)
        conn, addr = sock.accept()
        
        data = conn.recv(2**40)

        print(data.decode())
        
        if globals.CURRENT_IMAGE == "show.jpg":
            globals.CURRENT_IMAGE = "show2.jpg"
        else:
            globals.CURRENT_IMAGE = "show.jpg"
        
        
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