import os
import socket
from random import randint

import globals
from config import PORT, STATIC_PATH
from src.api.api import bytes_to_img
from src.ui.ImageViewerPage import setImage


def start_listener():
    globals.SERVER_RUNNING = True
        
    sock = socket.socket()
    sock.bind(('', int(PORT)))

    while True:
        sock.listen(1)
        conn, addr = sock.accept()

        req = []

        a = conn.recv(2**30)
        while a:
            req.append(a)
            a = conn.recv(2**30)
            
        req.append(a)

        conn.close()
        
        body = ""
        for x in req[1:]:
            body += x.decode()

        images = os.listdir(STATIC_PATH)
        
        # if body != "no_img":
        
        # name = str(len(images)-1)
        # bytes_to_img(body, name)
        # globals.CURRENT_IMAGE = name + ".jpg"
            
        # else:
        
        new_img_num = randint(0, len(images)-2)
        
        while (images[new_img_num] == globals.CURRENT_IMAGE):
            new_img_num = randint(0, len(images))
        
        globals.CURRENT_IMAGE = images[new_img_num]
            
        setImage(f"{STATIC_PATH}/{globals.CURRENT_IMAGE}")