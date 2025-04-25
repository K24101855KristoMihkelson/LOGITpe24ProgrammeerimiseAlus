#2 – Teeviit v2

#

# kirjutage tkinteriga programm, mis:

# - joonistab ekraanile liiklusmärgi, kasutades TASIKLI

# - liiklusmärgil peab olema vähemalt üks element, mida märgil mitu korda kuvatakse

# - ei saa vastu võtta juba valitud liiklusmärke

# - link: https://et.wikipedia.org/wiki/Eesti_liiklusmærket

#NB! liiklusmärk peab täitma akent (määrama akna õigesse mõõtu) ja olema tegeliku märgiga sarnaste proportsioonidega



from tkinter import*


raam = Tk()
raam.title("Liiklusmärk")
tahvel = Canvas(raam, width = 600, height = 600)
tahvel.create_polygon(276,37,17,456,522,460,276,37,width = 24, fill = "yellow",outline = "red")
tahvel.create_polygon(182,433, 180,325, 224,260, 300,190, 265,195, 268,297, 237,335, 230,428, 182,433, width = 30, fill = "black")
tahvel.pack()
raam.mainloop()