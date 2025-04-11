from tinker import*

raam = Tk()
raam.title("empty tahvel")

tahvel = Canvas(raam, width=600, height=600)


tahvel.create_line(50,50,100,50) #(x1,y1,x2,y2)
tahvel.create_line(200,200,200,300,300,300,200,200, width=2, fill="green", arrow = LAST)#(x1,y1,x2,y2,x3,y3,x4,y4)

tahvel.create_rectangle(50,100,100,300, outline="orange", fill="yellow")
tahvel.pack()

tahvel.create_polygon(200,400,200,500,300,500, width=2, outline="black", fill="cyan")#(x1,y1,x2,y2,x3,y3,x4,y4)

tahvel.create_oval(400,200,500,300, width=7, outline="red", fill="orange")
tahvel.create_oval(500,200,600,500, width=7, outline="red", fill="orange")

tahvel.create_text(300,300, text="HÄLLO WÜRL", fill="blue")

tahvel.pack()

raam.mainloop()