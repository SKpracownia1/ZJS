#Zadanie 9

tab=[]
liczba=input("Podaj liczbe:")
import math

licznik=0
while liczba>=1:
	tab.append(liczba%10)
	liczba=math.trunc(liczba/10)
	licznik+=1

licznik-=1

while licznik>=0:
	if tab[licznik]==1:
		print "jeden"
	elif tab[licznik]==2:
		print "dwa"
	elif tab[licznik]==3:
		print "trzy"
	elif tab[licznik]==4:
		print "cztery"
	elif tab[licznik]==5:
		print "piec"
	elif tab[licznik]==6:
		print "szesc"
	elif tab[licznik]==7:
		print "siedem"
	elif tab[licznik]==8:
		print "osiem"
	elif tab[licznik]==9:
		print "dziewiec"
	else:
		print"Error"
	licznik-=1


