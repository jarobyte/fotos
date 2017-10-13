from Tkinter import *
import subprocess
import time
from tkFileDialog   import askdirectory

folder = "imagenesRetinas"
run = False 

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

def iniciar():
    global run
    run = True
    
    

def cerrar():
    global run
    run = False

root = Tk()   
root.title("Monitorear carpeta")
errmsg = 'Error!'

w = Label(root, text = "La siguiente carpeta est siendo monitoreada:")
w.pack()
w2 = Label(root, text = folder, bg = "red")
w2.pack()

Button(root, text='Seleccionar otra carpeta', command=callback).pack(fill=X)
Button(root, text='Iniciar monitoreo', command=iniciar).pack(fill=X)
Button(root, text='Parar monitoreo', width=25, command=cerrar).pack(fill = X)

root.after(1000, monitor)
root.mainloop()
