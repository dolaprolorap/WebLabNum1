import tkinter as tk

import httpx

    
def send(HOST: str):
    
    try:
        req = httpx.post(f"http://127.0.0.1:5001", data="hello")

        if req.status_code == 200:
            return {"status": "success", "detail": "change success"}
        
        return {"status": "fail", "detail": req.json()}
    
    except:

        return {"status": "fail", "detail": "incorrect host"}
    
