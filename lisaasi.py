õhupallid = 0
    kook_küünlatega = 0
    liigub = 0
    
    while õhupallid == 0: # while tsükkel mis toimib niikaua kuni õhupalle on 0
        õhupallid = int(input("Kui palju sul õhupalle vaja on ? ")) # kasutaja sisestab mitu õhupalli ta tahab
        x_telg = 0 # x telje liikumine
        y_telg = 0 # y telje liikumine
        while õhupallid > 0: # tsükkel mis toimib niikaua kuni õhupalle on rohkem kui 0

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
                while õhupallid < 10 and õhupallid > -1:
                    tahvel.create_oval(100 + x_telg,110 + y_telg,68 + x_telg,71 + y_telg,fill="red") # joonistatakse õhupalli pall
                    tahvel.create_line(77 + x_telg,130 + y_telg,74 + x_telg,164 + y_telg) # joonistatakse õhupalli nöör
                    x_telg += 50 # kui kaugel on järgmine õhupall
                    õhupallid -= 1 # lahutatakse maha 1 õhupall
    
    while kook_küünlatega == 0:
        kook_küünlatega = int(input("Kui palju sa küünlaid koogile soovid ? "))
        x_telg = 0
        y_telg = 0
        tahvel.create_rectangle(10 + x_telg ,200,1000 + x_telg,500, fill = "pink", outline= "black" )
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
    
    tahvel.create_rectangle(81,280,310 ,460,width=2,fill="red",outline="black")
    tahvel.create_line(186 ,270,188 ,467,width=2,fill="yellow")
    tahvel.create_line(85 ,360,308 ,354,width=2,fill="yellow")
    
    
    kook_küünlatega = int(input("Kui palju sa küünlaid koogile soovid ? ")) #73
    
     elif sünnipäevakaart == 2:
        kook_küünlatega()
        
#         while kook == 0:
#             kook = int(input("Kui palju sul kooke vaja on ? "))
#             liigub = 0
#             while kook > 0:
#                 kook -= 1
#                 tahvel.create_polygon(100 + liigub,100,400 + liigub,100,400 + liigub,300,100 + liigub,300,100 + liigub,100, fill = "pink", outline= "black" )
#                 liigub += 50
#             kook += 1
    elif sünnipäevakaart == 3:
        kook_küünlatega()
#         while küünlad == 0:
#             küünlad = int(input("Kui palju sa küünlaid soovid ? "))
#             liigub = 0
#             while küünlad > 0:
#                 küünlad -= 1
#                 tahvel.create_line(100 + liigub,200,100 + liigub,100,fill = "red")
#                 liigub += 50
#             küünlad += 1

#         õhupallid += 1 # õhupallidele liidetakse 1 juurde,
# kuidas eristada seda, et reas on vähem kui kümme õhupalli alles
# for tsükkel teeb terve rea, while tsükkel teeb osalise rea
    
    #õhupallid = 0
    #kook_küünlatega = 0
    #liigub = 0
    
#     while õhupallid == 0:
#          õhupallid = int(input("Kui palju sul õhupalle vaja on ? "))
#          while õhupallid > 0:
#              õhupallid -= 1
#              for i in range(10):
#                 tahvel.create_oval(100 + liigub,110,68 + liigub,71,fill="red")
#                 tahvel.create_line(77+ liigub,130,74+ liigub,164)
#                 liigub += 50
#          õhupallid += 1