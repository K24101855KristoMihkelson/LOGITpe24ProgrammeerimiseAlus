def liida(a,b):
    return a+b
def lahuta(a,b):
    return a-b
def korruta(a,b):
    return a*b
def jaga(a,b):
    return a/b
def astenda(a,b):
    return a**b
valitehe = """Palun vali tehe:
¤ liida
¤lahuta
¤jaga
¤korruta
¤astenda
"""
variableA = 0
variableB = 0
tehe = ""
while tehe == "":
    tehe = input(valitehe)
    variableA = input("sisesta esimene arv (korrutatav jagatav)")
    variableB = input("sisesta teine arv (korrutatav jagatav)")
    
    if tehe == "liida":
        liida(variableA,variableB)
    elif tehe == "lahuta":
        lahuta(variableA,variableB)
    elif tehe == "jaga":
        jaga(variableA,variableB)
    elif tehe == "korruta":
        korruta(variableA,variableB)
    elif tehe == "astenda":
        astenda(variableA,variableB)
    if tehe != "liida" and tehe != "lahuta" and tehe != "jaga" and tehe != "korruta" and tehe != "astenda":
        jaga(variableA,variableB):
            print("Ei tunne tehte liiki,palun sisesta uuesti")
        tehe == ""
