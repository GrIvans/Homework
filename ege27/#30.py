data = open('27data/30/27-30a.txt')
data = open('27data/30/27-30b.txt')
#data = open('input.txt')
#1--4913
#2--15089332
kolvo = int(data.readline())
summa, razn = 0, 100001

for i in range(kolvo):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), min(a, b, c)
    summa += c
    d1 = abs(a - c)
    if d1 != 0:
        razn = min(razn, d1)
    d2 = abs(b - c)
    if d2 != 0:
        razn = min(razn, d2)
if summa % 7 != 0:
    print(summa)
else:
    print(summa + razn)
