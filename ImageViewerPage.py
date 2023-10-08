import tkinter as tk
import Paths as Paths

from Pages import pages
from PIL import ImageTk, Image  

def getImageViewer(root : tk.Frame):
    imageViewer = tk.Frame(root)
    
    content = getContent(imageViewer)
    content.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    return imageViewer

def getContent(frame : tk.Frame):
    content = tk.Frame(frame)

    img = Image.open(Paths.image)
    test = ImageTk.PhotoImage(img)

    lb = tk.Label(content, image=test)
    lb.image = test
    lb.pack()

    return content