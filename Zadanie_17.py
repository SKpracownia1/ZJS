#17. Zaokrąglij do pierwszego miejsca po przecinku liczby znajdujące się na liście liczb rzeczywistych.

import math
lista=[-3.1, 0.3, 1.1212, 111.21212, math.pi , 15]

print(list(map(lambda x: round(x,1), lista)))







