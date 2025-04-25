# NB! kõik küsimised on tsüklis mis kontrollitud tsüklimuutujaga (mitte True ja break)
# NB! kõik sisendud töödeldakse standardkujule
# kirjuta programm mis
#
# küsib kasutajalt tema lemmikfilme (mitmus = järjend)
# programm küsib ainsana tema aegade kõige lemmikumat filmi (ainsus = muutuja)
# programm kontrollib et tema kõige lemmikum film oleks ka lemmikfilmide järjendis
# - kui on siis öeldakse kasutajale Ossa, oled oma <lemmikfilmi> isegi kaks korda pannud
# - kui ei ole, siis küsitakse aga kus on sinu <lemmikfilm>?
# programm küsib kasutajalt kas talle meeldib <programmeerija lemmikfilm>?
# - kui jah, siis lisatakse film lemmikfilmide järjendisse
# - kui ei, programm vingub "aga miks? see on ju hea"
# kui programm tuvastab et üks filmidest lemmikfilmide järjendis on Terminator siis öeldakse kasutajale et "youll be back"
# kui programm tuvastab et üks filmidest lemmikfilmide järjendis on Vanamehe Film, siis öeldakse "aga kuš šu šnikurš on šiiš?"
# kõige lõpuks loendab programm kokku mitu filmi on tema lemmikfilmide järjendis, ning
# - kui arv on 5 või vähem, öeldakse, sa ei vaata väga palju filme vist.
# - kui arv on 10 või vähem aga rohkem kui 5, "käid tihti kinos?"
# - kui arv on rohkem kui 10, "siis, pole mul siin midagi öelda härra movieguru, headaega"


lemmikfilmid = []
hetkesisestus = "a"
while(hetkesisestus != ""):
    hetkesisesus = input("Sisesta oma kõige lemmikumad filmid siia kogu aja jooksul,kui rohkem ei ole,siis vajuta enter")
    if hetkesisestus != "":
        lemmikfilmid.append(hetkesisestus)
        
kõigelemmikumfilm = []
hetkesisestus = "a"
while(hetkesisestus != ""):
    hetkesisestus = input("Sisesta oma aegade parim film,kui rohkem ei ole,vajuta enter")
    if hetkesisestus != "":
        kõigelemmikumfilm = append(hetkesisestus)




