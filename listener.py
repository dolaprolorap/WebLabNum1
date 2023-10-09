import socket
import globals

from config import PORT


def start_listener():
    
    globals.SERVER_RUNNING = True
        
    sock = socket.socket()
    sock.bind(('', int(PORT)))

    while True:
        sock.listen(1)
        conn = sock.accept()
        
        if globals.CURRENT_IMAGE == "show.jpg":
            globals.CURRENT_IMAGE = "show2.jpg"
        else:
            globals.CURRENT_IMAGE = "show.jpg"
        