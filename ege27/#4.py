data = open('27data/4/27-4a.txt')
# 1--123430 неверно
# 2--402332230 верно
data = open('27data/4/27-4b.txt')
#data = open('input.txt')

kolvo = int(data.readline())
summa = 0
minrazn = []
for i in range(kolvo):
    a, b = map(int, data.readline().split())
    summa += max(a, b)
    d = abs(a - b)
    if d != 0 and d % 5 != 0:
        minrazn.append(d)
minrazn.sort()
if summa % 5 == 0:
    print(summa)
else:
    for i in minrazn:
        if (summa - i) % 5 == 0:
            print(summa - i)
            break
