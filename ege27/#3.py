data = open('27data/3/27-3a.txt')
#data = open('27data/3/27-3b.txt')
#data = open('input.txt')
#1--66480 неправильно
#2--203412732 верно
kolvo = int(data.readline())

summa, minRazn = 0, []
for i in range(kolvo):
    a, b = map(int, data.readline().split())
    summa += min(a, b)
    d = abs(a - b)
    if d != 0:
        minRazn.append(d)
minRazn.sort()
if summa % 3 == 0:
    print(summa)
else:
    for i in (minRazn):
        if (i + summa) % 3 == 0:
            print(i + summa)
            break
