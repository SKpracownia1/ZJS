#Zadanie 1. (if-else)

d=input("Podaj date: ")
if d%4==0 and d%100<>0 or d%400==0:
    print "Rok", d, "jest przestepny"
else:
    print "Rok", d, "nie jest przestepny"