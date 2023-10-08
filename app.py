import tkinter as tk

from Pages import pages
from ChangeImagePage import getChangeImagePage
from ConnectPage import getConnectPage
from ImageViewerPage import getImageViewer

root = tk.Tk()
root.title('My App')
root.geometry("600x500")

pages["changeImage"] = getChangeImagePage(root)
pages["connect"] = getConnectPage(root)
pages["imageViewer"] = getImageViewer(root)

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=10)

connectBtn = tk.Button(root, text="Управление", command=lambda: pages["connect"].tkraise())
connectBtn.grid(row=0, column=0)

imageBtn = tk.Button(root, text="Получение", command=lambda: pages["imageViewer"].tkraise())
imageBtn.grid(row=0, column=1)

pages["changeImage"].grid(row=1, column=0, columnspan=2, sticky="nsew")
pages["connect"].grid(row=1, column=0, columnspan=2, sticky="nsew")
pages["imageViewer"].grid(row=1, column=0, columnspan=2, sticky="nsew")

pages["connect"].tkraise()

root.mainloop()