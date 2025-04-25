loomanimed = []
hetkenimi = "a"
while (hetkenimi != ""):
    hetkenimi = input("Sisesta lemmiklooma nimi")
    if hetkenimi != "":
        loomanimed += [hetkenimi]
        
for i in range(len(loomanimed)):
    print(loomanimed[i])
    