import tkinter as tk

import globals


def button_action(HOST: str) -> None:
    globals.PAGES["changeImage"].tkraise()
    globals.HOST = HOST
    

def getConnectPage(root : tk.Frame) -> tk.Frame:
    connect = tk.Frame(root)

    content = getContent(connect)
    content.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    return connect


def getContent(frame : tk.Frame) -> tk.Frame:
    content = tk.Frame(frame)

    inviteLabel = tk.Label(content, text="Введите IP-адрес хоста")
    inviteLabel.pack()

    inviteInp = tk.Entry(content)
    inviteInp.pack()

    btnStartConnect = tk.Button(content, text="Начать", 
                                command=lambda: button_action(inviteInp.get()))
    btnStartConnect.pack()

    return content