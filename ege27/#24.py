data = open('27data/24/27-24a.txt')
data = open('27data/24/27-24b.txt')
#data = open('input.txt')
# 1--8015  верно
# 2--19596697 верно
kolvo = int(data.readline())
summa = 0
dmin = 100001
for i in range(kolvo):
    a, b = map(int, data.readline().split())
    summa += min(a, b)
    d = abs(a - b)
    r = d % 10
    if r != 0:
        dmin = min(dmin, d)
if summa % 10 != 6:
    print(summa)
else:
    print(summa + dmin)
