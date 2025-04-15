from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():
    tervitus = "Good morning " + nimi.get()
    messagebox.showinfo(message=tervitus)

raam = Tk()
raam.title("CostCo Greeting program")
# raam.geometry("300x100")

silt = ttk.Label(raam, text="nimi")
silt.grid(column=0,row=0,padx=5,pady=5,sticky=(N,W))

nimi = ttk.Entry(raam)
nimi.grid(column=1,row=0,padx=5,pady=5,sticky=(N,W,E))

nupp = ttk.Button(raam, text="Customer greeting", command=tervita)
nupp.grid(column=1,row=1,padx=5,pady=5,sticky=(N,S,E,W))

raam.columnconfigure(1, weight=1)
raam.rowconfigure(1, weight=1)

raam.mainloop()