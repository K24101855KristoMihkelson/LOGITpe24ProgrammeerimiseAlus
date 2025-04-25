tänavanimed = []
kasutajasisestus = "a"
mitteeimeelditäht = ""
while(kasutajasisestus != ""):
    kasutajasisestus = input("Sisesta oma kodukandi tänavanimi,kui rohkem ei ole,siis vajuta enter")
    if kasutajasisestus != "":
        tänavanimed.append(kasutajasisestus)


while(mitteeimeelditäht == ""):
    mitteeimeelditäht = input("Milline tähestiku täht sulle ei meeldi")
    if (len(mitteeimeelditäht) > 1):
        print("Sisesta ainult üks täht,proovi uuesti")
        mitteeimeeldivtäht = ""
        
ontäht = []
eioletäht = []
TNarv = len(tänavanimed)-1
while TNarv >= 0:
    if mitteeimeeldivtäht in tänavanimed [TNarv]:
        ontäht.append(tänavanimed[TNarv])
    else:
        eioletäht.append(tänavanimed[TNarv])
        
    TNarv -= 1
    print("Järgnevates tänavanimedes ei esine  ebameeldivat tähte_",eioletäht)
    print("Tänavanimesid kus aga ebameeldiv täht esineb on",len(ontäht),"tükki")
    