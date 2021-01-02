data = open('27data/5/27-5a.txt')
data = open('27data/5/27-5b.txt')
#data = open('input.txt')
# 1--75960 верно
# 2--203343860 верно
kolvo = int(data.readline())
summa = 0
minrazn = []
for i in range(kolvo):
    a, b = map(int, data.readline().split())
    summa += min(a, b)
    d = abs(a - b)
    if d != 0:
        minrazn.append(d)
if summa % 5 == 0:
    print(summa)
else:
    for i in sorted(minrazn):
        if (summa + i) % 5 == 0:
            print(i + summa)
            break
