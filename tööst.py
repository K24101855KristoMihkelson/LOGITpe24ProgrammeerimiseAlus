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


from tkinter import*
import time

objekt = ""
while(objekt = ""):
    objekt = int(input("Vali enda jaoks sobiv objekt: valikus on  pall,ruubik-kuubik,vihmavari,vape"))
    objekt = ""
    while(