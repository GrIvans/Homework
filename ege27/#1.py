#data = open('27data/1/27-1a.txt')
#1--60650
#2--200147771
data = open('27data/1/27-1b.txt')
summa = 0
minRazn = 100000
kolvo = int(data.readline())
for i in range(kolvo):
    a, b = map(int, data.readline().split())
    summa += min(a, b)
    d = abs(a - b)
    if d % 3 > 0:
        minRazn = min(minRazn, d)
if summa % 3 != 0:
    print(summa)
else:
    print(summa + minRazn)
