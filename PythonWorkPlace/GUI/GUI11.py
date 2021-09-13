# Menu Widget

from tkinter import *

root = Tk()

def hello():
    print("hello!")

menubar = Menu(root)
menubar.add_command(label="Hello", command=hello)
menubar.add_command(label="Quit!", command=root.quit)

root.config(menu=menubar)

root.mainloop()