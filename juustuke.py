#kirjuta programm mis
#kasutab time paketti
#kasutab tkinter paketti
#
# * küsi kasutajalt milline objekt talle kõige rohkem meeldib (valikus on pall, ruubiku-kuubik, vihmavari, vape)
# programm otsib samast kaustast pildi selle nimega kas gif või png formaadis.
# kasutades time.sleep() ja tahvel.move() ning raam.update() käsklusi
# pane objekt ümber ekraani tsükli abil liikuma
# - kõigepealt edasi-tagasi
# - ja siis üles-alla
# - ning siis ürita tsüklid ringiminemise jaoks ühendada
# tahvel.coords() seab objektile uued koordinaadid (muutuja, uus x1, uus y1, uus x2, uus y2)
# tahvel.move() liigutab objekti, parameetrid: (muutuja, kui palju x muuta, kui palju y muuta)
# raam.update() värskendab akna sisu, vajalik enne ka tahvel.pack() teha
# time.sleep() pidurdab programmi tööd sekunditega
# raam.after() pidurdab raami uuendust millisekundites, 1000ms = 1s
# loe lisa siit: https://web.htk.tlu.ee/digitaru/programmeerimine/chapter/lisalugemine-funktsiooni-graafik-liikuvad-pildid/
 
# ülesande standardlahendus: objekt liigub ruudukujulise trajektooriga akna sees
# ülesande boonuslahendus: objekt liigub ringi trajektooriga akna sees

from tkinter import *
import time
raam = Tk()
raam.title("CHEEZ")
tahvel = Canvas(width = 500, height = 500, background = "white")

x = 0
y = 0

def uuenda():
    global x
    tahvel.move(img, x, y)
#     time.sleep(0.01)
#     uuenda()
    print(x)
    raam.after(200,uuenda)
    
juust = PhotoImage(file="juust.png")
img = tahvel.create_image(0,0, image=juust, anchor=NW)

#print(str(img.bbox()))

while x < 500:
    x +=1
    uuenda()
    tahvel.pack()
    raam.mainloop()

x = 0
y = 0

def uuenda():
    global x
    tahvel.move(img, x, y)
#     time.sleep(0.01)
#     uuenda()
    print(x)
    raam.after(200,uuenda)
    
juust = PhotoImage(file="juust.png")
img = tahvel.create_image(0,0, image=juust, anchor=NW)

#print(str(img.bbox()))

while x < 500:
    x -=1
    uuenda()
    tahvel.pack()
    raam.mainloop()