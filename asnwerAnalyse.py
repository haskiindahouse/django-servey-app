import csv
from matplotlib import pyplot as plt
i = -1
third = []
first = []
second = []
fourth = []
with open('survey_answer.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        i += 1
        if i != 0:
            switch = i % 4
            if switch == 0:
                fourth.append(row[1])
            if switch == 1:
                first.append(row[1])
            if switch == 2:
                second.append(row[1])
            if switch == 3:
                third.append(row[1])
i = -1
firstA = []
secondA = []
thirdA = []
fourthA = []
with open('survey_option.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        i += 1
        if i != 0:
            switch = i % 4
            if switch == 0:
                fourthA.append(row[1])
            if switch == 1:
                firstA.append(row[1])
            if switch == 2:
                secondA.append(row[1])
            if switch == 3:
                thirdA.append(row[1])
# Анализ результатов
fC, sC, tC, foC = 0, 0, 0, 0
fCA, sCA, tCA, foCA = firstA[0], secondA[0], thirdA[0], fourthA[0]
for i in range(len(first)):
    if first[i] == '1':
        fC += 1
    if first[i] == '2':
        sC += 1
    if first[i] == '3':
        tC += 1
    if first[i] == '4':
        foC += 1
vals = [fC, sC, tC, foC]
labels = [fCA, sCA, tCA, foCA]
explode = (0.15, 0.05, 0.15, 0.15)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.title('Результаты опроса:\n' + 'Сколько должен стоить подарок?', fontsize=18)
plt.savefig('res1.png')
# Продолжение анализа
fC, sC, tC, foC = 1, 1, 1, 1
fCA, sCA, tCA, foCA = firstA[1], secondA[1], thirdA[1], fourthA[1]
for i in range(len(first)):
    if first[i] == '1':
        fC += 1
    if first[i] == '2':
        sC += 1
    if first[i] == '3':
        tC += 1
    if first[i] == '4':
        foC += 1
vals = [fC, sC, tC, foC]
labels = [fCA, sCA, tCA, foCA]
explode = (0.15, 0.05, 0.15, 0.15)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.title('Результаты опроса:\n' + 'Какого цвета он должен быть?', fontsize=18)
plt.savefig('res2.png')
# --------
fC, sC, tC, foC = 2, 2, 2, 2
fCA, sCA, tCA, foCA = firstA[2], secondA[2], thirdA[2], fourthA[2]
for i in range(len(first)):
    if first[i] == '1':
        fC += 1
    if first[i] == '2':
        sC += 1
    if first[i] == '3':
        tC += 1
    if first[i] == '4':
        foC += 1
vals = [fC, sC, tC, foC]
labels = [fCA, sCA, tCA, foCA]
explode = (0.15, 0.05, 0, 0)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.title('Результаты опроса:\n' + 'Какая категория вам больше всего нравится?', fontsize=18)
plt.savefig('res3.png')
# -------
fC, sC, tC, foC = 3, 3, 3, 3
fCA, sCA, tCA, foCA = firstA[3], secondA[3], thirdA[3], fourthA[3]
for i in range(len(first)):
    if first[i] == '1':
        fC += 1
    if first[i] == '2':
        sC += 1
    if first[i] == '3':
        tC += 1
    if first[i] == '4':
        foC += 1
vals = [fC, sC, tC, foC]
labels = [fCA, sCA, tCA, foCA]
explode = (0.05, 0.05, 0, 0.15)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.title('Результаты опроса:\n' + 'Когда будем его дарить?', fontsize=18)
plt.savefig('res4.png')
