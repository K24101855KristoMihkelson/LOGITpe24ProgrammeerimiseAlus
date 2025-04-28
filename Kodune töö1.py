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

lemmikfilmid = []
hetkesisestus = "a"
while(hetkesisestus != ""):
    hetkesisestus = input("Sisestage enda lemmikud filmid,kui rohkem ei ole,vajutage enter")
    if hetkesisestus != "":
        lemmikfilmid.append(hetkesisestus)
print(lemmikfilmid)
KõigeLemmikumFilm = ""
while(KõigeLemmikumFilm == ""):
    KõigeLemmikumFilm = input("\nMis on sinu kõige lemmikum film kogu aegade jooksul? ")
    if KõigeLemmikumFilm in lemmikfilmid:
        print("Ossa, oled oma lemmiku isegi kaks korda pannud!")
    else:
        print(f"Aga kus on sinu '{KõigeLemmikumFilm}'?")
        muljetavaldav = input(f"Kas sulle meeldib '{KõigeLemmikumFilm}'? (jah/ei): ").lower()
        if muljetavaldav == "jah":
            lemmikfilmid.append(KõigeLemmikumFilm.strip())
            print(f"Lisati '{KõigeLemmikumFilm}' ka sinu lemmikfilmide nimekirja!")
        else:
            print("Aga miks? See on ju hea film!")

if "Terminaator" in lemmikfilmid:
    print("Youll be back")
elif "Vanamees" in lemmikfilmid:
    print("Aga kuš šu šnikurš on šiiš?")
else:
    print("Vali enda jaoks sobiv film,siis")
    
filmide_arv = len(lemmikfilmid)
print(f"\nSul on kokku {filmide_arv} lemmikfilmi.")
if filmide_arv <= 5:
    print("Sa ei vaata väga palju filme vist.")
elif 5 < filmide_arv <= 10:
    print("Käid tihti kinos?")
elif filmide_arv > 10:
    print("Siis, pole mul siin midagi öelda härra movieguru, headaega.")
                   

        
                    
                    
                
    
        
                            
            
        
            
    
    