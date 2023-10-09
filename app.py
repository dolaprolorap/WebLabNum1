import tkinter as tk
import threading

from config import WINDOW_HEIGHT, WINDOW_WIDTH, STATIC_PATH
from listener import start_listener
from src.ui.ChangeImagePage import getChangeImagePage
from src.ui.ConnectPage import getConnectPage
from src.ui.ImageViewerPage import setImage, getImageViewer
import globals

def but(root: tk.Tk):
    globals.PAGES["imageViewer"].tkraise()
    
    root.update()
    
    print(globals.CURRENT_IMAGE)
    setImage(f"{STATIC_PATH}\\{globals.CURRENT_IMAGE}")
    
    if not globals.SERVER_RUNNING:
        
        t2 = threading.Thread(target=start_listener, daemon=True)
        t2.start()

globals.init()

root = tk.Tk()

def change_img():
    changeImage(root)

globals.ROOT_PAGE = root

root.title('image_changer')
root.geometry(f"{WINDOW_HEIGHT}x{WINDOW_WIDTH}")

globals.PAGES["changeImage"] = getChangeImagePage(root)
globals.PAGES["connect"] = getConnectPage(root)
globals.PAGES["imageViewer"] = getImageViewer(root)

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=10)

connectBtn = tk.Button(root, text="Управление",
                    command=lambda: globals.PAGES["connect"].tkraise())
connectBtn.grid(row=0, column=0)

imageBtn = tk.Button(root, text="Получение",
                    command=lambda: but(root))
imageBtn.grid(row=0, column=1)

globals.PAGES["changeImage"].grid(row=1, column=0, columnspan=2, sticky="nsew")
globals.PAGES["connect"].grid(row=1, column=0, columnspan=2, sticky="nsew")
globals.PAGES["imageViewer"].grid(row=1, column=0, columnspan=2, sticky="nsew")

globals.PAGES["connect"].tkraise()

def start_app():
    root.mainloop()

start_app()