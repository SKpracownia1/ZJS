#6. Napisz funkcję, która oblicza iloczyn skalarny dwóch wektorów

import math

def il_skalarny(w1,w2,deg):
    deg=math.cos(math.radians(int(deg)))
    x=int(w1)*int(w2)*deg
    return x

wektor1=input("Podaj dl. wektora 1: ")
wektor2=input("Podaj dl. wektora 2: ")
kat=input("Podaj kat miedzy wektorami:")
print("Iloczyn skalarny wynosi: ", round(il_skalarny(wektor1,wektor2,kat),2))
