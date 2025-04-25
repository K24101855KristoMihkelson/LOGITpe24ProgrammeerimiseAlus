#1 – püstine müügiautomaat

# kirjutage programm, mis:

# - küsib kasutajalt, kas ta soovib kuulda anekdooti?

# - kui jah, siis küsib kasutajalt, kas talle meeldib:

# - - rahvused

# - - linnud-loomad

# - - või sõda

# - kui kasutaja valib rahvuse, esitatakse kasutajale juhuslik arv 1 kolmest rahvusega seotud anekdoodist

# - kui kasutaja valib linnud-loomad, esitatakse kasutajale juhuslik arv 1 kolmest lindude ja loomadega seotud anekdoodist

# - kui kasutaja valib sõja, esitatakse kasutajale juhuslik arv 1 kolmest sõjaga seotud anekdoodist.

# - kui kasutaja otsustab anekdooti mitte tahta, hakkab programm küsima

# NB - anekdoodid tuleb avaldada nii, et anekdoodis endas kasutatakse jutumärke

from random import randint

anekdoot = ""
anekdoot = input("Sa tahad kuulda anekdooti: (jah/ei)")
if anekdoot == "jah":
    rahvused = ""
    while(rahvused == ""):
        rahvused = input("Sisesta rahvustega seotud anektoodid")
        suvaline_arv = randint(1,3)
        if suvaline_arv == 1 :
            print(" 'Karu hüppas vetsupoti peale' ")
        elif suvaline_arv == 2:
            print = (" 'Tort visati inimesele näkku' ")
        elif suvaline_arv == 3:
            print = (" 'Vanamees sai suure kulbi' ")
    print(suvaline_arv)
elif anekdoot == "jah":
    LiLo = ""
        while(LiLo = ""):
            LiLo = input("'Sisesta lindude ja loomade anekdooti'")
            suvaline_arv = randint(1,3)
            if suvaline_arv == 1:
                print(" 'Lind tegi enda asju sinu pea peale' ")
            elif suvaline_arv == 2:
                print("'Su pea on nagu linnu pesa'")
            elif suvaline_arv == 3:
                print("'Karuott tõstis enda päkad ülesse'")
        print(suvaline_arv)
elif anekdoot == "jah":
    sõda = ""
    while(sõda = ""):
        sõda = input("Sisesta sõja anekdoodid:")
        suvaline_arv = randint(1,3)
        if suvaline_arv == 1:
            print("'Bomb maandus sinna kuhu kedagi ei oodatud'")
        elif suvaline_arv ==2:
            print("'ise ei tapnud vaenlast vaid iseennast'")
        elif suvaline_arv ==3:
            print("'Vaenlane oli lollim ja andis enda tarkuse mulle edasi'")
    print(suvaline_arv)
else:
    ei_taha_anekdooti = ""
    while( ei_taha_anekdooti = ""):
        ei_taha_anekdooti = input("Sa tahad anekdooti? (jah/ei)")
        if ei_taha_anekdooti == "jah":
            print("head aega")
        elif ei_taha_anekdooti == "ei":
            print("Mine tagasi algusesse")
            
    