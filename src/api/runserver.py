import os
import socket
from sys import platform

import globals

def start_server():

    globals.SERVER_RUNNING = True

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    if platform in ["linux", "darwin", "linux2"]:
        os.system(f"python3 -m uvicorn src.api.api:api --port 8202 --host {ip_address}")
    elif platform  == "win32":
        os.system(f"python -m uvicorn src.api.api:api --port 8202 -- host {ip_address}")
    else:
        print(f"No matching function to OS {platform}")
        