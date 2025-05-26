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


from tkinter import*
from time import*

objektid = ["pall","ruubik-kuubik","vihmavari","vape"]
objekt = 0
def uuenda():
    global x
    tahvel.move(img, x, y)
    print("uuenda")
    return
    
while objekt == 0:
    objekt = int(input("Sisesta "+str(objektid)+ " numbritena, 1,2,3,4"))
raam = Tk()
raam.title("pall")
tahvel = Canvas(width = 3000, height = 3000, background = "white")

x = 0
y = 0
        
tahvel.grid()
pall =  PhotoImage(file="pall.png")
img = tahvel.create_image(0,0, image=pall, anchor=NW)

    
while x < 25:
    print(x)
    x +=1
    raam.after(50,uuenda())
    tahvel.pack()
    raam.uptade()
    
while x < 25:
    print(x)
    x -=1
    raam.after(50,uuenda())
    tahvel.pack()
    
raam.uptade()
raam.mainloop()


    
    




    

    
#     pall = PhotoImage(file="pall.png")
#     img = tahvel.create_image(0,0, image=pall, anchor=NW)
#     def uuenda(img):
#         global x
#         tahvel.move(img, x, y)
#     print(x)
#     raam.after(200,uuenda(img))
#     
#     while y < 700:
#         y +=1
#         uuenda(img)
#         tahvel.pack()
#         x = 0
#         y = 0
#     
#     pall = PhotoImage(file="pall.png")
#     img = tahvel.create_image(0,0, image=pall, anchor=NW)
# def uuenda(img):
#     global y
#     tahvel. move(img, x, y)
# print(y)

    
    
        