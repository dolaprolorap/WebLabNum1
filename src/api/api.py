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


def bytes_to_img(file: str, name: str):
    
    try:

        byte_arr = list(map(lambda x: int(x), file.split(",")))
        some_bytes = bytearray(byte_arr)

        immutable_bytes = bytes(some_bytes)

        with open(f"{STATIC_PATH}/{name}.jpg", "wb") as f:
            f.write(immutable_bytes)
        
        f.close()
        
    except Exception as e:
        print(e)
    
    
    
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
    
    except Exception as e:
        return None