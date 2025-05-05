nimi1=""
nimi2 =""
jalkaskoor= [0,0]

while nimi1 == "" or nimi2 == "":
    nimi1 = input("Sisesta esimese jalgpalluri nimi")
    nimi2 = input("Sisesta esimese jalgpalluri nimi")
    i = len(jalkaskoor)
    while i > 0:
        currentskoor = int(input("Sisesta",+str(i)+,"meeskonna skoor"))
        jalkaskoor[i-1] = currentskoor
        i -= 1
print(nimi1,nimi2,jalkaskoor)

fail = open("uuendandmed.txt", "w")
fail.write(nimi1 + "\n")
fail.write(nimi2 + "\n")
fail.write(str(jalkaskoor)+"\n")
fail.close()