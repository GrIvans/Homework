data = open('27data/32/27-32a.txt')
data = open('27data/32/27-32b.txt')
#data = open('input.txt')
#1--5907 неверно
#2--14078757 верно
kolvo = int(data.readline())
summa, razn = 0, []
for i in range(kolvo):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), min(a, b, c)
    summa += c
    d = abs(c - a)
    if d != 0:
        razn.append(d)
    d = abs(b - c)
    if d != 0:
        razn.append(d)
if summa % 11 == 0:
    print(summa)
else:
     for i in sorted(razn):
        if (summa + i) % 11 == 0:
            print(summa + i)
            break
