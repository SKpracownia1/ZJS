#Zadanie 6. (funkcje)

liczba=input("podaj liczbe: ")

def il_cyfr(liczba):
    dl=0
    while (liczba/10>0):
        liczba=liczba/10
        dl=dl+1
    return (dl+1)

il=int(il_cyfr(liczba))

if il==1:
    print "liczba", liczba ,"ma 1 cyfre"
elif il in (2,3,4):
    print "liczba", liczba ,"ma", il, "cyfry"
else:
    print "liczba", liczba ,"ma", il, "cyfr"