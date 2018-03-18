#15. Przy pomocy lambda wyrażeń i funkcji filter stwórz listę kolejnych liczb podzielnych przez 13 spośród liczb z przedziału [100,200]

print(list(filter(lambda x: not x % 13, range(100,200))))





