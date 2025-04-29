# - küsib kasutajalt kas ta otsib mingit seent või marja
# - küsimine toimub tsükli sees
# - - kui seent, siis programm esitab talle seente järjendi sisu. (seal on seened mida te panna otsustasite)
# - - - siis küsib kasutajalt millise seene kohta ta lugeda tahab, ning teisest - sisujärjendist - kuvatakse
# kasutajale seene kohta tekst
# - - - - Kasutajale antakse koos seeneloendiga ka üks alati esinev valikuvõimalus - "lisa juurde"
# Lisa juurde valikuga lisatakse seentejärjendile otsa uus element, mille sisend küsitakse kasutajalt
# - - - - sama tehakse ka sisujärjendiga kuhu küsitakse otsa uue sisestatud seene juurde ka selle seene kirjelduslikm info.
# - - kui marja, siis programm esitab talle marjade järjendi sisu. (seal on marjad mida te panna otsustasite)
# - - - siis küsib kasutajalt millise marja kohta ta lugeda tahab, ning teisest - sisujärjendist - kuvatakse
# kasutajale marja kohta tekst
# - - - - Kasutajale antakse koos marjaloendiga ka üks alati esinev valikuvõimalus - "lisa juurde"
# Lisa juurde valikuga lisatakse marjajärjendile otsa uus element, mille sisend küsitakse kasutajalt
# - - - - sama tehakse ka sisujärjendiga kuhu küsitakse otsa uue sisestatud marja juurde ka selle marja kirjelduslikm info.
# - pärast seda küsib programm uuesti kas ta tahab lugeda veel millegi kohta, ning programm läheb
from random import randint
from tkinter import*

valik = ""
while(valik == ""):
    valik = input("Kas sa otsid mingit seent või marja:").lower()
    if valik == "seent":
        seent = []
        seente_kirjeldused = ()
        hetkesisestus = "a"
        while(hetkesisestus != ""):
            hetkesisestus = input("Sisestage enda jaoks sobivaimaid seeni,kui rohkem ei ole,vajuta enter").capitalize()
            if hetkesisestus != "":
                kirjeldus= input("Kirjelda konkreetset seent " + str(hetkesisestus) + ": ")
                seent.append(hetkesisestus)
                seente_kirjeldused.append(kirjeldus)
         
print("\nSinu valitud seened:")
for seened in seente_valik:
    print(" +str(seened) + "" +str(seente_kirjeldused)+ " + str(seen) + "")    
            
    elif valik == "marja":
        marja = []
        marjade_kirjeldused = ()
        hetkesisestus = "a"
        while(hetkesisestus != ""):
            hetkesisestus = input("Sisesta enda jaoks sobivaimaid marju,kui rohkem ei ole,siis vajuta enter")
            if hetkesisestus != "":
                kirjeldus = ""
                kirjeldus= input("Kirjelda konkreetset marja " + str(hetkesisestus) + "")
                marja.append(hetkesisestus)
                marjade_kirjeldused.append(kirjeldus)
        
    print("\nSinu valitud seened:")
    for mari in seente_valik:
        print(" +str(mari) + ":" +str(marjade_kirjeldused)+ " + str(mari) + "")        
else:
    SaTahadVeelMidagiVeelUurida = ""
    SaTahadVeelMidagiVeelUurida = input("Kas sa tahad veel midagi lugeda: (jah/ei)").lower()
    if SaTahadVeelMidagiVeelUurida == "jah":
        print("Mine internetti ja otsi maasikate või puravikude kohta infot juurde").lower()
    elif SaTahadVeelMidagiVeelUurida == "ei":
        raam = Tk()
        raam.title("marja ots")
        tahvel = Canvas(raam,width = 700, height = 700)
        tahvel.create_line(387,289,387,130,width = 5, fill = "brown")
        tahvel.create_polygon(387,289,393,277,440,221,520,206,541,220,width = 5,fill = "brown",outline = "black")
        tahvel.create_polygon(387,289,282,271,348,233,299,211,289,222,267,235,width = 5,fill = "brown",outline = "black")
        tahvel.create_polygon(387,289,382,249, 366,197,341,157, 281,156,width = 5,fill = "brown",outline = "black")
        tahvel.create_polygon(387,289,393,260,430,188,472,150,518,144,width = 5,fill = "brown",outline = "black")
        tahvel.pack()
        raam.mainloop()



            
    
    
            