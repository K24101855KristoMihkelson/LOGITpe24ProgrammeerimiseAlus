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
kook_küünlatega += 1


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

for i in range(10):