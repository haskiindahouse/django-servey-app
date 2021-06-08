import random
import names
from statistics import median
import numpy as np

# Метод средних арифметических рангов
n = int(input())
expertMatrix = {names.get_full_name(): [random.randint(1, n) for i in range(n)] for j in range(n)}
sumProject = [[0, i] for i in range(n)]
transpose = [[] for _ in range(n)]
for expert, rates in expertMatrix.items():
    for i in range(n):
        transpose[i].append(rates[i])
        sumProject[i][0] += rates[i]
# Сразу округленное
count = n
for i in range(n):
    for j in range(n):
        if sumProject[i][0] == sumProject[j][0]:
            print(count)
            count -= 1
            sumProject[i][1] = sumProject[j][1]
print(sumProject)
averageProject = [round(sumProject[i][0] /n) for i in range(n)]
print('Итоговый ранг по методу средних арифметических рангов', averageProject)
print(transpose)
medianProject = [round(median(transpose[i])) for i in range(n)]
averageOfSumProject = sum(sumProject) / n
print('Итогвый ранг по медианам', medianProject)
print(averageOfSumProject)
dispersionProject = [sumProject[i][0] - averageOfSumProject for i in range(n)]
print(dispersionProject)
squareOfdispersionProject = [dispersionProject[i] ** 2 for i in range(n)]
print(squareOfdispersionProject)
sumOfsquareDispPrj = sum(squareOfdispersionProject)
print(sumOfsquareDispPrj)
