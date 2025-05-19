from tkinter import *
from time import sleep
from os import path

# 1. Küsi objekti nime
objektid = ["pall", "ruubik-kuubik", "vihmavari", "vape"]
objekt = input("Mis objekt sulle meeldib " + str(objektid) + "? ")

# 2. Kontrolli, kas fail olemas gif või png kujul
failinimed = [objekt + ".gif", objekt + ".png"]
fail = None
for f in failinimed:
    if path.exists(f):
        fail = f
        break  # kui esimene sobiv leiti, lõpeta otsimine

if not fail:
    print("Pildi faili ei leitud.")
    exit()


raam = Tk()
raam.title("Liikuv objekt")
tahvel = Canvas(raam, width=1000, height=1000)
tahvel.pack()

pilt = PhotoImage(file="soccer-ball.png")
obj = tahvel.create_image(1000, 1000, image=pall)

pilt = PhotoImage(file="ruubik-kuubik.png")
obj = tahvel.create_image(600, 600, image=ruubik-kuubik)

pilt = PhotoImage(file="vihmavari.png")
obj = tahvel.create_image(1000, 1000, image=vihmavari)

pilt = PhotoImage(file="vape.png")
obj = tahvel.create_image(1000, 1000, image=vape)



raam.update()


for i in range(50):
    tahvel.move(obj, 5, 0)
    raam.update()
    sleep(0.03)

for i in range(50):
    tahvel.move(obj, -5, 0)
    raam.update()
    sleep(0.03)


for i in range(50):
    tahvel.move(obj, 0, 5)
    raam.update()
    sleep(0.03)

for i in range(50):
    tahvel.move(obj, 0, -5)
    raam.update()
    sleep(0.03)


for _ in range(30):
    tahvel.move(obj, 5, 0)
    raam.update()
    sleep(0.02)

for _ in range(30):
    tahvel.move(obj, 0, 5)
    raam.update()
    sleep(0.02)

for _ in range(30):
    tahvel.move(obj, -5, 0)
    raam.update()
    sleep(0.02)

for _ in range(30):
    tahvel.move(obj, 0, -5)
    raam.update()
    sleep(0.02)

raam.mainloop()