data = open('27data/25/27-25a.txt')
#data = open('27data/25/27-25b.txt')
#data = open('input.txt')
# 1--12727 неверно
# 2--40382425 неверно
kolvo = int(data.readline())
summa, razn = 0, []
for i in range(kolvo):
    a, b = map(int, data.readline().split())
    summa += max(a, b)
    d = abs(a - b)
    if d != 0:
        razn.append(d)
if summa % 8 == 3:
    print(summa)
else:
    for i in sorted(razn):
        if int(oct(summa - i)[2:]) % 8 == 3:
            print(summa - i)
            break
