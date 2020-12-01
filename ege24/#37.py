s = open('24data/k7c-5.txt').read()

k = 0
for i in range(len(s) - 4):
    fl = True
    stroka = ''
    for n in range(5):
        stroka += s[i + n]
    if stroka[1] != stroka[0] and stroka[1] != stroka[2] and\
        stroka[3] != stroka[4] and stroka[2] != stroka[3]:
            k += 1
print(k)