import tkinter as tk

import httpx
from fastapi import FastAPI

import globals
from src.ui.ImageViewerPage import getImageViewer


api = FastAPI()

# @api.get("/change")
# def get():
    
#     getImageViewer(globals.ROOT_PAGE)
    
#     print(1)
    
    
def send(HOST: str):
    
    try:
        # req = httpx.get(f"http://{HOST}:8202/change")
        req = httpx.get(f"https://fefufit.dvfu.ru/api2/serverStatus")
        
        print(req.json())

        if req.status_code == 200:
            return {"status": "success", "detail": "change success"}
        
        return {"status": "fail", "detail": req.json()}
    
    except:

        return {"status": "fail", "detail": "incorrect host"}