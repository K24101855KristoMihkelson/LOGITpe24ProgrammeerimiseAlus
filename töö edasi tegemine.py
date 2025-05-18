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
# raam.after() pidurdab raami uuendust mill isekundites, 1000ms = 1s
# loe lisa siit: https://web.htk.tlu.ee/digitaru/programmeerimine/chapter/lisalugemine-funktsiooni-graafik-liikuvad-pildid/
 
# ülesande standardlahendus: objekt liigub ruudukujulise trajektooriga akna sees
# ülesande boonuslahendus: objekt liigub ringi trajektooriga akna sees

from tkinter import*
from time import*
from os import*


valik = ["pall", "ruubiku-kuubik", "vihmavari", "vape"]

objekt = ""
for objekt in range(4):
    sisend = input("Vali objekt "+str(valik)+": ").lower()
    if sisend in valikud:
        objekt = sisend
    else:
        print("Vale valik. Proovi uuesti.")
if objekt == "":
    print("Ei valitud sobivat objekti. Programm lõpetab.")
    exit()
failinimi = "+str(objekt)+".gif
if not os.path.exists(failinimi):
    print("Pilt failinimega", failinimi, "ei leitud!")
    exit()
raam = tk.Tk()
raam.title("Objekti joonistamine")
raam.geometry("600x400")
tahvel = tk.Canvas(raam, width=600, height=400)
tahvel.pack()

pildiks = tk.PhotoImage(file=failinimi)
kujutis = tahvel.create_image(50, 50, anchor="nw", image=pildiks)

def liigu_edasi_tagasi():
    for _ in range(50):
        tahvel.move(kujutis , 5, 0)
        raam.update()
        time.sleep(0.03)
    for _ in range(50):
        tahvel.move(kujutis, -5, 0)
        raam.update()
        time.sleep(0.03)
        
def liigu_yles_alla():
    for _ in range(30):
        tahvel.move(kujutis, 0, 5)
        raam.update()
        time.sleep(0.03)
    for _ in range(30):
        tahvel.move(kujutis, 0, -5)
        raam.update()
        time.sleep(0.03)

liigu_edasi_tagasi()
liigu_yles_alla()

raam.mainloop()