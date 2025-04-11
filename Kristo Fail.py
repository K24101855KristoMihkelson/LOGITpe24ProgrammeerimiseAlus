from random import randint
from tkinker import*

kVanus=""
while(kVanus=""):
    if vanus < 3:
        print("Oled liiga noor,kujundit ei joonista sulle ")
    else:
        lemmikvärv = ""
        while(värv == ""):
            lemmikvärv = int(input("Mis on su lemmikvärv? sisesta oma lemmikvärv inglise keeles."))
        lemmikkujund = ""
        while(lemmikkujund == ""):
            lemmikkujund = int(input("Sisesta siia oma lemmikkujund, valikus on: kolmnurk,ruut,ristkülik,ring,ovaal,kaheksanurk"))
            if lemmikkujund == "kolmnurk":
               raam = Tk()
               raam.title("empty tahvel")
               tahvel = Canvas(raam, width=600, height=600)
               tahvel.create_polygon(120, 300, 232, 80, 344, 300)
               tahvel.pack()
               raam.mainloop()
            elif lemmikkujund == "ruut":
                raam = Tk()
                raam.title("empty tahvel")
                tahvel = Canvas(raam, width=600, height=600)
                canvas.create_rectangle(10,10,110,110,width = 2,outline ="black",fill ="white")
                tahvel.pack()
                raam.mainloop()
            elif lemmikkujund == "ristkülik":
                raam = Tk()
                raam.title("empty tahvel")
                tahvel = Canvas(raam, width=600, height=600)
                tahvel.create_rectangle(210,10,310,210,width =2,outline ="black",fill ="white")
                tahvel.pack()
                raam.mainloop()
            elif lemmikkujund == "ring":
                raam = Tk()
                raam.title("empty tahvel")
                tahvel = Canvas(raam, width=600, height=600)
                tahvel.create_oval(110,10,210,110,width = 2,outline = "black",fill = "white")
                tahvel.pack()
                raam.mainloop()
            elif lemmikkujund == "ovaal":
               raam = Tk()
               raam.title("empty tahvel")
               tahvel = Canvas(raam, width=600, height=600)
               tahvel.create_oval(50,50,100,80,width = 2, outline = "black", fill = "white")
               tahvel.pack()
               raam.mainloop()
            elif lemmikkujund == "kaheksanurk":
                
        

