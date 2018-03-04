# Zadanie 2. (if-elif-else)

import sys
import math
w=input("Wybierz figure:\n 1.Kwadrat\n 2.Prostakat\n 3.Kolo\n ")

if w not in (1,2,3):
    print "Error"
    raise  SystemExit
elif w==1:
    a=input("Podaj dl. boku: ")
    print "Pole: ", a*a
elif w==2:
    a=input("Podaj dl. boku a: ")
    b=input("Podaj dl. boku b: ")
    print "Pole: ", a*b
else:
    a=input("Podaj promien kola: ")
    print "Pole: ", math.pi*a*a


