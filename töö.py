# Kirjuta ülesanne mis: (vaja teha)
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

valik = ""
while(valik == ""):
    valik = input("Sulle meeldivad rohkem seened kui marjad (Marjad/seened)")
seened = ""
marjad = ""
seened = []
hetkesisestus = "a"
while(hetkesisestus != ""):
    hetkesisestus = input("sisestage enda jaoks sobivaimaid seeni,kui rohkem ei ole,siis vajuta enter")
    if hetkesisestus != "":
        seened.append(hetkesisestus)


marjad = []
hetkesisestus = "a"
while(hetkesisestus != ""):
    hetkesisestus = input("Sisesta enda jaoks sobivaimaid marju,kui rohkem valikus pole midagi,siis vajuta enter")
    if hetkesisestus != "":
        marjad.append(hetkesisestus)
