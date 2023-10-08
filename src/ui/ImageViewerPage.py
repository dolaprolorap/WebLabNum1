import tkinter as tk

from PIL import Image, ImageTk
import globals
from config import STATIC_PATH, WINDOW_HEIGHT, WINDOW_WIDTH


def getImageViewer(root : tk.Frame):
    imageViewer = tk.Frame(root)
    
    content = getContent(imageViewer)
    content.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    return imageViewer


def getContent(frame : tk.Frame):
    content = tk.Frame(frame)

    img = Image.open(f"{STATIC_PATH}/{globals.CURRENT_IMAGE}")

    height, width = img.height, img.width
    
    while (height > int(WINDOW_HEIGHT) and width > int(WINDOW_WIDTH)):
        height, width = int(height * 0.7), int(width * 0.7)
        
        img_rs = img.resize((height, width))
        
    while (height < int(WINDOW_HEIGHT) and width < int(WINDOW_WIDTH)):
        height, width = int(height * 1.3), int(width * 1.3)
        
        img_rs = img.resize((height, width))
    
    test = ImageTk.PhotoImage(img_rs)

    lb = tk.Label(content, image=test)
    lb.image = test
    lb.pack()

    return content