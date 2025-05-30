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
tahvel = Canvas(raam,width =1000, height = 1000, background="white")
def õhupallid():
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
def kook_küünlatega():
    kook_küünlatega = 0
    while kook_küünlatega == 0:
        kook_küünlatega = int(input("Kui palju sa küünlaid koogile soovid ? "))
        x_telg = 0
        y_telg = 0
        tahvel.create_rectangle(10 +x_telg ,200,1000 + x_telg,500, fill = "pink", outline= "black" )
        while kook_küünlatega > 0:
            for i in range(10):
                kook_küünlatega -=1
                tahvel.create_oval(37 + x_telg,163 + y_telg,57 + x_telg,187 + y_telg,width=2,fill = "yellow")
                tahvel.create_rectangle(36 + x_telg,189 + y_telg,57 + x_telg,230 + y_telg, width=2,fill = "white",outline="black")
                x_telg += 50
            y_telg += 30
            x_telg = 0
        kook_küünlatega += 1
    
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
    tahvel.create_text(300,50,text="Palju õnne "+str(Sunimi)+", "+str(vanus)+" saamise puhul ""!")
    kook = 0
    küünlad = 0
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
        while kook == 0:
            kook = int(input("Kui palju sul kooke vaja on ? "))
            liigub = 0
            while kook > 0:
                kook -= 1
                tahvel.create_polygon(100 + liigub,100,400 + liigub,100,400 + liigub,300,100 + liigub,300,100 + liigub,100, fill = "pink", outline= "black" )
                liigub += 50
            kook += 1
    elif sünnipäevakaart == 3:
        
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
            kook_küünlatega = int(input("Kui palju sa küünlaid koogile soovid ? "))
            x_telg = 0
            y_telg = 0
            tahvel.create_rectangle(10 +x_telg ,200,1000 + x_telg,500, fill = "pink", outline= "black" )
            while kook_küünlatega > 0:
                for i in range(10):
                    if kook_küünlatega < 10:
                        kook_küünlatega -=1
                        tahvel.create_oval(37 + x_telg,163 + y_telg,57 + x_telg,187 + y_telg,width=2,fill = "yellow")
                        tahvel.create_rectangle(36 + x_telg,189 + y_telg,57 + x_telg,230 + y_telg, width=2,fill = "white",outline="black")
                        x_telg += 50 
                    else:
                        kook_küünlatega -=1
                        tahvel.create_oval(37 + x_telg,163 + y_telg,57 + x_telg,187 + y_telg,width=2,fill = "yellow")
                        tahvel.create_rectangle(36 + x_telg,189 + y_telg,57 + x_telg,230 + y_telg, width=2,fill = "white",outline="black")
                        x_telg += 50
                    y_telg += 30
                    x_telg = 0
                    kook_küünlatega += 1
    elif sünnipäevakaart == 5:
        kingitused = 0
        while õhupallid == 0:
            õhupallid = int(input("Kui palju sul õhupalle vaja on ? "))
            liigub = 0
            while õhupallid > 0:
                õhupallid -= 1
                tahvel.create_oval(100 + liigub,110,68 + liigub,71,fill="red")
                tahvel.create_line(77+ liigub,130,74+ liigub,164)
                liigub += 50
            õhupallid += 1
                 
                 
                 
tahvel.pack()
raam.mainloop()