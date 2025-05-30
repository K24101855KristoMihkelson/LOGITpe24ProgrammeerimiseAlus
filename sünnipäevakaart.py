# NB! kõik küsimised on tsüklis mis kontrollitud tsüklimuutujaga (mitte True ja break)
# NB! kõik sisendud töödeldakse standardkujule
# NB! kõik funktsionaalsed osad mis pole üldise programmi osa, peab olema kirjutatud funktsioonina
# kasutab tkinterit
# kirjuta programm mis
#
# Küsib kasutajalt tema ees ja perekonnanime
# küsib kasutajalt tema sünnipäeva
# küsib kasutajalt tema vanust
# küsib kasutajalt mida ta oma sünnipäevakaardile näha tahab
# - kas õhupalle (jah/ei) #õhupalli joonistamine on alamfunktsioon
# - - kui jah siis mitu (arv)
# - kas kooki küünaldega (jah/ei) (küünalde arv on kasutaja vanus +=1) #koogi ja küünalde joonistamine on alamfunktsioon)
# - kas kingitust õnnesoovidega (palju õnne vanus +=1 saamise puhul)
# - või kas kõike korraga
# programm joonistab kasutajale tkinteri abil sünnipäevakaardi.

from tkinter import*

raam = Tk()
raam.title("sünnipäevakaart")
tahvel = Canvas(raam,width = 700, height = 700, background="white")

EP = ""
while EP == "":
    EP = input("Sisesta oma ees-ja perenimi")
sünnipäev = ""
while sünnipäev == "":
    sünnipäev = input("Sisesta oma sünniaeg: nt: 20.06.2010")
vanus = 0
while vanus == 0:
    vanus = int(input("Sisesta oma vanus:"))
sünnipäevakaardiIdeed = ["õhupall","kook","küünlad","kook küünlatega","kingitused õnnesoovidega","kõik korraga"]
sünnipäevakaart = 0
while sünnipäevakaart == 0:
    sünnipäevakaart = int(input("Mida sa soovid enda sünnipäevakaardil näha,kas "+str(sünnipäevakaardiIdeed)+"?"))
    Sunimi = EP
    tahvel.create_text(300,50,text="Palju õnne "+str(Sunimi)+"!")
    if sünnipäevakaart == 1:
        õhupallid = 0
        while õhupallid == 0:
            õhupallid = int(input("Kui palju sul õhupalle vaja on ? "))
            liigub = 0
            while õhupallid > 0:
                õhupallid -= 1
                tahvel.create_oval(100 + liigub,110,68 + liigub,71,fill="red")
                tahvel.create_line(77+ liigub,130,74+ liigub,164)
                liigub += 50
            õhupallid += 1
    elif sünnipäevakaart == 2:
        kook = 0
        while kook == 0:
            kook = int(input("Kui palju sul kooke vaja on ? "))
            liigub = 0
            while kook > 0:
                kook -= 1
                tahvel.create_polygon(100 + liigub,100,400 + liigub,100,400 + liigub,300,100 + liigub,300,100 + liigub,100, fill = "pink", outline= "black" )
                liigub += 50
            kook += 1
    elif sünnipäevakaart == 3:
        küünlad = 0
        while küünlad == 0:
            küünlad = int(input("Kui palju sa küünlaid soovid ? "))
            liigub = 0
            while küünlad > 0:
                küünlad -= 1
                tahvel.create_line(100 + liigub,200,100 + liigub,100,fill = "red")
                liigub += 50
            küünlad += 1
    elif sünnipäevakaart == 4:
        kook_küünlatega = 0
        while kook_küünlatega == 0:
            kook_küünlatega = int(input("Kui palju sa kooke küünlatega soovid ? "))
            liigub = 0
            while kook > 0 and küünlad > 0:
                 kook -= 1
                 tahvel.create_polygon(100 + liigub,100,400 + liigub,100,400 + liigub,300,100 + liigub,300,100 + liigub,100, fill = "pink", outline= "black" )
                 küünlad -= 1
                 tahvel.create_line(100 + liigub,200,100 + liigub,100,fill = "red")
                 liigub += 50
             küünlad += 1
             kook += 1
            
                 
                 
                 
            
        
                
        
                
         
            
                
                    
tahvel.pack()
raam.mainloop()