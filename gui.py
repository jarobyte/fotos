#-*- coding: utf-8 -*-
from Tkinter import *
import subprocess
import time
from tkFileDialog   import askdirectory

folder = open("historial", "r").readline().strip("\n")

run = True

def callback():
    name= askdirectory() 
    global folder
    folder = str(name)
    global w2
    w2.config(text = folder)

def monitor():
    if run:
        subprocess.call(["python", "monitor.py", folder])
    root.after(1000, monitor)

root = Tk()   
root.title("Monitorear carpeta")
errmsg = 'Error!'

w = Label(root, text = "La siguiente carpeta está siendo monitoreada:")
w.pack()
w2 = Label(root, text = folder, bg = "red")
w2.pack()

monitor()

Button(root, text='Seleccionar otra carpeta', command=callback).pack(fill=X)

root.after(1000, monitor)
root.mainloop()
