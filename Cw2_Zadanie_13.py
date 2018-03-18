#13. Użyj lambda wyrażenia do obliczenia 200! (200 silnia). Proszę nie używać pętli.

from functools import reduce
n=200
print(reduce(lambda x, y: x * y, range(1,n+1)))