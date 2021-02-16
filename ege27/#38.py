f = open('27data/38/27-38a.txt')
#f = open('27data/38/27-38b.txt')
n = int(f.readline())
dict = {}
for i in range(n):
    inp = int(f.readline())
    dict[inp] = dict.get(inp, 0) + 1

summa = 0
mx_nechet = 0
for chislo in dict:
    kolvo = dict[chislo]
    if kolvo % 2 == 0:
        print(chislo, kolvo * chislo)
        summa += kolvo * chislo
    else:
        summa += (kolvo - 1) * chislo
        print(chislo, (kolvo - 1) * chislo)
        mx_nechet = max(chislo, mx_nechet)

if mx_nechet != 0:
    print(summa + mx_nechet)
else:
    print(summa)
#1 -- 71 verno
#2 -- 254363 verno
