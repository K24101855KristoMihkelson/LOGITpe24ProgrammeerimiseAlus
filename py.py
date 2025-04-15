# NB! kasutajalt sisendi võtmine peab igal juhul tsüklis olema niikaua kuni programm saab õige sisendi
# NB! kasutajasisend tuleb töödelda standardkujuke, nime puhul esisuurtäht, programmi jaoks vajalik sisend ühtlasele kujule jne
# kirjuta programm mis

# küsib kasutajalt tema pin koodi
# küsib kasutajalt tema isikukoodi
# kasutaja saab sisestada pin koodi ainult 3 korda
# kasutaja saab sisestada isikukoodi ka ainult 3 korda
# kui kasutaja on kõik korrad valesti sisestanud kas isikukoodi või pin koodi:
# - joonista kasutajale pilt, kus on kurb nägu trellide taga
# kui pinkood ja isikukood on õiged, küsi kasutajalt:
# - kas ta tahab raha välja võtta või oma pangakaarti tagasi
# - kui ta tahab raha välja võtta siis
# - - küsi kasutajalt kui palju ning joonista talle rahaleht mille peal on väljavõetud summa kirjutatud
# - kui ta tahab oma pangakaarti tagasi siis
# - - joonista talle pangakaart mille peal on tema isikukood
from random import randint
from tkinter import *
kPin_kood = 0
kIsikukood = 0
õige_isikukood =12345678901
õige_pin_kood =1234
while(kPin_kood == 0 or kIsikukood == 0):
    kPin_kood = int(input("Sisesta oma pin-kood: (jah/ei)"))
    kIsikukood = int(input("Sisesta oma isikukood: (jah/ei)"))
    if kPin_kood == õige_pin_kood and  kIsikukood == õige_isikukood:
        print("Kas sa tahad raha välja võtta või oma pangakaarti tagasi")
        raha_välja_võtta = ""
        välja_võte = 100
        while(raha_välja_võtta == ""):
            raha_välja_võtta = input("Sa tahad raha välja: (jah/ei)")
            if raha_välja_võtta == "ei":
                print("Annan sulle tagasi pangakaarti")
else:
    raam = Tk()
    raam.title("joonistamine")
    tahvel = Canvas(raam,width=500, height=500)
    tahvel.create_oval(50,50,450,450,width = 2, outline = "black", fill = "Yellow")
    tahvel.create_oval(150,150,170,170,width = 2, outline = "black", fill = "black")
    tahvel.create_oval(300,150,320,170,width = 2, outline = "black", fill = "black")
    tahvel.pack()
    raam.mainloop()
    
    
    
    
#JOONISTAMISHARJUTUSED TKINTERIGA:
# MAJA (AKEN UKS, KORSTEN, KOLMNURKNE KATUS)
# KULDMÜNT(KOLLANE, RAHAARV, NURGELINE POLÜGON "VAPIKS")
# JÄNES LIHGAVÕTTEMUNADE JA MURUGA (OVAALID, POLÜGONID)

