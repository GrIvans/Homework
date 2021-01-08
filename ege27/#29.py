data = open('27data/29/27-29a.txt')
data = open('27data/29/27-29b.txt')
#data = open('input.txt')
# 1--25034  верно
# 2--76468978  верно
kolvo = int(data.readline())
summa, razn = 0, 100001
for i in range(kolvo):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), a + b + c - max(a, b, c) - \
        min(a, b, c), min(a, b, c)
    summa += a + b
    d1 = abs(a - c)
    if d1 != 0:
        razn = min(razn, d1)
    d2 = abs(b - c)
    if d2 != 0:
        razn = min(razn, d2)
if summa % 5 != 0:
    print(summa)
else:
    print(summa - razn)
