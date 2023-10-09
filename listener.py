import socket
import time
import globals

from config import STATIC_PATH


def start_listener():
    
    globals.SERVER_RUNNING = True
        
    sock = socket.socket()
    sock.bind(('', 5001))

    while True:
        sock.listen(1)
        conn, addr = sock.accept()

        print('connected:', addr)
        
        time.sleep(2)
        
        data = conn.recv(1024)
        text = data.decode()
        
        globals.CURRENT_IMAGE = "show2.jpg"
        