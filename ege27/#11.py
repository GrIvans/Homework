data = open('27data/11/27-11a.txt')
data = open('27data/11/27-11b.txt')
#data = open('input.txt')
#1--14432 верно
#2--45978688 верно
kolvo = int(data.readline())

summa = 0
razn = []
for i in range(kolvo):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), min(a, b, c), a + b + c - max(a, b, c) - min(a, b, c)
    summa += a
    d = [10001]
    if abs(a - b) != 0:
        d.append(abs(a - b))
    if abs(a - c) != 0:
        d.append(abs(a - c))
    razn.append(min(d))
razn.sort()
if summa % 8 == 0:
    print(summa)
else:
    for i in razn:
        if (summa - i) % 8 == 0:
            print(summa - i)
            break