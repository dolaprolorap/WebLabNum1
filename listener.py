import socket
import time
from src.api.api import bytes_to_img
import globals

from src.ui.ImageViewerPage import setImage
from config import PORT, STATIC_PATH


def start_listener():
    
    globals.SERVER_RUNNING = True
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', int(PORT)))

    while True:
        s.listen(1)

        conn, addr = s.accept()
        
        with conn:

            data = conn.recv(2048)
            request = data.decode('utf-8')

            headers, body = request.split('\r\n\r\n', 1)
            
            print(headers)
            print("Body: " + body)
            
            if body == "no_img":
                if globals.CURRENT_IMAGE == "show.jpg":
                    globals.CURRENT_IMAGE = "show2.jpg"
                else:
                    globals.CURRENT_IMAGE = "show.jpg"
            
            ret = bytes_to_img(body)
            
            if ret != None:
                print(ret)
                print(body)

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