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
    õhupallid = 0 # õhupallide arv, hetkel on 0
    while õhupallid == 0: # while tsükkel mis toimib niikaua kuni õhupalle on 0
        õhupallid = int(input("Kui palju sul õhupalle vaja on ? "))-1 # kasutaja sisestab mitu õhupalli ta tahab
        x_telg = 0 # x telje liikumine
        y_telg = 0 # y telje liikumine
        while õhupallid > 0: # tsükkel mis toimib niikaua kuni õhupalle on rohkem kui 0
#             while õhupallid < 10: # tsükkel mis toimib niikaua kuni õhupalle on vähem kui 10 õhupallid -= 1 #?
                if õhupallid > 9:
                    for i in range(10): #for tsükkel mis toimib range poolt määratud vahemiku alusel, 0-10 (11tk)
                        tahvel.create_oval(100 + x_telg,110 + y_telg,68 + x_telg,71 + y_telg,fill="red") # joonistatakse õhupalli pall
                        tahvel.create_line(77 + x_telg,130 + y_telg,74 + x_telg,164 + y_telg) # joonistatakse õhupalli nöör
                        x_telg += 50 # kui kaugel on järgmine õhupall
                        õhupallid -= 1 # lahutatakse maha 1 õhupall
                    y_telg += 30 # kui kaugel on järgmine rida
                    x_telg = 0 # viib järgmise rea tagasi algusesse, 0
                elif õhupallid < 10:
                    while õhupallid < 10 and õhupallid > -1:
                        tahvel.create_oval(100 + x_telg,110 + y_telg,68 + x_telg,71 + y_telg,fill="red") # joonistatakse õhupalli pall
                        tahvel.create_line(77 + x_telg,130 + y_telg,74 + x_telg,164 + y_telg) # joonistatakse õhupalli nöör
                        x_telg += 50 # kui kaugel on järgmine õhupall
                        õhupallid -= 1 # lahutatakse maha 1 õhupall
                        
def kook_küünlatega():
    kook_küünlatega = 0
    while kook_küünlatega == 0:
        kook_küünlatega = vanus
        x_telg = 0
        y_telg = 0
        tahvel.create_rectangle(10 +x_telg ,200,1000 + x_telg,500, fill = "pink", outline= "black" )
        while kook_küünlatega > 0:
            if kook_küünlatega > 9:
                for i in range(10):
                    tahvel.create_oval(37 + x_telg,163 + y_telg,57 + x_telg,187 + y_telg,width=2,fill = "yellow")
                    tahvel.create_rectangle(36 + x_telg,189 + y_telg,57 + x_telg,230 + y_telg, width=2,fill = "white",outline="black")
                    x_telg += 50
                    kook_küünlatega -= 1
                y_telg += 30
                x_telg = 0
            elif kook_küünlatega < 10:
                while kook_küünlatega < 10 and kook_küünlatega > -1: 
                    tahvel.create_oval(37 + x_telg,163 + y_telg,57 + x_telg,187 + y_telg,width=2,fill = "yellow")
                    tahvel.create_rectangle(36 + x_telg,189 + y_telg,57 + x_telg,230 + y_telg, width=2,fill = "white",outline="black")
                    x_telg += 50
                    kook_küünlatega -= 1
                
        
def kingitus_õnnesoovidega():
    tahvel.create_rectangle(81,380,310 ,560,width=2,fill="red",outline="black")
    tahvel.create_line(186 ,370,188 ,567,width=2,fill="yellow")
    tahvel.create_line(85 ,460,308 ,454,width=2,fill="yellow")
def kõik_korraga():
    õhupallid()
    kook_küünlatega()
    kingitus_õnnesoovidega()
    
EP = ""
while EP == "":
    EP = input("Sisesta oma ees-ja perenimi")
sünnipäev = ""
while sünnipäev == "":
    sünnipäev = input("Sisesta oma sünniaeg: nt: 20.06.2010")
vanus = 0
while vanus == 0:
    vanus = int(input("Sisesta oma vanus:"))
sünnipäevakaardiIdeed = ["õhupall","kook küünlatega","kingitused õnnesoovidega","kõik korraga"]
sünnipäevakaart = 0
while sünnipäevakaart == 0:
    sünnipäevakaart = int(input("Mida sa soovid enda sünnipäevakaardil näha,kas "+str(sünnipäevakaardiIdeed)+"?"))
    Sunimi = EP
    tahvel.create_text(300,50,text="Palju õnne "+str(Sunimi)+", "+str(vanus + 1)+" aasta saamise puhul ""!")
    kook = 0
    küünlad = vanus  + 1
    if sünnipäevakaart == 1:
        õhupallid()
    elif sünnipäevakaart == 2:
        kook_küünlatega()
    elif sünnipäevakaart == 3:
        kingitus_õnnesoovidega()
    elif sünnipäevakaart == 4:
        kõik_korraga()
    
    
tahvel.pack()
raam.mainloop()