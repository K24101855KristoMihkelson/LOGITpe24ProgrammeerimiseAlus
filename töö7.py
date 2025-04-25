nimed = ""
while(nimed == ""):
    nimed = input("Sisesta kõik oma nimed").title()
    nimearv = nimed.count(" ")+nimed.count(",")+1
print("Sul on  "+str(nimearv)+" nime")