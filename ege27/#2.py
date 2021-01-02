#data = open('27data/2/27-2a.txt')
#1--109737
#2--401536407
data = open('27data/2/27-2b.txt')
#data = open('input.txt')
kolvo = int(data.readline())
minRazn = []
summa = 0
for i in range(kolvo):
    a, b = map(int, data.readline().split())
    summa += max(a, b)
    d = abs(a - b)
    if d != 0 and d % 3 != 0:
        minRazn.append(d)
if summa % 3 == 0:
    print(summa)
else:
    for i in sorted(minRazn):
        if (summa - i) % 3 == 0:
            print(summa - i)
            break
