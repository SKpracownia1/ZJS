#9.

def kwadrat(a):
    return a*a
 
a=input("Podaj liczbe: ")
a=int(a)

print(kwadrat(a))

sqr = lambda a: a*a
print(sqr(a))

print((lambda a: a*a)(a))