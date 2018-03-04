
d1=[]
d2=[]

import datetime

print "Data 1"
d1.append(input("Dzien:"))
d1.append(input("Miesiac:"))
d1.append(input("Rok:"))
print "Data 2"
d2.append(input("Dzien:"))
d2.append(input("Miesiac:"))
d2.append(input("Rok:"))
print "Data 1: ",str(d1[2])+"-"+str(d1[1])+"-"+str(d1[0])
print "Data 2: ",str(d2[2])+"-"+str(d2[1])+"-"+str(d2[0])
print "Roznica: ",abs(datetime.date(d1[2],d1[1],d1[0])-datetime.date(d2[2],d2[1],d2[0]))

