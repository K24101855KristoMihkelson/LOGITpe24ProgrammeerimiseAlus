

# 1. Küsime kasutajalt lemmikfilmid
lemmikfilmid = []

print("Sisesta oma lemmikfilmid ükshaaval. Kui rohkem ei ole, vajuta lihtsalt enter.")
while True:
    film = input("Sisesta filmi nimi: ")
    if film == "":
        break
    lemmikfilmid.append(film)

print("\nSinu lemmikfilmid:")
for film in lemmikfilmid:
    print("-", film)

# 2. Küsime kõige lemmikumat filmi
koige_lemmik = input("\nMis on sinu kõige lemmikum film kogu aegade jooksul? ")

# 3. Kontrollime, kas see film on juba lemmikfilmide nimekirjas
if koige_lemmik in lemmikfilmid:
    print("Ossa, oled oma lemmiku isegi kaks korda pannud!")
else:
    print(f"Aga kus on sinu '{koige_lemmik}'?")
    meeldib = input(f"Kas sulle meeldib '{koige_lemmik}'? (jah/ei): ").lower()
    if meeldib == "jah":
        lemmikfilmid.append(koige_lemmik)
        print(f"Lisati '{koige_lemmik}' ka sinu lemmikfilmide nimekirja!")
    else:
        print("Aga miks? See on ju hea film!")

# 4. Kontrollime erifilmid
if "Terminator" in lemmikfilmid:
    print("You’ll be back.")
if "Vanamehe Film" in lemmikfilmid:
    print("Aga kuš šu šnikurš on šiiš?")

# 5. Loendame mitu filmi kokku on
filmide_arv = len(lemmikfilmid)
print(f"\nSul on kokku {filmide_arv} lemmikfilmi.")

if filmide_arv <= 5:
    print("Sa ei vaata väga palju filme vist.")
elif 5 < filmide_arv <= 10:
    print("Käid tihti kinos?")
else:
    print("Siis, pole mul siin midagi öelda härra movieguru, headaega.")
