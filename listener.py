import os
from random import randint
import socket
import globals

from config import PORT, STATIC_PATH
from src.ui.ImageViewerPage import setImage


def start_listener():
    globals.SERVER_RUNNING = True
        
    sock = socket.socket()
    sock.bind(('', int(PORT)))

    while True:
        sock.listen(1)
        conn, addr = sock.accept()
        
        images = os.listdir(STATIC_PATH)
        
        print(len(images)-1)
        
        new_img_num = randint(0, len(images)-1)
        
        while (images[new_img_num] == globals.CURRENT_IMAGE):
            new_img_num = randint(0, len(images))
        
        globals.CURRENT_IMAGE = images[new_img_num]
        
        setImage(f"{STATIC_PATH}/{globals.CURRENT_IMAGE}")