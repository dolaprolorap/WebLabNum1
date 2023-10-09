import os
from sys import platform
import socket
import globals
import subprocess

globals.init()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

if platform in ["linux", "darwin", "linux2"]:
    subprocess.call(["python3", "app.py"])
    subprocess.call(["python3", "api.py"])
elif platform  == "win32":
    os.system(f"python -m uvicorn src.ui.app:api --port 8203 -- host {ip_address}")
else:
    print(f"No matching function to OS {platform}")