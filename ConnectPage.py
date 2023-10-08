import tkinter as tk
from Pages import pages

def getConnectPage(root : tk.Frame):
    connect = tk.Frame(root)

    content = getContent(connect)
    content.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    return connect

def getContent(frame : tk.Frame):
    content = tk.Frame(frame)

    inviteLabel = tk.Label(content, text="Введите IP-адрес хоста")
    inviteLabel.pack()

    inviteInp = tk.Entry(content)
    inviteInp.pack()

    btnStartConnect = tk.Button(content, text="Начать", command=lambda: pages["changeImage"].tkraise())
    btnStartConnect.pack()

    return content