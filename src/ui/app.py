import tkinter as tk

import globals
from config import WINDOW_HEIGHT, WINDOW_WIDTH
from api.runserver import start_server
from src.ui.ChangeImagePage import getChangeImagePage
from src.ui.ConnectPage import getConnectPage
from src.ui.ImageViewerPage import getImageViewer

globals.init()
    

def img_page_button():
    
    globals.PAGES["imageViewer"].tkraise()
    
    if not globals.SERVER_RUNNING:
        start_server()

root = tk.Tk()

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
                     command=img_page_button)
imageBtn.grid(row=0, column=1)

globals.PAGES["changeImage"].grid(row=1, column=0, columnspan=2, sticky="nsew")
globals.PAGES["connect"].grid(row=1, column=0, columnspan=2, sticky="nsew")
globals.PAGES["imageViewer"].grid(row=1, column=0, columnspan=2, sticky="nsew")

globals.PAGES["connect"].tkraise()

root.mainloop()