from urllib.request import urlopen
from webbrowser import *


failVeebis = urlopen("https://juriVaitmaa21.thkit.ee/kurwa.txt ")
baildid = failVeebis.read()
tekst = baildid.decode()
tekstiridadena = tekst.splitlines()
failVeebis.close()
print(tekstiridadena[9][16])

filenamefromsite = input("millistfaili avada tahad")
open("https://juriVaitmaa21.thkit.ee/"+filenamefromsite+".txt ")
