#14. Użyj lambda wyrażenia do znalezienia największej liczby spośród listy liczb. Proszę nie używać pętli.

from functools import reduce

f = lambda a,b: a if (a > b) else b
print(reduce(f, [12,11,52,102,13]))
