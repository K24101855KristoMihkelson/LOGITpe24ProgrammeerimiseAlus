# loeb failist laulusõnu (ise valid laulu)
# kuvab välja kõik sõnad
# arvutab kokku mitu täishäälikut on (aeiouõäöüy)
# kuvab välja kõik sõnad mis on pikemad kui 7 tähte
# laseb kasutajal kirjutada ise ühe värsi (4 rida) juurde

import csv
with open("laul.csv", newline='', encoding="utf-8") as csvfile:
    csvlugeja = csv.reader(csvfile)
    laulusõnad = []
    for rida in csvlugeja:
        laulusõnad.extend(rida)  
print("Laulusõnad:")
for sõna in laulusõnad:
    print(sõna)
täishäälikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü", "y"]
count = 0
värsiRida = "Anna, poiss, karikas mulle,\n Täida head jooki ta täis!\n:,: Tuluks jook mulle ja sulle, Kui ta ka keelatud näis.".capitalize()
for tähemärk in värsiRida:
    if tähemärk.lower() in täishäälikud:  
        count += 1
print("Täishäälikute arv antud värsireas on:", count)
pikemad_sõnad = [sõna for sõna in laulusõnad if len(sõna) > 7]
print("\nSõnad, mis on pikemad kui 7 tähte:")
for sõna in pikemad_sõnad:
    print(sõna)
print("\nPalun sisestage oma värsiread (4 rida):")
kasutaja_värs = []
for i in range(4):
    rida = input("Rida "+str(i + 1)+": ")
    kasutaja_värs.append(rida)
kasutaja_värsi_sõne = "\n".join(kasutaja_värs)
print("\nTeie lisatud värsid:")
print(kasutaja_värsi_sõne)