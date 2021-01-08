data = open('27data/31/27-31a.txt')
data = open('27data/31/27-31b.txt')
#data = open('input.txt')
#1--15148 верно
#2--29466419 верно
kolvo = int(data.readline())
summa, minraz = 0, 100001
for i in range(kolvo):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), min(a, b, c)
    summa += b + c
    d = abs(a - b)
    if d != 0:
        minraz = min(minraz, d)
    d = abs(a - c)
    if d != 0:
        minraz = min(minraz, d)
if summa % 9 != 0:
    print(summa)
else:
    print(summa + minraz)