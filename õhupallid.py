from tkinter import*

raam = Tk()
raam.title("sünnipäevakaart")
tahvel = Canvas(raam,width =1000, height = 1000, background="white")

õhupallid = 0 # õhupallide arv, hetkel on 0
while õhupallid == 0: # while tsükkel mis toimib niikaua kuni õhupalle on 0
    õhupallid = int(input("Kui palju sul õhupalle vaja on ? ")) # kasutaja sisestab mitu õhupalli ta tahab
    while õhupallid > 0: # tsükkel mis toimib niikaua kuni õhupalle on rohkem kui 0
        x_telg = 0 # x telje liikumine
        y_telg = 0 # y telje liikumine
#             while õhupallid < 10: # tsükkel mis toimib niikaua kuni õhupalle on vähem kui 10
#                 õhupallid -= 1 #?
       
            
        if õhupallid > 9:
            for i in range(10): #for tsükkel mis toimib range poolt määratud vahemiku alusel, 0-10 (11tk)
                tahvel.create_oval(100 + x_telg,110 + y_telg,68 + x_telg,71 + y_telg,fill="red") # joonistatakse õhupalli pall
                tahvel.create_line(77 + x_telg,130 + y_telg,74 + x_telg,164 + y_telg) # joonistatakse õhupalli nöör
                x_telg += 50 # kui kaugel on järgmine õhupall
                õhupallid -= 1 # lahutatakse maha 1 õhupall
            y_telg += 30 # kui kaugel on järgmine rida
            x_telg = 0 # viib järgmise rea tagasi algusesse, 0
        elif õhupallid < 10:
            while  õhupallid < 10 and õhupallid > -1:
                tahvel.create_oval(100 + x_telg,110 + y_telg,68 + x_telg,71 + y_telg,fill="red") # joonistatakse õhupalli pall
                tahvel.create_line(77 + x_telg,130 + y_telg,74 + x_telg,164 + y_telg) # joonistatakse õhupalli nöör
                x_telg += 50 # kui kaugel on järgmine õhupall
                õhupallid -= 1 # lahutatakse maha 1 õhupall
tahvel.pack()
raam.mainloop()