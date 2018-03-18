#Zadanie 5. Napisać funkcję wykorzystującą algorytm Euklidesa znajdujący największy wspólny dzielnik dwóch liczb.

def euk(a,b):
    while b!=0:
       a, b = b, a%b
    return a

l1=input("Podaj 1 liczbe:")
l2=input("Podaj 1 liczbe:")

print("NWD: ", euk(int(l1),int(l2)))