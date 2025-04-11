# kirjuta programm mis
# küsib kasutajalt tsükli sees
# kas tal on hapukapsas
# - kui kasutajal ei ole, siis öeldakse et saab hautist
# kas tal on pott
# - kui kasutajal potti ei ole, siis öeldakse et suppi teha ei saa
# kas tal on vett
# - kui kasutajal vett ei ole, siis öeldakse et saab mulgikapsaid teha
# kas tal on kartulit
# kas tal on puljongit
# kas kasutajal on midagi muud kapis (ei/kasutajavastus)
# - kui kasutajal ei ole, siis öeldakse midagi eelnevatest sobivatest vastustest
# - kui kasutajal on, siis öeldakse et saab ühepajatoitu
# kogu arvutamine peab toimuma loogiliste tehetega
hapukapsas = ""
pott = ""
vesi = ""
kartul = ""
puljong = ""
midagi_muud = ""
while(hapukapsas == "" or pott == "" or vesi == "" or kartul == "" or puljong == "" or midagi_muud == "") :
   hapukapsas = input("Kas sul on olemas hapukapsas? (jah/ei) ").lower()
   pott = input("Kas sul on olemas pott? (jah/ei) ").lower()
   vesi = input("Kas sul on olemas vesi? (jah/ei) ").lower()
   kartul = input("Kas sul on olemas kartulit? (jah/ei) ").lower()
   puljong = input("Kas sul on olemas puljongit? (jah/ei) ").lower()
   midagi_muud = input("Kas sul on kapis midagi muud? (jah/ei) ").lower()

if(hapukapsas == "jah" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "jah" and midagi_muud == "ei"):
    print("Sa saad teha hapukapsasuppi")
    
elif(hapukapsas == "ei" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "jah" and midagi_muud == "ei"):
    print("Sa saad teha  hautist")
    

elif(hapukapsas == "jah" and pott == "ei" and vesi == "jah" and kartul == "jah" and puljong == "jah" and midagi_muud == "jah"):
    print("Sa ei saa teha mitte midagi")
    

elif(hapukapsas == "jah" and pott == "jah" and vesi == "ei" and kartul == "ei" and puljong == "ei" and midagi_muud == "ei"):
    print("Sa saad panna hapukapsa potti")
    

elif(hapukapsas == "jah" and pott == "jah" and vesi == "ei" and kartul == "jah" and puljong == "jah" and midagi_muud == "ei"):
    print("Sa saad teha mulgikapsaid")
    

elif(hapukapsas == "ei" and pott == "ei" and vesi == "ei" and kartul == "ei" and puljong == "ei" and midagi_muud == "ei"):
    print("Sul pole söögi tegemiseks midagi,mine poodi ja osta toiduaineid")
    

elif(hapukapsas == "ei" and pott == "ei" and vesi == "ei" and kartul == "jah" and puljong == "jah" and midagi_muud == "jah"):
    print("Sa ei saa teha midagi, on vaja omada potti")
    
elif(hapukapsas == "jah" and pott == "jah" and vesi == "jah" and kartul == "ei" and puljong == "jah" and midagi_muud == "jah"):
    print("Sa saad teha suppi ilma kartulita")
    
elif(hapukapsas == "jah" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "ei" and midagi_muud == "ei"):
    print("Su tehtud supp tuleb maitsetu")
    

elif(hapukapsas == "jah" and pott == "ei" and vesi == "ei" and kartul == "jah" and puljong == "ei" and midagi_muud == "jah"):
    print("Sa ei saa teha midagi, sul pole potti")
    

elif(hapukapsas == "jah" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "jah" and midagi_muud == "ei"):
    print("Siis sa pead valima enda eelnevatest valikutest.")
    

elif(hapukapsas == "jah" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "jah" and midagi_muud == "jah"):
    print("Sa saad teha ühepajatoitu")
    

