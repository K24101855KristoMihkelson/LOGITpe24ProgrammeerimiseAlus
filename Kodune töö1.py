# küsib kasutajalt tema lemmikfilme (mitmus = järjend)
# programm küsib ainsana tema aegade kõige lemmikumat filmi (ainsus = muutuja)
# programm kontrollib et tema kõige lemmikum film oleks ka lemmikfilmide järjendis
# - kui on siis öeldakse kasutajale Ossa, oled oma isegi kaks korda pannud
# - kui ei ole, siis küsitakse aga kus on sinu ?
# programm küsib kasutajalt kas talle meeldib ?
# - kui jah, siis lisatakse film lemmikfilmide järjendisse
# - kui ei, programm vingub "aga miks? see on ju hea"
# kui programm tuvastab et üks filmidest lemmikfilmide järjendis on Terminator siis öeldakse kasutajale et "youll be back"
# kui programm tuvastab et üks filmidest lemmikfilmide järjendis on Vanamehe Film, siis öeldakse "aga kuš šu šnikurš on šiiš?"
# kõige lõpuks loendab programm kokku mitu filmi on tema lemmikfilmide järjendis, ning
# - kui arv on 5 või vähem, öeldakse, sa ei vaata väga palju filme vist.
# - kui arv on 10 või vähem aga rohkem kui 5, "käid tihti kinos?"
# - kui arv on rohkem kui 10, "siis, pole mul siin midagi öelda härra movieguru, headaega"

from random import randint
Lfilm = ""
Lfilm_nimetused = ["Kevad","Suvi","Sügis","Talv"]

lemmikfilmid = []
hetkesisestus = "a"
while(hetkesisestus != ""):
    hetkesisestus = input("Sisestage enda lemmikud filmid,kui rohkem ei ole,vajutage enter")
    if hetkesisestus != "":
        filmi_nimetus = ""
        filmi_nimetus = input(f"Sisesta filmi nimetus '{hetkesisestus}': ")
        lemmikfilmid.append(hetkesisestus)
        Lfilm_nimetused.append(filmi_nimetus)
    print(f"Lisati: {lemmikfilmid} - {filmi_nimetus}")
    print(lemmikfilmid)
    print(Lfilmi_nimetused)

KõigeLemmikumFilm = ""
while(KõigeLemmikumFilm == ""):
    KõigeLemmikumFilm = input("Mis on sinu kõige lemmikum film kogu aegade jooksul? 1-Kevad,2-Suvi,3-Sügis,4-Talv")
    suvaline_arv = randint(1,4)
    if suvaline_arv ==1:
        print("Kevad")
    elif suvaline_arv ==2:
        print("Suvi")
    elif suvaline_arv ==3:
        print("Sügis")
    elif suvaline_arv ==4:
        print("Talv")
    print(suvaline_arv)
    
    KõigeLemmikumFilm = input("Kas su film on siin järjendis olemas? (jah/ei)")
    if KõigeLemmikumFilm == "jah":
        print("Ossa,oled olnud kaks korda enda lemmikfilmi pannud")
    elif KõigeLemmikumFilm == "ei":
        KusOn = ""
        KusOn = input("Kus on sinu film?(kuskil on/ei tea)")
        if KusOn == "kuskil on":
            print("Siis,sisesta enda lemmikfilm ka siia nimekirja.")
        elif KusOn == "ei tea":
            print("Kui ei tea siis ei tea,vaata filmide nimekirju,võib olla leiad enda lemmikfilmi ka sealt üles")
            film = ""
            while(film == ""):
                film = input("Kas sulle meeldib sisestatud film? (jah/ei)")
                if film == "jah":
                    lemmikfilmid = []
                    hetkesisestus = "a"
                    while(hetkesisestus != ""):
                        hetkesisestus = input("Sisestage enda lemmikud filmid,kui rohkem ei ole,vajutage enter")
                        if hetkesisestus != "":
                            lemmikfilmid.append(hetkesisestus)
                        print(lemmikfilmid)
                elif film == "ei":
                    print("aga miks? See on ju hea")
                    
                    Terminaator = ""
                    Vanamehe_film = ""
                    Terminaator = input("Su üks lemmikfilmidest oli Terminaator,valik(1)")
                    Vanamehe_film = input("Su üks lemmikfilmidest oli Vanamehe film,valik(2)")
                    suvaline_arv = randint(1,2)
                    if suvaline_arv ==1:
                        print("youll be back")
                    elif suvaline_arv ==2:
                        print("aga kuš šu šnikurš on šiiš?")
filmiloend = ""
while(filmiloend == ""):
    filmiloend = int(input("Loenda kõik filmid kokku?"))
    if filmiloend <= 5:
        print("sa ei vaata väga palju filme vist")
    if filmiloend >= 5 and arv <= 10:
        print("käid tihti kinos?")
    elif filmiloend > 10:
        print("siis, pole mul siin midagi öelda härra movieguru, headaega")
        
                    
                    
                
    
        
                            
            
        
            
    
    