#11. Zdefiniuj lambda wyrażenia: wyznaczające minimalną i maksymalną wartość spośród dwóch liczb oraz obliczającą wartość bezwzględną.

l1=11
l2=100

a=(lambda x,y: min(x,y))
print("Min:",a(l1,l2))
b=(lambda x,y: max(x,y))
print("Max:",b(l1,l2))
c=(lambda x,y: abs(x-y))
print("Abs:",c(l1,l2))




