from urllib.request import urlopen
from webbrowser import *


failVeebis = urlopen("https://juriVaitmaa21.thkit.ee/kurwa.txt ")
baildid = failVeebis.read()
tekst = baildid.decode()
tekstridadena = tekst.splitlines()
failVeebis.close()

tõde =0
õigus =0

for rida in tekstridadena:
    sõnad = rida.split()
    
    
    for s in sõnad:
        if s.strip(".,?") == "tõde":
            tõde += 1
         s.replace("õ","6")
         print(s)
        if s.strip(".,?") == "õigus":
            õigus +=1
        s.replace("õ","6")
        print(s)
print("Failis on sõna  tõde "+str(tõde)+"korda")
print("Failis on sõna  tõde "+str(õigus)+"korda")