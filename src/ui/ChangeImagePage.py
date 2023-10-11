import tkinter as tk
from tkinter import filedialog as fd

import globals
from src.api.api import send


def upload_btn():
    name = fd.askopenfilename() 
    globals.UPLOADED_FILE = name
        
        
def send_signal() -> None:
    send(globals.HOST)


def send_file():
    send(globals.HOST, globals.UPLOADED_FILE)


def getChangeImagePage(root: tk.Frame):
    changeImage = tk.Frame(root)

    content = getContent(changeImage)
    content.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    content2 = uploadButton(changeImage)
    content2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    return changeImage


def getContent(frame: tk.Frame):
    content = tk.Frame(frame)

    label = tk.Label(content, text="Нажмите, чтобы изменить картинку")
    label.pack()

    btn = tk.Button(content, text="Изменить", command=send_signal)
    btn.pack()

    return content


def uploadButton(frame: tk.Frame):
    content = tk.Frame(frame)
    
    label = tk.Label(content, text="Нажмите, чтобы отправить файл")
    label.pack()
    
    upd_btn = tk.Button(content, text='Файл',  command=upload_btn)
    upd_btn.pack()
    
    send_btn = tk.Button(content, text='Отправить',  command=send_file)
    send_btn.pack()
    
    return content