# 3 - kasutajatuvastus: kirjuta programm mis:

# küsib kasutajalt tema kasutajanime ja parooli.

# - tsükkel kontrollib et mõlemad oleksid õiged

# - tsükkel toimib niikaua kuni üks kahest on vale

# - kasutajal on 3 katset sisselogimiseks

# - - kui kasutaja on sisestanud õige kasutajanime ja parooli,

# - - küsitakse tsükliga kuuekohalist 2FA arvkoodi.

# - - programm ei pea teadma kas 2FA kood on õige või mitte,

# - - peab kontrollima ainult et arv on kuuekohaline, ja et andmetüüp oleks täisarv (mitte sellises järjestuses)


from random import randint


kasutajaNimi = Kristo
parool = 1234

while kasutajaNimi == Kristo and parool == 1234:
    if kasutajaNimi == parool:
        print("õigesti vastasid nime ja parooli")
    elif kasutajaNimi != parool:
        print("Su andmete sisestus on vale proovi uuesti, sul on 2 katset jäänud")
    else:
        print("Jälle vale arvamus, sul jäi üks katse jäänud")
else:
    print("Sa ei saanudki kasutajasse sisse")
    if kasutajaNimi == parool == "jah":
        twoFA
        twoFA = 0
        while twoFA == 0:
            twoFa int(input("Sisesta kuuekohaline arvkood"))
            if twoFA == len(6):
                print("õige")
            else:
                print("vale")
                
            
        
        
        
        