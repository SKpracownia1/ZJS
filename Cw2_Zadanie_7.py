#7. Napisać funkcję, która dla liczby podanej jako argument funkcji zwraca jej zapis słowny w postaci listy.

cyfry = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"piec", 6:"szesc", 7:"siedem", 8:"osiem", 9:"dziewiec", 0:"zero"}
import math

def liczba_slownie(l):
	lista=[]
	while int(l)>=1:
		lista.insert(0,cyfry.get(int(l)%10))
		l=math.trunc(int(l)/10)
	return lista

liczba=input("Podaj liczbe:")
print(liczba_slownie(liczba))