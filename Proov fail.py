from tkinter import *

raam = Tk()
raam.title("empty tahvel")

tahvel = Canvas(raam, width=600, height=600)

tahvel.create_polygon(100,0,200,0,300,100,300,200,200,300,100,300,0,200,0,100,width = 15, outline = "black", fill = "white")

tahvel.pack()

raam.mainloop()