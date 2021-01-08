data = open('27data/23/27-23a.txt')
data = open('27data/23/27-23b.txt')
#data = open('input.txt')
# 1--13159 верно
# 2--40799380 верно
kolvo = int(data.readline())
summa = 0
razn = 100001
for i in range(kolvo):
    a, b = map(int, data.readline().split())
    summa += max(a, b)
    r = abs(a - b)
    if r % 10 != 0:
        razn = min(r, razn)
if summa % 10 != 5:
    print(summa)
else:
    print(summa - razn)
