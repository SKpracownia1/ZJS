# Zadanie 3. (while)

a=0
b=1
licznik=0

print "F",licznik,"=", a
while b<1000000:
    licznik=licznik+1
    print "F",licznik,"=", b
    temp=a
    a=b
    b=b+temp
 

