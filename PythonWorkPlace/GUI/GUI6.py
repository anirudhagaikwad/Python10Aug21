# Geometry Managers : --> place()


import tkinter as tk
from tkinter import *
from tkinter.constants import RAISED

win=tk.Tk()
win.geometry("500x400")
var=StringVar()
username=tk.Label(win,text="Username",bd=5,bg="red",relief=RAISED).place(x=30,y=50)
email=tk.Label(win,text="Email").place(x=30,y=90)
passwd=tk.Label(win,text="Password",textvariable=var).place(x=30,y=130)
submit=tk.Button(win,text="Submit").place(x=160,y=160)
var.set("new text ... ")
e1=tk.Entry(win).place(x=80,y=50)
e2=tk.Entry(win).place(x=80,y=90)
e3=tk.Entry(win).place(x=95,y=130)
win.mainloop()