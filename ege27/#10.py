#data = open('27data/10/27-10a.txt')
data = open('27data/10/27-10b.txt')
#data = open('input.txt')
# 1--15062
# 2--45226419
kolvo = int(data.readline())

summa = 0
razn = 10001
for i in range(kolvo):
    an = [10001]
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), min(a, b, c), a + b + \
        c - max(a, b, c) - min(a, b, c)
    summa += a
    if a == b:
        d = a - c
        if d % 4 > 0:
            razn = min(razn, d)
    else:
        d = a - b
        if d % 4 > 0:
            razn = min(razn, d)
if summa % 4 != 0:
    print(summa)
else:
    print(summa - razn)
