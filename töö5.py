perekonnaliikmed = ""
while(perekonnaliikmed == ""):
    perekonnaliikmed = input("Kas sul on olemas perekonnaliikmeid: (jah/ei)")
    if perekonnaliikmed == "jah":
        lemmikloomanimed = []
        hetkesisestus = "a"
        while(hetkesisestus != ""):
            hetkesisestus = input("Sisestage välja perekonnaliikmete lemmiklooma nimed,kui rohkem ei ole,vajuta enter")
            if hetkesisestus != "":
                lemmikloomanimed.append(hetkesisestus)
        print(lemmikloomanimed)
    elif perekonnaliikmed == "ei":
        lemmikloomanimi = ""
        while( lemmikloomanimi == ""):
            lemmikloomanimi = input("Kas sul on olemas lemmikloom: (jah/ei)")
            if lemmikloomanimi == "jah":
                loomanimi = []
                hetkesisestus = "m"
                while(hetkesisestus != ""):
                    hetkesisestus = input("Sisestage oma lemmikloomade nimed siia,kui rohkem ei ole,siis vajuta enter")
                    if hetkesisestus != "":
                        loomanimi.append(hetkesisestus)
                print(loomanimi)
            elif lemmikloomanimi == "ei":
                kuiloomipole = ""
                kuiloomipole = input("Kahju,pesaleidjas on palju kasse kes tahaksid kodu")
