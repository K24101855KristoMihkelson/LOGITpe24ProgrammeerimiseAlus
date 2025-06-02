from tkinter import*

raam = Tk()
raam.title("sünnipäevakaart")
tahvel = Canvas(raam,width =300, height = 300, background="white")

def kujund():
    tahvel.create_rectangle(50,50,200,100, fill="orange")

vastus = input("kas sul on täna pakk kätte saada")
if vastus.lower() == "jah":
    kujund()
else:
    print("ok täna pakki ei ole")
    

tahvel.pack()
raam.mainloop()