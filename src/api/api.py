import os
import tkinter as tk

import httpx
import numpy as np

from config import PORT

def img_to_bytes(path: str):

    with open(path, 'rb') as f:
        bytes_data = f.read()

    int_array = np.frombuffer(bytes_data, dtype=np.uint8)

    file = str(list(int_array))[1:-1]
    
    return file

    
def send(HOST: str, data: str = ""):
    
    try:
        if data != "":
            
            try:
                os.stat(data)
                data = img_to_bytes(data)
                
            except:
                data = ""
        
        req = httpx.post(f"http://{HOST}:{PORT}", data="mememme")

        if req.status_code == 200:
            return {"status": "success", "detail": "change success"}
        
        return {"status": "fail", "detail": req.json()}
    
    except:
        return {"status": "fail", "detail": "incorrect host"}
    

# import websocket
 
# def on_open(ws):
#     print("Connection opened")
#     ws.send("Hello, WebSocket!")
 
# def on_message(ws, message):
#     print(f"Received message: {message}")
 
# def on_close(ws):
#     print("Connection closed")
 
# ws = websocket.WebSocketApp("ws://localhost/ws",
#                             on_open=on_open,
#                             on_message=on_message,
#                             on_close=on_close)
 
# ws.run_forever()