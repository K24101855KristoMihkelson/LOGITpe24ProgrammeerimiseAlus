#kirjuta programm mis
#kasutab time paketti
#kasutab tkinter paketti
#
# küsi kasutajalt milline objekt talle kõige rohkem meeldib (valikus on pall, ruubiku-kuubik, vihmavari, vape)
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
from time import*

objektid = ["pall", "ruubiku-kuubik", "vihmavari", "vape"]
objekt = 0
while objekt == 0:
    objekt = int(input("Sisesta sisse "+str(objektid)+" numbritena, 1,2,3,4: "))
    if objekt == 1:
        raam = Tk()
        raam.title("pall")
        tahvel = Canvas(raam, width=1000, height=1000, background="white")
        tahvel.pack()
    pall = PhotoImage(file="pall.png") 
    img = tahvel.create_image(0, 0, image=pall, anchor=NW)

    x = 0
    y = 0
    while x < 200:
        tahvel.move(img, 1, 0)
        x += 1
        raam.update()
        sleep(0.01)
    while y < 200:
        tahvel.move(img, 0, 1)
        y += 1
        raam.update()
        sleep(0.01)
    while x > 0:
        tahvel.move(img, -1, 0)
        x -= 1
        raam.update()
        sleep(0.01)
    while y > 0:
        tahvel.move(img, 0, -1)
        y -= 1
        raam.update()
        sleep(0.01)

for pall in range(100):
    tahvel.move(img, 1, 0)
    raam.update()
    sleep(0.01)
for pall in range(90):
    tahvel.move(img, -1, 0)
    raam.update()
    sleep(0.01)
for pall in range(100):
    tahvel.move(img, 0, 1)
    raam.update()
    sleep(0.01)
for pall in range(90):
    tahvel.move(img, 0, -1)
    raam.update()
    sleep(0.01)

tahvel.pack()
raam.mainloop()