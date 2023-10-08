import tkinter as tk
from Pages import pages

def getChangeImagePage(root : tk.Frame):
    changeImage = tk.Frame(root)

    content = getContent(changeImage)
    content.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    return changeImage

def getContent(frame : tk.Frame):
    content = tk.Frame(frame)

    label = tk.Label(content, text="Нажмите, чтобы изменить картинку")
    label.pack()

    btn = tk.Button(content, text="Изменить")
    btn.pack()

    return content