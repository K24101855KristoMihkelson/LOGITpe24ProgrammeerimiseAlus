from random import randint
from tkinter import *

valik = ""
while valik == "":
    valik = input("Kas sa otsid mingit seent või marja: ").lower()
    
    if valik == "seent":
        seente_valik = []
        seente_kirjeldused = {}
        hetkesisestus = "a"
        
        while hetkesisestus != "":
            hetkesisestus = input("Sisestage enda jaoks sobivaimaid seeni, kui rohkem ei ole, vajuta enter: ")
            if hetkesisestus != "":
                seente_valik.append(hetkesisestus)
                kirjeldus = input(f"Kirjelda konkreetset seent '{hetkesisestus}': ")
                seente_kirjeldused[hetkesisestus] = kirjeldus

        print("\nSinu valitud seened:")
        for seened in seente_valik:
            print(f"{seened}: {seente_kirjeldused[seen]}")

    elif valik == "marja":
        marjade_valik = []
        marjade_kirjeldused = {}
        hetkesisestus = "a"
        
        while hetkesisestus != "":
            hetkesisestus = input("Sisesta enda jaoks sobivaimaid marju, kui rohkem ei ole, siis vajuta enter: ")
            if hetkesisestus != "":
                marjade_valik.append(hetkesisestus)
                kirjeldus = input(f"Kirjelda konkreetset marja '{hetkesisestus}': ")
                marjade_kirjeldused[hetkesisestus] = kirjeldus

        print("\nSinu valitud marjad:")
        for mari in marjade_list:
            print(f"{mari}: {marjade_kirjeldused[mari]}")

    else:
        print("Palun vali ainult 'seent' või 'marja'!")

# Pärast sisestamist
SaTahadVeelMidagiVeelUurida = input("\nKas sa tahad veel midagi lugeda? (jah/ei): ").lower()
if SaTahadVeelMidagiVeelUurida == "jah":
    print("Mine internetti ja otsi näiteks maasikate või puravike kohta rohkem infot!")
elif SaTahadVeelMidagiVeelUurida == "ei":
    raam = Tk()
    raam.title("Marja ots")
    tahvel = Canvas(raam, width=700, height=700)
    tahvel.create_line(387, 289, 387, 130, width=5, fill="brown")  
    tahvel.create_polygon(387, 289, 393, 277, 440, 221, 520, 206, 541, 220, width=5, fill="brown", outline="black")
    tahvel.create_polygon(387, 289, 282, 271, 348, 233, 299, 211, 289, 222, 267, 235, width=5, fill="brown", outline="black")
    tahvel.create_polygon(387, 289, 382, 249, 366, 197, 341, 157, 281, 156, width=5, fill="brown", outline="black")
    tahvel.create_polygon(387, 289, 393, 260, 430, 188, 472, 150, 518, 144, width=5, fill="brown", outline="black")
    tahvel.pack()
    raam.mainloop()