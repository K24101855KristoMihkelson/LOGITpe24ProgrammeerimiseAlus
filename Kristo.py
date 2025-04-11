kNimi = ""
while( kNimi == "" ):
    kNimi = input("Sisesta oma ees-ja perekonnanimi").title()
kasOnLoom = ""
millineLoomaliik = ""
while(millineLoomaliik == ""):
    kasOnLoom = input("Kas sul on koduloom? (jah/ei) ")
    if kasOnLoom == "jah":
        millineLoomaliik = input("Kas sul on koduloomaks koer või kass?").lower()
    else:
        break
if(kasOnLoom == "jah"):
    if(millineLoomaliik == "kass"):
        mituKassi = int(input("Mitu kassi sul on?"))
        kassiNimed = ""
        mitmes = 1
        while(mituKassi > 0):
            print("Sisesta oma "+str(kassiNimed)+"kassi nimi:")
            kassiNimed +=" , "
            kassiNimed+=input()
            mitmes +=1
            mituKassi -= 1
        print(kNimi, "Olen kindel et"+kassiNimed+" on täitsa armsad")
    if(millineLoomaliik == "koer"):
        koeraliik = ""
        koeraNimi = ""
        while(koeraliik == "" or koeraNimi == ""):
            if koeraliik == "":
                koeraliik = input("Palun ütle oma koera tõug")
            if koeraNimi == "":
                koeraNimi = input("Palun ütle oma koera nimi ka")
            print(kNimi,"teil on ilus "+koeraliik+" koer,",koeraNimi)
elif(kasOnLoom == "ei"):
    kasOnKonsool = input("Kas sul on konsoole? (jah/ei) ").lower()
    if kasOnKonsool == "ei":
        print("Head aega")
    else:
        mituKonsooli = int(input("Mitu konsooli sul on"))
        konsooliTsükkel = mituKonsooli
        konsoolid = ""
        mitmes = 1
        while(mituKonsooli > 0):
            print("Sisesta oma"+str(mitmes)+". konsool")
            konsoolid += (input()+" , ")
            mitmes += 1
            mituKonsooli -= 1
        if mituKonsooli > 1:
            print("Go touch grass nerd")
        elif mituKonsooli == 1:
            print(kNimi, "Loodan,et oled oma"+konsoolid+"konsooliga epic gamer")
            