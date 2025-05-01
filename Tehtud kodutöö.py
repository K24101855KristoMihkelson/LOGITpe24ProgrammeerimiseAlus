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

seened = ["puravik","kukeseen","kukeseen"]

seente_kirjeldused = ["Puravik on paksu jalaga söögiseen.","Kukeseen on kollane ja väga maitsev seen.","Kärbseseen on mürgine ja punase mütsiga seen."]


marjad = ["maasikas","mustsõstar","jõhvikas"]
marjade_kirjeldused = ["Maasikas on magus ja punane mari, mida armastatakse suvel süüa.","Jõhvikas on hapukas punane mari, mida kasutatakse sageli mahlades ja moosides.","Mustsõstar on tumeda värvusega mari, millel on tugev ja aromaatne maitse."]
valik = ""
while(valik == ""):
    valik = input("Kas sa otsid mingit seent või marja:").lower()
    if valik == "seent":
        hetkesisestus = 0
        while(hetkesisestus == 0):
            hetkesisestus = int(input("Vali enda jaoks sobivaimaid seened " + str(seened) + " ,vali enda jaoks sobiv arv,vajuta enter"))
            if hetkesisestus != 0:
                print(seente_kirjeldused[hetkesisestus -1])
    
    elif valik == "marja":
        hetkesisestus = 0
        while(hetkesisestus == 0):
            hetkesisestus = int(input("Vali enda jaoks sobivaimaid marju " + str(marjad) + ",vali enda jaoks sobiv arv,vajuta enter"))
            if hetkesisestus != 0:
                print(marjade_kirjeldused[hetkesisestus -1])
               
else:
    SaTahadVeelMidagiVeelUurida = ""
    SaTahadVeelMidagiVeelUurida = input("Kas sa tahad veel midagi lugeda: (jah/ei/lisa)").lower()
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
    elif SaTahadVeelMidagiVeelUurida == "lisa":
        if valik == "seent":
            seened = ["puravik","kukeseen","kärbseseen"]
            uusSeen = input("Lisa juurde uus seen:")
            seened.append(uusSeen)
            print(seened)
        elif valik == "marja":
            marjad = ["maasikas","mustsõstar","jõhvikas"]
            uusmari = input("Lisa juurde uus mari:")
            marjad.append(uusmari)
            print(marjad)
        