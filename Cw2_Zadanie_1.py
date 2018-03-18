#Zadanie 1


lista=[10,20,30,40,50]
print("a) Utworz liste skladajaca sie pieciu liczb calkowitych.")
print(lista)

print("b) Dodaj na koniec listy dwie liczby calkowite. Uzyj dwoch roznych sposobow.")

print("Sposob I: Append:") 
lista.append(65) 
print(lista)

print("Sposob II: Extend:")                            
lista.extend([100])   
print(lista)

print("c) Wstaw liczbe na poczatek listy.") 
lista.insert(0,0)
print(lista)

print("d) Usun istniejacy element z listy.")
lista.remove(50)  

print("e) Pobierz i usun pierwszy element z listy.")
lista.pop(0)
print(lista)

print("f) Pobierz i usun ostatni element z listy.")
lista.pop()
print(lista)

print("g) Dolacz do listy druga taka sama liste.")
lista.extend(lista)   
print(lista)

print("h) Odwroc porzadek listy.")
lista.reverse()
print(lista)

print("i) Posortuj elementy listy.")
lista.sort()
print(lista)

print("j) Oblicz ilosc elementow listy.")
print(len(lista))

print("k) Oblicz ile razy wystepuje istniejacy element listy.")
print("Ilosc wystapien liczby 10: "+str(lista.count(10)))









