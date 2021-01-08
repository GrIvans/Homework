data = open('27data/33/27-33a.txt')
data = open('27data/33/27-33b.txt')
#data = open('input.txt')
#1--18284 неверно
#2--58701760 верно
kolvo = int(data.readline())
summa, razn = 0, []
for i in range(kolvo):
    inp = sorted(list(map(int, data.readline().split())), reverse=1)
    a, b, c = inp[0], inp[1], inp[2]
    summa += a + b
    razn.append(abs(a - c))
    razn.append(abs(b - c))
if summa % 4 == 0:
    print(summa)
else:
    for i in sorted(razn):
        if (summa - i) % 4 == 0:
            print(summa - i)
            break
