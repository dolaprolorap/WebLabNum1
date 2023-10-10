import os
import tkinter as tk

import httpx
import numpy as np

from config import PORT, STATIC_PATH

def img_to_bytes(path: str):

    with open(path, 'rb') as f:
        bytes_data = f.read()

    int_array = np.frombuffer(bytes_data, dtype=np.uint8)

    file = str(list(int_array))[1:-1]
    
    return file


def bytes_to_img(file: str):
    
    try:
        
        byte_arr = list(map(lambda x: int(x), file.split(",")))
        some_bytes = bytearray(byte_arr)

        immutable_bytes = bytes(some_bytes)

        with open(f"{STATIC_PATH}/show.jpg", "wb") as f:
            f.write(immutable_bytes)
        
        f.close()
        
    except Exception as e:
        return e
    
    
    
def send(HOST: str, path: str = ""):
    
    data = None
    
    try:
        if data != "":
            
            try:
                os.stat(path)
                data = img_to_bytes(path)
                
            except:
                data = "no_img"
        
        req = httpx.post(f"http://{HOST}:{PORT}", data=data)

        if req.status_code == 200:
            return {"status": "success", "detail": "change success"}
        
        return {"status": "fail", "detail": req.json()}
    
    except Exception as e:
        print(e)
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